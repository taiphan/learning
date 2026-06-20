#!/usr/bin/env python3
"""Weeks 25–28 — CLI RAG over policy text."""
import argparse
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'lib'))

from rag_simple import TfidfIndex, load_policy_chunks

POLICY = Path(__file__).resolve().parent.parent / "data" / "sample_policy.txt"

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("question", nargs="?", default="Max DTI for POS motorbike loan?")
    a = p.parse_args()
    index = TfidfIndex(load_policy_chunks(POLICY))
    resp = index.answer(a.question)
    print("Answer:", resp["answer"])
    print("Confidence:", resp["confidence"])
    for s in resp["sources"]:
        print(f"  Source [{s['index']}] score={s['score']}: {s['text'][:100]}...")
