---
name: lesson-video
description: Make, revise, or re-render an AI learning program lesson video (AI Foundations 101, Building with AI 201, AI Thinking 201) end to end, from a rough idea or an existing lesson draft through a Codex Astra script review, owner approval, build, frame QA and render. Use when the user asks to produce a lesson's video (e.g. "make the T201.3 video", "build B201.4"), turn an idea into a lesson video, improve a lesson's A-roll or B-roll, change a lesson video's narration, scenes or timing, or re-render one. Routes framework work to /hyperframes; this skill owns the order of steps and where each reference lives.
---

# Lesson video

This skill holds the steps. The facts live in the files it links, one place each; read them instead of restating them.

**A-roll** is the narration (`## A-roll script` in the lesson file). **B-roll** is what's on screen (`## Visual treatment` and `## On-screen cues`). The lesson file is the source of truth for both; `SCRIPT.md` and `src/` follow it.

These videos are **voice-only**: narration from the local `bliu-voice` clone, full-frame animated scenes, no avatar. Ignore the root `CLAUDE.md` HeyGen avatar and HeyGen pacing sections; `assemble.py` handles section gaps.

## References

| Need | File |
|---|---|
| Lesson shape, required sections | `shared/lesson-template.md`; reference lesson `courses/foundations-101/lessons/F101.8-permission-modes-and-undo.md` |
| Narration wording and tone | `shared/wording-content-reference.md` |
| Palette, type, logos | `shared/branding-kit/heygen-brand-kit.md`, `shared/design.md`, `shared/app-logos.md` |
| Claude Code terminal scenes | `shared/cc-cli-refence/` |
| Review protocol and a finished example | `courses/foundations-101/reviews/F101.8-review.md` |
| Build scripts, placeholders, pipeline | `shared/video-kit/GUIDE.md` |
| Export name, publishing checklist | root `CLAUDE.md` ("Video export", "Publishing", "Knowledge sharing") |
| Reference video project to copy | `videos/foundations-101/F101.7-agentic-system` |

Paths: lessons are in `courses/foundations-101/lessons/` or `courses/<course>/201/lessons/`; reviews in the sibling `reviews/` folder; video projects in `videos/<slug>/<lesson>/`, where the slug is `foundations-101`, `building-with-ai-201` or `ai-thinking-201`. Lessons in `videos/_legacy/` predate the kit; never copy them as a template.

## 1. Intake: draft or idea

- **A lesson file exists** (most 201 lessons do): improve it; don't start over. Keep its key concept, learner outcome, exercise, boundary and duration target (201 lessons: 2–3 minutes) unless the user asks to change them. Bring it up to the reference lesson's shape:
  - A-roll: the fixed series opening and close from `shared/lesson-template.md`; one idea per section, each headed by a timing line like `(0:09–0:27) | Who Approves Each Step` computed at 136 wpm with 0.8 s section gaps (1.0 s before the close); a `**Timing basis:**` header line; plain spoken English; a concrete example from analytics work.
  - B-roll: add `## Visual treatment` (layout, the recurring component, dark or light scenes) and expand `## On-screen cues` to one bullet per section naming what appears and the phrase it lands on. The existing cues are the brief; keep their intent.
- **Only an idea**: ask for the course, the audience, and the one thing the learner should do afterwards, then write a new lesson file from `shared/lesson-template.md` in the reference lesson's shape. Propose the next free lesson code and confirm it with the user.

## 2. Codex Astra review, before the owner sees it

Create the review doc in the lesson's `reviews/` folder as `<code>-review.md`. Copy F101.8's review header (title, lesson link, Reviewer/Author/Owner lines) and its "How this works" section, then write this lesson's "Fixed constraints": owner decisions, product facts, the duration target, and anything from intake the reviewer must not undo.

Each round, from the repo root:

```bash
codex exec -m gpt-6-astra -s read-only -C . -o /tmp/<code>-round-N.md - <<'EOF'
You are the reviewer in <review doc path>. Read that file's protocol and fixed constraints, the lesson
<lesson path>, shared/lesson-template.md, shared/wording-content-reference.md, shared/design.md, and the
reference lesson courses/foundations-101/lessons/F101.8-permission-modes-and-undo.md for shape.
Write Round N (reviewer) exactly as the protocol specifies: a verdict (ALIGNED or CHANGES NEEDED), then
numbered findings under ### A-roll, ### B-roll and ### Sync, each quoting the line and proposing
replacement wording or a cue fix. From round 2, first close or reopen every earlier finding against the
edited lesson. Output only the Markdown for this round. Do not edit files.
EOF
```

Then:

1. Append the output to the review doc as `## Round N (reviewer)`.
2. Under each finding, add `**Author:**` with Accepted, Changed differently (why), or Declined (why), and edit the lesson to match.
3. Repeat until the verdict is ALIGNED. After four rounds, stop and hand the open findings to the owner.
4. Add `## Outcome` (rounds, date), and a `**Script review:**` line in the lesson file linking the review doc.

If `codex exec` fails (not installed, gateway auth expired), say so and stop. Don't substitute your own review for Astra's.

## 3. Owner review of the script

Show the owner the A-roll, the on-screen cues and the review outcome, then **wait**. Record their changes in the review doc as `## Owner feedback` (O.1, O.2, …) and apply them. A change to a claim or to meaning gets one more Astra round; a wording change doesn't. Show the changed lines and wait for approval again. No narration is synthesized before the owner approves.

## 4. Build the first draft

1. **Scaffold** `videos/<slug>/<lesson>/` by copying the reference project's `package.json`, `hyperframes.json`, `meta.json`, `CLAUDE.md`, `AGENTS.md` and `assets/` (not `voice/`); rename the project in `package.json` and `meta.json`. Don't run `hyperframes init`: it writes a generic `CLAUDE.md` listing workflows this course doesn't use.
2. **Brief.** `BRIEF.md` with the reference's frontmatter shape (`workflow: general-video`, `destination: internal-course`, `style_preset: a1-brand, creative motion`), the lesson's one-sentence `message`, and its visual treatment.
3. **Script.** `SCRIPT.md`: one `## Title (frame N)` section per lesson section, text indented four spaces, the approved A-roll exactly, with spelling changed only for pronunciation.
4. **Voice.** From the lesson folder: `node ../../../shared/video-kit/qwen-tts.mjs --ref bliu-voice`. Needs the local Qwen3-TTS server; if it isn't running, stop and tell the user.
5. **Scenes.** Load `/hyperframes`, then `/hyperframes-core` and `/hyperframes-animation`. Write `src/NN-*.html`, one per section, from the approved on-screen cues. Every cue is `{{T:phrase}}`, never seconds.
6. **Assemble** with the kit (`GUIDE.md`) and compare the total with the lesson's timing, then `npm run check` (0 errors).

## 5. Frame QA on the first draft

Run the `video-frame-qa` skill on the draft and apply its one-batch fix pass. Then confirm every on-screen cue from the lesson file appears at its phrase.

## 6. Sample review, render, publish

1. Show the owner the frame-QA contact sheets (and a short render of one scene if they ask). **Wait for approval** of the content-to-visual mapping before rendering.
2. If the owner flags geometry (uneven rings, mismatched boxes, arrows across borders), run `video-layout-polish`, then re-run `video-frame-qa` and show them again.
3. After approval: `npm run render`, export under the canonical lesson name, set the lesson file's **Duration** from the render, and follow the root `CLAUDE.md` publishing checklist.

## Revise an existing lesson video

- **Wording:** edit the lesson file first. A change to a claim or to meaning goes through one Astra round (step 2). Mirror the change into `SCRIPT.md`, regenerate only the changed sections with `--only NN`, and assemble. Cues move with the words.
- **Visuals:** edit `src/` and `assets/shared.css`, assemble, check, then step 5.
