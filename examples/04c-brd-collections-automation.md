# SAMPLE BRD — Collections Automation (DPD1–DPD7 SMS Reminder)

**Document ID:** BRD-2026-0071 (Sample — Training Only)  
**Version:** 1.0  
**Status:** Approved (Example)  
**Classification:** Internal

---

## A. REQUEST INFORMATION

| Field | Value |
|-------|-------|
| **BRD Title** | Automated SMS payment reminder for early delinquency (DPD1–DPD7) |
| **Business Unit** | Collections |
| **Requester Name** | Le Van C — Collections Strategy |
| **Business Sponsor** | Director, Collections |
| **Date Submitted** | 2026-01-20 |
| **Target Go-Live Date** | 2026-04-01 |
| **Priority Category** | Risk Reduction + Operational Efficiency |

---

## B. EXECUTIVE SUMMARY

**Business problem:**  
Collections officers manually export overdue accounts daily and send reminders via disparate channels. For DPD1–DPD7 personal loans, manual list preparation takes ~2 hours per team lead each morning. Many customers who would pay after a single reminder roll to DPD30+ because contact is delayed or inconsistent.

**Who is impacted:**  
- 35 collections team leads and 180 collectors  
- Personal loan customers in early delinquency (~22,000 accounts/month in DPD1–DPD7)

**Business impact if not addressed:**  
- DPD30 roll-forward rate: 38% (target 34%)  
- Collector capacity spent on low-complexity reminders instead of DPD30+ negotiation  
- Inconsistent customer experience; compliance risk from ad-hoc messaging

**Proposed business outcome:**  
Automatically send Legal-approved SMS reminders to eligible personal loan customers on DPD1, DPD3, and DPD7, excluding restricted accounts, with full audit trail and opt-out respect.

---

## C. BUSINESS OBJECTIVES & SUCCESS METRICS

| # | Objective | Baseline | Target | Measurement | Owner |
|---|-----------|----------|--------|-------------|-------|
| 1 | Reduce DPD30 roll-forward from DPD1–DPD7 cohort | 38% | 34% | Collections vintage report | Risk |
| 2 | Reduce manual list prep time per team lead | 2 hr/day | 15 min/day | Ops time study | Collections Ops |
| 3 | Increase cure rate within 7 days of first DPD | 52% | 58% | DPD cure dashboard | Collections |

---

## D. BACKGROUND & CURRENT STATE

### D.1 Current process

| Step | Actor | Activity | Pain point |
|------|-------|----------|------------|
| 1 | Team lead | Export DPD report from core | Manual, 1–2 hours |
| 2 | Team lead | Filter accounts, assign collectors | Inconsistent rules |
| 3 | Collector | Call or SMS customer | Delayed until afternoon |
| 4 | Collector | Log outcome in collections system | Incomplete logs |

### D.2 Volume
| Metric | Value |
|--------|-------|
| Personal loan accounts in DPD1–DPD7 | ~22,000/month |
| SMS capacity via existing gateway | 500,000/day (sufficient) |
| Scope | Personal cash loans only; national |

---

## E. PROPOSED TO-BE STATE

Each eligible morning, system identifies accounts hitting DPD1, DPD3, or DPD7 and sends templated SMS with payment amount, due date, and payment channels. Collectors see reminder status on account timeline. Team leads receive exception report only (failed SMS, opt-out, legal hold).

---

## F. SCOPE

### In scope
- Automated SMS for personal loan DPD1, DPD3, DPD7
- Eligibility rules and exclusion list per Section H
- Audit log and daily operations report
- Integration with existing collections worklist (visibility only)

### Out of scope
- Voice bot / IVR campaigns
- DPD30+ restructuring workflows
- Credit card collections (separate BRD)
- Email reminders
- Legal escalation letters

### Assumptions
- SMS gateway and sender ID already approved
- Payment channel URLs in SMS are existing approved links

---

## G. STAKEHOLDERS & USERS

| Role | # | Access |
|------|---|--------|
| Collections team lead | 35 | View reports, exceptions |
| Collector | 180 | View reminder history on account |
| Customer | ~22,000/mo | Receives SMS |
| Legal / Compliance | 3 | Approve templates |

---

## H. BUSINESS RULES

| Rule ID | Rule |
|---------|------|
| BR-01 | Product: personal cash loans only |
| BR-02 | Send on DPD1, DPD3, DPD7 at 09:00 customer local time batch |
| BR-03 | Max 1 SMS per account per day |
| BR-04 | Exclude: legal hold, deceased flag, fraud investigation, restructuring in progress |
| BR-05 | Exclude: customers with marketing/collections opt-out flag |
| BR-06 | Exclude: accounts with payment received but not yet posted (grace 24h) |
| BR-07 | SMS content must use Legal template COL-SMS-2025-03 only |
| BR-08 | Include outstanding amount and Finance payment channels only |
| BR-09 | Do not include full account number; mask loan ID (last 4 digits) |
| BR-10 | If mobile number invalid, route to collector manual queue |

**Exception handling:** Team lead can suppress next SMS for account with documented customer dispute (maker-checker).

---

## I. DATA & SECURITY REQUIREMENTS

**Data types:** Customer PII (phone), loan balance (Confidential)  
**Sharing:** SMS via approved telecom gateway only  
**Audit:** Log account ID, DPD day, template version, send time, delivery status  
**Consent:** Collections contact permitted under loan agreement; opt-out honored per policy  
**Retention:** SMS logs 7 years per collections compliance standard

---

## J. REPORTING & CONTROLS

| Report | Audience | Frequency |
|--------|----------|-----------|
| Daily SMS sent / delivered / failed | Collections Ops | Daily |
| Exclusion summary by reason | Team leads | Daily |
| Cure rate by reminder day | Risk | Weekly |

**Controls:** Template changes require Legal approval. Maker-checker for manual suppression > 48 hours.

---

## K. IMPLEMENTATION & ROLLOUT

**Approach:** Pilot 2 regions (4 weeks) → national  
**Training:** 1-hour briefing for team leads; collector FAQ  
**Language:** Vietnamese SMS  
**Fallback:** Disable automation flag; revert to manual export process

---

## L. RISKS

| Risk | L | I | Mitigation |
|------|---|---|------------|
| Customer complaint — harassment | M | M | BR-03 frequency cap; opt-out |
| Wrong amount in SMS | L | H | Amount from core EOD balance; reconciliation |
| SMS to wrong number | L | H | Phone validation; audit |
| Regulatory — non-approved wording | L | H | Legal template lock |

---

## M. ACCEPTANCE CRITERIA

| AC ID | Criterion |
|-------|-----------|
| AC-01 | **Given** account reaches DPD1 and is eligible, **when** batch runs at 09:00, **then** customer receives COL-SMS-2025-03 template SMS. |
| AC-02 | **Given** account has opt-out flag, **when** batch runs, **then** no SMS is sent and account appears on exclusion report. |
| AC-03 | **Given** account on legal hold, **when** batch runs, **then** no SMS is sent. |
| AC-04 | **Given** payment posted within grace window, **when** batch runs, **then** account is excluded. |
| AC-05 | **Given** SMS sent, **when** collector opens account, **then** reminder event visible on timeline within 15 minutes. |
| AC-06 | **Given** team lead documents dispute with approval, **when** next batch runs, **then** SMS suppressed for that account. |

---

## N. COMPLIANCE SCREENING

| Question | Yes | No |
|----------|-----|-----|
| Changes origination/disbursement? | ☐ | ☑ |
| Changes interest/fees/contract? | ☐ | ☑ |
| Sends customer notifications? | ☑ | ☐ |
| Third-party data exchange? | ☑ (SMS gateway) | ☐ |
| Affects collections/legal? | ☑ | ☐ |
| Audit trail required? | ☑ | ☐ |

**Risk/Compliance review:** Required (collections + customer communication + vendor gateway)

---

## O. APPROVALS

| Role | Date |
|------|------|
| Sponsor — Director, Collections | 2026-01-25 |
| Legal (template) | 2026-02-01 |
| Risk/Compliance | 2026-02-10 |

---

*Sample BRD for training — not an official Finance project document.*
