#!/usr/bin/env python3
"""Week 26 — Persist TF-IDF index to disk (Chroma substitute, no extra deps)."""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'lib'))

from rag_simple import TfidfIndex, load_policy_chunks

LAB = Path(__file__).resolve().parent.parent
POLICY = LAB / "data" / "sample_policy.txt"
STORE = LAB / "data" / "tfidf_index.json"

if __name__ == "__main__":
    chunks = load_policy_chunks(POLICY)
    index = TfidfIndex(chunks)
    STORE.write_text(json.dumps({"docs": chunks}, indent=2), encoding="utf-8")
    reloaded = TfidfIndex(json.loads(STORE.read_text())["docs"])
    hit = reloaded.search("DTI motorbike", top_k=1)[0]
    print(f"Persisted {len(chunks)} chunks → {STORE}")
    print(f"Reload test score: {hit[1]:.3f}")
