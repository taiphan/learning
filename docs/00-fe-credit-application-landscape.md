# FE Credit — Application & System Landscape

Reference for business users writing BRDs. Use **application names** and **business capabilities** in your BRD — not internal technical components (Kafka, Redis, etc.) unless requesting integration with an approved partner.

> **Note:** Names reflect publicly documented systems. Internal teams should align with your CMDB / application catalog.

---

## 1. Customer-facing applications

| Application | Primary users | Business purpose | Typical BRD topics |
|-------------|---------------|------------------|-------------------|
| **FE ONLINE 2.0** | Customers | Multifunction mobile app: cash loans, cards, loan management, digital banking features | eKYC, upload docs, UX, notifications, loan tracking |
| **$NAP** | Customers | End-to-end digital lending: apply, near-instant approval, credit management | Onboarding, OCR, scoring UX, disbursement journey |
| **SHIELD** | Customers | Consumer loan, credit card, insurance products (mobile) | Product features, cross-sell, self-service |
| **Partner POS / LOS tablet** | POS sales agents, partner staff | In-store origination for motorbike, phone, durable goods | Approval visibility, contract signing, partner workflow |
| **Website / landing** | Prospects | Campaigns, product info, lead capture | Forms, tracking, consent |

---

## 2. Core banking & operations systems

| System | Business purpose | Data sensitivity |
|--------|------------------|------------------|
| **Finacle LMS** (Loan Management) | Loan accounts, disbursement, repayment schedules | Restricted |
| **Finacle CIF** | Customer master, KYC profile | Confidential / Restricted |
| **Finacle Assure** | Assurance / related Finacle modules per product setup | Restricted |
| **Card platform (FirstVision)** | Credit card issuance, loan-on-card, card servicing | Restricted |
| **Collections platform** | DPD management, reminders, recovery workflows | Confidential |
| **eSign** | Electronic contract signing | Confidential |
| **Workflow engine (e.g. Flowable)** | Approval chains, business process automation | Internal |

**Hosting:** Core Finacle suite and mission-critical apps run on **AWS** (SaaS/cloud model). Customer PII residency rules apply per FE Credit policy and SBV requirements.

---

## 3. Supporting platforms

| Platform | Purpose |
|----------|---------|
| **Keycloak / IAM** | Identity and access for staff and apps |
| **Call center / CRM** | Inbound/outbound customer contact, tickets |
| **AI chatbot** | 24/7 customer support (~130k users/month publicly cited) |
| **SMS / Email gateway** | Customer notifications, OTP, collections |
| **CIC / Credit bureau** | External credit checks |
| **BI / Reporting** | Management reports, dashboards |
| **HR / Internal systems** | Staff — not for customer data BRDs unless HR project |

---

## 4. Product lines → systems map

| Product | Origination channel | Core servicing | Collections |
|---------|--------------------|----------------|-------------|
| Personal cash loan | FE ONLINE, $NAP, branches | Finacle LMS | Collections platform |
| Two-wheeler installment | Partner POS / LOS | Finacle LMS | Collections platform |
| Consumer durable (phone, electronics) | Partner POS | Finacle LMS | Collections platform |
| Credit card | FE ONLINE, $NAP, SHIELD | FirstVision + Finacle | Collections platform |

---

## 5. Business units (BRD routing)

| Business unit | Typical requesters | Common systems touched |
|---------------|-------------------|------------------------|
| **Digital & CX** | Product owners, app owners | FE ONLINE, $NAP, SHIELD, chatbot |
| **Sales / Partner (POS)** | Regional sales, partner ops | POS LOS, Finacle LMS |
| **Credit & Risk** | Policy, underwriting | Finacle LMS, CIF, bureau |
| **Collections & Recovery** | Collections strategy, ops | Collections, SMS, Finacle LMS |
| **Cards** | Card product team | FirstVision, SHIELD, FE ONLINE |
| **Customer Service** | Call center, CX ops | CRM, chatbot, FE ONLINE |
| **Operations** | Back-office, disbursement | Finacle LMS, workflow |
| **Finance** | Accounting, reconciliation | Finacle, BI |
| **Legal & Compliance** | Policy, regulatory | All — advisory on BRDs |
| **IT** | Internal enablement | Infrastructure — use IT change process if no business change |

---

## 6. Data classification guide (BRD Section I)

| Class | Examples at FE Credit | Default handling |
|-------|----------------------|------------------|
| **Public** | Marketing, published rates | Standard |
| **Internal** | Procedures, org charts | Staff access only |
| **Confidential** | Loan applications, CIC results, income docs | Managed device, DLP, audit |
| **Restricted** | Core admin, payment keys, bulk customer export | VDI, PAM, no home download |

---

## 7. Compliance triggers (Vietnam consumer finance)

| Trigger | Route to |
|---------|----------|
| Change to lending decision / disbursement | Credit Policy + Risk |
| Interest rate, fee, contract template | Legal + Finance |
| Customer SMS / email / push | Legal (template approval) |
| CIC / third-party data sharing | Compliance + Vendor Risk |
| Collections contact rules | Collections Compliance |
| Cross-border or offshore processing | Legal + Security + SBV policy |
| POS / field device showing customer data | Security + Data owner |

---

## 8. BRD writing rules per application

### FE ONLINE 2.0 / $NAP / SHIELD
- State **customer journey step** (e.g., "after eKYC", "at disbursement")
- Specify **consent** and **notification** needs
- Do not specify React, AWS, OCR engine — say "automated document capture"

### Partner POS / LOS
- Name **partner type** (motorbike dealer, electronics chain)
- Address **on-site data display** (masking rules)
- Include **training** for POS agents

### Finacle LMS / CIF
- Use **business terms**: disbursement, repayment schedule, account status
- Flag if **financial posting** or **accounting** impact
- Expect **Risk + IT Architecture** review

### Collections
- Document **contact frequency**, **opt-out**, **legal hold** exclusions
- SMS templates require **Legal template ID**

---

## 9. What NOT to put in a business BRD

| Avoid | Write instead |
|-------|----------------|
| "Use RabbitMQ" | "Near real-time status update at POS" |
| "Deploy on AWS Lambda" | "Scalable peak campaign volume" |
| "Integrate Keycloak" | "Staff login with existing bank credentials" |
| "OCR with Python" | "Auto-read ID document from photo" |

---

## 10. Integration partners (reference only)

Documented ecosystem includes Infosys Finacle, ITC ($NAP/OCR), Fiserv (cards), AWS. New vendors require **Vendor Risk Assessment** — note in BRD Section N Q4.

---

*Landscape v1.0 — align with internal CMDB. Last updated for BRD training package.*
