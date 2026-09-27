---
name: lesson-video
description: Make, revise, or re-render an AI learning program lesson video (AI Foundations 101, Building with AI 201, AI Thinking 201) with the shared video kit and HyperFrames. Use when the user asks to produce the video for a lesson (e.g. "make the F101.9 video", "build B201.4"), change a lesson video's narration, scenes, or timing, or re-render one. Routes framework work to /hyperframes; this skill owns the order of steps and where each reference lives.
---

# Lesson video

This skill holds the steps. The facts live in the files it links, one place each; read them instead of restating them, and don't copy their rules into the lesson.

## References

| Need | File |
|---|---|
| Narration wording and tone | `courses/<course>/lessons/<lesson>.md` (source of truth), `shared/wording-content-reference.md` |
| Palette, type, logos | `shared/branding-kit/heygen-brand-kit.md`, `shared/design.md`, `shared/app-logos.md` |
| Claude Code terminal scenes | `shared/cc-cli-refence/` |
| Build scripts, placeholders, pipeline | `shared/video-kit/GUIDE.md` |
| Pacing, voice, export name, publishing checklist | repo root `CLAUDE.md` |
| Series order and review gate | `courses/foundations-101/production-plan.md` |
| Reference lesson to copy | `videos/foundations-101/F101.7-agentic-system` |

Lessons in `videos/_legacy/` (F101.0–F101.5, B201.7) predate the kit. Never copy them as a template.

## New lesson

1. **Read** the lesson file and the reference lesson's `BRIEF.md`, `SCRIPT.md` and two or three `src/` scenes.
2. **Scaffold** `videos/<course>/<lesson>/` by copying the reference lesson's `package.json`, `hyperframes.json`, `meta.json`, `CLAUDE.md`, `AGENTS.md` and `assets/` (not `voice/`), then rename the project in `package.json` and `meta.json`. Do not run `hyperframes init`: it writes a generic scaffold `CLAUDE.md` that lists workflows this course doesn't use.
3. **Brief.** Write `BRIEF.md` with the same frontmatter shape as the reference (`workflow: general-video`, `destination: internal-course`, `style_preset: a1-brand, creative motion`), the lesson's one-sentence `message`, and its layout from the production plan's lesson-variation table.
4. **Script.** Write `SCRIPT.md`: one `## Title (frame N)` section per scene, text indented four spaces, the lesson's A-roll exactly, with spelling changed only for pronunciation.
5. **Voice.** From the lesson folder: `node ../../../shared/video-kit/qwen-tts.mjs --ref bliu-voice`. Needs the local Qwen3-TTS server; if it isn't running, stop and tell the user.
6. **Scenes.** Load `/hyperframes`, then `/hyperframes-core` and `/hyperframes-animation`, and write `src/NN-*.html`, one per section. Every cue is `{{T:phrase}}`, never a time in seconds. Use `{{I:name}}` icons; a missing icon goes into the kit's `ICONS`, not inline in one lesson.
7. **Assemble.** `python3 ../../../shared/video-kit/assemble.py .` and check the total against the lesson's **Duration**. Read every `fuzzy cue` line it prints and fix the phrase if it matched the wrong words.
8. **QA.** `npm run check` (0 errors), then the `video-frame-qa` skill; use `video-layout-polish` for geometry problems.
9. **Review gate.** Per the production plan, the content-to-visual mapping and a rendered sample need reviewer approval before the next lesson starts. Show the user the contact sheet and wait.
10. **Render and publish** only after approval: `npm run render`, export to `videos/<lesson-file-name>.mp4`, then the root `CLAUDE.md` publishing checklist.

## Revise an existing lesson

- Wording: edit the lesson file first, mirror it into `SCRIPT.md`, regenerate only the changed sections with `--only NN`, then assemble. Cues move with the words.
- Visuals: edit `src/` and `assets/shared.css`, assemble, check, QA. Never hand-edit `compositions/`, `index.html` or `audio/`.
- Stop any Studio preview before scripted edits (it stamps `data-hf-id` into `src/`).

## Changing the kit

A kit change reaches every current lesson. Follow "Changing the kit" in `shared/video-kit/GUIDE.md`: re-assemble each lesson under `videos/` and confirm the generated files are unchanged, or that every difference is intended.
