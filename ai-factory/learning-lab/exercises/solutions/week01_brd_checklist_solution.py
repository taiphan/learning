#!/usr/bin/env python3
"""Week 1 SOLUTION — BRD section checklist with file input."""

import argparse
from pathlib import Path

MANDATORY_SECTIONS = [
    "EXECUTIVE SUMMARY",
    "OBJECTIVES",
    "SCOPE",
    "BUSINESS RULES",
    "ACCEPTANCE CRITERIA",
]

SAMPLE_BRD_TEXT = """
## EXECUTIVE SUMMARY
POS staff cannot see approved loan status during customer visit.

## BUSINESS OBJECTIVES
Reduce drop-off from 18% to 10%.

## SCOPE
In scope: POS visibility. Out of scope: new product design.

## BUSINESS RULES
Approval authority: branch manager for amounts under 100M VND.
"""

DEFAULT_SAMPLE = Path(__file__).resolve().parent.parent.parent / "data" / "sample_brd_app_export.md"


def load_brd_text(path: Path | None) -> str:
    if path is None:
        return SAMPLE_BRD_TEXT
    if not path.is_file():
        raise FileNotFoundError(f"BRD file not found: {path}")
    return path.read_text(encoding="utf-8")


def brd_has_section(text: str, section_title: str) -> bool:
    """Return True if a markdown heading contains section_title (case-insensitive)."""
    needle = section_title.upper()
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#") and needle in stripped.upper():
            return True
    return False


def audit_brd(text: str, required: list[str]) -> dict[str, bool]:
    return {section: brd_has_section(text, section) for section in required}


def print_report(results: dict[str, bool], source: str) -> None:
    print("=== BRD Section Audit ===")
    print(f"Source: {source}\n")
    missing = []
    for section, ok in results.items():
        status = "OK" if ok else "MISSING"
        print(f"  [{status}] {section}")
        if not ok:
            missing.append(section)
    if missing:
        print(f"\nAction: add sections: {', '.join(missing)}")
    else:
        print("\nAll mandatory sections present.")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Audit a BRD markdown file.")
    parser.add_argument("brd_file", nargs="?", type=Path)
    parser.add_argument("--app-sample", action="store_true")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    if args.app_sample:
        brd_path = DEFAULT_SAMPLE
    elif args.brd_file:
        brd_path = args.brd_file
    else:
        brd_path = None

    text = load_brd_text(brd_path)
    source = str(brd_path) if brd_path else "built-in SAMPLE_BRD_TEXT"
    print_report(audit_brd(text, MANDATORY_SECTIONS), source)
