"""Build app-files-manifest.json — every learning asset browsable in the app Library."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from learning_data import TRACK_B_CHECKPOINTS, WEEKS
from repo_paths import APPS_LEARNING, CURRICULUM, LAB, REPO

REPO_BLOB = "https://github.com/taiphan/learning/blob/main"

CATEGORIES: dict[str, str] = {
    "curriculum": "Curriculum guides",
    "lab": "Lab exercises & projects",
    "track_b": "Track B deliverables",
    "docs": "Requirements & docs",
    "decks": "Slide decks",
    "app": "App & setup",
    "brd": "BRD app",
}

CURRICULUM_DOCS = [
    "career-timeline.md",
    "head-of-ai-track.md",
    "track-b-delivery.md",
    "video-learning-enrichment.md",
    "job-skills-adaptation.md",
    "learning-lab-guide.md",
    "ai-skills-workbook.md",
    "ai-skills-catalog.md",
    "reading-path.md",
    "zero-to-ai-expert-syllabus.md",
    "project-adaptation.md",
    "governance-mlops.md",
    "cv-templates.md",
    "README.md",
]

APP_FILES = [
    "apps/learning/README.md",
    "apps/learning/AUTH-SETUP.md",
    "apps/learning/firestore.rules.example",
    "apps/brd/README.md",
]

APP_SCAN_EXTENSIONS = {".js", ".html", ".css", ".md", ".json"}
APP_SCAN_SKIP_DIRS = {"decks", "data", "__pycache__"}

KIND_BY_EXT = {
    ".md": "markdown",
    ".py": "python",
    ".sql": "sql",
    ".json": "json",
    ".js": "javascript",
    ".html": "html",
    ".css": "css",
    ".pptx": "deck",
    ".txt": "text",
    ".csv": "data",
    ".ipynb": "notebook",
    ".yml": "yaml",
    ".yaml": "yaml",
}


def _kind(path: Path) -> str:
    return KIND_BY_EXT.get(path.suffix.lower(), "file")


def _rel(path: Path) -> str:
    return path.relative_to(REPO).as_posix()


def _entry(
    path: Path,
    *,
    category: str,
    label: str | None = None,
    week: int | None = None,
    description: str | None = None,
    local_url: str | None = None,
) -> dict[str, Any]:
    rel = _rel(path)
    return {
        "path": rel,
        "name": path.name,
        "category": category,
        "kind": _kind(path),
        "label": label or path.name,
        "week": week,
        "description": description,
        "url": f"{REPO_BLOB}/{rel}",
        "local_url": local_url,
    }


def _week_by_exercise() -> dict[str, tuple[int, str]]:
    out: dict[str, tuple[int, str]] = {}
    for w in WEEKS:
        ex = w.get("exercise")
        if ex:
            out[ex.replace("\\", "/")] = (w["week"], w["title"])
        run = w.get("run", "")
        m = re.search(r"exercises/(\S+\.py)", run)
        if m:
            p = f"lab/exercises/{m.group(1)}"
            out.setdefault(p, (w["week"], w["title"]))
    return out


def _collect() -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    seen: set[str] = set()
    week_map = _week_by_exercise()

    def add(entry: dict[str, Any]) -> None:
        if entry["path"] in seen:
            return
        seen.add(entry["path"])
        items.append(entry)

    for name in CURRICULUM_DOCS:
        p = CURRICULUM / name
        if p.is_file():
            add(_entry(p, category="curriculum", label=name.replace(".md", "").replace("-", " ").title()))

    templates = CURRICULUM / "templates"
    if templates.is_dir():
        for p in sorted(templates.rglob("*")):
            if p.is_file() and p.suffix.lower() in {".md", ".txt"}:
                add(_entry(p, category="curriculum", label=p.stem.replace("_", " ").title()))

    for p in sorted(LAB.rglob("*")):
        if not p.is_file():
            continue
        if "__pycache__" in p.parts or p.suffix.lower() in {".pyc", ".db"}:
            continue
        rel = _rel(p)
        if p.suffix.lower() not in {".py", ".sql", ".md", ".csv", ".json", ".ipynb", ".txt"}:
            continue
        cat = "track_b" if "delivery/track-b" in rel else "lab"
        week_info = week_map.get(rel)
        week = week_info[0] if week_info else None
        label = week_info[1] if week_info else p.name
        add(_entry(p, category=cat, label=label, week=week))

    for cp in TRACK_B_CHECKPOINTS:
        fname = {
            "H0": "h0-ai-strategy.md",
            "H1": "h1-pd-value-case.md",
            "H2": "h2-copilot-governance.md",
            "H3": "h3-ninety-day-plan.md",
            "H4": "h4-steering-deck.md",
        }.get(cp["id"])
        if fname:
            p = LAB / "delivery" / "track-b" / fname
            if p.is_file():
                add(
                    _entry(
                        p,
                        category="track_b",
                        label=f"{cp['id']} — {cp['label']}",
                        week=cp["after_week"],
                        description="Save your Track B deliverable here",
                    )
                )

    docs_dir = REPO / "docs" / "learning-requirements"
    if docs_dir.is_dir():
        for p in sorted(docs_dir.glob("*.md")):
            add(_entry(p, category="docs", label=p.stem.replace("-", " ").title()))

    for rel in APP_FILES:
        p = REPO / rel
        if p.is_file():
            cat = "brd" if rel.startswith("apps/brd") else "app"
            add(_entry(p, category=cat, label=p.name))

    if APPS_LEARNING.is_dir():
        for p in sorted(APPS_LEARNING.rglob("*")):
            if not p.is_file():
                continue
            if any(part in APP_SCAN_SKIP_DIRS for part in p.parts):
                continue
            if p.suffix.lower() not in APP_SCAN_EXTENSIONS:
                continue
            rel = _rel(p)
            if rel in seen:
                continue
            label = p.stem.replace("-", " ").title() if p.suffix.lower() != ".json" else f"Data: {p.stem}"
            desc = "Generated export" if p.parent.name == "data" else None
            add(_entry(p, category="app", label=label, description=desc))

    decks_dir = APPS_LEARNING / "decks"
    if decks_dir.is_dir():
        for p in sorted(decks_dir.glob("*.pptx")):
            add(
                _entry(
                    p,
                    category="decks",
                    label=p.stem.replace("-", " "),
                    local_url=f"decks/{p.name}",
                )
            )

    return sorted(items, key=lambda x: (x["category"], x.get("week") or 0, x["path"]))


def manifest_dict() -> dict[str, Any]:
    files = _collect()
    by_cat: dict[str, int] = {}
    for f in files:
        by_cat[f["category"]] = by_cat.get(f["category"], 0) + 1
    return {
        "version": "1.0",
        "repo": "https://github.com/taiphan/learning",
        "repo_blob": REPO_BLOB,
        "categories": CATEGORIES,
        "total": len(files),
        "counts": by_cat,
        "files": files,
    }


def export_files_manifest(path: Path | None = None) -> Path:
    path = path or APPS_LEARNING / "data" / "app-files-manifest.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(manifest_dict(), indent=2, ensure_ascii=False) + "\n"
    path.write_text(payload, encoding="utf-8")
    return path


if __name__ == "__main__":
    out = export_files_manifest()
    m = json.loads(out.read_text())
    print(f"→ {out} ({m['total']} files)")
