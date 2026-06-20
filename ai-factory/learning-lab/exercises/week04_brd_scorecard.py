#!/usr/bin/env python3
"""Week 4 — BRDScorecard class."""
import argparse
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'lib'))

from brd_utils import BRDScorecard, load_brd_text

DEFAULT = Path(__file__).resolve().parent.parent / "data" / "sample_brd_app_export.md"

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("brd_file", nargs="?", type=Path, default=DEFAULT)
    a = p.parse_args()
    card = BRDScorecard(load_brd_text(a.brd_file, ""))
    print(card.report())
