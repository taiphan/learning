#!/usr/bin/env python3
"""Week 2 — Loan rules from CSV."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'lib'))

from loan_utils import load_applications, evaluate

DATA = Path(__file__).resolve().parent.parent / "data" / "sample_loans.csv"

if __name__ == "__main__":
    apps = load_applications(DATA)
    print(f"Loaded {len(apps)} applications\n")
    for row in apps:
        ok, reasons = evaluate(row)
        print(f"{row['application_id']}: {'APPROVE' if ok else 'DECLINE'}")
        for r in reasons:
            print(f"    - {r}")
