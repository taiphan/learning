# 52-Week Learning App

Browser cockpit for the AI engineer learning path — progress tracking, study/lab tabs, notes.

## Run locally

```bash
cd apps/learning
python3 -m http.server 8081
# Open http://localhost:8081
```

**Important:** Use a local server (not `file://`) so the app can load `learning-data.json`.

## Regenerate curriculum JSON

```bash
python3 curriculum/generate_all_learning.py
# or export only:
python3 -c "import sys; sys.path.insert(0,'curriculum'); from learning_loader import export_json; export_json()"
```

## Data source

Single source: [`learning_data.py`](../curriculum/learning_data.py) → [`learning-data.json`](learning-data.json)

Same content as slide decks and `lab/` exercises.

## Related

- [Learning lab](../../lab/README.md) — hands-on Python exercises
- [Learning Master Slides](../../exports/learning/Learning-Master-Slides.pptx)
- [Workbook](../curriculum/ai-skills-workbook.md)
- [BRD Intake app](../brd/) — Week 1 bridge
