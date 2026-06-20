# Learning — 52-Week Banking → AI Engineer Path

Local folder: `~/Projects/learning` · GitHub: [learning](https://github.com/taiphan/learning)

Training materials, **learning app**, and **Learning BRD intake app** for business users (consumer finance scenario — FE ONLINE 2.0, Finacle on AWS, nationwide POS).

## Repository layout

```
learning/
├── apps/
│   ├── learning/     # 52-week cockpit (GitHub Pages `/`)
│   └── brd/          # BRD intake wizard (`/brd/`)
├── curriculum/       # learning_data.py, generators, workbook, career docs
├── lab/              # Python/SQL exercises, projects, notebooks
├── docs/             # BRD templates, governance, IT ops
├── examples/         # Sample BRDs
├── training/         # Trainer slide outlines
├── exports/
│   ├── learning/     # AI learning slide decks + weeks/
│   └── *.pptx        # BRD training exports (Word/PPTX)
└── scripts/          # Office file generator for BRD package
```

## Quick start — Learning app

```bash
cd apps/learning && python3 -m http.server 8081
# Open http://localhost:8081
```

## Quick start — BRD Intake App

```bash
cd apps/brd && python3 -m http.server 8080
# Open http://localhost:8080
```

See [apps/brd/README.md](apps/brd/README.md).

## Regenerate curriculum

```bash
python3 curriculum/generate_all_learning.py
```

| Resource | Path |
|----------|------|
| Learning app | [apps/learning](apps/learning/) |
| Lab exercises | [lab](lab/) |
| Curriculum source | [curriculum/learning_data.py](curriculum/learning_data.py) |

**Live site:** https://taiphan.github.io/learning/ — learning app at `/`, BRD intake at `/brd/`.

## Contents

| # | File | Description |
|---|------|-------------|
| 0 | [docs/00-finance-application-landscape.md](docs/00-finance-application-landscape.md) | **Finance apps & systems** — reference for BRD writers |
| 1 | [docs/01-brd-template-en.md](docs/01-brd-template-en.md) | Full BRD template (English) — copy into Word/Confluence |
| 2 | [docs/02-brd-template-bilingual-vi-en.md](docs/02-brd-template-bilingual-vi-en.md) | Bilingual BRD template (Vietnamese + English) for field teams |
| 3 | [training/03-trainer-slide-outline.md](training/03-trainer-slide-outline.md) | Trainer slide outline (28 slides, 4 sessions) |
| 4a | [examples/04a-brd-pos-lending.md](examples/04a-brd-pos-lending.md) | Sample BRD: POS motorbike/installment lending |
| 4b | [examples/04b-brd-fe-online-ekyc.md](examples/04b-brd-fe-online-ekyc.md) | Sample BRD: FE ONLINE 2.0 eKYC |
| 4c | [examples/04c-brd-collections-automation.md](examples/04c-brd-collections-automation.md) | Sample BRD: collections automation |
| 5 | [docs/05-brd-quality-checklist.md](docs/05-brd-quality-checklist.md) | BA quality rubric (≥ 80% gate) |
| 6 | [docs/06-brd-cheat-sheet.md](docs/06-brd-cheat-sheet.md) | One-page BRD cheat sheet |
| 7 | [docs/07-servicenow-jira-intake-mapping.md](docs/07-servicenow-jira-intake-mapping.md) | ITSM field mapping |
| 8 | [docs/08-confluence-structure.md](docs/08-confluence-structure.md) | Confluence space structure |
| 9 | [docs/09-rollout-plan-8-weeks.md](docs/09-rollout-plan-8-weeks.md) | 8-week rollout plan |
| 10 | [docs/10-governance-raci.md](docs/10-governance-raci.md) | Governance RACI |
| 11 | [docs/11-operations-manager-checklist.md](docs/11-operations-manager-checklist.md) | Ops manager checklist |
| 12 | [docs/12-it-operations-stakeholder-framework.md](docs/12-it-operations-stakeholder-framework.md) | IT Ops stakeholder framework |
| 13 | [docs/13-service-owner-delivery-control-guide.md](docs/13-service-owner-delivery-control-guide.md) | Service owner guide |
| 14 | [docs/14-it-operations-runbook.md](docs/14-it-operations-runbook.md) | IT operations runbook |

## AI learning path

Adaptation guide: [curriculum/project-adaptation.md](curriculum/project-adaptation.md)

Workbook: [curriculum/ai-skills-workbook.md](curriculum/ai-skills-workbook.md)

## Generate office files

```bash
python3 scripts/generate_office_files.py
```

Outputs to `exports/` (BRD training DOCX/PPTX).

## License

Internal training use.
