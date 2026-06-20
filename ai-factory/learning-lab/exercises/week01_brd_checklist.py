#!/usr/bin/env python3
"""Week 1 — BRD section audit."""
import argparse
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'lib'))

from brd_utils import MANDATORY_SECTIONS, audit_brd, load_brd_text

SAMPLE = Path(__file__).resolve().parent.parent / "data" / "sample_brd_app_export.md"
DEFAULT = Path(__file__).resolve().parent.parent / "data" / "sample_brd_app_export.md"

def print_report(results, source):
    print("=== BRD Section Audit ===")
    print(f"Source: {source}\n")
    missing = [s for s, ok in results.items() if not ok]
    for s, ok in results.items():
        print(f"  [{'OK' if ok else 'MISSING'}] {s}")
    print("\nAction: add " + ", ".join(missing) if missing else "\nAll mandatory sections present.")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("brd_file", nargs="?", type=Path)
    p.add_argument("--app-sample", action="store_true")
    a = p.parse_args()
    path = DEFAULT if a.app_sample else a.brd_file
    text = load_brd_text(path, "")
    if not text and not path:
        text = load_brd_text(None, "EXECUTIVE SUMMARY\nOBJECTIVES\nSCOPE\nBUSINESS RULES")
    print_report(audit_brd(text), str(path or "inline"))
