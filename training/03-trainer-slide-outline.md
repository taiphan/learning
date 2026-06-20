# FE Credit BRD Training — Slide Outline (28 slides)

**Program:** Business User BRD Writing Training  
**Audience:** Sales/POS, Digital, Collections, Operations, Product, Risk liaisons  
**Total duration:** ~10 hours across 4 sessions  
**Format:** Instructor-led + exercises + real BRD peer review

---

## Session 1 — Why BRD Matters at FE Credit (2 hours)

### Slide 1 — Title
- **FE Credit Business Requirements Document (BRD) Training**
- Subtitle: Write requirements IT can deliver — without rework
- Trainer, date, version

### Slide 2 — Learning objectives
By end of program, participants will:
- Write a complete BRD using FE Credit template
- Separate business need from technical solution
- Define testable acceptance criteria
- Pass BRD quality gate (≥ 80%)

### Slide 3 — Why we are here
- High volume of IT requests from business
- Rework cost: delay, UAT defects, compliance risk
- Goal: faster triage, predictable delivery

### Slide 4 — What is a BRD?
- Definition: document describing **business problem, outcomes, rules, scope**
- What it is **not**: technical design, vendor selection, project plan

### Slide 5 — BRD vs other documents
| BRD | FRD | Technical Design | UAT |
|-----|-----|------------------|-----|
| Business | BA + IT | IT | Business + QA |

### Slide 6 — FE Credit context
- Consumer finance: personal loans, POS installment, cards, digital app (FE ONLINE 2.0)
- Nationwide POS network, call center, collections
- High regulatory and audit expectations

### Slide 7 — Request journey (end-to-end)
Business BRD → BA quality review → IT triage → Risk (if needed) → FRD → Build → UAT → Go-live

### Slide 8 — Good vs bad request (live examples)
**Bad:** "Build Kafka API to Finacle"  
**Good:** "POS needs same-day approval visibility during customer visit"

### Slide 9 — The BRD golden rule
> Write the **problem and rules**, not the **system design**.

### Slide 10 — Activity 1 (20 min)
Rewrite 3 vague requests into clear business outcomes  
- Debrief in plenary

### Slide 11 — Session 1 recap + homework
- Read BRD template Section A–C
- Bring 1 real work pain point to Session 2

---

## Session 2 — How to Write Each BRD Section (3 hours)

### Slide 12 — Template walkthrough overview
Sections A–P map; mandatory vs optional

### Slide 13 — Section A: Request information
- Sponsor requirement (Director+)
- Priority categories: regulatory vs convenience
- **Common mistake:** no sponsor, "ASAP" only

### Slide 14 — Section B: Executive summary
Formula: **[Role] cannot [task] because [constraint], causing [impact]**
- FE Credit example: POS motorbike loan drop-off

### Slide 15 — Section C: Objectives & KPIs
- Baseline → target → measurement method
- Weak vs strong KPI table

### Slide 16 — Section D: Current state
- Step-by-step process table
- Systems: FE ONLINE, LOS, Finacle, CRM
- Volume/frequency data sources

### Slide 17 — Section E: To-be state
- Business process only
- **Stop list:** API names, cloud vendor, middleware

### Slide 18 — Section F: Scope
- In scope / out of scope / assumptions
- Why out-of-scope prevents project failure

### Slide 19 — Section G & H: Users and business rules
- Role, location, user count
- Rules IT must not guess: eligibility, approval, cut-off, exceptions

### Slide 20 — Section I & J: Data, security, controls
- Data classification at FE Credit
- When remote/home access triggers Security review
- Maker-checker, reconciliation, fraud controls

### Slide 21 — Section M: Acceptance criteria
**Given / When / Then** format  
- Live example: disbursement before 17:00

### Slide 22 — Activity 2 (40 min)
Draft Sections B, C, F, M for a sample POS lending scenario  
- Pair review with checklist

### Slide 23 — Session 2 recap + homework
- Complete draft BRD Sections A–M for own use case

---

## Session 3 — Data, Risk & Compliance at FE Credit (2 hours)

### Slide 24 — Why compliance section is not optional
- SBV / internal audit / privacy expectations
- Consequences of unclear data handling

### Slide 25 — FE Credit compliance screening (Section N)
7 yes/no questions and auto-escalation to Risk

### Slide 26 — Data classification quick guide
| Public | Internal | Confidential | Restricted |
| Customer marketing | Internal policy | Loan file, CIC | Payment admin, core access |

### Slide 27 — Remote work and data leakage (link to security architecture)
- Managed device, CASB, VDI, no personal cloud
- How BRD statements trigger security evaluation

### Slide 28 — Third-party and partner data
- Vendor assessment trigger
- Cross-border data flag

### Slide 29 — Customer communication rules
- SMS/email/app: Legal-approved content
- Opt-out and contact frequency (collections)

### Slide 30 — Activity 3 (30 min)
Compliance screening on 3 sample BRDs — decide: standard path vs Risk review

### Slide 31 — Session 3 recap + homework
- Finalize compliance sections I, J, N, L

---

## Session 4 — BRD Review Workshop & Certification (3 hours)

### Slide 32 — BRD quality rubric
- 0 / 1 / 2 scoring per section
- Gate: ≥ 80% + sponsor sign-off

### Slide 33 — Top 10 BRD mistakes at FE Credit
1. Solution not need  
2. No KPI baseline  
3. Missing business rules  
4. No out-of-scope  
5. Multiple projects in one BRD  
6. No acceptance criteria  
7. No sponsor  
8. Ignoring POS/training impact  
9. No data classification  
10. Copy-paste vendor brochure text

### Slide 34 — How BA will feedback your BRD
- Returned with gap list (specific sections)
- SLA: quality review in 2 business days

### Slide 35 — Activity 4 (90 min) — Peer review
- Each team presents 10-min BRD summary
- Peer scoring with rubric
- BA coach gives top 3 improvements

### Slide 36 — Approval workflow & tooling
- ServiceNow/Jira BRD form mandatory fields
- Attachments: process diagram, policy refs

### Slide 37 — Certification criteria
- Attendance all 4 sessions
- Submit 1 BRD scoring ≥ 80%
- Sponsor sign-off on submitted BRD
- Badge: "BRD Ready — FE Credit"

### Slide 38 — Q&A and next steps
- Office hours schedule (weekly)
- Template location on Confluence
- Program KPIs: first-pass acceptance rate, rework cycles

---

## Trainer notes

### Materials needed
- Printed cheat sheet (VI + EN for POS teams)
- Quality checklist handout
- 3 sample BRDs (POS, eKYC, Collections)
- Projector + whiteboard

### Facilitator roles
| Role | Responsibility |
|------|----------------|
| Lead trainer (BA) | Template, exercises, scoring |
| IT representative | Intake process, what happens after BRD |
| Risk/Compliance | Section N, data classification |
| Digital/Sales guest | 15-min "good BRD" story |

### Timing buffer
- Add 15 min per session for Q&A
- Session 4 may need 3.5h if > 8 teams present

---

*Slide outline v1.0 | 38 slides (includes title/recap slides; core content ~28)*
