# F101.5 narration source

Use the A-roll script in `../../../courses/foundations-101/lessons/F101.5-tools-mcp-access.md` exactly, excluding timing labels, Markdown formatting, on-screen cues, exercises, boundaries, and source notes.

`audio/f1015-narration-bliu.wav` is the narration timing truth (277.2 seconds, local Qwen3-TTS clone of the owner's voice, 0.8s section gaps and 1.0s before Continue Learning). Scene start times in `index.html` follow its word timings.

Edit scenes in `src/`, then run `python3 build.py` to expand fonts, logos, icons, and timeline helpers into `compositions/`. Stop any Studio preview before scripted edits, because it stamps `data-hf-id` attributes into the source files.
