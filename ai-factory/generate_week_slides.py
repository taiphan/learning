#!/usr/bin/env python3
"""Generate individual PPTX deck for each of the 52 weeks."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from learning_data import WEEKS  # noqa: E402
from week_slide_builders import build_single_week_deck, week_slug  # noqa: E402

OUTPUT = ROOT / "exports" / "weeks"
OUTPUT.mkdir(parents=True, exist_ok=True)


def generate() -> list[Path]:
    paths: list[Path] = []
    for week in WEEKS:
        name = week_slug(week) + ".pptx"
        out = OUTPUT / name
        build_single_week_deck(week, out)
        paths.append(out)
        print(f"  Week {week['week']:02d} → {out.name}")
    print(f"\nCreated {len(paths)} week decks in {OUTPUT}")
    return paths


if __name__ == "__main__":
    generate()
