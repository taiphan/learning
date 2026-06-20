# Agent session

> Cross-tool handoff state. Update at session end (`/handoff`); read at start (`/resume`).

## Meta

| Field | Value |
|-------|-------|
| **Updated** | 2026-06-20 |
| **Phase** | build |
| **Tool** | cursor |
| **Persona** | learner — banking BA → AI engineer |

## Goal

Use **fe-credit-brd-training** as dual base: (1) FE Credit BRD domain credibility, (2) **ai-factory/** 12-month path to hire-ready AI engineer (OCB/NAB/VPBank; Anthropic stretch). Zero Python today · 10 hrs/week.

## Done

- Single learning data source: `learning_data.py` → `learning-data.json`
- **All 52 weeks** — runnable code via `generate_all_weeks.py` (exercises, SQL, projects, notebooks, career templates)
- Shared libs: `learning-lab/lib/` (brd_utils, loan_utils, rag_simple)
- **Learning-Master-Slides.pptx** — 164 slides (3 per week + index); clickable W01–W52
- **exports/weeks/** — 52 individual week decks (4 slides each: title + overview + study + lab)
- AI skills catalog, workbook, visual decks wired to same data source

## In progress

- User learning Skill 1 (Python) — start week 1 exercises
- **Blockers:** none

## Next

1. **Learning app:** `cd ai-factory/learning-app && python3 -m http.server 8081`
2. `cd ai-factory/learning-lab && pip install -r requirements.txt && python3 setup_db.py`
3. Follow week 1 in the app → run lab commands in Cursor

## Decisions

- Corporate FE Credit materials stay as-is; personal coding in `ai-factory/learning-lab/` + external repos
- BRD app scoring aligned with `docs/05-brd-quality-checklist.md` — exercises mirror same gates
- SESSION resume = Read this file, not CodeGraph

## Gotchas

- `.agent/SESSION.md` previously had class-ai-agent maintainer goals — replaced for this project
- BRD app is static (no backend); drafts in browser localStorage only
- CodeGraph indexes Python generators + `app/*.js` — run `codegraph sync` after edits

## Pointers

| Item | Location |
|------|----------|
| Project map | `.agent/PROJECT.md` |
| Adaptation guide | `ai-factory/project-adaptation.md` |
| Workbook | `ai-factory/ai-skills-workbook.md` |
| Reading order | `ai-factory/reading-path.md` |
| BRD app | `app/` — `python3 -m http.server 8080` |
| Exercises | `ai-factory/learning-lab/exercises/` |
| Branch | `main` |
