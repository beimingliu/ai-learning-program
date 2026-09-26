# B201.7 narration (TTS source; spelling adjusted for pronunciation)

## Series Introduction (frame 1)

    Welcome to the Analytics AI Enablement education series. Today in Building with AI, we focus on
    prompt caching.

## The Agent Re-reads Everything (frame 2)

    An agent works differently from a chat. Every time it calls a tool, it sends the whole
    conversation back to the model: the system prompt, the tools, every file it read, every result
    so far. In my own session logs, an agent reads more than a hundred tokens for every token it
    writes. So agentic work mostly costs re-reading the same context.

## What the Cache Stores (frame 3)

    Before a model writes anything, it processes your prompt and stores a key and a value for every
    token, at every layer. That stored state is the K V cache. If the next request starts with
    exactly the same tokens, the provider reuses it and processes only what is new. Two rules
    follow. Only an exact prefix counts: change one token near the top, and everything after it is
    processed again. And the cache expires. On Claude, the default lifetime is five minutes, reset
    each time it is used.

## What a Hit Is Worth (frame 4)

    Reading from the cache costs a tenth of the normal input price on most Claude models. Writing to
    it costs one and a quarter times. It is faster too: Anthropic measured a one hundred thousand
    token prompt dropping from eleven and a half seconds to about two and a half before the first
    word.

## Same Model, Different Harness (frame 5)

    Here is what I found in ninety days of my own sessions. This is one person's usage, not a
    benchmark. Claude Code with Claude models reused ninety-three percent of its input. Codex with G
    P T models reused about ninety. Claude Code pointed at G P T or open-weight models reused
    nothing, across more than a thousand calls before this week. Same G P T models, different
    harness. The provider decides what can be cached; the harness decides whether each request
    starts with the same bytes as the last. Both harnesses went through the same Lite L L M proxy.
    Codex speaks OpenAI's format, so nothing is translated. Claude Code's requests are translated on
    the way. In my tests, the break came down to one detail: Claude Code sends a mid-conversation
    notice as a list the first time, and as plain text after that. Anthropic's cache still hits, so
    it appears to treat them as the same. After translation they are different bytes, so the cache
    breaks there on every call.

## Time Is the Other Half (frame 6)

    Even in a pairing that works, time matters. In my logs, calls made within a minute of the last
    one hit ninety-nine percent. After more than five minutes idle, the hit rate fell to twenty-six
    percent, and most of the context was written again.

## The Calculation (frame 7)

    Now a worked example, modeled rather than measured: one hundred calls, with context growing to
    about one hundred thirty thousand tokens. At my measured hit rate, input costs about sixty
    percent more than the ideal. With no hits and a write premium on every call, it costs about
    eleven times the ideal. On a short, eight-call task the gap is small in dollars, so choose the
    model you want.

## Four Habits (frame 8)

    First, pair each model with the harness built for it: Claude models in Claude Code, G P T models
    in Codex. Second, after a long break, start fresh instead of resuming a large session, or use
    the one-hour cache if your setup offers it. Third, avoid switching models or compacting mid-
    task. Both discard the cache. Fourth, when you try a new pairing, check the cache numbers after
    ten calls, before you give it a day of work.

## Continue Learning (frame 9)

    Explore other videos in this series, and leave a comment in the Analytics AI knowledge sharing
    channel so we can improve the course.
