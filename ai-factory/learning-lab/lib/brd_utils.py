"""Shared BRD audit helpers — weeks 1, 3, 4."""

from __future__ import annotations

from pathlib import Path

MANDATORY_SECTIONS = [
    "EXECUTIVE SUMMARY",
    "OBJECTIVES",
    "SCOPE",
    "BUSINESS RULES",
    "ACCEPTANCE CRITERIA",
]

SECTION_WEIGHTS: dict[str, float] = {
    "EXECUTIVE SUMMARY": 15,
    "OBJECTIVES": 15,
    "SCOPE": 10,
    "BUSINESS RULES": 25,
    "ACCEPTANCE CRITERIA": 20,
}


def load_brd_text(path: Path | None, fallback: str) -> str:
    if path is None:
        return fallback
    if not path.is_file():
        raise FileNotFoundError(f"BRD file not found: {path}")
    return path.read_text(encoding="utf-8")


def brd_has_section(text: str, section_title: str) -> bool:
    needle = section_title.upper()
    for line in text.splitlines():
        if line.strip().startswith("#") and needle in line.upper():
            return True
    return False


def audit_brd(text: str, required: list[str] | None = None) -> dict[str, bool]:
    required = required or MANDATORY_SECTIONS
    return {s: brd_has_section(text, s) for s in required}


def weighted_score(results: dict[str, bool]) -> float:
    total_w = sum(SECTION_WEIGHTS.get(s, 10) for s in results)
    earned = sum(SECTION_WEIGHTS.get(s, 10) for s, ok in results.items() if ok)
    return 100.0 * earned / total_w if total_w else 0.0


class BRDScorecard:
    def __init__(self, text: str, required: list[str] | None = None):
        self.text = text
        self.required = required or MANDATORY_SECTIONS
        self.results = audit_brd(text, self.required)

    def score(self) -> float:
        return weighted_score(self.results)

    def missing_sections(self) -> list[str]:
        return [s for s, ok in self.results.items() if not ok]

    def report(self) -> str:
        lines = ["=== BRD Scorecard ===", f"Score: {self.score():.1f}%", ""]
        for section, ok in self.results.items():
            lines.append(f"  [{'OK' if ok else 'MISSING'}] {section}")
        missing = self.missing_sections()
        if missing:
            lines.append(f"\nAction: add {', '.join(missing)}")
        return "\n".join(lines)
