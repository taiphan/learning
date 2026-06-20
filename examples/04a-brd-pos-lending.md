# SAMPLE BRD — POS Motorbike / Installment Lending (Same-Day Approval Visibility)

**Document ID:** BRD-2026-0042 (Sample — Training Only)  
**Version:** 1.0  
**Status:** Approved (Example)  
**Classification:** Internal

---

## A. REQUEST INFORMATION

| Field | Value |
|-------|-------|
| **BRD Title** | Enable real-time loan approval status for POS motorbike installment sales |
| **Business Unit** | Sales / POS |
| **Requester Name** | Nguyen Van A — Regional Sales Operations |
| **Business Sponsor** | Director, Partner Sales |
| **Date Submitted** | 2026-03-01 |
| **Target Go-Live Date** | 2026-07-01 |
| **Priority Category** | Revenue / Growth + Customer Experience |

---

## B. EXECUTIVE SUMMARY

**Business problem:**  
POS sales staff at partner motorbike dealerships cannot confirm whether a customer's installment loan is **finally approved** during the customer visit. Approval status is only visible in the back-office system the next business day. Customers leave without signing contract; ~18% of approved-in-principle cases do not convert to disbursed loans.

**Who is impacted:**  
- ~2,400 POS sales users nationwide  
- Partner dealership staff (view-only status)  
- Customers applying for two-wheeler installment loans  

**Business impact if not addressed:**  
- Estimated VND 45B annual disbursement leakage (2025 baseline)  
- Partner NPS decline; duplicate store visits  
- Competitor win during cooling-off period  

**Proposed business outcome:**  
Enable authorized POS users to see final approval status and approved installment plan **during the customer visit**, supporting same-day contract signing where policy allows.

---

## C. BUSINESS OBJECTIVES & SUCCESS METRICS

| # | Objective | Baseline | Target | Measurement | Owner | Frequency |
|---|-----------|----------|--------|-------------|-------|-----------|
| 1 | Increase approved-to-disbursed conversion at motorbike POS | 72% | 80% | LOS conversion report by product | Sales Analytics | Weekly |
| 2 | Reduce customer repeat visits for same application | 1.4 visits avg | 1.1 visits avg | POS visit log / partner survey | Regional Sales | Monthly |
| 3 | Reduce approval status inquiry calls to support | 320/day | 200/day | Call center ticket category | CX Ops | Weekly |

---

## D. BACKGROUND & CURRENT STATE

### D.1 Current process

| Step | Actor | Activity | System | Pain point |
|------|-------|----------|--------|------------|
| 1 | POS sales | Capture customer application | Partner POS / LOS tablet | — |
| 2 | Credit ops | Approve / reject / request docs | Finacle LMS / credit workflow | Customer waits or leaves |
| 3 | POS sales | Call hotline or wait for email | Manual | No real-time visibility |
| 4 | Customer | Returns next day to sign | — | Drop-off risk |
| 5 | POS sales | Disbursement trigger | LOS + core | Delayed TAT |

### D.2 Volume

| Metric | Value |
|--------|-------|
| POS users affected | ~2,400 |
| Motorbike installment applications/month | ~28,000 |
| Peak periods | Month-end, holiday campaigns |
| Geographic scope | National (phased rollout) |

---

## E. PROPOSED TO-BE STATE

Authorized POS users see a clear status on the **Partner POS / LOS tablet**: **Submitted / In Review / Approved / Rejected / Pending Documents**, including approved amount, tenor, and monthly installment (if approved). When status = Approved, POS can proceed to contract signing workflow per existing policy. Customer receives SMS when status changes to Approved or Rejected.

**Customer experience change:** Fewer return visits; immediate next-step clarity at dealership.

---

## F. SCOPE

### In scope
- Real-time status display on Partner POS / LOS tablet for motorbike installment product
- SMS notification to customer on final decision
- Audit log of who viewed approval details at POS
- Pilot: 3 regions (South, Central, North) — 120 POS points

### Out of scope
- Changes to credit scoring model or approval policy thresholds
- New partner onboarding workflow
- Personal cash loan products (separate BRD)
- Contract e-sign vendor change

### Assumptions
- POS tablets remain bank-managed devices on corporate network
- Existing LOS product configuration for motorbike loans unchanged

### Dependencies
| Dependency | Owner | Status |
|------------|-------|--------|
| Legal confirmation of SMS wording | Legal | In progress |
| Partner training materials | Sales Training | Not started |

---

## G. STAKEHOLDERS & USERS

| Role | Department | # users | Location | Access |
|------|------------|---------|----------|--------|
| POS sales agent | Partner Sales | 2,400 | POS | View status; proceed if approved |
| Regional supervisor | Sales | 85 | Field | View + exception escalate |
| Credit approver | Credit | 40 | HQ/Regional | Unchanged — back-office |
| Customer | — | — | POS | Receives SMS only |

**Customer impact:** Yes  
**Partner impact:** Yes — dealership staff may view status screen alongside FE Credit agent

---

## H. BUSINESS RULES

| Rule ID | Business rule | Source |
|---------|---------------|--------|
| BR-01 | Only users with active POS agent ID can view application status | Sales policy POS-2024-11 |
| BR-02 | Approved amount, tenor, installment visible only when status = Approved | Product standard |
| BR-03 | Customer CCCD full number masked on POS screen (show last 4 digits only) | Data policy |
| BR-04 | Rejection reason shown as standard code only; no internal score details | Risk policy |
| BR-05 | Same-day contract signing allowed only before 17:00 local time | Ops cut-off |
| BR-06 | If status = Pending Documents, POS sees document checklist only | Credit ops SOP |

**Approval authority:** Unchanged from current motorbike installment policy.  
**Exception handling:** If status service unavailable > 15 minutes, POS follows manual hotline escalation (existing SOP).

---

## I. DATA & SECURITY REQUIREMENTS

**Data types:** Customer PII, loan application data, decision outcome  
**Classification:** Confidential  
**Sharing:** Internal + authorized POS users only; no export to personal devices  
**Audit:** Log user ID, POS ID, application ID, timestamp for each status view  
**Customer consent:** Existing loan application consent covers SMS decision notification  
**Remote access:** N/A — POS on-site only; managed tablet

---

## J. REPORTING & CONTROLS

| Report | Audience | Frequency |
|--------|----------|-----------|
| POS conversion by status visibility | Sales leadership | Weekly |
| Status view audit trail | Internal audit | On demand |
| SMS delivery success rate | CX Ops | Daily |

**Controls:** Status changes only by credit system; POS read-only. Maker-checker on approval unchanged.

---

## K. IMPLEMENTATION & ROLLOUT

**Approach:** Pilot 6 weeks → phased national rollout 8 weeks  
**Training:** 2-hour POS webinar + quick reference card (Vietnamese)  
**Language:** Vietnamese UI; SMS Vietnamese  
**Fallback:** Revert to hotline/email process per current SOP

---

## L. RISKS

| Risk | Description | L | I | Mitigation |
|------|-------------|---|---|------------|
| Operational | POS misreads "in principle" vs "final" approval | M | H | Clear status labels; training |
| Customer | SMS sent before customer informed in person | L | M | SMS after status = final only |
| Compliance | Unauthorized viewing of customer data at partner site | M | H | Masking, audit, device compliance |
| Financial | Premature contract signing | L | H | Enforce BR-05 cut-off and final status flag |

---

## M. ACCEPTANCE CRITERIA

| AC ID | Criterion |
|-------|-----------|
| AC-01 | **Given** application is finally approved, **when** POS agent refreshes status on tablet, **then** status shows "Approved" with amount, tenor, and installment within 60 seconds. |
| AC-02 | **Given** application is rejected, **when** POS views status, **then** only standard rejection code is shown and no credit score is displayed. |
| AC-03 | **Given** status changes to Approved, **when** system processes event, **then** customer receives SMS within 5 minutes. |
| AC-04 | **Given** unauthorized user (no POS agent ID), **when** they attempt to view status, **then** access is denied. |
| AC-05 | **Given** full CCCD on record, **when** displayed on POS, **then** only last 4 digits are visible. |
| AC-06 | **Given** system unavailable, **when** outage exceeds 15 minutes, **then** POS sees maintenance message and hotline number. |

---

## N. COMPLIANCE SCREENING

| Question | Yes | No |
|----------|-----|-----|
| Changes origination/approval/disbursement? | ☐ | ☑ (display only; no policy change) |
| Changes interest/fees/contract? | ☐ | ☑ |
| Sends customer notifications? | ☑ | ☐ |
| Third-party data exchange? | ☐ | ☑ |
| Affects collections/legal? | ☐ | ☑ |
| Audit trail required? | ☑ | ☐ |
| Exposes data on POS devices? | ☑ | ☐ |

**Risk/Compliance review:** Required (customer notification + POS data display)

---

## O. APPROVALS

| Role | Name | Date |
|------|------|------|
| Requester | Nguyen Van A | 2026-03-01 |
| Sponsor | Director, Partner Sales | 2026-03-05 |
| Risk/Compliance | (Review complete) | 2026-03-12 |

---

*Sample BRD for training — not an official FE Credit project document.*
