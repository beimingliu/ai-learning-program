# Verification notes

## Checks passed

| Check | Result | Lesson A-roll |
| --- | --- | --- |
| Completed orders | 67 | Matches the expected 67 |
| Joined payment rows | 76 | Not specified in the A-roll; retained as an audit detail |
| Payment sum before conversion | 110,300 cents | Matches the expected 110,300 cents |
| Dollar conversion | 110,300 ÷ 100 = $1,103 | Matches the expected $1,103 |
| Monthly reconciliation | $424 + $400 + $279 = $1,103 | Matches the expected monthly values |
| Order 2 trace | completed → credit card → 2,000 cents → $20 | Matches the expected trace |
| Payment-method reconciliation | $243 + $127 + $627 + $106 = $1,103 | Extra detail; not specified in the A-roll |

The saved `03-results.json` is byte-for-byte equivalent to the stdout from `02-calculate.py`, and the JSON parses successfully. The source CSVs were read only; the report and calculation artifacts are new files under `analysis-run/`.

## Remaining uncertainty

The source files support the amounts, joins, and comparisons above, but they do not provide evidence for why March is lower than January or February. The report states the observed difference without assigning a cause. The source orders include April rows, but all April orders are `placed`, so they contribute no completed-order payment value under the supplied rule and are not shown as a positive month in the chart.

The checks cover the headline, monthly reconciliation, payment-method reconciliation, and one end-to-end order trace; they do not prove that every source row is free of data-quality issues.

## A-roll comparison

No mismatch was found with the lesson's expected verification values. The analysis adds the joined-row count and payment-method breakdown requested by the exercise brief.
