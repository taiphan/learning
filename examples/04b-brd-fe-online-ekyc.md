# SAMPLE BRD — FE ONLINE 2.0 eKYC Document Upload Improvement

**Document ID:** BRD-2026-0058 (Sample — Training Only)  
**Version:** 1.0  
**Status:** Approved (Example)  
**Classification:** Internal

---

## A. REQUEST INFORMATION

| Field | Value |
|-------|-------|
| **BRD Title** | Improve income document upload in FE ONLINE 2.0 digital loan journey |
| **Business Unit** | Digital |
| **Requester Name** | Tran Thi B — Digital Product |
| **Business Sponsor** | Head of Digital Lending |
| **Date Submitted** | 2026-02-15 |
| **Target Go-Live Date** | 2026-05-15 |
| **Priority Category** | Customer Experience + Revenue / Growth |

---

## B. EXECUTIVE SUMMARY

**Business problem:**  
Customers applying for personal cash loans via FE ONLINE 2.0 frequently fail at the income document upload step. Current 5MB file size limit and accepted formats (PDF only) cause 34% of users to abandon the journey after ID verification. Support tickets cite blurry photos and "file too large" errors.

**Who is impacted:**  
- Digital loan applicants (~45,000/month)  
- Digital operations support team  
- Credit underwriting (incomplete applications)

**Business impact if not addressed:**  
- Application completion rate stuck at 58% (vs 70% target)  
- ~VND 12B/month potential disbursement not reached (forecast model)  
- Increased call center load: ~1,200 tickets/month on upload issues

**Proposed business outcome:**  
Allow customers to upload income proof via photo (JPG/PNG) and PDF up to 10MB with guided capture, reducing upload-step drop-off and re-submission rates.

---

## C. BUSINESS OBJECTIVES & SUCCESS METRICS

| # | Objective | Baseline | Target | Measurement | Owner |
|---|-----------|----------|--------|-------------|-------|
| 1 | Increase end-to-end application completion rate | 58% | 68% | Digital funnel dashboard | Digital Analytics |
| 2 | Reduce drop-off at document upload step | 34% | 18% | Funnel step 4 analytics | Digital Product |
| 3 | Reduce upload-related support tickets | 1,200/mo | 600/mo | CRM ticket tag | CX |

---

## D. BACKGROUND & CURRENT STATE

### D.1 Current process

| Step | Actor | Activity | Pain point |
|------|-------|----------|------------|
| 1 | Customer | Complete ID + selfie eKYC | — |
| 2 | Customer | Upload income PDF ≤ 5MB | Photos rejected; size errors |
| 3 | Customer | Retake photo, convert to PDF externally | Friction, abandonment |
| 4 | Credit | Manual review of unclear docs | Rework, delays |

### D.2 Systems
- FE ONLINE 2.0 mobile app (Android/iOS) — primary channel
- Digital origination services behind app
- Document storage per FE Credit data policy

### D.3 Volume
| Metric | Value |
|--------|-------|
| Digital personal loan applications/month | ~45,000 |
| Upload step drop-off | 34% |
| Scope | National, all digital personal loan applicants |

---

## E. PROPOSED TO-BE STATE

After eKYC, customer is guided to capture or upload income documents with:
- Accepted formats: PDF, JPG, PNG
- Max size: 10MB per file; max 3 files per application
- On-screen tips (lighting, full page, no glare)
- Immediate validation feedback before submit

Customer sees clear error messages in Vietnamese. Successful upload triggers confirmation screen; credit team receives documents in existing review queue.

---

## F. SCOPE

### In scope
- Upload UX improvement for income documents on FE ONLINE 2.0
- Format and size rule changes per business rules below
- Customer-facing error messages and capture guidance
- Metrics events for funnel analytics

### Out of scope
- OCR / auto-income verification (future BRD)
- Changes to credit approval policy
- Credit card or motorbike POS journeys
- Redesign of entire loan application UI

### Assumptions
- Existing eKYC (ID + liveness) unchanged
- Legal-approved list of acceptable income document types unchanged

---

## G. STAKEHOLDERS & USERS

| Role | Users | Access |
|------|-------|--------|
| Digital loan applicant | ~45,000/month | Upload documents |
| Credit analyst | 25 | Review in back-office (unchanged) |
| CX agent | 60 | Handle escalations |

**Customer impact:** Yes  
**Partner impact:** No

---

## H. BUSINESS RULES

| Rule ID | Rule |
|---------|------|
| BR-01 | Accepted types: salary slip, bank statement, tax confirmation per existing product policy |
| BR-02 | Max 10MB per file; max 3 files per application |
| BR-03 | Formats: PDF, JPG, PNG only |
| BR-04 | Documents must be uploaded within 72 hours of eKYC completion or application expires |
| BR-05 | Customer must confirm data processing notice before upload (existing consent flow) |
| BR-06 | Rejected file shows specific reason: format / size / unreadable |

**Cut-off:** Application expiry rules unchanged.  
**Customer communication:** In-app messages only; no marketing SMS.

---

## I. DATA & SECURITY REQUIREMENTS

**Data types:** Customer PII, income documents (Confidential)  
**Retention:** Per existing digital loan retention policy (minimum 5 years post loan closure)  
**Audit:** Log upload timestamp, device type, file hash; not full file in audit log  
**Consent:** Existing FE ONLINE privacy notice + loan application consent  
**Deletion:** Auto-delete orphaned uploads for expired applications after 90 days  
**Remote access:** Customer home mobile device — documents go to bank-controlled storage only; no local bank copy on server at customer device beyond app cache (cleared on logout)

---

## J. REPORTING & CONTROLS

| Report | Frequency |
|--------|-----------|
| Funnel step 4 conversion | Daily |
| Upload failure reason breakdown | Weekly |
| Document resubmission rate | Weekly |

**Fraud controls:** Duplicate file hash check across active applications; virus/malware scan on upload.

---

## K. IMPLEMENTATION & ROLLOUT

**Approach:** A/B test 10% traffic for 2 weeks → full rollout  
**Training:** CX FAQ update; credit team memo on new formats  
**Language:** Vietnamese in-app; error messages Vietnamese  
**Fallback:** Revert to PDF-only 5MB via feature flag

---

## L. RISKS

| Risk | L | I | Mitigation |
|------|---|---|------------|
| Fraudulent edited images | M | H | Existing manual review + hash check |
| Larger files increase storage cost | L | L | 10MB cap; lifecycle deletion |
| Privacy incident if misconfigured | L | H | Security review before go-live |

---

## M. ACCEPTANCE CRITERIA

| AC ID | Criterion |
|-------|-----------|
| AC-01 | **Given** customer selects JPG income photo ≤ 10MB, **when** they upload, **then** upload succeeds and confirmation is shown. |
| AC-02 | **Given** file is 12MB, **when** customer uploads, **then** clear Vietnamese error explains size limit. |
| AC-03 | **Given** customer uploads .HEIC file, **when** they submit, **then** upload is rejected with format guidance. |
| AC-04 | **Given** application expired (>72h post eKYC), **when** customer attempts upload, **then** upload is blocked and customer directed to restart. |
| AC-05 | **Given** successful upload, **when** credit analyst opens case, **then** document appears in existing review queue within 2 minutes. |
| AC-06 | **Given** malware detected in file, **when** scan completes, **then** upload rejected and event logged to security monitoring. |

---

## N. COMPLIANCE SCREENING

| Question | Yes | No |
|----------|-----|-----|
| Changes origination/approval/disbursement? | ☑ (journey step only) | ☐ |
| Changes interest/fees/contract? | ☐ | ☑ |
| Sends customer notifications? | ☐ | ☑ (in-app only) |
| Third-party data exchange? | ☐ | ☑ |
| Audit trail required? | ☑ | ☐ |

**Risk/Compliance review:** Required (customer PII documents on digital channel)

---

## O. APPROVALS

| Role | Date |
|------|------|
| Sponsor — Head of Digital Lending | 2026-02-20 |
| Risk/Compliance | 2026-02-28 |

---

*Sample BRD for training — not an official FE Credit project document.*
