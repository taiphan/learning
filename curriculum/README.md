# Curriculum — 52-Week Learning Path

**Start here:** [project-adaptation.md](project-adaptation.md) → [apps/learning/](../apps/learning/) Week 1.

| File | Use when |
|------|----------|
| [learning_data.py](learning_data.py) | **Source of truth** — weeks, skills, lab paths (edit → regenerate) |
| [project-adaptation.md](project-adaptation.md) | How BRD app + learning app + lab connect |
| [zero-to-ai-expert-syllabus.md](zero-to-ai-expert-syllabus.md) | 12-month timeline overview |
| [reading-path.md](reading-path.md) | Books & free resources by phase |
| [ai-skills-workbook.md](ai-skills-workbook.md) | Deep exercises, steps, answers per skill |
| [learning-lab-guide.md](learning-lab-guide.md) | How to study (4-step loop, env setup) |
| [job-skills-adaptation.md](job-skills-adaptation.md) | OCB / NAB / VPBank JD mapping |
| [anthropic-career-adaptation.md](anthropic-career-adaptation.md) | Anthropic stretch roles |
| [cv-templates.md](cv-templates.md) | CV & cover letter (Week 45+) |
| [governance-mlops.md](governance-mlops.md) | Responsible AI / MLOps (Weeks 37–40) |

## Generate assets

```bash
python3 curriculum/generate_all_learning.py
```

Outputs: `learning-data.json`, `lab/`, `exports/learning/Learning-Master-Slides.pptx`, roadmap deck.

BRD corporate decks: `python3 scripts/generate_office_files.py` → `exports/Learning-BRD-*.pptx`

## Archived (optional)

[../archive/](../archive/) — Head of AI Factory pack, per-week PPTX generators, duplicate catalogs.
