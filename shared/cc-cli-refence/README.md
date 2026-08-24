# cc-cli-ref — Claude Code CLI reference composition

**This is the canonical template for any "Claude Code" / terminal scene in the teaser.**
Every video segment that depicts the Claude Code CLI (the hook split-screen, the
teaser loop, future episodes) should **copy or edit `index.html` from here** instead of
rebuilding the terminal look from scratch. This keeps all terminal scenes visually
consistent and saves tokens.

## How to reuse

1. Copy this project (or just `index.html`) into the target segment's folder, or edit
   in place for a variant.
2. Swap the **content** — the prompt text, tool-call lines, diff, response, todo items —
   and adjust `data-start` / `data-duration` timings for the new beat.
3. Keep the **style layer** (`:root` tokens, `.screen` / `.statusbar` / `.diff` /
   `.inputbar` / `.todo` CSS) intact so it matches every other terminal scene.
4. Run `npm run check` before handoff.

## Component patterns (match these exactly — they mirror real Claude Code)

These are the pieces most often gotten wrong. Copy the markup/CSS from `index.html`
rather than re-inventing them:

- **Thinking line**: coral `✳` spinner + **coral bold gerund verb** (`Cogitating…`) +
  **gray metadata in parens** (`(1.4s · ↑1.2k tokens · esc to interrupt)`), with an
  optional gray `└` tree sub-line underneath. The verb is coral, NOT muted gray.
- **Tool-call lines**: green `●` bullet + verb + blue `#5A9CF8` path + faint detail
  (e.g. `● Read src/status.ts  (42 lines)`).
- **Todo checkboxes** (`.todo` / `.titem`), three states:
  - **done** = green `✓` check with NO box + label **struck through** and dimmed to `#9B9B9B`.
  - **in-progress** = filled **coral `■` square** (`#D97757`) + **bold** full-white
    (`#E5E5E5`) label, NOT struck through.
  - **pending** = empty square outline (`#6B6B6B` border, no fill) + normal `#E5E5E5` text.

  On completion an item flips in place: in-progress → done (square cross-fades to the green
  check, label gains its strikethrough). All marks are **CSS-drawn** (`.check-glyph` /
  `.sq-glyph` / `.box-glyph`) — do NOT use unicode `☑`/`☐`, which render too thin in
  monospace, and do NOT wrap done items in a rounded bordered box.
- **Response line**: coral `⏺` glyph + text; wrap paragraphs with `.para`.
- **Input box**: the one framed element — rounded, `#262626` fill, coral `>` + blinking caret.

## Style source of truth

Course colors and typography live in `../branding-kit/heygen-brand-kit.md`. Terminal behavior, motion, and layout rules live in `../design.md` § 6.
(**Claude Code Style — Terminal UI**). The tokens in `index.html`'s `:root` mirror that
section; if they ever diverge, `design.md` wins.

## What this composition shows

An ~8.5s single-scene CLI session: typewriter prompt → thinking spinner → `Read` / `Edit`
tool calls → colorized diff → response line → todo checklist with a pending→checked flip,
plus the framed input box with a blinking caret. 1920×1080, one paused GSAP timeline,
fully deterministic (no clocks / random / network).

## Commands

```bash
npm run dev      # preview server (run in background)
npm run check    # lint + validate + inspect
npm run render   # render to MP4
```
