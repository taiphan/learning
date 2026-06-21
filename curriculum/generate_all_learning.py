#!/usr/bin/env python3
"""Generate lean learning assets from learning_data.py (single source)."""

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
    scaffold()

    scripts = [
        "generate_learning_master_slides.py",
        "generate_ai_roadmap_slides.py",
        "generate_track_b_slides.py",
    ]
    for name in scripts:
        print(f"3. Run {name}")
        subprocess.run([sys.executable, str(ROOT / name)], check=True)

    print("\nDone.")
    print("  Master deck: exports/learning/Learning-Master-Slides.pptx")
    print("  Roadmap:     exports/learning/Zero-to-AI-Expert-Roadmap-Slides.pptx")
    print("  Track B:     exports/learning/Learning-Track-B-Slides.pptx")
    print("  App:         cd apps/learning && python3 -m http.server 8081")


if __name__ == "__main__":
    main()
