---
format: 1920x1080
duration: 218s
message: "AI can build the first pass; you control the steps and decide when it is complete"
arc: Series context → stop the one-shot attempt → understand the task → inspect data → agree on a plan → build a first pass → validate → inspect and correct → decide complete
audience: Analytics colleagues who are new to agentic AI
mode: autonomous
concept: "A real Claude Code session in which the human controls each handoff"
rhythm: measured open → deliberate interruption → readable exploration → planned build → confident first pass → mismatch reveal → verified close
audio: voice-only cloned narration; no avatar, music, or captions
---

## Frame 1 — Set the pace

- status: animated
- src: compositions/01-intro-brief.html
- duration: 41.33s
- transition_in: cut
- scene: The clean course title gives way to a real Claude Code workspace; the agent starts writing too early and the learner interrupts it.
- voiceover: Introduce the series, then explain why the tutorial does not begin with a one-shot report request.
- poster: 32s
- motion: waterfall-entry + svg-path-draw + ambient-glow-bloom

The title frame lasts only long enough to establish the series and bridge from F101.1's goal, data and tools, context, output, and manual verification. In Claude Code, the learner asks what is in the folder and explicitly says not to write code. When the agent begins `generate_report.py` anyway, the learner stops it. The input bar and orange callout make human control visible.

## Frame 2 — Understand the assignment

- status: animated
- src: compositions/02-inspect-files.html
- duration: 28.53s
- transition_in: push-slide
- scene: The learner identifies the downloadable F101.2 folder and its two CSVs and Markdown guides, then Claude Code reads the README and explains the deliverable and rules without writing code.
- voiceover: Confirm that the learner and agent understand the same assignment.
- poster: 17s
- motion: spring-pop-entrance + svg-path-draw + ambient-glow-bloom

Name `F101.2-jaffle-shop` and show `raw_orders.csv`, `raw_payments.csv`, `README.md`, and `metric-definitions.md` as the downloadable exercise. Use the canonical dark terminal layout and reproduce the useful part of the real response: completed-only filter, order-ID join, cents-to-dollars conversion, and the required HTML sections. Keep the answer cropped and readable.

## Frame 3 — Inspect the CSVs

- status: animated
- src: compositions/03-prompt-report.html
- duration: 27.16s
- transition_in: push-slide
- scene: Claude Code shows the real headers and representative rows from both CSVs, then summarizes the relationships and edge cases.
- voiceover: Inspect the data before agreeing to an implementation.
- poster: 23s
- motion: waterfall-entry + anchored-layout-expand + card-morph-anchor

Show `raw_orders.csv` and `raw_payments.csv` as terminal output, not abstract file cards. Highlight the status field, amounts in cents, multiple payments, zero-value rows, and the join key. End with the learner asking for a plan.

## Frame 4 — Plan, then build a first pass

- status: animated
- src: compositions/04-verify-number.html
- duration: 44.79s
- transition_in: blur-crossfade
- scene: The agent proposes its data-processing, reporting, and verification plan. After approval it writes the generator, requests command approval, and reports success.
- voiceover: Read and correct the plan before allowing implementation; treat success as a first pass.
- poster: 38s
- motion: counting-dynamic-scale + stat-bars-and-fills + control-target-sync

The plan must visibly contain an independent check. The implementation view focuses on only the filter, join, conversion, and aggregation logic. The confident completion summary is labeled **First pass · not yet verified** and retains the incorrect monthly breakdown from the original run.

## Frame 5 — Validate, inspect, and correct

- status: animated
- src: compositions/05-trace-correct.html
- duration: 55.34s
- transition_in: push-slide
- scene: A sub-agent with fresh context exposes the polished report's incorrect breakdown. The learner traces order 2, opens the corrected HTML, and checks every visible section.
- voiceover: Use a sub-agent for an independent source calculation, compare every visible number, trace a known record, and reopen the report after correction.
- poster: 42s
- motion: svg-path-draw + scale-swap-transition + card-morph-anchor

The first-pass and source-calculation panels are visually separate. Label **sub-agent** and **fresh context**, and note that both concepts are covered later. Show the incorrect February and March values beside the verified `$424 + $400 + $279 = $1,103` result and reconcile payment methods too. Then trace `order 2 → completed → credit_card → 2,000 cents → $20`. The browser view uses the actual report structure and ends with a completion checklist.

## Frame 6 — You decide

- status: animated
- src: compositions/06-recap-outro.html
- duration: 22.85s
- transition_in: blur-crossfade
- scene: The five teaching steps resolve into one accountable owner, followed by the standard Continue Learning card.
- voiceover: Recap the staged workflow, then invite learners to explore other videos and send feedback.
- poster: 17s
- motion: spring-pop-entrance + waterfall-entry + ambient-glow-bloom

The recap names Orient, Inspect, Plan, Build, and Validate. It resolves to **The AI builds quickly. You decide.** The outro reuses the opening title system, stays under ten seconds, and ends with the standard Continue Learning message plus **Comment in #analytics-ai-knowledge-sharing**.
