# F101.2 exercise — Verify a completed-order report

Use an approved AI agent that can read local files and create a new file.

## Files

- `raw_orders.csv`: 99 synthetic orders.
- `raw_payments.csv`: 113 synthetic payment records.
- `metric-definitions.md`: the business rules for this lesson.

## Task

Ask the AI to analyze completed-order payment value by month and payment method, then create `jaffle-shop-report.html` in this folder. Preserve the three source files.

The report should contain one headline number, a monthly chart, a payment-method table, three evidence-based observations, and the calculations needed for manual verification.

## Source

The CSV files are copied from dbt Labs' archived [Jaffle Shop Classic](https://github.com/dbt-labs/jaffle-shop-classic) repository. Jaffle Shop is synthetic practice data. The original repository is licensed under Apache License 2.0; the license is included in this folder.

