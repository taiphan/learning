#!/usr/bin/env python3
"""Week 29 — Extract structured policy fields (regex lab; optional API)."""
import json
import re

SAMPLE = """
POS motorbike installment product maximum loan 100 million VND.
Debt-to-income ratio must not exceed 40 percent for approval.
"""

def extract_regex(text: str) -> dict:
    limit = re.search(r"(\d+)\s*million\s*VND", text, re.I)
    dti = re.search(r"(\d+)\s*percent", text, re.I)
    return {
        "product": "POS motorbike installment" if "motorbike" in text.lower() else "unknown",
        "limit_vnd": int(limit.group(1)) * 1_000_000 if limit else None,
        "dti_max": float(dti.group(1)) / 100 if dti else None,
    }

if __name__ == "__main__":
    data = extract_regex(SAMPLE)
    print(json.dumps(data, indent=2))
    print("\nProduction: replace extract_regex with Claude API + JSON schema.")
