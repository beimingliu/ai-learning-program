# B201.3 narration (TTS source; spelling adjusted for pronunciation)

Spoken text matches the A-roll in the lesson file exactly, apart from pronunciation spellings.

Build: `node scripts/qwen-tts.mjs --ref bliu-voice [--only 02,05]` writes `assets/voice/NN.wav` and `audio_meta.json`; then `python3 assemble.py` trims each section, inserts the 0.8s and 1.0s gaps, writes `audio/narration-bliu.wav`, expands `src/` into `compositions/` with `{{T:phrase}}` cue times from the word timings, and rewrites `index.html`. Edit scenes in `src/`, never `compositions/`.

## Series Introduction (frame 1)

    Welcome to the Analytics AI Enablement education series. Today in Building with AI, we choose a
    model and effort level in practice.

## What Effort Changes (frame 2)

    Foundations 101 split the two settings: the model decides how capable Claude is, and effort decides
    how hard it works. Tariq Shihipar, on Anthropic's Claude Code team, tested every effort level on
    the same tasks. He found that effort mostly changes two things: how much Claude checks its own
    work, and how much it decides on its own. Think of a deadline. Given one hour, you'd build a solid
    first version and expect feedback. Given twelve, you'd test, second-guess, and polish without
    asking. Effort tells Claude which deadline it has.

## How Much You Stay in the Loop (frame 3)

    So effort also decides how much you stay in the loop. He gave Claude a vague request: build a
    workout tracker. At low effort, it took about a minute and a half and returned a simple log and
    chart. At max, it took over an hour, returned much more, and Claude made more of the choices itself.
    With a detailed spec, the levels came out much closer. Low effort gives you a quick draft to steer.
    High effort does more of the work, and makes more assumptions for you.

## Where Effort Pays Off (frame 4)

    Effort pays off when the work hides edge cases. One benchmark task was a data analysis: from protein
    measurements, find which of eight treatments resemble a target tissue. At low effort, Claude picked
    one reasonable way to prepare the data, ran it, and reported. At high, it tried two ways, saw the
    answer change, and worked out why before choosing. It went from zero of five attempts correct to
    four. That's the reconciliation you'd want before a number reaches a stakeholder. But across the
    benchmark, more effort cut missed edge cases without fixing a wrong approach. If the plan is wrong,
    fix the task, or try a stronger model.

## A Loop for Everyday Work (frame 5)

    Here's a loop he uses, adapted for analytics. First, ask Claude to interview you about the analysis:
    the grain, the date window, what counts. Second, draft on low or medium effort. Third, review that
    it got the gist, and iterate quickly. Fourth, raise effort to high and ask Claude to verify:
    reconcile totals, test nulls and date boundaries, and try a second method. You can change effort
    mid-conversation with slash effort.

## Test It on Your Own Task (frame 6)

    Treat his rule of thumb as a starting point. Models and their defaults change with each release, so
    test it on your own work. Pick one recurring task with two or three checks. Run it at the default,
    and record four things: which checks passed, what it missed, how long it took, and how much it
    used. Then change only the effort, and run it again. More effort costs more time and tokens, so it
    has to buy something your checks can see. If the higher run caught edge cases the first one missed,
    keep high effort for the verify step. If both runs took the wrong approach, go back to the task or
    the model. One run is a practical check, not an evaluation. A workflow you rely on needs repeated
    runs.

## Write Your Rule (frame 7)

    Finish with one sentence. Use the default for this. Raise effort when this, because the check
    showed this. Tariq's full article, with the benchmark details, is linked on the course page.

## Continue Learning (frame 8)

    Explore other videos in this series, and leave a comment in the Analytics AI knowledge sharing
    channel so we can improve the course.
