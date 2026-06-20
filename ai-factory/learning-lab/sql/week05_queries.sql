-- Week 5 SQL SOLUTIONS
-- Setup (SQLite): import sample_loans.csv into table `applications`

CREATE TABLE IF NOT EXISTS applications (
    application_id TEXT PRIMARY KEY,
    customer_age INTEGER,
    monthly_income_vnd INTEGER,
    existing_debt_vnd INTEGER,
    loan_amount_vnd INTEGER,
    employment_months INTEGER,
    region TEXT
);

-- Q1: Count applications per region
SELECT region, COUNT(*) AS app_count
FROM applications
GROUP BY region
ORDER BY app_count DESC;

-- Q2: Average loan where employment >= 12 months
SELECT AVG(loan_amount_vnd) AS avg_loan_vnd
FROM applications
WHERE employment_months >= 12;

-- Q3: High DTI (> 0.40)
SELECT application_id,
       monthly_income_vnd,
       existing_debt_vnd,
       CAST(existing_debt_vnd AS REAL) / monthly_income_vnd AS dti
FROM applications
WHERE CAST(existing_debt_vnd AS REAL) / monthly_income_vnd > 0.40;

-- Q4: Top 3 regions by total loan amount
SELECT region, SUM(loan_amount_vnd) AS total_loan_vnd
FROM applications
GROUP BY region
ORDER BY total_loan_vnd DESC
LIMIT 3;

-- Q5: Fail min income rule (< 15,000,000 VND)
SELECT application_id, monthly_income_vnd, region
FROM applications
WHERE monthly_income_vnd < 15000000;
