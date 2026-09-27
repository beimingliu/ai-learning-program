#!/usr/bin/env node
// Narration via the local Qwen3-TTS server instead of HeyGen/Kokoro. Writes the same
// audio_engine_meta.json + audio_meta.json shapes the faceless-explainer scripts consume.
//   node scripts/qwen-tts.mjs [--ref Quick-and-punchy] [--tempo 0.9] [--gap 0.45] [--only 03,07]
import { execFileSync } from "node:child_process";
import { existsSync, mkdirSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { join } from "node:path";

const flag = (n, d) => {
  const i = process.argv.indexOf(`--${n}`);
  return i >= 0 ? process.argv[i + 1] : d;
};
const SERVER = flag("server", "http://localhost:8001");
const REF = flag("ref", "Quick-and-punchy");
const TEMPO = Number(flag("tempo", "0.9"));
const GAP = Number(flag("gap", "0.45"));
const ONLY = flag("only", null)?.split(",");
const ROOT = process.cwd();
const TMP = join(ROOT, ".hyperframes", "qwen-tmp");

function parseScript(md) {
  const out = [];
  let cur = null;
  for (const line of md.split(/\r?\n/)) {
    const h = line.match(/^##\s+.*?\(frame\s+(\d+)\)/i);
    if (h) {
      if (cur) out.push(cur);
      cur = { id: String(h[1]).padStart(2, "0"), text: "" };
      continue;
    }
    const m = cur && line.match(/^(?: {4,}|\t)(.+)$/);
    if (m) cur.text += (cur.text ? " " : "") + m[1].trim();
  }
  if (cur) out.push(cur);
  return out;
}

const norm = (s) => s.toLowerCase().replace(/[^a-z0-9 ]+/g, " ").split(/\s+/).filter(Boolean);
// Fraction of script words recovered, in order (LCS / script length).
function recall(expected, heard) {
  const a = norm(expected), b = norm(heard);
  const dp = Array.from({ length: a.length + 1 }, () => new Array(b.length + 1).fill(0));
  for (let i = 1; i <= a.length; i++)
    for (let j = 1; j <= b.length; j++)
      dp[i][j] = a[i - 1] === b[j - 1] ? dp[i - 1][j - 1] + 1 : Math.max(dp[i - 1][j], dp[i][j - 1]);
  return dp[a.length][b.length] / Math.max(1, a.length);
}

const sh = (cmd, args) => execFileSync(cmd, args, { stdio: ["ignore", "pipe", "pipe"] }).toString();
const duration = (p) => Number(sh("ffprobe", ["-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p]));

function transcribe(wav) {
  const dir = join(TMP, "tr-" + Date.now());
  sh("npx", ["--yes", "hyperframes@0.8.77", "transcribe", wav, "--model", "small.en", "--dir", dir]);
  const words = JSON.parse(readFileSync(join(dir, "transcript.json"), "utf8"));
  rmSync(dir, { recursive: true, force: true });
  return words;
}

async function synthSentence(text, outWav) {
  for (let i = 0; ; i++) {
    try {
      return await synthOnce(text, outWav);
    } catch (e) {
      if (i >= 4) throw e;
      console.error(`  server error (${e.cause?.code ?? e.message}), retrying in ${5 * (i + 1)}s`);
      await new Promise((r) => setTimeout(r, 5000 * (i + 1)));
    }
  }
}

async function synthOnce(text, outWav) {
  const fd = new FormData();
  fd.set("text", text);
  fd.set("language", "English");
  fd.set("reference_id", REF);
  const r = await fetch(`${SERVER}/api/clone`, { method: "POST", body: fd });
  if (!r.ok) throw new Error(`clone ${r.status}: ${await r.text()}`);
  const { audio_url } = await r.json();
  const buf = Buffer.from(await (await fetch(audio_url)).arrayBuffer());
  writeFileSync(outWav, buf);
}

async function synthLine({ id, text }) {
  const sentences = text.match(/[^.!?]+[.!?]+/g)?.map((s) => s.trim()) ?? [text];
  const parts = [];
  for (const [k, s] of sentences.entries()) {
    const p = join(TMP, `${id}-${k}.wav`);
    let best = null;
    for (let attempt = 0; attempt < 4; attempt++) {
      await synthSentence(s, p);
      const heard = transcribe(p).map((w) => w.text).join(" ");
      const score = recall(s, heard);
      const d = duration(p);
      const wps = norm(s).length / d;
      // Reject garbled takes and runaway takes (long silence / babble after the sentence).
      const ok = score >= 0.9 && wps > 1.2;
      if (!best || score > best.score) best = { score, buf: readFileSync(p) };
      if (ok) break;
      console.error(`  retry ${id}.${k} (recall ${score.toFixed(2)}, ${wps.toFixed(1)} w/s): "${heard}"`);
    }
    writeFileSync(p, best.buf);
    if (best.score < 0.9) console.error(`  ! ${id}.${k} best recall only ${best.score.toFixed(2)}`);
    parts.push(p);
  }
  // Trim edge silence per sentence, join with a fixed gap, slow slightly (pitch-preserving).
  const out = join(ROOT, "assets", "voice", `${id}.wav`);
  const inputs = parts.flatMap((p) => ["-i", p]);
  const trims = parts
    .map((_, i) => `[${i}:a]aresample=24000,silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse,apad=pad_dur=${GAP}[s${i}]`)
    .join(";");
  const cat = parts.map((_, i) => `[s${i}]`).join("") + `concat=n=${parts.length}:v=0:a=1,atempo=${TEMPO},adelay=150|150[out]`;
  sh("ffmpeg", ["-y", "-v", "error", ...inputs, "-filter_complex", `${trims};${cat}`, "-map", "[out]", "-ar", "24000", "-ac", "1", out]);
  const words = transcribe(out).map((w, i) => ({ id: `w${i}`, text: w.text, start: w.start, end: w.end }));
  const d = duration(out);
  console.error(`  voice ${id}: ${d.toFixed(2)}s, ${words.length} words, recall ${recall(text, words.map((w) => w.text).join(" ")).toFixed(2)}`);
  return { id, path: `assets/voice/${id}.wav`, duration_s: Math.round(d * 1000) / 1000, words };
}

mkdirSync(TMP, { recursive: true });
mkdirSync(join(ROOT, "assets", "voice"), { recursive: true });
const lines = parseScript(readFileSync(join(ROOT, "SCRIPT.md"), "utf8")).filter((l) => !ONLY || ONLY.includes(l.id));
const neutralPath = join(ROOT, "audio_engine_meta.json");
const prev = existsSync(neutralPath) ? JSON.parse(readFileSync(neutralPath, "utf8")) : { voices: [], sfx: [], bgm: null };
const byId = new Map(prev.voices.map((v) => [v.id, v]));
for (const l of lines) byId.set(l.id, await synthLine(l));
const voices = [...byId.values()].sort((a, b) => a.id.localeCompare(b.id));
const neutral = {
  ...prev,
  tts_provider: "qwen3-local",
  voice_id: REF,
  voices,
  total_duration_s: Math.round(voices.reduce((a, v) => a + v.duration_s, 0) * 1000) / 1000,
};
writeFileSync(neutralPath, JSON.stringify(neutral, null, 2));
const meta = {
  bgm: prev.bgm ?? null,
  bgm_pending: false,
  voices: voices.map((v) => ({ frame: Number(v.id), path: v.path, duration_s: v.duration_s, words: v.words })),
  sfx: (prev.sfx ?? []).map((s) => ({ frame: Number(s.id), file: s.file, offset_s: s.offset_s ?? 0, duration_s: s.duration_s ?? 1, volume: s.volume ?? 0.35 })),
};
writeFileSync(join(ROOT, "audio_meta.json"), JSON.stringify(meta, null, 2));
console.log(`✓ qwen-tts: ${voices.length} voices, ${neutral.total_duration_s}s total`);
