# F101.7 narration (TTS source; spelling adjusted for pronunciation)

Spoken text matches the A-roll in the lesson file exactly, apart from pronunciation spellings.

Build (from the lesson folder): `node ../../../shared/video-kit/qwen-tts.mjs --ref bliu-voice [--only 02,05]` writes `assets/voice/NN.wav` and `audio_meta.json`; then `python3 ../../../shared/video-kit/assemble.py .` trims each section, inserts the 0.8s and 1.0s gaps, writes `audio/narration-bliu.wav`, expands `src/` into `compositions/` with `{{T:phrase}}` cue times from the word timings, and rewrites `index.html`. Edit scenes in `src/`, never `compositions/`. See `shared/video-kit/GUIDE.md`.

## Series Introduction (frame 1)

    Welcome to the Analytics AI Enablement education series. Today in Foundations, we focus on the
    agentic system and subagents.

## What Just Happened in There (frame 2)

    You ask Claude a question. It reads six files, runs some code, and hands back a number. What just
    happened in there? You've been using this system for six lessons. This is the one where we open it
    up. Four parts work together, and once you can name them, you can say which one failed, instead of
    blaming the A I.

## The Four Parts (frame 3)

    The model reasons. It reads the goal and decides the next step. That's the part you chose in the
    last lesson. Tools act. They read files, run code, search Glean, and write the report. Without
    tools, the model can only reply. Context is what the model can see right now: your brief, the files
    it has read, and the results so far. You met it in F one oh one point three. The loop joins them.
    Claude gathers context, uses a tool, looks at the result, checks its progress, and then goes around
    again or stops. That loop is what makes it agentic. Claude Code is the harness around all four. It
    decides what the model sees and what it's allowed to do. Building with AI 201 covers it.

## Replay the Jaffle Shop (frame 4)

    Let's replay the Jaffle Shop analysis from F one oh one point two. The brief, the two C S V files,
    and the metric definitions were the context. The model decided to join payments to orders by order
    ID. Tools read the files, ran the calculation, and wrote the H T M L report. The loop went around
    several times: read, calculate, check, and read again. You were in the loop too. You stopped it
    before it wrote code too early, you approved the plan, and you decided when the result was good
    enough. And the first pass wasn't right. The total was correct, but the monthly breakdown was wrong.
    A right total with a wrong breakdown isn't "close enough." One part broke, and you can find which
    one.

## A Second Agent, Fresh Context (frame 5)

    You caught that mismatch with a subagent. A subagent is a second agent that Claude starts for one
    job. It gets its own context window. It doesn't see your conversation. It sees only the brief Claude
    writes for it, and the files it reads itself. It does its job, and it sends back a short summary.
    That separation is the point. An agent checking its own work usually agrees with itself. A fresh
    subagent never saw that reasoning, so it can disagree. But only if you ask it the right way. Tell it
    to calculate from the source files first, and compare with the report second. Then look at how it
    checked. And if both agents read the same flawed file, they can be wrong the same way.

## Find the Part That Failed (frame 6)

    These four parts let the system act. They don't make it right, and any one of them can break. Say
    the report is missing a region. Before you switch models, find out why. If the file was never
    loaded, that's context. If the connector points at the wrong system, that's tools. If Claude stopped
    before checking coverage, that's the loop. If the goal never said which regions to include, the
    brief was the problem, not the model. So ask which part failed, and what evidence shows it.

## Label One Run (frame 7)

    Now try it. Open one agent session you've finished, or use this Jaffle Shop replay. Label the
    model's decision, one tool action, the context it used, one trip around the loop, and one moment you
    stepped in. If a subagent checked the work, note what brief it got and how it checked.

## Continue Learning (frame 8)

    Explore other videos in this series, and leave a comment in the Analytics AI knowledge sharing
    channel so we can improve the course.
