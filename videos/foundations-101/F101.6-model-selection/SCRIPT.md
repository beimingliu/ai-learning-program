# F101.6 narration (TTS source; spelling adjusted for pronunciation)

Spoken text matches the A-roll in the lesson file exactly, apart from pronunciation spellings.

Build: `node scripts/qwen-tts.mjs --ref bliu-voice [--only 02,05]` writes `assets/voice/NN.wav` and `audio_meta.json`; then `python3 assemble.py` trims each section, inserts the 0.8s and 1.0s gaps, writes `audio/narration-bliu.wav`, expands `src/` into `compositions/` with `{{T:phrase}}` cue times from the word timings, and rewrites `index.html`. Edit scenes in `src/`, never `compositions/`.

## Series Introduction (frame 1)

    Welcome to the Analytics AI Enablement education series. Today in Foundations, we focus on model
    selection and effort.

## More Models Than Ever (frame 2)

    Open the model picker, and you'll see a few names. Aledade's model gateway offers many more: Claude
    models from Anthropic, G P T models from OpenAI, and open-weight models like G L M, Kimi, and
    DeepSeek. Open-weight means anyone can download and run the model. On our gateway, they also cost
    much less to use. New models arrive every few weeks. When a result disappoints, the instinct is to
    pick the biggest name and hope. That's usually the wrong first move.

## Fix the Task First (frame 3)

    Before you change the model, check the task. Is the goal specific? Did Claude read the right source?
    Does it have the tool it needs? Is there a check that shows when it's done? A bigger model can't
    open a file it was never given, or fix a metric definition that was wrong to begin with. If your
    brief says count every visit when you meant completed visits, fix the brief, not the model. When
    Claude gets it wrong, look at the context before you touch a setting.

## Two Settings, Two Questions (frame 4)

    Once the task is clear, you have two settings. The model decides how capable the worker is. Effort
    decides how hard it works: how much it reasons, how many files it reads, and how far it goes before
    it checks back with you. So ask one question. Did Claude not know enough, or did it not try hard
    enough? Say Claude gets last month's visit count wrong. If it read the right table, ran your check,
    and still got it wrong, it didn't know enough: pick a stronger model. If it skipped the check, it
    didn't try hard enough: raise the effort. Anthropic's own tests show the same split: more effort
    caught more missed edge cases, but it didn't fix a wrong approach. In Claude Code, type slash
    effort. More effort makes those steps likely, not certain, so you still check.

## Choose by the Shape of the Work (frame 5)

    Choose by the shape of the work, not the brand or the version number. For routine work you can
    describe exactly, like explaining one sequel file, use a fast, low-cost model: Haiku, G P T Luna, or
    G L M Flash. Everyday models, like G P T Sol, fit most analysis, writing, and coding. The strongest
    models, like Opus or G P T Astra, fit ambiguous problems, like a dashboard number that won't match
    its source. The names will change; these three kinds of work won't.

## Match the Model to Its Harness (frame 6)

    A model works best in the harness built for it: Claude models in Claude Code, and G P T models in
    Codex. Pick the model when you start, and keep it. Switching mid-session throws away the cache, and
    answers can get worse. If you need a different model, start a new session. Building with AI 201
    explains why.

## Start at Medium (frame 7)

    Start with the model your setup gives you, and set effort to medium. That's our default. Higher
    effort costs much more, and often adds little. Raise effort when the work has many edge cases, like
    a quarter-end reconciliation. Lower it for a quick draft you'll steer, like a first outline of a
    memo. Change one setting at a time, on the same task with the same check. Building with AI 201 shows
    how, and what each step costs.

## Record the Decision (frame 8)

    Now try it. Staff it like a team: routine work goes to an analyst, and the expert comes in only when
    needed. For one task you do often, finish this sentence. I'll start with this model because of this,
    and switch only if this check fails. For example: G P T Sol for the weekly memo, because it's
    everyday writing, and Opus only if the totals don't match the dashboard.

## Continue Learning (frame 9)

    Explore other videos in this series, and leave a comment in the Analytics AI knowledge sharing
    channel so we can improve the course.
