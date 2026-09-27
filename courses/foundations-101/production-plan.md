# Foundations 101 — Sequential Video Production Plan

## Production contract

Each lesson uses the approved narration in `lessons/`. HeyGen MCP generates clean presenter A-roll with the same avatar and voice. HyperFrames adds the teaching cues, applies the A-1 brand system, checks the composition, and renders the final MP4.

F101.2 is the voice-only prototype: use the same cloned voice without an avatar and give the full frame to the real analysis demonstration.

Every A-roll script opens with a series-and-topic introduction of no more than 10 seconds. It closes by inviting learners to explore other videos and send feedback, also in no more than 10 seconds.

Script durations are computed, not estimated. The cloned voice delivers **136 words per minute** in production; each lesson header records this as a `**Timing basis:**` line. Section boundaries carry an enforced 0.8-second gap, and 1.0 second before Continue Learning, inserted locally with FFmpeg after synthesis. A section's stamped window is its word count at 136 wpm — no two sections may share a boundary second.

Videos are produced in lesson order. A Terra/high reviewer must approve each lesson's content-to-visual mapping and rendered sample before the next HeyGen job starts.

## Shared visual system

- 1920×1080, presenter-led split screen, no persistent logo.
- White, brand blue, pale blue, orange signal markers, and dark ink.
- Literata titles and IBM Plex Sans supporting text.
- Presenter audio and picture play at 1.15×.
- One focal teaching idea per cue; no decorative B-roll or subtitles.
- Exact evidence, boundaries, and human decision points stay visible when taught.

## Lesson variation

| Lesson | Split and cue treatment |
|---|---|
| F101.0 | Presenter left; orientation, evidence, mechanics, and series-path panels on the right |
| F101.1 | Presenter left; five-part brief stack and complexity ladder on the right |
| F101.2 | Full-frame voice-only demo; real files, prompt, report, separate calculation, and correction |
| F101.3 | Presenter left; information cards move into six labeled layers on the right |
| F101.4 | Presenter right; three nested CLAUDE.md scopes on the left, stacking in load order |
| F101.5 | Presenter left; file-to-tool-to-MCP access ladder on the right |
| F101.6 | Presenter right; model lanes and task-first diagnostic strip on the left |
| F101.7 | Presenter left; four-part agent diagram on the right, harness as a named outer boundary, subagent as a second sealed context window |

## Per-video call sequence

```text
produceLesson
├── loadApprovedLesson
├── generateAroll
│   ├── heygen.create_video_from_avatar
│   └── heygen.get_video [poll until complete]
├── assembleCourseCut
│   ├── downloadAndProbeAroll
│   ├── transcribeForTiming
│   ├── authorLessonCues
│   └── hyperframes.check --snapshots
├── validateLessonVideo [Terra/high]
│   ├── compareNarrationToLesson
│   ├── inspectContactSheet
│   └── approveOrRequestChanges
├── renderFinalMp4
│   ├── hyperframes.render --quality high
│   └── ffprobe
└── advanceToNextLesson [only after approval]
```

## Output roots

- Course materials: `courses/foundations-101/`
- Video projects: `videos/foundations-101/` (F101.6 onward, built with `shared/video-kit/`); F101.0–F101.5 are in `videos/_legacy/foundations-101/`
- Final MP4s: `videos/`
