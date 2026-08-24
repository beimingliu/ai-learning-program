# Inspection notes

## Sources and schemas

| File | Data rows | Columns |
| --- | ---: | --- |
| `raw_orders.csv` | 99 | `id`, `user_id`, `order_date`, `status` |
| `raw_payments.csv` | 113 | `id`, `order_id`, `payment_method`, `amount` |
| `metric-definitions.md` | n/a | Business rules for the metric |

The order file covers dates from `2018-01-01` through `2018-04-09`. The payment file stores `amount` as integer cents. The order and payment IDs are represented as CSV fields, so the calculation compares their values as strings and converts payment amounts to integers before summing.

## Rules discovered

- Keep orders where `status = completed`.
- Join `raw_orders.id` to `raw_payments.order_id`.
- Include every payment row joined to a completed order, including zero-amount rows and orders with more than one payment row.
- Use the calendar month from the completed order's `order_date` for monthly grouping.
- Divide the summed cents by 100 for the dollar display.

## Initial checks

- There are 67 completed orders among the 99 orders.
- The completed-order join produces 76 payment rows among the 113 payment records.
- The payment rows sum to 110,300 cents before conversion.
- The calculation script is `02-calculate.py`; it reads the source CSVs and writes only JSON to stdout.
