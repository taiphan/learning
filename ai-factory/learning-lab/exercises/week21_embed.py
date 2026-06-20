#!/usr/bin/env python3
"""Weeks 21–23 — TF-IDF policy similarity."""
import time
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'lib'))

from rag_simple import TfidfIndex, load_policy_chunks

POLICY = Path(__file__).resolve().parent.parent / "data" / "sample_policy.txt"

if __name__ == "__main__":
    chunks = load_policy_chunks(POLICY)
    index = TfidfIndex(chunks)
    query = "maximum DTI for motorbike loan"
    t0 = time.perf_counter()
    hits = index.search(query, top_k=3)
    ms = (time.perf_counter() - t0) * 1000
    print(f"Query: {query}\nLatency: {ms:.1f} ms\n")
    for i, score, text in hits:
        print(f"  [{score:.3f}] chunk {i}: {text[:80]}...")
