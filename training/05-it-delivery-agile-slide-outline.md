# IT Delivery Framework & Agile/Scrum — Slide Outline

**Program:** IT Operations & Delivery Framework  
**Audience:** IT Ops, Dev leads, BA, IT Product, IT-Governance, IT-Security  
**Duration:** ~90 minutes  
**Companion deck:** `exports/FE-Credit-IT-Delivery-Framework-Slides.pptx`

---

## Slide 1 — Title
- **FE Credit IT Delivery Framework**
- Subtitle: Requirement → BRD → FSD → Test → UAT → Ship → Operations Support
- Agile/Scrum internal process + stakeholder governance

## Slide 2 — Learning objectives
- Understand end-to-end delivery pipeline and gates
- Map Agile/Scrum ceremonies to FE Credit governance
- Know stakeholder roles: Business, Dev, IT-Gov, IT-Security, GRC, Audit
- Apply "no BRD → no code" and evidence chain for release

## Slide 3 — Big picture (one diagram)
End-to-end swimlane: Business | BA | IT Product | Scrum Team | QA | Ops | Assurance

## Slide 4 — Document chain
| Stage | Document | Owner |
| BRD | Business need | Business |
| FSD/FRD | Functional spec | BA + IT |
| Stories/AC | Backlog | BA + Dev |
| Test cases | SIT + UAT | QA + Business |
| CR | Change record | Ops + IT-Gov |

## Slide 5 — Three lanes
Demand (Business+BA) | Delivery (Product+Dev+Ops) | Assurance (IT-Gov+IT-Sec+GRC+Audit)

## Slide 6 — Stakeholder map
Business, IT Delivery, IT-Governance, IT-Security, GRC/Legal, Audit, BOD

## Slide 7 — IT-Gov vs IT-Sec vs GRC
Routing rule slide

## Slide 8 — Phase 1: Receive requirement
ITSM catalog → classify bucket → BRD or standard ticket

## Slide 9 — Phase 2: BRD & quality gate
Business writes → Sponsor signs → BA scores ≥80% → compliance flags

## Slide 10 — Phase 3: IT triage & backlog
IT Product prioritizes → approved for FSD → enters product backlog

## Slide 11 — Phase 4: FSD / FRD
BA creates functional spec from BRD → linked in Jira → sprint-ready stories

## Slide 12 — Agile/Scrum overlay
Where Scrum fits inside governed delivery (diagram)

## Slide 13 — Scrum roles at FE Credit
PO (IT Product) | SM (Dev lead) | Dev Team | BA (requirements) | Ops (release)

## Slide 14 — Product backlog → Sprint backlog
Epic (BRD) → Feature (FSD) → User stories → Tasks

## Slide 15 — Sprint ceremonies calendar
Planning | Daily | Review | Retro — mapped to delivery phase

## Slide 16 — Sprint planning gate
Checklist: accepted BRD? FSD linked? security flags clear? capacity?

## Slide 17 — Definition of Done (Dev)
Code + review + unit tests + SIT pass + traceability to AC + release notes

## Slide 18 — Phase 5: Test (SIT / QA)
Dev unit → QA SIT → regression → defect loop → exit criteria

## Slide 19 — Phase 6: UAT
Business executes AC from BRD → Sponsor sign-off → no IT proxy acceptance

## Slide 20 — Phase 7: Ship (release)
CAB → IT-Gov approval → deploy → post-deploy verify → CMDB update

## Slide 21 — Phase 8: Operations support
Hypercare T+1–14 → handover to BAU → incident/RCA → audit evidence

## Slide 22 — Release readiness checklist
BRD + FSD + SIT + UAT + CAB + Security (if flagged)

## Slide 23 — Dual-track diagram
Governance track (parallel) vs Delivery track (Scrum)

## Slide 24 — Hard gates (non-negotiable)
No FSD without BRD | No prod without UAT | No deploy without CAB

## Slide 25 — Evidence pack for audit
13 artifacts list

## Slide 26 — Escalation & conflict
Common conflicts and resolution paths

## Slide 27 — Metrics dashboard
First-pass BRD, triage days, deploys without BRD, UAT before prod

## Slide 28 — Summary & next steps
Framework docs on Confluence; Ops checklist; weekly CAB

---

*Slide outline v1.0 | 28 slides*
