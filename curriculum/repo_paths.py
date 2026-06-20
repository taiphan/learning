"""Shared repository paths — curriculum/ is sibling to apps/, lab/, docs/."""

from pathlib import Path

CURRICULUM = Path(__file__).resolve().parent
REPO = CURRICULUM.parent
LAB = REPO / "lab"
APPS_LEARNING = REPO / "apps" / "learning"
APPS_BRD = REPO / "apps" / "brd"
EXPORTS = REPO / "exports"
EXPORTS_LEARNING = EXPORTS / "learning"
