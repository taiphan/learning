#!/usr/bin/env python3
"""Week 27 — Policy RAG CLI over repo BRD sample."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "lib"))
from rag_simple import TfidfIndex, chunk_text

REPO = Path(__file__).resolve().parents[3]
BRD = REPO / "examples" / "04a-brd-pos-lending.md"

if __name__ == "__main__":
    text = BRD.read_text(encoding="utf-8") if BRD.exists() else "No BRD found"
    index = TfidfIndex(chunk_text(text, max_words=100))
    q = sys.argv[1] if len(sys.argv) > 1 else "What is the business problem?"
    resp = index.answer(q)
    print(resp["answer"][:500])
