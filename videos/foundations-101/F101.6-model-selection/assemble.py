"""Build narration, compositions, and index.html from assets/voice/*.wav and src/*.html.

Each src/NN-*.html is the scene for voice section NN+1. {{T:phrase}} resolves to the
scene-relative start of the first word of `phrase` in that section's transcript, so cues
follow the narration when a section is regenerated. {{T:phrase+0.4}} adds an offset.
"""
import json, pathlib, re, subprocess, sys

ROOT = pathlib.Path(__file__).parent
sys.path.insert(0, str(ROOT))
import build  # noqa: E402  (expands fonts, logos, icons, helpers)

TAIL = 0.25  # silence kept after the last word of each section
GAP, LAST_GAP = 0.8, 1.0
TITLE = (ROOT / "meta.json").exists() and json.loads((ROOT / "meta.json").read_text())["name"]

meta = json.loads((ROOT / "audio_meta.json").read_text())
voices = sorted(meta["voices"], key=lambda v: v["frame"])
scenes = sorted((ROOT / "src").glob("*.html"))
assert len(scenes) == len(voices), (len(scenes), len(voices))

norm = lambda s: re.sub(r"[^a-z0-9]+", "", s.lower())


def cue(words, phrase):
    phrase, _, off = phrase.partition("+")
    want = [norm(w) for w in phrase.split() if norm(w)]
    toks = [norm(w["text"]) for w in words]
    for i in range(len(toks)):
        if toks[i : i + len(want)] == want:
            return words[i]["start"] + float(off or 0)
    # Transcripts mishear names ("Aledade" as "LDAs"), so fall back to the closest window.
    import difflib
    best = max(range(len(toks)), key=lambda i: difflib.SequenceMatcher(None, "".join(want), "".join(toks[i : i + len(want)])).ratio())
    score = difflib.SequenceMatcher(None, "".join(want), "".join(toks[best : best + len(want)])).ratio()
    if score < 0.6:
        raise SystemExit(f"cue not found: {phrase!r}")
    print(f"  fuzzy cue {phrase!r} -> {' '.join(w['text'] for w in words[best:best+len(want)])!r} ({score:.2f})")
    return words[best]["start"] + float(off or 0)


tmp = ROOT / ".hyperframes" / "assemble"
tmp.mkdir(parents=True, exist_ok=True)
parts, rows, t = [], [], 0.0
for i, (v, src) in enumerate(zip(voices, scenes)):
    last = i == len(voices) - 1
    speech = v["words"][-1]["end"] + TAIL
    gap = 0 if last else (LAST_GAP if i == len(voices) - 2 else GAP)
    seg = tmp / f"{i:02d}.wav"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", ROOT / v["path"], "-af", f"atrim=0:{speech},apad=pad_dur={gap}", "-ar", "24000", "-ac", "1", seg], check=True)
    dur = speech + gap
    html = build.expand(src.read_text())
    html = re.sub(r"\{\{T:([^}]+)\}\}", lambda m: f"{cue(v['words'], m.group(1)):.2f}", html)
    html = html.replace("{{DUR}}", f"{dur:.2f}")
    (ROOT / "compositions" / src.name).write_text(html)
    sid = src.name[:2]
    rows.append(f'      <div id="el-s{sid}" data-composition-id="s{sid}" data-composition-src="compositions/{src.name}" data-start="{t:.2f}" data-duration="{dur:.2f}" data-track-index="1" data-width="1920" data-height="1080"></div>')
    parts.append(seg)
    t += dur

out = ROOT / "audio" / "narration-bliu.wav"
lst = tmp / "list.txt"
lst.write_text("".join(f"file '{p}'\n" for p in parts))
subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", out], check=True)
total = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", out]))

shared = (ROOT / "assets" / "shared.css").read_text()
index = f"""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=1920, height=1080">
    <title>{TITLE}</title>
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <style>
      {build.FONTS}
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ width: 1920px; height: 1080px; overflow: hidden; background: #ffffff; }}
      :root {{ --blue: #003da5; --pale: #eaf2ff; --orange: #ff6900; --ink: #091f31; --muted: rgba(9, 31, 49, 0.72); --line: rgba(0, 61, 165, 0.28);
        --t-bg: #1e1e1e; --t-elev: #262626; --t-fg: #e5e5e5; --t-muted: #9b9b9b; --t-faint: #808080; --t-border: #3a3a3a; --t-coral: #d97757; --t-green: #4ebe96; --t-info: #5a9cf8; }}
      #root {{ position: relative; width: 100%; height: 100%; overflow: hidden; font-family: "IBM Plex Sans", "Helvetica Neue", Arial, sans-serif; color: var(--ink); }}
      #root > div[data-composition-src] {{ position: absolute; inset: 0; }}
{shared}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-width="1920" data-height="1080" data-duration="{t:.2f}">
{chr(10).join(rows)}

      <audio id="narration" src="audio/narration-bliu.wav" data-start="0" data-duration="{total:.2f}" data-track-index="10" data-volume="1"></audio>
    </div>
    <script>
      window.__timelines["main"] = gsap.timeline({{ paused: true }});
    </script>
  </body>
</html>
"""
(ROOT / "index.html").write_text(index)
print(f"assembled {len(rows)} scenes, {t:.2f}s video, {total:.2f}s narration")
