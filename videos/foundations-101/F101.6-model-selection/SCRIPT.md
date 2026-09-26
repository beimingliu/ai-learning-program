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
    open a file it was never given, or fix a metric definition that was wrong to begin with. When Claude
    gets it wrong, look at the context before you touch a setting.

## Two Settings, Two Questions (frame 4)

    Once the task is clear, you have two settings. The model decides how capable the worker is. Effort
    decides how hard it works: how much it reasons, how many files it reads, and how far it goes before
    it checks back with you. So ask one question. Did Claude not know enough, or did it not try hard
    enough? If it had everything it needed, clearly tried, and was still wrong, pick a stronger model.
    If it skipped a file, didn't run the check, or stopped halfway, try more effort. Anthropic's own
    tests show the same split: more effort caught more missed edge cases, but it didn't fix a wrong
    approach. In Claude Code, type slash effort. More effort makes those steps likely, not certain, so
    you still check.

## Choose by the Shape of the Work (frame 5)

    Choose by the shape of the work, not the brand or the version number. For routine work you can
    describe exactly, like explaining one sequel file, use a fast, low-cost model: Haiku, G P T Luna, or
    G L M Flash. Everyday models, like Sonnet or G P T Sol, fit most analysis, writing, and coding. The
    strongest models, like Opus or G P T Astra, fit ambiguous problems and stubborn bugs. The names will
    change with the next release; these three kinds of work won't. Cheaper models are closer than you
    might expect. In a five-task test I ran in September, G P T five point six Luna scored almost as
    well as Opus five, for about one cent per task instead of almost three dollars. That's one small
    test, not a ranking, but it's a good reason to try the cheaper model first.

## Match the Model to Its Harness (frame 6)

    A model works best in the harness built for it: Claude models in Claude Code, and G P T models in
    Codex. Building with AI 201 explains why, in Prompt Caching and the Cost of Agentic Work.

## Start With the Default (frame 7)

    Start with the default your setup gives you. Each model's default effort is set for most work. Lower
    it when you want a quick draft that you'll steer yourself. Raise it when the work has many edge
    cases to check. When you do change something, change one setting at a time, on the same task with
    the same check. Building with AI 201 shows how to run that comparison.

## Record the Decision (frame 8)

    Now try it. Pick one task you do often, and finish this sentence. I'll start with this model,
    because of this. I'll switch only if this happens, and I'll judge the switch by this check.

## Continue Learning (frame 9)

    Explore other videos in this series, and leave a comment in the Analytics AI knowledge sharing
    channel so we can improve the course.
