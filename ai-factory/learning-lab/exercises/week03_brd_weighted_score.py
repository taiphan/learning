#!/usr/bin/env python3
"""Week 3 — Weighted BRD quality score."""
import argparse
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'lib'))

from brd_utils import load_brd_text, audit_brd, weighted_score, MANDATORY_SECTIONS

DEFAULT = Path(__file__).resolve().parent.parent / "data" / "sample_brd_app_export.md"

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("brd_file", nargs="?", type=Path, default=DEFAULT)
    a = p.parse_args()
    text = load_brd_text(a.brd_file, "")
    results = audit_brd(text)
    score = weighted_score(results)
    print(f"Weighted BRD score: {score:.1f}%")
    for s in MANDATORY_SECTIONS:
        print(f"  [{'OK' if results[s] else 'MISS'}] {s} (weight applied)")
    print("Gate ≥80%:", "PASS" if score >= 80 else "FAIL — revise before export")
