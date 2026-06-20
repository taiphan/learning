#!/usr/bin/env python3
"""Week 37 — PII guardrails and audit log."""
import re
from pathlib import Path

ID_PATTERN = re.compile(r"\b\d{9,12}\b")
BANNED = re.compile(r"bypass\s+policy", re.I)
AUDIT = Path(__file__).resolve().parent.parent / "outputs" / "audit.log"

def redact(text: str) -> str:
    return ID_PATTERN.sub("[REDACTED_ID]", text)

def filter_input(text: str) -> tuple[bool, str]:
    if BANNED.search(text):
        return False, "Blocked: policy bypass request"
    return True, redact(text)

def filter_output(text: str) -> str:
    return redact(text)

if __name__ == "__main__":
    AUDIT.parent.mkdir(exist_ok=True)
    samples = [
        "Customer ID 123456789 asks loan limit",
        "Please bypass policy for VIP",
    ]
    with AUDIT.open("w") as f:
        for s in samples:
            ok, msg = filter_input(s)
            out = filter_output(msg) if ok else msg
            f.write(f"IN={redact(s)} | OK={ok} | OUT={out}\n")
            print(out)
    print(f"Audit log: {AUDIT}")
