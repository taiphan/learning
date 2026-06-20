# AI Learning App — Week by week

Interactive browser app for the **52-week Banking → AI Engineer** path. Progress is saved in your browser (localStorage).

## Run locally

```bash
cd ai-factory/learning-app
python3 -m http.server 8081
# Open http://localhost:8081
```

**Important:** Use a local server (not `file://`) so the app can load `../learning-data.json`.

If curriculum changed, regenerate JSON first:

```bash
python3 ai-factory/generate_all_learning.py
# or only JSON:
python3 -c "import sys; sys.path.insert(0,'ai-factory'); from learning_loader import export_json; export_json()"
```

## Features

| Feature | Description |
|---------|-------------|
| **Dashboard** | Progress %, current week, next checkpoint |
| **Week sidebar** | All 52 weeks, filter by phase, ✓ when complete |
| **Week detail** | Overview · Study · Lab · Notes tabs |
| **Lab tab** | Exercise path, run command (copy button), done-when checklist |
| **Progress** | Mark week complete — stored locally |
| **Continue** | Jumps to first incomplete week |

## Data source

Single source: [`learning_data.py`](../learning_data.py) → [`learning-data.json`](../learning-data.json)

Same content as slide decks and `learning-lab/` exercises.

## Related

- [Learning lab](../learning-lab/README.md) — hands-on Python exercises
- [Learning Master Slides](../exports/Learning-Master-Slides.pptx)
- [Workbook](../ai-skills-workbook.md)
