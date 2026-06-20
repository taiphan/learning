# FE Credit BRD Intake App

Interactive web form adapted to **FE Credit's application landscape** and **IT delivery governance framework** (BRD → FSD → Scrum → UAT → CAB ship).

## Features

- 8-step BRD wizard aligned with the official template
- **Request type classifier** — redirects access/incident to Service Desk; flags data import bucket
- **Delivery pipeline** sidebar — shows where BRD fits in the full IT path
- **Stakeholder routing** — IT-Governance, IT-Security, GRC/Legal (grouped)
- **Hard gates** reminder — no FSD without BRD; no ship without UAT + CAB
- **VI / EN** language toggle for field teams
- FE Credit **system picker** grouped by channel / core / ops
- **Compliance screening** with auto-routing preview
- **Quality score** preview (target ≥ 80%)
- **Technical keyword coach** — flags API/Kafka-style text in to-be section
- **New integration** flag → routes to IT-Governance (ARB)
- **Export** to Markdown with delivery path and stakeholder routing
- **Auto-save** draft in browser localStorage

## Run locally

ES modules require a local server:

```bash
cd app
python3 -m http.server 8080
```

Open http://localhost:8080

## Configuration

Edit `config/fe-credit.js` to match your internal CMDB:

- Business units
- Application catalog
- Request types and buckets
- Delivery phases (Agile/Scrum pipeline)
- Compliance questions and routing
- IT-Governance / IT-Security route categories

## Related docs

- [IT Operations Stakeholder Framework](../docs/12-it-operations-stakeholder-framework.md)
- [Operations Manager Checklist](../docs/11-operations-manager-checklist.md)
- [Application landscape](../docs/00-fe-credit-application-landscape.md)
- [BRD template (EN)](../docs/01-brd-template-en.md)
- [ServiceNow/Jira field mapping](../docs/07-servicenow-jira-intake-mapping.md)
