"""Load curriculum from learning_data.py — resolve colors, export JSON."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from learning_data import CHECKPOINTS, CAREER_PATH, META, PHASES, SKILLS, TRACK_B_CHECKPOINTS, WEEKS
from repo_paths import APPS_LEARNING, CURRICULUM

COLOR_MAP: dict[str, Any] = {}


def _resolve_colors() -> None:
    from anthropic_theme import CLAY, SKY, OLIVE, FIG, CACTUS, SLATE

    COLOR_MAP.update(
        {
            "CLAY": CLAY,
            "SKY": SKY,
            "OLIVE": OLIVE,
            "FIG": FIG,
            "CACTUS": CACTUS,
            "SLATE": SLATE,
        }
    )


def skill_by_id(skill_id: int) -> dict[str, Any]:
    for s in SKILLS:
        if s["id"] == skill_id:
            return s
    raise KeyError(f"skill_id {skill_id}")


def weeks_for_skill(skill_id: int) -> list[dict]:
    return [w for w in WEEKS if w["skill_id"] == skill_id]


def phase_for_week(week_num: int) -> dict:
    w = next(x for x in WEEKS if x["week"] == week_num)
    return next(p for p in PHASES if p["id"] == w["phase"])


def curriculum_dict() -> dict[str, Any]:
    return {
        "meta": META,
        "phases": PHASES,
        "career_path": CAREER_PATH,
        "skills": SKILLS,
        "weeks": WEEKS,
        "checkpoints": CHECKPOINTS,
        "track_b_checkpoints": TRACK_B_CHECKPOINTS,
    }


def export_json(path: Path | None = None) -> Path:
    path = path or CURRICULUM / "learning-data.json"
    payload = json.dumps(curriculum_dict(), indent=2, ensure_ascii=False) + "\n"
    path.write_text(payload, encoding="utf-8")
    app_copy = APPS_LEARNING / "learning-data.json"
    app_copy.parent.mkdir(parents=True, exist_ok=True)
    app_copy.write_text(payload, encoding="utf-8")
    return path


def skills_for_slides() -> list[dict]:
    """Skills with accent RGB resolved for PPTX generators."""
    _resolve_colors()
    out = []
    for s in SKILLS:
        row = dict(s)
        row["accent"] = COLOR_MAP[s["color"]]
        out.append(row)
    return out


def phase_color(phase_id: str):
    _resolve_colors()
    p = next(x for x in PHASES if x["id"] == phase_id)
    return COLOR_MAP[p["color"]]
