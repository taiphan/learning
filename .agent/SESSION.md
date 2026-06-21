# Agent session

> Cross-tool handoff state. Update at session end (`/handoff`); read at start (`/resume`).

## Meta

| Field | Value |
|-------|-------|
| **Updated** | 2026-06-21 |
| **Phase** | build |
| **Tool** | cursor |
| **Persona** | learner — banking BA → AI engineer |

## Goal

Use **learning** repo as dual base: (1) Finance BRD domain credibility, (2) **curriculum/** 12-month path to hire-ready AI engineer (OCB/NAB/VPBank; Anthropic stretch). Zero Python today · 10 hrs/week (8h Track A + 2h Track B).

## Done

- Single learning data source: `learning_data.py` → `learning-data.json`
- **All 52 weeks** — runnable code via `generate_all_weeks.py`
- Shared libs: `lab/lib/` (brd_utils, loan_utils, rag_simple)
- **Learning-Master-Slides.pptx** — 165 slides (Track B on ◆ weeks + H0–H4 slide)
- **Learning-Track-B-Slides.pptx** — 9 slides (VPBank HoAI steering variant)
- **Zero-to-AI-Expert-Roadmap-Slides.pptx** — dual-track + Track B milestone slide
- Repo **lean** cleanup: `archive/`; 3 learning PPTX in `exports/learning/`
- **Track B:** app Leadership tab, H0–H4 templates, VPBank JD §F.4, `vpbank_steering_one_pager.md`
- **App polish:** deck downloads (`apps/learning/decks/`), Track B pill `B 0/5`, Pages deploy `/decks/`

## In progress

- User learning Skill 1 (Python) — start week 1 exercises
- **Blockers:** none

## Next

1. Week 1 loop: learning app → BRD export → `week01_brd_checklist.py`
2. Mark weeks complete in learning app as you finish labs
3. At week 8: complete Track B H0 (AI strategy template) alongside CP1

## Decisions

- Corporate Finance materials stay as-is; personal coding in `lab/` + external repos
- BRD app scoring aligned with `docs/05-brd-quality-checklist.md`
- Head of AI Factory (VPBank) = Year 4–5 stretch; apply AI Engineer first
- SESSION resume = Read this file, not CodeGraph

## Gotchas

- BRD app is static (no backend); drafts in browser localStorage only
- Slide decks: regenerate then `apps/learning/decks/` syncs on `generate_all_learning.py`
- GitHub Pages serves decks at `/decks/*.pptx`

## Pointers

| Item | Location |
|------|----------|
| Project map | `.agent/PROJECT.md` |
| Adaptation guide | `curriculum/project-adaptation.md` |
| Track B guide | `curriculum/head-of-ai-track.md` |
| HoAI templates | `curriculum/templates/hoai/` |
| VPBank JD map | `curriculum/job-skills-adaptation.md` §F.4 |
| Portfolio checklist | `lab/projects/PORTFOLIO.md` |
| Workbook | `curriculum/ai-skills-workbook.md` |
| BRD app | `apps/brd/` |
| Exercises | `lab/exercises/` |
| Branch | `main` |
