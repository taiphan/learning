# Project structure map

> Persistent overview for AI agents. Updated 2026-06-21.

## Meta

| Field | Value |
|-------|-------|
| **Updated** | 2026-06-21 |
| **Tool** | cursor |
| **Owner context** | Banking domain expert · zero Python · 12-month AI engineer path |

## Stack

| Layer | Technology |
|-------|------------|
| Learning app | Vanilla JS, HTML, CSS — no build step |
| BRD web app | Vanilla JS (ES modules), HTML, CSS — no build step |
| Office exports | Python 3.11+ · `python-docx` · `python-pptx` |
| Curriculum decks | Python · `anthropic_theme.py` |
| Learning lab | Python exercises · CSV/SQL · Jupyter |
| Agent scaffolding | `class-ai-agent` 1.6.5 · `.cursor/` `.claude/` `.kiro/` `.agents/` |
| Code intelligence | CodeGraph · `.codegraph/codegraph.db` |

## Layout

| Path | Purpose |
|------|---------|
| `apps/learning/` | **52-week learning cockpit** — progress, study/lab tabs, localStorage |
| `apps/brd/` | **BRD Intake web app** — 8-step wizard, scoring, export (VI/EN) |
| `apps/brd/config/learning.js` | Org, BUs, apps, products, score weights, routing rules |
| `curriculum/` | `learning_data.py`, generators, workbook, career docs |
| `lab/` | Hands-on Python/SQL exercises (week01–52), projects, notebooks |
| `docs/` | BRD templates, governance, IT ops, ServiceNow mapping (00–14) |
| `examples/` | Gold-standard sample BRDs |
| `training/` | Trainer slide outlines and speaker notes |
| `exports/learning/` | **2 slide decks** — Master (52 weeks) + Roadmap |
| `exports/` | BRD training DOCX/PPTX (`Learning-BRD-*`) |
| `archive/` | HoAI pack, superseded docs, optional generators |
| `scripts/generate_office_files.py` | Master generator for BRD Word/PowerPoint |
| `.agent/` | Session handoff (`SESSION.md`), this map |

## Entry points

| What | How to run |
|------|------------|
| **Learning app** | `cd apps/learning && python3 -m http.server 8081` |
| **BRD Intake App** | `cd apps/brd && python3 -m http.server 8080` |
| **Live site** | https://taiphan.github.io/learning/ (learning) · `/brd/` (BRD) |
| **Regenerate curriculum** | `python3 curriculum/generate_all_learning.py` |
| **Week 1 exercise** | `python3 lab/exercises/week01_brd_checklist.py` |

## Key files

| Area | Files |
|------|-------|
| BRD template | `docs/01-brd-template-en.md`, `docs/05-brd-quality-checklist.md` |
| App config / scoring | `apps/brd/config/learning.js` |
| App core logic | `apps/brd/app.js` |
| Curriculum source | `curriculum/learning_data.py` → `learning-data.json` |
| Adaptation guide | `curriculum/project-adaptation.md` |
| Sample BRD | `examples/04a-brd-pos-lending.md` |

## Commands

| Action | Command |
|--------|---------|
| Run learning app | `cd apps/learning && python3 -m http.server 8081` |
| Run BRD app | `cd apps/brd && python3 -m http.server 8080` |
| Generate all learning assets | `python3 curriculum/generate_all_learning.py` |
| Generate BRD exports | `python3 scripts/generate_office_files.py` |
| CodeGraph re-index | `codegraph index --force` |

## Notes

- **Dual purpose repo:** (1) BRD training package (`docs/`, `apps/brd/`), (2) personal zero→AI-engineer journey (`curriculum/`, `lab/`, `apps/learning/`).
- **No backend:** drafts in `localStorage` (`learning-brd-draft`, `learning-ai-learning-progress`).
- **Scoring gate:** Export warns if quality score &lt; 80%.
