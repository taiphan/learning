#!/usr/bin/env python3
"""Generate all learning assets from learning_data.py (single source)."""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))


def main():
    from learning_loader import export_json
    from scaffold_learning_lab import scaffold

    print("1. Export learning-data.json")
    json_path = export_json()
    print(f"   → {json_path}")

    print("2. Generate all week implementations")
    subprocess.run([sys.executable, str(ROOT / "generate_all_weeks.py")], check=True)

    print("2b. Update WEEKS.md index")
    from scaffold_learning_lab import scaffold

    scaffold()

    scripts = [
        "generate_learning_master_slides.py",
        "generate_week_slides.py",
        "generate_ai_skills_slides.py",
        "generate_ai_skills_visual_slides.py",
        "generate_ai_roadmap_slides.py",
    ]
    for name in scripts:
        print(f"3. Run {name}")
        subprocess.run([sys.executable, str(ROOT / name)], check=True)

    print("\nDone. Open exports/Learning-Master-Slides.pptx — click W## on index.")
    print("Individual week decks: exports/weeks/Week-NN-*.pptx")
    print("Learning app: cd learning-app && python3 -m http.server 8081")


if __name__ == "__main__":
    main()
