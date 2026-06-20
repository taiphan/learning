#!/usr/bin/env python3
"""Week 31 — Agent with lookup, calculator, escalate tools."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "lib"))
from rag_simple import TfidfIndex, load_policy_chunks

POLICY = Path(__file__).resolve().parent.parent.parent / "data" / "sample_policy.txt"

def policy_lookup(q: str):
    return TfidfIndex(load_policy_chunks(POLICY)).answer(q)

def dti_calculator(income: float, debt: float):
    return {"dti": round(debt / income, 3) if income else 1.0}

def escalate(reason: str):
    return {"escalated": True, "reason": reason}

def handle(question: str):
    if "dti" in question.lower() and "income" in question.lower():
        return dti_calculator(25_000_000, 8_000_000)
    resp = policy_lookup(question)
    if resp["confidence"] < 0.05:
        return escalate("low confidence")
    return resp

if __name__ == "__main__":
    print(handle(sys.argv[1] if len(sys.argv) > 1 else "Max DTI?"))
