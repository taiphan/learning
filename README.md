# Learning — 52-Week Banking → AI Engineer Path

Local folder: `~/Projects/learning` · GitHub: [learning](https://github.com/taiphan/learning)

Training materials, **learning app**, and **Finance BRD intake app** for business users (consumer finance — FE ONLINE 2.0, Finacle on AWS, nationwide POS).

## Quick start — BRD Intake App

```bash
cd app && python3 -m http.server 8080
# Open http://localhost:8080
```

See [app/README.md](app/README.md).

## AI learning path (52 weeks)

```bash
cd ai-factory/learning-app && python3 -m http.server 8081
# Open http://localhost:8081
```

| Resource | Path |
|----------|------|
| Learning app | [ai-factory/learning-app](ai-factory/learning-app/) |
| Lab exercises | [ai-factory/learning-lab](ai-factory/learning-lab/) |
| Curriculum source | [ai-factory/learning_data.py](ai-factory/learning_data.py) |

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
| 4c | [examples/04c-brd-collections-automation.md](examples/04c-brd-collections-automation.md) | Sample BRD: Collections automation |
| — | [docs/05-brd-quality-checklist.md](docs/05-brd-quality-checklist.md) | Quality checklist and scoring rubric |
| — | [docs/06-brd-cheat-sheet.md](docs/06-brd-cheat-sheet.md) | 1-page cheat sheet for business users |
| 5 | [docs/07-servicenow-jira-intake-mapping.md](docs/07-servicenow-jira-intake-mapping.md) | ServiceNow/Jira form — 46 fields, routing, SLA |
| 6 | [docs/08-confluence-structure.md](docs/08-confluence-structure.md) | Confluence space layout and dashboard |
| 7 | [docs/09-rollout-plan-8-weeks.md](docs/09-rollout-plan-8-weeks.md) | 8-week training and governance rollout |
| 8 | [docs/10-governance-raci.md](docs/10-governance-raci.md) | RACI, approval matrix, escalation |
| 9 | [docs/11-operations-manager-checklist.md](docs/11-operations-manager-checklist.md) | **Ops Manager checklist** — intake, deployment gates, risk control |
| 10 | [docs/12-it-operations-stakeholder-framework.md](docs/12-it-operations-stakeholder-framework.md) | **Stakeholder framework** — dev, business, IT-Governance, IT-Security, GRC, audit, BOD |
| 11 | [docs/13-service-owner-delivery-control-guide.md](docs/13-service-owner-delivery-control-guide.md) | **SO/Manager guide** — pipeline control, evaluation, BA/Dev/QC/Ops sizing |
| 12 | [docs/14-it-operations-runbook.md](docs/14-it-operations-runbook.md) | **Ops runbook** — SR bucket allocation, BOD/EOD/EOM/BOM, incidents, post-mortem |
| — | [training/07-it-operations-slide-outline.md](training/07-it-operations-slide-outline.md) | **IT Ops guide** — delivery control, SR, incidents, BOD/EOD monitoring |
| — | [training/06-business-user-brd-writing-slides-outline.md](training/06-business-user-brd-writing-slides-outline.md) | Business user BRD writing guide — slide outline |
| — | [training/05-it-delivery-agile-slide-outline.md](training/05-it-delivery-agile-slide-outline.md) | IT delivery + Agile/Scrum slide outline |
| — | [training/04-trainer-speaker-notes.md](training/04-trainer-speaker-notes.md) | Detailed facilitator speaker notes |
| — | [app/](app/) | **BRD intake web app** (VI/EN, routing, export) |

## Office exports (Word / PowerPoint)

Generate with:

```bash
python3 scripts/generate_office_files.py
```

| File | Description |
|------|-------------|
| `exports/Finance-BRD-Template.docx` | Fillable BRD template for Word |
| `exports/Finance-BRD-Cheat-Sheet.docx` | Printable cheat sheet |
| `exports/Finance-BRD-Training-Slides.pptx` | Core training slide deck (19 slides) |
| `exports/Finance-Business-User-BRD-Guide-Slides.pptx` | **Business user guide** — how to write a BRD (29 slides) |
| `exports/Finance-IT-Delivery-Framework-Slides.pptx` | IT delivery framework — pipeline, **swimlane, dual-track, scrum, org chart** (32 slides) |
| `exports/Finance-IT-Operations-Guide-Slides.pptx` | **IT Ops guide** — roster, shifts, catalog SR, **triage flowchart, org chart** (34 slides) |

## How to use

1. Import templates into Confluence ([structure guide](docs/08-confluence-structure.md)) or distribute Word export.
2. Configure ServiceNow/Jira using [field mapping](docs/07-servicenow-jira-intake-mapping.md).
3. Run training per [8-week rollout](docs/09-rollout-plan-8-weeks.md) with slides + [speaker notes](training/04-trainer-speaker-notes.md).
4. Share sample BRDs as gold-standard references during workshops.
5. Enforce quality gate: BRD score ≥ 80% per [checklist](docs/05-brd-quality-checklist.md) and [governance](docs/10-governance-raci.md).
6. Operations Managers: use [intake & deployment checklist](docs/11-operations-manager-checklist.md) and [stakeholder framework](docs/12-it-operations-stakeholder-framework.md).
7. Service Owners / Managers: use [delivery control & resourcing guide](docs/13-service-owner-delivery-control-guide.md) for pipeline KPIs and team sizing.
8. IT Operations / Service Desk: use [operations runbook](docs/14-it-operations-runbook.md) for SR bucket allocation, BOD/EOD/EOM/BOM, and incidents.
9. Train Ops / Service Desk with [IT Operations slides](exports/Finance-IT-Operations-Guide-Slides.pptx) (~90 min).

## Suggested rollout

See full plan: [docs/09-rollout-plan-8-weeks.md](docs/09-rollout-plan-8-weeks.md)

- Week 1–2: Publish templates; train BAs; configure ITSM form
- Week 3–6: Training Sessions 1–4 by business unit
- Week 7: Soft gate (form required)
- Week 8: Hard gate (no FRD without accepted BRD)
