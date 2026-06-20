# Confluence Space Structure — FE Credit BRD Program

Recommended Confluence space layout for templates, training, and living BRD repository.

---

## Space name

**FE Credit — Business Requirements (BRD)**

| Setting | Value |
|---------|-------|
| Space key | `FECBRD` (adjust to your naming standard) |
| Visibility | Internal — all employees read; BA/editors write |
| Template space | Clone structure below |

---

## Page tree

```text
FECBRD (Home)
├── 📋 Start Here
│   ├── What is a BRD?
│   ├── When do I need a BRD?
│   ├── BRD vs FRD vs CR
│   └── How to submit (ServiceNow/Jira link)
│
├── 📝 Templates
│   ├── BRD Template (English) ← copy from 01-brd-template-en.md
│   ├── BRD Template (Bilingual VI-EN) ← copy from 02-brd-template-bilingual-vi-en.md
│   ├── Quality Checklist ← 05-brd-quality-checklist.md
│   └── Cheat Sheet (printable) ← 06-brd-cheat-sheet.md
│
├── 📚 Training
│   ├── Training Program Overview (8-week rollout)
│   ├── Session 1–4 Materials
│   ├── Slide Deck (link to exports/FE-Credit-BRD-Training-Slides.pptx)
│   └── Certification — BRD Ready
│
├── ⭐ Gold Standard Examples
│   ├── Sample — POS Lending
│   ├── Sample — FE ONLINE eKYC
│   └── Sample — Collections Automation
│
├── 🔄 Process & Governance
│   ├── BRD Workflow (diagram)
│   ├── RACI — Who approves what
│   ├── IT Ops Manager — Stakeholder framework ← 12-it-operations-stakeholder-framework.md
│   ├── Service Owner — Delivery control & resourcing ← 13-service-owner-delivery-control-guide.md
│   ├── IT Ops Manager — Intake & deployment checklist ← 11-operations-manager-checklist.md
│   ├── SLA and escalation
│   ├── ServiceNow/Jira field mapping
│   └── BA Review feedback guide
│
├── 🏛️ Compliance & Security
│   ├── Data classification guide
│   ├── Compliance screening (Section N) explained
│   ├── When to involve Legal / Risk / Security
│   └── Remote access & data handling policy links
│
└── 📁 BRD Repository (by year)
    ├── 2026
    │   ├── BRD-2026-0001 [Title]
    │   └── ...
    └── Archive
```

---

## Confluence page templates

### Template 1: New BRD page
- Use **BRD Template (English)** as Confluence blueprint
- Add labels: `brd`, `{business-unit}`, `{year}`, `{status}`
- Status values: `draft`, `under-review`, `accepted`, `deferred`, `rejected`

### Template 2: BA Review page (child of BRD)
```text
BRD Review — [BRD-ID]
Reviewer:
Date:
Score: __%
Decision: Accept / Return / Reject
Gaps:
Risk routing:
Next action:
```

---

## Macros and labels

| Label | Use |
|-------|-----|
| `brd` | All BRD pages |
| `brd-draft` | Not yet submitted |
| `brd-accepted` | Passed quality gate |
| `needs-compliance` | Risk review required |
| `needs-security` | Security review required |
| `gold-standard` | Training examples only |

**Recommended macros:**
- `{info}` on Start Here — link to ServiceNow form
- `{warning}` on Compliance page — no BYOD for customer data
- `{expand}` for long business rules tables
- Page Properties Report for BRD dashboard by status and unit

---

## BRD dashboard (Page Properties)

Configure page properties on each BRD:

| Property | Type |
|----------|------|
| BRD ID | Text |
| Business Unit | Select |
| Sponsor | User |
| Status | Select |
| Score % | Number |
| Target Go-Live | Date |
| Compliance Required | Checkbox |

Create **Page Properties Report** on Home for PMO/BA visibility.

---

## Import steps

1. Create space `FECBRD`
2. Create page tree per structure above
3. Copy markdown content from `docs/` and `examples/` into pages
4. Set **BRD Template (English)** as blueprint template
5. Link ServiceNow catalog item on Start Here page
6. Restrict **BRD Repository** edit to BA + requester + sponsor
7. Announce space in training Session 1

---

## Permissions

| Group | Start Here / Templates | Repository |
|-------|---------------------|------------|
| All staff | Read | Read own BU (optional) |
| Business users | Read | Create draft in own BU folder |
| BA team | Edit all | Edit all |
| Risk / Legal | Read | Comment on flagged BRDs |
| Leadership | Read | Read dashboards |

---

*Confluence structure v1.0 | FE Credit BRD Training Package*
