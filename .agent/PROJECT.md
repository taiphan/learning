# Project structure map

> Persistent overview for AI agents. Updated 2026-06-20 via `/understand` (Cursor).

## Meta

| Field | Value |
|-------|-------|
| **Updated** | 2026-06-20 |
| **Tool** | cursor |
| **Owner context** | Banking domain expert · zero Python · 12-month AI engineer path |

## Stack

| Layer | Technology |
|-------|------------|
| BRD web app | Vanilla JS (ES modules), HTML, CSS — no build step |
| Office exports | Python 3.11+ · `python-docx` · `python-pptx` |
| AI-factory decks | Python · `anthropic_theme.py` (Anthropic brand PPTX/DOCX) |
| Learning lab | Python exercises · CSV/SQL · Jupyter (planned) |
| Agent scaffolding | `class-ai-agent` 1.6.5 · `.cursor/` `.claude/` `.kiro/` `.agents/` |
| Code intelligence | CodeGraph 1.0.1 · `.codegraph/codegraph.db` (22 files indexed) |

## Layout

| Path | Purpose |
|------|---------|
| `app/` | **BRD Intake web app** — 8-step wizard, scoring, export (VI/EN) |
| `ai-factory/learning-app/` | **52-week learning cockpit** — progress, study/lab tabs, localStorage |
| `app/config/finance.js` | Org, BUs, apps, products, score weights, routing rules |
| `app/app.js` | Form logic, scoring, risk, export, i18n (~860 lines) |
| `docs/` | BRD templates, governance, IT ops, ServiceNow mapping (00–14) |
| `examples/` | Gold-standard sample BRDs (POS lending, eKYC, collections) |
| `training/` | Trainer slide outlines and speaker notes |
| `exports/` | Generated DOCX/PPTX (Finance training + AI learning decks) |
| `scripts/generate_office_files.py` | Master generator for Finance Word/PowerPoint |
| `ai-factory/` | **Personal AI learning path** — syllabus, workbook, career docs, slide generators |
| `ai-factory/learning-lab/` | Hands-on Python/SQL exercises (week01–02 + solutions) |
| `ai-factory/exports/` | AI Skills slides, roadmap, visual deck |
| `.agent/` | Session handoff (`SESSION.md`), this map, onboarding marker |
| `.cursor/` | Cursor rules, commands, MCP config (CodeGraph, Supabase) |

## Entry points

| What | How to run |
|------|------------|
| **BRD Intake App** | `cd app && python3 -m http.server 8080` → http://localhost:8080 |
| **Learning app (52 weeks)** | `cd ai-factory/learning-app && python3 -m http.server 8081` |
| **Live site** | https://taiphan.github.io/finance-brd-training/ (learning) · `/brd/` (BRD) |
| **Regenerate curriculum** | `python3 ai-factory/generate_all_learning.py` |
| **AI skills slides** | `python3 ai-factory/generate_ai_skills_slides.py` |
| **AI visual slides** | `python3 ai-factory/generate_ai_skills_visual_slides.py` |
| **AI roadmap slides** | `python3 ai-factory/generate_ai_roadmap_slides.py` |
| **Week 1 exercise** | `python3 ai-factory/learning-lab/exercises/week01_brd_checklist.py` |

## Key files

| Area | Files |
|------|-------|
| BRD template (source of truth) | `docs/01-brd-template-en.md`, `docs/05-brd-quality-checklist.md` |
| App config / scoring | `app/config/finance.js` — `scoreWeights`, `selfCheckItems`, `requestTypes` |
| App core logic | `app/app.js` — `computeScore`, `exportBRD`, `computeRouting`, `init` |
| Sample BRD for exercises | `examples/04a-brd-pos-lending.md` |
| Learning start | `ai-factory/ai-skills-workbook.md`, `ai-factory/reading-path.md` |
| Career targets | `ai-factory/job-skills-adaptation.md`, `ai-factory/cv-cover-letter.md` |
| AI governance narrative | `ai-factory/governance-mlops.md` |
| Adaptation guide | `ai-factory/project-adaptation.md` |

## Commands

| Action | Command |
|--------|---------|
| Install npm dep | `npm install` (class-ai-agent only) |
| Run BRD app | `cd app && python3 -m http.server 8080` |
| Generate FE exports | `python3 scripts/generate_office_files.py` |
| Generate AI decks | `python3 ai-factory/generate_ai_skills_*.py` |
| CodeGraph status | `codegraph status` |
| CodeGraph re-index | `codegraph index --force` |
| Python exercises | `cd ai-factory/learning-lab/exercises && python3 week01_*.py` |

## Code intelligence

| Item | Status |
|------|--------|
| CodeGraph index | Present — `/Users/phantuantai/Projects/finance/.codegraph/` |
| Indexed | 22 files · 555 nodes · Python generators + `app/app.js`, `finance.js` |
| Workspace root | `/Users/phantuantai/Projects/finance` |
| OntoSight | `npx @royalsolution/ontosight@0.2.0 "/Users/phantuantai/Projects/finance" --symbol init --path app` |

## Notes

- **Dual purpose repo:** (1) Finance corporate BRD training package, (2) `ai-factory/` overlay for personal zero→AI-engineer journey.
- **No backend:** BRD app is static; drafts in `localStorage` key `finance-brd-draft`.
- **Scoring gate:** Export warns if quality score &lt; 80% — mirrors `docs/05-brd-quality-checklist.md`.
- **Do not commit:** `.env`, API keys, real customer PII in BRD exports.
- **SESSION.md** was from class-ai-agent template — updated for this project's learning goal.
