# FE CREDIT — BUSINESS REQUIREMENTS DOCUMENT (BRD)

**Document ID:** BRD-YYYY-NNNN  
**Version:** 1.0  
**Status:** Draft / Under Review / Approved  
**Classification:** Internal

---

## Instructions for business users

- Complete all **mandatory** sections before submission.
- Write **what** the business needs and **why** — not how IT should build it.
- Use clear, testable language. Avoid technical solution details (API, database, vendor product names unless requesting a specific approved partner).
- Attach process diagrams, sample reports, or policy documents if available.
- Obtain **Business Sponsor** sign-off before submitting to IT/BA intake.

**Submit to:** [ServiceNow / Jira BRD queue — update internally]  
**Questions:** [BA team contact — update internally]

---

## A. REQUEST INFORMATION *(Mandatory)*

| Field | Value |
|-------|-------|
| **BRD Title** | |
| **Business Unit** | ☐ Sales / POS ☐ Digital ☐ Collections ☐ Risk ☐ Cards ☐ Operations ☐ Finance ☐ HR ☐ Other: ___ |
| **Requester Name** | |
| **Requester Email** | |
| **Business Sponsor** (Director or above) | |
| **Date Submitted** | |
| **Target Go-Live Date** | |
| **Priority Category** | ☐ Regulatory / Audit ☐ Revenue / Growth ☐ Customer Experience ☐ Operational Efficiency ☐ Risk Reduction ☐ Other |
| **Regulatory Deadline** (if applicable) | |
| **Related BRD / Project IDs** | |

---

## B. EXECUTIVE SUMMARY *(Mandatory — max 15 lines)*

**Business problem:**

> _Describe the pain in plain language. Example: "POS sales staff cannot confirm final approved installment plan during the customer visit because approval status is only available the next business day."_

**Who is impacted:**

> _Roles, customers, partners, regions._

**Business impact if not addressed:**

> _Quantify where possible: % drop-off, hours wasted, compliance exposure, customer complaints/month._

**Proposed business outcome (one sentence):**

> _Example: "Enable same-day contract signing at partner POS for approved motorbike installment loans."_

---

## C. BUSINESS OBJECTIVES & SUCCESS METRICS *(Mandatory)*

List 1–3 objectives. Each must have a **baseline**, **target**, and **how measured**.

| # | Objective | Baseline (current) | Target | Measurement method | Measurement owner | Review frequency |
|---|-----------|-------------------|--------|------------------|-------------------|------------------|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |

**Objective examples (Finance):**
- Reduce digital loan application completion rate drop-off from 42% to 30%
- Reduce POS same-day disbursement TAT from 24 hours to 4 hours
- Reduce manual collections list preparation from 2 hours/day to 15 minutes/day

---

## D. BACKGROUND & CURRENT STATE *(Mandatory)*

### D.1 Current process (step-by-step)

| Step | Actor | Activity | System/tool used | Pain point |
|------|-------|----------|------------------|------------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

### D.2 Current systems involved

Select from [Finance Application Landscape](00-finance-application-landscape.md). Common systems:

| System | Purpose in current process |
|--------|--------------------------|
| FE ONLINE 2.0 | Customer mobile app — loans, cards, loan management |
| Partner POS / LOS tablet | In-store origination at partner points |
| Finacle LMS | Loan accounts, disbursement, repayment |
| Finacle CIF | Customer master / KYC |
| Finacle Assure | Finacle assurance module |
| Card platform (FirstVision) | Credit card issuance and servicing |
| Collections platform | DPD, reminders, recovery |
| Call center / CRM | Customer contact, tickets |
| AI Chatbot | Digital customer support |
| eSign | Electronic contract signing |
| Workflow / BPM | Approval chains |
| BI / Reporting | Dashboards and reports |
| SMS / Email gateway | Customer notifications |

### D.3 Volume and frequency

| Metric | Value |
|--------|-------|
| Number of users affected | |
| Transactions / cases per day | |
| Customers impacted per month | |
| Peak periods (e.g., month-end, campaign) | |
| Geographic scope (national / regions / pilot) | |

---

## E. PROPOSED TO-BE STATE *(Mandatory — business view only)*

### E.1 Desired future process (high level)

> _Describe the future process from a business/user perspective. Do not specify technical architecture._

### E.2 Expected changes

| Dimension | Current | To-be |
|-----------|---------|-------|
| User experience | | |
| Processing time | | |
| Manual steps | | |
| Customer communication | | |
| Control / audit | | |

### E.3 Process flow diagram

> _Attach swimlane or flowchart (Visio, draw.io, photo of whiteboard). Optional but recommended._

---

## F. SCOPE *(Mandatory)*

### F.1 In scope

- 
- 
- 

### F.2 Out of scope

- 
- 
- 

### F.3 Assumptions

- 
- 

### F.4 Dependencies

| Dependency | Owner | Status | Impact if delayed |
|------------|-------|--------|-------------------|
| | | | |

---

## G. STAKEHOLDERS & USERS *(Mandatory)*

| Role | Department | Est. # users | Location | Access needed (view / create / approve) |
|------|------------|--------------|----------|----------------------------------------|
| | | | HQ / Branch / POS / Remote | |
| | | | | |

**Customer impact:** ☐ Yes ☐ No — describe: ___

**Partner / vendor impact:** ☐ Yes ☐ No — describe: ___

---

## H. BUSINESS RULES *(Mandatory for lending, collections, cards)*

> _IT and Risk must not guess these rules. Document explicitly or attach approved policy._

### H.1 Eligibility and product rules

| Rule ID | Business rule | Source (policy / regulation) |
|---------|---------------|------------------------------|
| BR-01 | | |
| BR-02 | | |

### H.2 Approval authority

| Condition | Approver role | Escalation |
|-----------|---------------|------------|
| | | |

### H.3 Pricing / fees / interest (business level)

> _Describe business logic. Do not write code or formulas unless already approved by Finance/Product._

### H.4 Exception handling

> _What happens when data is missing, bureau unavailable, system down, after cut-off time?_

### H.5 Cut-off times and calendars

| Event | Cut-off | Non-working day behavior |
|-------|---------|--------------------------|
| | | |

### H.6 Customer communication rules

| Trigger | Channel | Content owner (Legal/Marketing) | Opt-out required? |
|---------|---------|--------------------------------|-------------------|
| | SMS / Email / App push | | ☐ Yes ☐ No |

---

## I. DATA & SECURITY REQUIREMENTS *(Mandatory)*

### I.1 Data types involved

☐ Customer PII (name, CCCD, phone, address)  
☐ Financial data (income, loan balance, DPD)  
☐ Credit bureau / CIC data  
☐ Payment / card data  
☐ Employee data  
☐ Other: ___

### I.2 Data classification

☐ Public ☐ Internal ☐ Confidential ☐ Restricted

### I.3 Data sharing

| Data | Shared with | Purpose | Cross-border? |
|------|-------------|---------|---------------|
| | Internal only / Partner / Vendor | | ☐ Yes ☐ No |

### I.4 Retention and deletion

> _How long must data be kept? When must it be deleted?_

### I.5 Audit requirements

> _Who did what, when? Logs required for regulator/internal audit?_

### I.6 Customer consent and notification

☐ Consent required before launch  
☐ Privacy notice update required  
☐ Customer notification (SMS/email) required  
☐ Legal review required

**Description:**

### I.7 Remote / home access implications

☐ No remote access  
☐ Managed device only  
☐ VDI required for restricted data  
☐ File download to local device — **requires Security exception if Confidential/Restricted**

---

## J. REPORTING & CONTROLS *(Mandatory)*

### J.1 Reports required

| Report name | Audience | Frequency | Key fields |
|-------------|----------|-----------|------------|
| | | Daily / Weekly / Monthly | |

### J.2 Control points

| Control | Maker | Checker | Evidence |
|---------|-------|---------|----------|
| | | | |

### J.3 Reconciliation

> _What must be reconciled (e.g., disbursement vs core ledger)?_

### J.4 Fraud and risk controls

> _Expected business controls: velocity checks, blacklist, duplicate detection, etc._

---

## K. IMPLEMENTATION & ROLLOUT *(Mandatory)*

### K.1 Rollout approach

☐ Pilot (specify region/partner: ___)  
☐ Phased nationwide  
☐ Big bang

### K.2 Training needs

| Audience | Training type | Owner |
|----------|---------------|-------|
| POS staff | | |
| Call center | | |
| Back office | | |

### K.3 Language

☐ Vietnamese only ☐ English only ☐ Bilingual (VN + EN)

### K.4 Business continuity

> _What is the fallback if the new process/system is unavailable?_

---

## L. RISKS & IMPACT IF IMPLEMENTED INCORRECTLY *(Mandatory)*

| Risk type | Description | Likelihood (L/M/H) | Impact (L/M/H) | Mitigation (business) |
|-----------|-------------|-------------------|----------------|----------------------|
| Operational | | | | |
| Customer | | | | |
| Financial | | | | |
| Compliance / Regulatory | | | | |
| Reputational | | | | |

---

## M. ACCEPTANCE CRITERIA *(Mandatory — minimum 5 testable statements)*

Use **Given / When / Then** format. These become UAT test cases.

| AC ID | Acceptance criterion |
|-------|---------------------|
| AC-01 | **Given** [context], **when** [action], **then** [expected result]. |
| AC-02 | |
| AC-03 | |
| AC-04 | |
| AC-05 | |

---

## N. FE CREDIT COMPLIANCE SCREENING *(Mandatory)*

| # | Question | Yes | No | N/A |
|---|----------|-----|-----|-----|
| 1 | Does this change loan origination, approval, or disbursement? | ☐ | ☐ | ☐ |
| 2 | Does this change interest, fees, or contract terms? | ☐ | ☐ | ☐ |
| 3 | Does this send customer notifications? | ☐ | ☐ | ☐ |
| 4 | Does this involve third-party data exchange? | ☐ | ☐ | ☐ |
| 5 | Does this affect collections or legal recovery? | ☐ | ☐ | ☐ |
| 6 | Does this require audit trail for SBV / internal audit? | ☐ | ☐ | ☐ |
| 7 | Does this expose customer data on POS/field devices? | ☐ | ☐ | ☐ |

**If any "Yes" above:** Route to Risk / Compliance review before build.

---

## O. APPROVALS *(Mandatory before IT intake)*

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Business Requester | | | |
| Business Sponsor (Director+) | | | |
| Business Unit Head | | | |
| Risk / Compliance (if required) | | | |
| Data Owner (if required) | | | |

---

## P. REVISION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | | | Initial submission |

---

## APPENDIX (optional)

- A1. Process diagrams  
- A2. Sample reports / screen mockups (business wireframes only)  
- A3. Reference policies  
- A4. Glossary  

---

*Template version: 1.0 | Finance BRD Training Package*
