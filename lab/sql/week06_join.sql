-- Week 6 — JOIN customers and applications
SELECT c.customer_id, c.segment, a.application_id, a.loan_amount_vnd, a.region
FROM customers c
JOIN applications a ON a.customer_id = c.customer_id
ORDER BY a.loan_amount_vnd DESC;

SELECT c.region, COUNT(*) AS apps, SUM(a.loan_amount_vnd) AS total_loan
FROM customers c
JOIN applications a ON a.customer_id = c.customer_id
GROUP BY c.region;
