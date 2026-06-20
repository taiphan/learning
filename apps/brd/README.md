# Learning BRD Intake App

Interactive web form for **business users** to draft BRDs aligned with the learning lab governance model and the IT delivery pipeline.

## Features

- 8-step BRD wizard aligned with the official template (sections A–O)
- **Weighted quality score** (matches BA rubric in `docs/05-brd-quality-checklist.md`, gate ≥ 80%)
- **Auto risk level** (Low / Medium / High / Critical)
- **8-step self-check** sidebar (live ✓ as you complete the form)
- **Request type classifier** — redirects access/incident to Service Desk
- **Delivery pipeline** — BRD → FSD → Scrum → UAT → CAB
- **Stakeholder routing** — IT-Governance, IT-Security, GRC/Legal
- **Export warning** if score &lt; 80% or wrong request bucket
- VI / EN toggle · auto-save · Markdown export

## Run locally

```bash
cd apps/brd
python3 -m http.server 8080
# Open http://localhost:8080
```

## Configuration

Edit `config/learning.js`:

- Business units, applications, compliance questions
- Request types, delivery phases, score weights
- Risk level rules, self-check items

## Related docs

- [Business user BRD slides](../../exports/FE-Credit-Business-User-BRD-Guide-Slides.pptx)
- [BRD quality checklist](../../docs/05-brd-quality-checklist.md)
- [IT Ops framework](../../docs/12-it-operations-stakeholder-framework.md)
- [ServiceNow/Jira mapping](../../docs/07-servicenow-jira-intake-mapping.md)
