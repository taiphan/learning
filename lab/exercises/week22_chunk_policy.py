#!/usr/bin/env python3
"""Week 22 — Chunk policy text and write manifest JSON."""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'lib'))

from rag_simple import chunk_text, load_policy_chunks

POLICY = Path(__file__).resolve().parent.parent / "data" / "sample_policy.txt"
OUT = Path(__file__).resolve().parent.parent / "data" / "policy_chunks.json"

if __name__ == "__main__":
    chunks = load_policy_chunks(POLICY)
    manifest = [{"id": i, "chars": len(c), "preview": c[:60]} for i, c in enumerate(chunks)]
    OUT.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"Wrote {len(chunks)} chunks to {OUT}")
