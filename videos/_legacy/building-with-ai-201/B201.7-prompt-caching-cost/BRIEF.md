---
workflow: general-video
flow: automation
storyboard: no
message: "An agent re-reads its whole context on every call; the harness decides whether that re-reading hits the cache"
destination: internal-course
aspect: 1920x1080
language: en
audience: analysts and builders who already run multi-step agent tasks
length: narration-driven, about 4 minutes
---

## Intent

Building with AI 201 lesson B201.7. Explain the KV cache, show measured hit rates by harness, diagnose
why the same GPT models cache in Codex and not in Claude Code through a LiteLLM proxy, and turn it into
four habits. 201 level: more technical than 101 and allowed its own look.

## Assets

- `../../../../courses/building-with-ai/201/lessons/B201.7-prompt-caching-cost.md`: approved narration and cues.
- Narration: cloned `bliu-voice` via the local Qwen3 TTS server (`scripts/qwen-tts.mjs`).
- Fonts copied from F101.4 (Literata, IBM Plex Sans, JetBrains Mono). Three.js vendored in `assets/vendor/`.

## Customizations

- Full frame, voice only, no avatar, no captions, no music.
- Dark "token room" look instead of the 101 white presenter split; brand blue, robin teal and orange kept.
- Three.js for the KV-cache grid (scene 3) and the 100-call cost bars (scene 7).

## Notes

- No company or gateway names on screen; say "a LiteLLM proxy".
- Render only after the owner approves the preview.
