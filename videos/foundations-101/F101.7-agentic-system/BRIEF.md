---
workflow: general-video
flow: automation
storyboard: no
message: "An agent is a model, tools, and context joined by a loop inside a harness; name the parts to find the one that failed. A subagent works in its own context, so it can check from the source if the brief lets it."
destination: internal-course
aspect: 1920x1080
language: en
audience: analytics professionals who completed the F101.2 Jaffle Shop exercise
length: 4m23s
style_preset: a1-brand, creative motion
---

## Intent

Voice-only build in the F101.5 style: dark and white scenes, mocked animated components, no live-tool screenshots. Narrated by the owner's local voice clone (`bliu-voice`).

## Assets

- `../../../courses/foundations-101/lessons/F101.7-what-makes-ai-agentic.md`: approved narration and cue source.
- `../../../shared/branding-kit/heygen-brand-kit.md` and `../../../shared/design.md`: palette, type, logo rules.
- `audio/narration-bliu.wav`: assembled from `assets/voice/NN.wav` by `shared/video-kit/assemble.py`.

## Customizations

- Recurring components: agent diagram (model node, tool chips, context window, loop ring) inside a harness frame; a second sealed context window for the subagent.
- Jaffle Shop filenames and numbers are the real F101.2 exercise data.

## Notes

- Scene script passed an external review (2026-09-25), then a newcomer read and a visual QA pass.
