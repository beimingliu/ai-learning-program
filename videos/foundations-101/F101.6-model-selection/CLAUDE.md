# Course lesson video

This folder is one lesson of the AI learning program, built with the shared kit. Use the `/lesson-video` skill for any work here; it loads `/hyperframes` for framework rules.

- Edit `SCRIPT.md`, `BRIEF.md`, `src/NN-*.html` and `assets/`. Never hand-edit `compositions/`, `index.html` or `audio/narration-bliu.wav`: they are generated.
- Rebuild from this folder: `python3 ../../../shared/video-kit/assemble.py .` (narration: `node ../../../shared/video-kit/qwen-tts.mjs --ref bliu-voice`). Placeholders and the pipeline are in `shared/video-kit/GUIDE.md`.
- After any change: `npm run check`. For a persistent Studio preview use `npx hyperframes preview --background`, check it with `--status` and stop it with `--stop`; stop it before scripted edits, because Studio stamps `data-hf-id` into `src/`.
- The CLI version is pinned in `package.json` so the lesson re-renders identically; don't upgrade it as part of a content change.
