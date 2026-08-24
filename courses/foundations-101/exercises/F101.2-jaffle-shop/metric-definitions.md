# Metric definitions

Use these definitions for the F101.2 exercise.

- A completed order has `status = completed`.
- Join `raw_orders.id` to `raw_payments.order_id`.
- `raw_payments.amount` is stored in cents. Divide by 100 to report dollars.
- Completed-order payment value is the sum of every payment row joined to a completed order.
- Assign payment value to the calendar month of `raw_orders.order_date`.
- Describe patterns supported by these files. Do not claim why a pattern occurred unless the files contain evidence for the cause.

