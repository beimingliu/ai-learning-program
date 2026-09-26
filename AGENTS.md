# Local Qwen3-TTS

Use the local Qwen3-TTS service first when generating TTS audio.

The project is at `/Users/beimingliu/beimingliu/tts-playground`.

## Start the service

First-time setup:

```sh
cd /Users/beimingliu/beimingliu/tts-playground
uv venv .venv
uv pip install -r requirements.txt
```

Start the service:

```sh
cd /Users/beimingliu/beimingliu/tts-playground
QWEN_TTS_MAX_TEXT_LENGTH=12000 QWEN_TTS_TARGET_ENGLISH_WPM=140 \
  .venv/bin/python -m uvicorn app.main:app --host 127.0.0.1 --port 8001
```

The web UI is available at <http://127.0.0.1:8001>. The service uses MLX Qwen3-TTS models on Apple Silicon and downloads missing models automatically.

## Generate English course narration by section

For English course narration, use the local zero-shot clone `heygen-beiming-clone` through `/api/clone`. Do not use the built-in `custom_voice` speakers for this narration.

English clone output targets approximately 140 words per minute. The service measures the generated track and applies FFmpeg pitch-preserving tempo correction using `QWEN_TTS_TARGET_ENGLISH_WPM=140`.

The reference must remain the full 203.624-second HeyGen cloned-voice narration and its complete matching 491-word F101.1 A-roll transcript. Do not replace it with a short excerpt.

Generate each labeled theme or section as a separate request by default. Do not generate the entire A-roll in one request unless the user explicitly asks for whole-script or whole-lesson audio.

Before generating, copy the finalized spoken A-roll into `/Users/beimingliu/beimingliu/tts-playground/evaluation/`, then split it into one ordered plain-text file per section. Exclude timing labels, Markdown formatting, on-screen cues, exercises, and other non-spoken text. Preserve the exact wording and section order.

Generate one section at a time:

```sh
cd /Users/beimingliu/beimingliu/tts-playground
curl -sS -X POST http://127.0.0.1:8001/api/clone \
  -F 'text=<evaluation/LESSON_ID/01-series-introduction.txt' \
  -F 'language=English' \
  -F 'reference_id=heygen-beiming-clone'
```

Copy each returned WAV from `generated/` into the lesson's evaluation folder using the same numbered section name. Review each section before assembly. Insert explicit local silence between files instead of relying on paragraph breaks or model-generated pauses:

For each API request, append a disposable tail anchor after the exact section text, such as `The next section begins now.` in a separate paragraph. Do not add the anchor to the saved section text or final narration. Use local speech recognition to confirm the section's expected final words, locate the anchor, and cut before it. During duration fitting, reserve 0.4 seconds of explicit digital silence at the end of every section. The processed section must retain at least 0.2 seconds after the final recognized word when checked with the cached medium speech model. Reject and regenerate any take that runs directly into the anchor or does not preserve the complete final phrase. Matching source text and duration alone are not sufficient verification.

- 0.8 seconds between ordinary sections.
- 1.0 second before the final Continue Learning or call-to-action section.

Concatenate the approved section WAVs and silence clips with FFmpeg. Preserve the section files so an individual section can be regenerated without replacing the rest of the lesson.

# Video generation

- Use the HeyGen MCP `create_video_from_avatar` tool for avatar video generation.
- Default to Avatar V with avatar look ID `73db92410a974bbc832b122638fe119f` and voice ID `0f5059914f5041d99c495142fea40c42`.
- Default to 1920×1080, 16:9 MP4 unless the task specifies another format.
- Do not pass `expressiveness` when using Avatar V; the Avatar V engine does not support it.
- Use a different avatar, voice, or engine only when the task explicitly requests one.

# Video export

- Export final HyperFrames MP4s to the project-root `videos/` folder, not into an individual task folder.
- Name each exported MP4 exactly after its canonical lesson filename under `courses/<course>/.../lessons/`, without the `.md` extension. Preserve the course code, capitalization, punctuation, and hyphenation; append `.mp4`.
- For example, `courses/foundations-101/lessons/F101.0-from-chatbot-to-agent.md` exports as `videos/F101.0-from-chatbot-to-agent.mp4`.

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
- For F101.1, `speed: 1.17` produced 203.624 seconds. Removing its 1.940 seconds of uncontrolled section gaps left 201.684 seconds, which was locally slowed with `atempo=0.9424508869` to the 214-second spoken target. Five 0.8-second pauses and one 1.0-second pause were then inserted to produce exactly 219.000 seconds.
- A higher speech speed shortens the audio but does not guarantee a faster HeyGen server response. The faster workflow comes from reusing this saved calibration and making one full production call. Do not split every section into parallel API calls unless the user accepts the additional calls and possible delivery differences.
