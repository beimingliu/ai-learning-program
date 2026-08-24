# HeyGen Avatar V expressiveness research

Date: 2026-08-20

## Repo truth

- `AGENTS.md` defaults avatar generation to Avatar V with look `73db92410a974bbc832b122638fe119f`.
- A live MCP render confirmed that Avatar V rejects the `expressiveness` parameter and succeeds when it is omitted.
- The installed HeyGen MCP schema exposes `motionPrompt`, but schema availability does not prove that every Avatar V look accepts it.

## External truth

- HeyGen's current Digital Twin guide says `expressiveness` is Avatar IV-only. It describes Avatar V as cross-reference-driven and currently lists `motion_prompt` for both IV and V.
- HeyGen's API reference and some cached documentation still describe `motion_prompt` as Avatar IV-only. The documentation is inconsistent during this rollout.
- Avatar V is primarily audio-driven. Voice energy, emotion, and prosody drive facial expression and motion.
- Avatar V learns characteristic gestures, facial behavior, and movement from its motion-reference recording. HeyGen recommends choosing or recording a reference with the desired energy.
- In HeyGen's product UI, an input image's expression and a More/Less Expressive motion setting provide additional control. These are not equivalent to the removed API enum.
- HeyGen describes Avatar V's control priority as audio, then input-image expression, then prompt.

## Recommendation

- Keep omitting `expressiveness` for Avatar V.
- Treat expressive voice delivery and the chosen motion reference as the primary replacement controls.
- Use script emphasis and natural punctuation to shape TTS prosody; use uploaded expressive audio when precise delivery matters.
- Treat `motionPrompt` as secondary direction, not as a replacement intensity knob. Before relying on it in production, run a short A/B API test because HeyGen's current reference pages conflict about Avatar V support.
- Use Avatar IV when explicit low/medium/high control and prompt-led customization matter more than Avatar V's identity and motion consistency.

## Risks

- Text-to-speech that is flat will produce restrained Avatar V motion regardless of prompting.
- The avatar used in this repo is reported by MCP as a photo avatar. HeyGen says Avatar V performs best with video-based avatars, so the full motion-reference benefit may be weaker than with a newly trained video Digital Twin.
- On HeyGen's current credit-based subscription plans, a Photo Look costs 48 credits/minute with Avatar V and 16 credits/minute with Avatar IV: exactly 3×. A Video Look costs 48 versus 31 credits/minute. The avatar used in this repo is a Photo Look, so the 3× estimate is expected.
- HeyGen's API-wallet pricing is a different billing system: the current developer table lists Avatar V Digital Twin at $4.002/minute, Avatar IV Photo Avatar at $3/minute, and Avatar IV Digital Twin at $4.002/minute. Do not mix API-dollar pricing with subscription-credit pricing.

## Sources

- https://developers.heygen.com/generate-avatar-video
- https://developers.heygen.com/reference/create-video
- https://help.heygen.com/en/articles/14602997-how-to-get-the-best-results-with-avatar-v-in-heygen
- https://help.heygen.com/en/articles/15544929-avatar-voice-faq-troubleshooting-best-practices-and-credits
- https://community.heygen.com/public/resources/avatar-v-live-webinar-recap-top-questions-answered-2026-04-16
- https://www.heygen.com/research/avatar-v-model
- https://help.heygen.com/en/articles/15126059-how-to-use-credits-on-heygen
- https://developers.heygen.com/docs/pricing

---

# F101.2 open-source analytics exercise research

Date: 2026-08-20

## Recommendation

Use the three seed CSVs from `dbt-labs/jaffle-shop-classic` as the source for the F101.2 guided analysis. The repository is Apache-2.0 licensed, the data is synthetic, and the files are small enough for learners and AI agents to inspect directly without installing dbt:

- `raw_customers.csv`: 100 data rows
- `raw_orders.csv`: 99 data rows
- `raw_payments.csv`: 113 data rows

Do not teach the dbt project itself. Package the CSVs with attribution, the Apache-2.0 license notice, and a short course-owned metric definition derived from the repository's staging SQL.

## Verified exercise

Analyze completed Jaffle Shop orders for Q1 2018. Produce an HTML report showing completed-order revenue by month and payment method, then verify the total and narrow any unsupported causal claim.

Verified results from the source CSVs:

- 67 completed orders
- 110,300 raw payment units for completed orders; the repository's `stg_payments.sql` says raw `amount` is cents, so completed-order revenue is $1,103.00
- Monthly completed revenue: January $424.00, February $400.00, March $279.00
- Completed revenue by method: credit card $627.00, bank transfer $243.00, coupon $127.00, gift card $106.00
- Every order has at least one payment row

This supports a concrete verification moment: an agent that treats raw `amount` as dollars will overstate revenue by 100×. The data can show that March completed revenue is lower; it cannot explain why.

## Tradeoffs

- The repository was archived in February 2025. That is acceptable for a frozen teaching fixture but should be disclosed.
- The current `dbt-labs/jaffle-shop` repository is actively maintained but introduces dbt Cloud and warehouse setup that is too heavy for this lesson.
- Plotly and Vega dataset collections are convenient for charts, but many individual datasets have separate or unclear provenance and are less suitable for a multi-file business verification exercise.

## Sources

- https://github.com/dbt-labs/jaffle-shop-classic
- https://github.com/dbt-labs/jaffle-shop-classic/tree/main/seeds
- https://github.com/dbt-labs/jaffle-shop-classic/blob/main/models/staging/stg_payments.sql
- https://github.com/dbt-labs/jaffle-shop-classic/blob/main/LICENSE
- https://github.com/dbt-labs/jaffle-shop
- https://github.com/plotly/datasets
- https://github.com/vega/vega-datasets
