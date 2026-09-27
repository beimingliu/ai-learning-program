# AI Learning Program

Course curriculum plus the avatar-narrated lesson videos built from it. See `README.md` for the course inventory.

- `courses/<course>/lessons/*.md` — canonical lesson scripts (source of truth for naming)
- `videos/<course>/<lesson>/` — one HyperFrames composition project per current lesson, built with `shared/video-kit/`
- `videos/_legacy/<course>/<lesson>/` — published lessons built before the kit (F101.0–F101.5, B201.7); fix in place, never copy
- `videos/*.mp4` — final exported renders
- `shared/` — facilitator guide, wording reference, QA and accuracy logs
- `shared/video-kit/` — the shared build scripts and `GUIDE.md` for lesson videos

To make or change a lesson video, use the `/lesson-video` skill. It points to every reference below and hands framework work to `/hyperframes`. The reference lesson is `videos/foundations-101/F101.7-agentic-system`.

# Video generation

- Use the HeyGen MCP `create_video_from_avatar` tool for avatar video generation.
- Default to Avatar V with avatar look ID `73db92410a974bbc832b122638fe119f` and voice ID `0f5059914f5041d99c495142fea40c42`.
- Default to 1920×1080, 16:9 MP4 unless the task specifies another format.
- Do not pass `expressiveness` when using Avatar V; the Avatar V engine does not support it.
- Use a different avatar, voice, or engine only when the task explicitly requests one.

# Video export

- Export final HyperFrames MP4s to the project-root `videos/` folder, not into an individual task folder.
- Name each exported MP4 exactly after its canonical lesson filename under `courses/<course>/.../lessons/`, without the `.md` extension. Preserve the course code, capitalization, punctuation, and hyphenation; append `.mp4`.
- Example: `courses/foundations-101/lessons/F101.0-from-chatbot-to-agent.md` → `videos/F101.0-from-chatbot-to-agent.mp4`.

# Publishing

- **Drive:** final MP4s go in the "education videos" folder [`1_uPd_gC_AW6Ee-n0f9BN_8t5b2xVCXH1`](https://drive.google.com/drive/folders/1_uPd_gC_AW6Ee-n0f9BN_8t5b2xVCXH1), one subfolder per course: `foundations-101`, `building-with-ai-201` (`1WMKBHxazfXJ_6UyVZalkfuvCm555XwlL`). The MCP gateway's `drive_files_create` takes metadata only and cannot upload a video, so copy the file into the Drive for Desktop mount at `~/Library/CloudStorage/GoogleDrive-bliu@aledade.com/My Drive/analytics ai fluency/education videos/<course>/` and let it sync. Uploads inherit domain "anyone with the link can view". Link videos as `https://drive.google.com/file/d/<id>/view`.
- **Wiki:** Confluence pages are published from Markdown sources in the `analytics-ai-enablement` repo under `docs/confluence/`; its `README.md` maps each source file to a page ID. Edit the source in a PR first, then publish the full file body. Course pages are siblings under parent `3216572453` in space `IA`: AI Foundations 101 `3219882030`, Building with AI 201 `3219128363`, AI Thinking 201 `3219357757`.
- **Jira:** course video production and publishing is tracked on [AIRML-9771](https://aledade.atlassian.net/browse/AIRML-9771); extend its scope for new lessons rather than opening new tickets.
- **Voice-only lessons** (no avatar) use the local Qwen3 TTS clone `bliu-voice` via `shared/video-kit/qwen-tts.mjs`, run from the lesson folder; see `shared/video-kit/GUIDE.md`.

# Knowledge sharing

- GitHub is the first-class copy. With every video generation, open one PR in `analytics-ai-enablement` that updates the Confluence source (`docs/confluence/<course>.md`) and the matching course README under `workshops/` with the same content.
- Publish that source to the Confluence page first, then push the PR so Git records what is live; record the page version in the PR.
- Checklist per video: MP4 in `videos/`, Drive upload with domain link sharing, lesson file **Duration** and **Published** lines, Confluence section, GitHub README mirror, AIRML-9771 comment, and a commit in this repo.

# Narration pacing

- Do not rely on blank lines, Markdown headings, or ellipses for section timing. In the 2026-08-20 test with the default cloned voice, a blank line produced the exact same audio and timestamps as a normal space. An ellipsis produced a longer pause in one sample but also changed the delivery, so it is not a timing control.
- The HeyGen `create_speech` schema supports `inputType: "ssml"` and second-based `<break>` tags, and the default cloned voice reports `support_pause: true`, but do not combine SSML with production speed control for this voice. In the full-length test, `speed: 1.17` with SSML produced 246.047 seconds while the same approved wording with plain text produced 203.624 seconds. Use plain text with `speed` and create the section pauses locally.
- Use local FFmpeg silence replacement for final timing. After synthesis and any speed adjustment, locate each section boundary from the returned word timestamps and confirm it with `silencedetect`; replace that gap with generated silence. The tested local replacement produced an exact 1.000-second gap.
- Target 0.8 seconds between ordinary sections and 1.0 second before the final Continue Learning or call-to-action section. Count those enforced gaps in the runtime budget and retime spoken intervals rather than compressing the final pauses.
- Before uploading audio for avatar generation, verify the total duration with `ffprobe`, measure every section boundary with `silencedetect`, and spot-check the transition into the final section.

# Narration speed and API efficiency

- Use HeyGen's `speed` parameter to get close to the target speaking duration in the first full production call. Do not generate the full script at 1.00× merely to calibrate it; the current MCP has no batch speech endpoint, and repeating a full call costs more time than a short representative calibration.
- The default cloned voice is not linear across the tested speed settings. On the same short passage, 1.00× produced 4.624 seconds, 1.10× produced 4.284 seconds, and 1.20× produced 3.997 seconds. These samples confirm nonlinearity but did not predict the full-script duration, so use a previous full lesson of similar length for the initial estimate instead of calibrating with a short phrase.
- For an exact runtime, first reserve the enforced section pauses: `spoken target = final target - total enforced pauses`. Choose the HeyGen speed that most closely matches that spoken target, make one plain-text TTS call, then use returned word timestamps to remove the uncontrolled section gaps. Apply the final FFmpeg speed correction only to the spoken intervals and concatenate the exact local pauses afterward.
- Worked example (F101.1): `speed: 1.17` produced 203.624 seconds. Removing its 1.940 seconds of uncontrolled section gaps left 201.684 seconds, which was locally slowed with `atempo=0.9424508869` to the 214-second spoken target. Five 0.8-second pauses and one 1.0-second pause were then inserted to produce exactly 219.000 seconds.
- A higher speech speed shortens the audio but does not guarantee a faster HeyGen server response. The faster workflow comes from reusing this saved calibration and making one full production call. Do not split every section into parallel API calls unless the user accepts the additional calls and possible delivery differences.
