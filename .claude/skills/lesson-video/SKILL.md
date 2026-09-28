---
name: lesson-video
description: Make, revise, or re-render an AI learning program lesson video (AI Foundations 101, Building with AI 201, AI Thinking 201) end to end, from a rough idea or an existing lesson draft through a script self-check, owner approval, a storyboard the owner confirms, build, frame QA and render. Use when the user asks to produce a lesson's video (e.g. "make the T201.3 video", "build B201.4"), turn an idea into a lesson video, improve a lesson's A-roll or B-roll, change a lesson video's narration, scenes or timing, or re-render one. Routes framework work to /hyperframes; this skill owns the order of steps and where each reference lives.
---

# Lesson video

This skill holds the steps. The facts live in the files it links, one place each; read them instead of restating them.

**A-roll** is the narration (`## A-roll script` in the lesson file). **B-roll** is what's on screen (`## Visual treatment` and `## On-screen cues`). The lesson file is the source of truth for both; `SCRIPT.md`, `STORYBOARD.md` and `src/` follow it.

These videos are **voice-only**: narration from the local `bliu-voice` clone, full-frame animated scenes, no avatar. Ignore the root `CLAUDE.md` HeyGen avatar and HeyGen pacing sections; `assemble.py` handles section gaps.

## References

| Need | File |
|---|---|
| Lesson shape, required sections | `shared/lesson-template.md`; reference lesson `courses/foundations-101/lessons/F101.8-permission-modes-and-undo.md` |
| Narration wording and tone | `shared/wording-content-reference.md` |
| Palette, type, logos | `shared/branding-kit/heygen-brand-kit.md`, `shared/design.md`, `shared/app-logos.md` |
| Claude Code terminal scenes | `shared/cc-cli-refence/` |
| Storyboard sheet and review loop | `/hyperframes-creative` `references/storyboard-recipe.md` § 3; `/hyperframes` `references/review-loop.md`, `storyboard-format.md` |
| Build scripts, placeholders, pipeline | `shared/video-kit/GUIDE.md` |
| Export name, publishing checklist | root `CLAUDE.md` ("Video export", "Publishing", "Knowledge sharing") |
| Reference video project to copy | `videos/foundations-101/F101.7-agentic-system` |

Paths: lessons are in `courses/foundations-101/lessons/` or `courses/<course>/201/lessons/`; reviews in the sibling `reviews/` folder; video projects in `videos/<slug>/<lesson>/`, where the slug is `foundations-101`, `building-with-ai-201` or `ai-thinking-201`. Lessons in `videos/_legacy/` predate the kit; never copy them as a template.

## 1. Intake: draft or idea

- **A lesson file exists** (most 201 lessons do): improve it; don't start over. Keep its key concept, learner outcome, exercise, boundary and duration target (201 lessons: 2–3 minutes) unless the user asks to change them. Bring it up to the reference lesson's shape:
  - A-roll: the fixed series opening and close from `shared/lesson-template.md`; one idea per section, each headed by a timing line like `(0:09–0:27) | Who Approves Each Step` computed at 136 wpm with 0.8 s section gaps (1.0 s before the close); a `**Timing basis:**` header line; plain spoken English; a concrete example from analytics work.
  - B-roll: add `## Visual treatment` (layout, the one element that stays on screen across sections, dark or light scenes) and expand `## On-screen cues` to one bullet per section naming what appears and the phrase it lands on. The existing cues are the brief; keep their intent.
  - For each section, the cues also say what the element that stays on screen shows now (F101.8: the approver slot is you in manual, nobody in accept edits, the plan in plan mode, a second model in auto), and end on what carries into the next section, so scenes hand off instead of fading.
- **Only an idea**: ask for the course, the audience, and the one thing the learner should do afterwards, then write a new lesson file from `shared/lesson-template.md` in the reference lesson's shape. Propose the next free lesson code and confirm it with the user.

## 2. Self-check, before the owner sees it

One pass, by a fresh subagent that did not write the script, so it reads the draft cold. Same model on purpose: a second model's rounds pull the wording toward its own taste without changing the lesson much.

Give the subagent the lesson path, `shared/lesson-template.md`, `shared/wording-content-reference.md`, `shared/design.md` and the reference lesson, plus the fixed constraints below. It checks, and reports each problem with the line quoted and a fix:

1. The lesson follows the template shape, and the timing lines add up to the duration target.
2. Plain spoken English per the wording reference; no em dashes.
3. Every fact matches the source it cites in `Source references`. This is the check that matters most: F101.8's review caught two wrong facts (how long "don't ask again" lasts; what rewind can't undo).
4. One idea per cue, and each cue's landing phrase appears word for word in the narration.
5. Each section states the element's current state and what carries into the next section.

Create `<code>-review.md` in the lesson's `reviews/` folder: title, lesson link, `## Fixed constraints` (owner decisions, product facts, the duration target, anything from intake the check must not undo), then `## Self-check` with each finding and what you did about it (fixed, or left for the owner and why). End it with what the subagent wasn't sure about, so the owner knows where to look. Apply the fixes to the lesson, and add a `**Script review:**` line in the lesson file linking the review doc.

## 3. Owner review of the script

Show the owner the A-roll, the on-screen cues and the self-check notes, then **wait**. Record their changes in the review doc as `## Owner feedback` (O.1, O.2, …) and apply them. When a change touches a fact, re-read the cited source for it and note the result under that O entry; a wording change needs no check. Show the changed lines and wait for approval again. No sketch or narration is made before the owner approves.

## 4. Storyboard

1. **Scaffold** `videos/<slug>/<lesson>/` by copying the reference project's `package.json`, `hyperframes.json`, `meta.json`, `CLAUDE.md`, `AGENTS.md` and `assets/` (not `voice/`); rename the project in `package.json` and `meta.json`. Don't run `hyperframes init`: it writes a generic `CLAUDE.md` listing workflows this course doesn't use.
2. **Brief.** `BRIEF.md` with the reference's frontmatter shape (`workflow: general-video`, `destination: internal-course`, `style_preset: a1-brand, creative motion`) but `storyboard: yes`, keeping `flow: automation` (that pair derives `mode: collaborative`), plus the lesson's one-sentence `message` and its visual treatment.
3. **`STORYBOARD.md`** at the project root: frontmatter with `mode: collaborative`, then one `## Frame N — Title` block per lesson section with `status: outline`, `duration` from the lesson's timing line (a 136 wpm estimate until the voice exists), `voiceover` (the section's narration), `src: src/NN-*.html`, and the section's cues as the narrative.
4. **`storyboard.html`** at the project root, per `storyboard-recipe.md` § 3: one still cell per section with `id="frame-NN"`, drawn inline with the real fonts, brand colors and on-screen text from `shared/design.md` and `assets/shared.css` (this course's stand-in for `frame.md`). Each cell's note names the phrase the key cue lands on and what carries into the next section. Never put sketches in `src/`: `assemble.py` stops if the scene count and voice section count differ.
5. Mark each frame `built`, give the owner the path to open in a browser, and **wait**. Redraw only the cells they name, bump the sheet's version, and show it again until they confirm the layout.

## 5. Build the first draft

1. **Script.** `SCRIPT.md`: one `## Title (frame N)` section per lesson section, text indented four spaces, the approved A-roll exactly, with spelling changed only for pronunciation.
2. **Voice.** From the lesson folder: `node ../../../shared/video-kit/qwen-tts.mjs --ref bliu-voice`. Needs the local Qwen3-TTS server; if it isn't running, stop and tell the user.
3. **Scenes.** Load `/hyperframes`, then `/hyperframes-core` and `/hyperframes-animation`. Write `src/NN-*.html`, one per section, from its confirmed sketch: keep the layout, add the motion. Build inline, scene by scene; skip `/general-video`'s frame-packet workers, which write into `compositions/`, a folder `assemble.py` owns. Every cue is `{{T:phrase}}`, never seconds. Mark each frame `animated`.
4. **Assemble** with the kit (`GUIDE.md`) and compare the total with the lesson's timing. For every `fuzzy cue` line it prints, check the word it landed on; if that's the wrong word, reword the cue phrase to match the narration exactly and assemble again. Then `npm run check` (0 errors).

## 6. Frame QA on the first draft

Run the `video-frame-qa` skill on the draft and apply its one-batch fix pass. Then confirm every on-screen cue from the lesson file appears at its phrase, and each scene still reads as its confirmed sketch.

## 7. Sample review, render, publish

1. Show the owner the frame-QA contact sheets (and a short render of one scene if they ask). **Wait for approval** before rendering. Content was settled in step 3 and layout in step 4, so this look is mostly about motion and polish.
2. If the owner flags geometry (uneven rings, mismatched boxes, arrows across borders), run `video-layout-polish`, then re-run `video-frame-qa` and show them again.
3. After approval: `npm run render`, export under the canonical lesson name, set the lesson file's **Duration** from the render, and follow the root `CLAUDE.md` publishing checklist.

## Revise an existing lesson video

- **Wording:** edit the lesson file first. A change to a fact is re-checked against its cited source (step 3). Mirror the change into `SCRIPT.md`, regenerate only the changed sections with `--only NN`, and assemble. Cues move with the words.
- **Visuals:** a layout change to a section updates its `storyboard.html` cell first and waits for the owner; a motion or polish fix goes straight to `src/` and `assets/shared.css`. Assemble, check, then step 6.
