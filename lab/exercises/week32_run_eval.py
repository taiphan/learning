#!/usr/bin/env python3
"""Week 32 — Golden eval harness."""
import sys
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'lib'))

from rag_simple import TfidfIndex, load_policy_chunks, run_eval

POLICY = Path(__file__).resolve().parent.parent / "data" / "sample_policy.txt"
GOLDEN = Path(__file__).resolve().parent.parent / "data" / "eval_questions.json"

if __name__ == "__main__":
    index = TfidfIndex(load_policy_chunks(POLICY))
    result = run_eval(index, GOLDEN)
    print(f"Grounded rate: {result['passed']}/{result['total']} = {result['grounded_rate']:.1%}")
    if result["grounded_rate"] < 0.85:
        sys.exit(1)
    print("PASS ≥85%")
