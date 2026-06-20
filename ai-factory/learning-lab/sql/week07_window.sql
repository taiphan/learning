-- Week 7 — Monthly disbursement trend (window)
SELECT application_month,
       SUM(loan_amount_vnd) AS month_total,
       SUM(SUM(loan_amount_vnd)) OVER (ORDER BY application_month) AS running_total
FROM applications
GROUP BY application_month
ORDER BY application_month;
