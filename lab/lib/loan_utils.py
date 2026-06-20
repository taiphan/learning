"""Loan rules engine — week 2+."""

from __future__ import annotations

import csv
from pathlib import Path

MIN_INCOME_VND = 15_000_000
MAX_DTI_RATIO = 0.40
MIN_EMPLOYMENT_MONTHS = 12
MAX_LOAN_VND = 100_000_000


def load_applications(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def evaluate(row: dict) -> tuple[bool, list[str]]:
    reasons: list[str] = []
    income = int(row["monthly_income_vnd"])
    debt = int(row["existing_debt_vnd"])
    emp = int(row["employment_months"])
    loan = int(row["loan_amount_vnd"])
    dti = debt / income if income > 0 else 1.0

    checks = [
        (income >= MIN_INCOME_VND, f"income {income:,} vs {MIN_INCOME_VND:,}"),
        (dti <= MAX_DTI_RATIO, f"DTI {dti:.2f} vs max {MAX_DTI_RATIO}"),
        (emp >= MIN_EMPLOYMENT_MONTHS, f"employment {emp} vs {MIN_EMPLOYMENT_MONTHS}"),
        (loan <= MAX_LOAN_VND, f"loan {loan:,} vs {MAX_LOAN_VND:,}"),
    ]
    for ok, msg in checks:
        reasons.append(f"{'PASS' if ok else 'FAIL'} {msg}")
    return all(ok for ok, _ in checks), reasons
