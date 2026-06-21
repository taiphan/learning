#!/usr/bin/env python3
"""Generate lean learning assets from learning_data.py (single source)."""

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from repo_paths import APPS_LEARNING, EXPORTS_LEARNING  # noqa: E402


def sync_decks_to_app():
    dest = APPS_LEARNING / "decks"
    dest.mkdir(parents=True, exist_ok=True)
    for pptx in EXPORTS_LEARNING.glob("*.pptx"):
        shutil.copy2(pptx, dest / pptx.name)
    print(f"   → {dest}/ ({len(list(dest.glob('*.pptx')))} decks)")


def main():
    from learning_loader import export_json
    from scaffold_learning_lab import scaffold

    print("1. Export learning-data.json")
    json_path = export_json()
    print(f"   → {json_path}")

    print("2. Generate all week implementations")
    subprocess.run([sys.executable, str(ROOT / "generate_all_weeks.py")], check=True)

    print("2b. Update WEEKS.md index")
    scaffold()

    scripts = [
        "generate_learning_master_slides.py",
        "generate_ai_roadmap_slides.py",
        "generate_track_b_slides.py",
    ]
    for name in scripts:
        print(f"3. Run {name}")
        subprocess.run([sys.executable, str(ROOT / name)], check=True)

    print("4. Sync slide decks → apps/learning/decks/")
    sync_decks_to_app()

    print("\nDone.")
    print("  Master deck: exports/learning/Learning-Master-Slides.pptx")
    print("  Roadmap:     exports/learning/Zero-to-AI-Expert-Roadmap-Slides.pptx")
    print("  Track B:     exports/learning/Learning-Track-B-Slides.pptx")
    print("  App:         cd apps/learning && python3 -m http.server 8081")


if __name__ == "__main__":
    main()
