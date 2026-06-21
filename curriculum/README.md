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
| [head-of-ai-track.md](head-of-ai-track.md) | **Track B** — 2h/week Head of AI leadership (W8, 16, 28, 40, 52) |
| [ai-factory-demo-case.md](ai-factory-demo-case.md) | Demo case for Track B governance & value templates |
| [templates/hoai/](templates/hoai/) | Fill-in templates at each Track B checkpoint |
| [templates/hoai/vpbank_steering_one_pager.md](templates/hoai/vpbank_steering_one_pager.md) | Week 52 VPBank HoAI steering one-pager (JD-aligned) |

## Generate assets

```bash
python3 curriculum/generate_all_learning.py
```

Outputs: `learning-data.json`, `lab/`, `exports/learning/Learning-Master-Slides.pptx`, roadmap deck, **Learning-Track-B-Slides.pptx**.

BRD corporate decks: `python3 scripts/generate_office_files.py` → `exports/Learning-BRD-*.pptx`

## Archived (optional)

[../archive/](../archive/) — Head of AI Factory pack, per-week PPTX generators, duplicate catalogs.
