# B201.3 narration (TTS source; spelling adjusted for pronunciation)

Spoken text matches the A-roll in the lesson file exactly, apart from pronunciation spellings.

Build (from the lesson folder): `node ../../../shared/video-kit/qwen-tts.mjs --ref bliu-voice [--only 02,05]` writes `assets/voice/NN.wav` and `audio_meta.json`; then `python3 ../../../shared/video-kit/assemble.py .` trims each section, inserts the 0.8s and 1.0s gaps, writes `audio/narration-bliu.wav`, expands `src/` into `compositions/` with `{{T:phrase}}` cue times from the word timings, and rewrites `index.html`. Edit scenes in `src/`, never `compositions/`. See `shared/video-kit/GUIDE.md`.

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
    the grain, the date window, what counts. Second, draft on medium. Third, review that it got the
    gist, and iterate quickly. Fourth, raise effort to high and ask Claude to verify: reconcile totals,
    test nulls and date boundaries, and try a second method. Change effort mid-conversation with slash
    effort, but keep the same model. Switching models mid-session throws away the cache, and answers can
    get worse.

## Test It on Your Own Task (frame 6)

    Start every task at medium. That's our default. Higher effort costs far more than it gains. On the
    Artificial Analysis benchmark, G P T six Sol goes from medium to max for about four times the cost
    and eight more points. Opus five point five pays four and a half times the cost for six. So test it
    on your own work. Pick one recurring task with two or three checks, like the weekly A W V summary,
    checked against the dashboard total, the market count, and the date range. Run it at medium, and
    record four things: which checks passed, what it missed, how long it took, and how much it used.
    Then change only the effort, and run it again. The extra cost has to buy something your checks can
    see. Here, medium missed two rows with blank dates, and high caught them. So keep high for the
    verify step. If both runs took the wrong approach, like joining on the wrong key, go back to the
    task or the model. A single run is a practical check, not an evaluation.

## Write Your Rule (frame 7)

    Finish with one sentence. Use medium for this. Raise effort when this, because the check showed
    this. For example: use medium for the weekly memo; raise it to high for the quarter-end
    reconciliation, because medium missed two blank date rows. Tariq's full article is linked on the
    course page.

## Continue Learning (frame 8)

    Explore other videos in this series, and leave a comment in the Analytics AI knowledge sharing
    channel so we can improve the course.
