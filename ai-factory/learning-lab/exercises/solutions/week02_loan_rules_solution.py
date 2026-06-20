#!/usr/bin/env python3
"""Week 2 SOLUTION — CSV loan rules engine."""

import csv
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent.parent / "data" / "sample_loans.csv"

MIN_INCOME_VND = 15_000_000
MAX_DTI_RATIO = 0.40
MIN_EMPLOYMENT_MONTHS = 12
MAX_LOAN_VND = 100_000_000


def load_applications(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def evaluate(row: dict) -> tuple[bool, list[str]]:
    reasons = []
    income = int(row["monthly_income_vnd"])
    debt = int(row["existing_debt_vnd"])
    emp = int(row["employment_months"])
    loan = int(row["loan_amount_vnd"])
    dti = debt / income if income > 0 else 1.0

    if income >= MIN_INCOME_VND:
        reasons.append(f"PASS income {income:,} >= {MIN_INCOME_VND:,}")
    else:
        reasons.append(f"FAIL income {income:,} < {MIN_INCOME_VND:,}")

    if dti <= MAX_DTI_RATIO:
        reasons.append(f"PASS DTI {dti:.2f} <= {MAX_DTI_RATIO}")
    else:
        reasons.append(f"FAIL DTI {dti:.2f} > {MAX_DTI_RATIO}")

    if emp >= MIN_EMPLOYMENT_MONTHS:
        reasons.append(f"PASS employment {emp} months >= {MIN_EMPLOYMENT_MONTHS}")
    else:
        reasons.append(f"FAIL employment {emp} months < {MIN_EMPLOYMENT_MONTHS}")

    if loan <= MAX_LOAN_VND:
        reasons.append(f"PASS loan {loan:,} <= {MAX_LOAN_VND:,}")
    else:
        reasons.append(f"FAIL loan {loan:,} > {MAX_LOAN_VND:,}")

    approved = all(r.startswith("PASS") for r in reasons)
    return approved, reasons


def main() -> None:
    apps = load_applications(DATA)
    print(f"Loaded {len(apps)} applications from {DATA.name}\n")
    for row in apps:
        ok, reasons = evaluate(row)
        label = "APPROVE" if ok else "DECLINE"
        print(f"{row['application_id']}: {label}")
        for r in reasons:
            print(f"    - {r}")


if __name__ == "__main__":
    main()
