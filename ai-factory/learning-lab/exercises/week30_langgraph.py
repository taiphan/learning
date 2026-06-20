#!/usr/bin/env python3
"""Week 30 — Simple agent state machine (LangGraph pattern)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'lib'))

from rag_simple import TfidfIndex, load_policy_chunks

POLICY = Path(__file__).resolve().parent.parent / "data" / "sample_policy.txt"

def run_agent(question: str) -> list[str]:
    trace = ["START: understand question"]
    index = TfidfIndex(load_policy_chunks(POLICY))
    trace.append("RETRIEVE: search policy")
    resp = index.answer(question)
    if resp["confidence"] < 0.05:
        trace.append("ESCALATE: low confidence → human")
        return trace
    trace.append(f"ANSWER: {resp['answer'][:60]}...")
    trace.append("END")
    return trace

if __name__ == "__main__":
    for step in run_agent("Who approves above 100M?"):
        print(" →", step)
