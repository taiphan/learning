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

Use **learning** repo as dual base: (1) Finance BRD domain credibility, (2) **curriculum/** 12-month path to hire-ready AI engineer (OCB/NAB/VPBank; Anthropic stretch). Zero Python today · 10 hrs/week.

## Done

- Single learning data source: `learning_data.py` → `learning-data.json`
- **All 52 weeks** — runnable code via `generate_all_weeks.py` (exercises, SQL, projects, notebooks, career templates)
- Shared libs: `lab/lib/` (brd_utils, loan_utils, rag_simple)
- **Learning-Master-Slides.pptx** — 164 slides (3 per week + index); clickable W01–W52
- **exports/learning/weeks/** — 52 individual week decks
- Repo **lean** cleanup: `archive/` (HoAI, duplicate decks/docs); 2 learning PPTX only; `cv-templates.md`

## In progress

- User learning Skill 1 (Python) — start week 1 exercises
- **Blockers:** none

## Next

1. Read [project-adaptation.md](curriculum/project-adaptation.md) — three-app workflow
2. Week 1 loop: learning app → BRD export → `week01_brd_checklist.py`
3. Mark weeks complete in learning app as you finish labs

## Decisions

- Corporate Finance materials stay as-is; personal coding in `lab/` + external repos
- BRD app scoring aligned with `docs/05-brd-quality-checklist.md` — exercises mirror same gates
- SESSION resume = Read this file, not CodeGraph

## Gotchas

- `.agent/SESSION.md` previously had class-ai-agent maintainer goals — replaced for this project
- BRD app is static (no backend); drafts in browser localStorage only
- CodeGraph indexes Python generators + `apps/brd/*.js` — run `codegraph sync` after edits

## Pointers

| Item | Location |
|------|----------|
| Project map | `.agent/PROJECT.md` |
| Adaptation guide | `curriculum/project-adaptation.md` |
| Workbook | `curriculum/ai-skills-workbook.md` |
| Reading order | `curriculum/reading-path.md` |
| BRD app | `apps/brd/` — `python3 -m http.server 8080` |
| Exercises | `lab/exercises/` |
| Branch | `main` |
