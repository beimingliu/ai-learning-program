---
workflow: general-video
flow: automation
storyboard: no
message: "AI can build the first pass; you control the steps and decide when it is complete"
destination: internal-course
aspect: 1920x1080
language: en
length: 3min38sec
style_preset: a1-brand
---

## Intent

Teach a reproducible analysis workflow with the real Jaffle Shop files as a full-frame, voice-only tutorial. Recreate the learner's Claude Code session: orient to the exercise, stop premature implementation, understand the task, inspect the CSVs, agree on a plan, build a first pass, validate it independently, inspect the HTML, correct it, and decide whether the work is complete.

## Assets

- `courses/foundations-101/lessons/F101.2-first-verified-result.md` — approved narration and cue source.
- `courses/foundations-101/exercises/F101.2-jaffle-shop/` — supplied orders, payments, metric definitions, and license.
- `courses/foundations-101/exercises/F101.2-jaffle-shop/analysis-run/` — Luna Max inspection, calculation, results, verification, and HTML report.
- `courses/foundations-101/exercises/screenshots/` — the learner's real Claude Code prompts and responses.
- `shared/cc-cli-refence/` — canonical Claude Code UI reference for terminal scenes.
- Local Qwen3-TTS zero-shot clone `heygen-beiming-clone` — narration only; do not generate an avatar video.

## Notes

- Use the seven staged prompts, source values, first-pass mismatch, and correction in the lesson file.
- The first-pass handoff is not proof of completion. It keeps the correct $1,103 headline but shows incorrect monthly and payment-method breakdowns. Independent source calculation must expose that mismatch.
- No avatar, persistent logo, subtitles, B-roll, or music.
- The voice track is generated section by section with the local Qwen3-TTS clone and assembled to exactly 218 seconds.
- Preserve 0.8-second pauses between ordinary sections and a 1.0-second pause before Continue Learning in the replacement voice track.
