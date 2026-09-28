# Lesson video kit

The build scripts shared by every current lesson video. A lesson folder under `videos/<course>/<lesson>/` holds only its own content (brief, script, scenes, voice, assets); the scripts live here and take the lesson folder as their working directory or argument.

Reference lesson to copy: [`videos/foundations-101/F101.7-agentic-system`](../../videos/foundations-101/F101.7-agentic-system). Lessons under `videos/_legacy/` were built before this kit and are not templates.

## Pipeline

```text
STORYBOARD.md + storyboard.html   one still sketch per section; the owner confirms the layout before any voice
  │
  ▼
SCRIPT.md            narration, one "## Title (frame N)" section per scene, text indented 4 spaces
  │ node ../../../shared/video-kit/qwen-tts.mjs --ref bliu-voice [--only 02,05]   (run inside the lesson folder)
  ▼
assets/voice/NN.wav + audio_meta.json   one take per section, with word timestamps
  │ python3 shared/video-kit/assemble.py videos/<course>/<lesson>
  ▼
audio/narration-bliu.wav   sections trimmed, 0.8 s gaps, 1.0 s before the last section
compositions/NN-*.html     src/NN-*.html with placeholders and {{T:phrase}} cue times filled in
index.html                 the root composition: one sub-composition per section, plus the narration
  │ npm run check, then npm run render (hyperframes, pinned in package.json)
  ▼
videos/<lesson-file-name>.mp4
```

`src/NN-*.html` is scene NN for voice section NN+1; the counts must match or `assemble.py` stops.

## What a lesson folder contains

| Path | Edit it? | Notes |
|---|---|---|
| `BRIEF.md`, `SCRIPT.md` | yes | brief frontmatter follows `/hyperframes`; `SCRIPT.md` is the TTS source |
| `STORYBOARD.md`, `storyboard.html` | yes | the plan and the sketch sheet the owner confirms; sketches live only here, never in `src/` |
| `src/NN-*.html` | yes | the scenes; the only place animation is written |
| `assets/shared.css`, `assets/logos.json`, `assets/fonts/` | yes | per lesson, because lessons use different logos and components |
| `assets/voice/`, `audio_meta.json`, `audio_engine_meta.json` | generated | by `qwen-tts.mjs` |
| `compositions/`, `index.html`, `audio/narration-bliu.wav` | generated | by `assemble.py`; never hand-edit |
| `package.json`, `hyperframes.json`, `meta.json` | rarely | copy from the reference lesson and rename |

## Placeholders in `src/`

| Placeholder | Becomes |
|---|---|
| `{{T:phrase}}` | scene-relative start of the first word of `phrase` in this section's narration; `{{T:phrase+0.4}}` adds an offset |
| `{{DUR}}` | the scene's duration in seconds |
| `{{FONTS}}` | the three `@font-face` rules (Literata, IBM Plex Sans, JetBrains Mono) |
| `{{H}}` | the GSAP timeline and helpers `A` (rise in), `P` (pop), `OUT`, `DRAW` (stroke), `LOOP` |
| `{{I:name}}` | an icon from `ICONS` in `build.py`, else a logo from the lesson's `assets/logos.json` |
| `{{CLAUDE}}` | the Claude Code logo from `assets/logos.json` |

Anchor every cue to a phrase. A time in seconds drifts the moment a section is re-recorded; the only literal times should be small offsets inside a scene's first second. When the transcript mishears a word (“Aledade” as “LDAs”), `cue()` falls back to the closest-scoring window and prints `fuzzy cue`: read that line and check it landed on the right word.

## Checks before render

1. `python3 shared/video-kit/assemble.py <lesson>` prints the scene count and total length; compare with the lesson file's **Duration**.
2. `npm run check` inside the lesson folder.
3. Frame QA with the `video-frame-qa` skill, and layout with `video-layout-polish` when the user reports UI problems.
4. Stop any Studio preview before scripted edits: it stamps `data-hf-id` attributes into `src/`.

## Changing the kit

A change here reaches every current lesson. After editing `assemble.py` or `build.py`, re-run it for each lesson under `videos/` (not `_legacy/`) and confirm `git diff` on `compositions/`, `index.html` and `audio/` is empty, or that every difference is intended. For a lesson not yet in git, `git diff` shows nothing either way: hash those outputs before the change (`find compositions index.html audio -type f -exec md5 -r {} \; | sort -k2`) and compare after. Add a new icon to `ICONS` rather than inlining SVG in one lesson.
