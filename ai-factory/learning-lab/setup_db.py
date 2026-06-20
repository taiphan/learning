#!/usr/bin/env python3
"""Create SQLite DB for SQL weeks 5–7 from CSV data."""

import csv
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
DB = ROOT / "loans.db"


def main() -> None:
    loans = list(csv.DictReader((DATA / "sample_loans.csv").open(encoding="utf-8")))
    customers = list(csv.DictReader((DATA / "sample_customers.csv").open(encoding="utf-8")))

    if DB.exists():
        DB.unlink()

    con = sqlite3.connect(DB)
    cur = con.cursor()
    cur.executescript(
        """
        CREATE TABLE customers (
            customer_id TEXT PRIMARY KEY,
            region TEXT,
            segment TEXT
        );
        CREATE TABLE applications (
            application_id TEXT PRIMARY KEY,
            customer_id TEXT,
            customer_age INTEGER,
            monthly_income_vnd INTEGER,
            existing_debt_vnd INTEGER,
            loan_amount_vnd INTEGER,
            employment_months INTEGER,
            region TEXT,
            application_month TEXT DEFAULT '2026-01'
        );
        """
    )

    for c in customers:
        cur.execute(
            "INSERT INTO customers VALUES (?,?,?)",
            (c["customer_id"], c["region"], c.get("segment", "mass")),
        )

    for i, row in enumerate(loans):
        cid = customers[i % len(customers)]["customer_id"]
        month = f"2026-{(i % 6) + 1:02d}"
        cur.execute(
            """INSERT INTO applications VALUES (?,?,?,?,?,?,?,?,?)""",
            (
                row["application_id"],
                cid,
                int(row["customer_age"]),
                int(row["monthly_income_vnd"]),
                int(row["existing_debt_vnd"]),
                int(row["loan_amount_vnd"]),
                int(row["employment_months"]),
                row["region"],
                month,
            ),
        )

    con.commit()
    con.close()
    print(f"Created {DB} — {len(loans)} applications, {len(customers)} customers")


if __name__ == "__main__":
    main()
