# VPBank — Head of AI Factory · Steering One-Pager (Track B · H4 variant)

**Use when:** Week 52 Leadership tab · internal steering · leadership second-round prep  
**JD source:** [VPBank Head of AI Factory — LinkedIn](https://vn.linkedin.com/jobs/view/head-of-ai-factory-at-vpbank-4424356100)  
**Time:** ~2h to adapt + rehearse · Export as 5 slides or 1-page PDF

> **Note:** This is a **scenario draft** for learning — not an application to the live posting. Replace metrics with real pilot data before any exec audience.

---

## Slide 1 — Title & hook

| Field | Content |
|-------|---------|
| **Title** | VPBank AI Factory — Year 1 Portfolio & Scale Plan |
| **Presenter** | [Your name] · [Date] |
| **Hook** | *Value-led predictive + generative AI at production scale — governance-assured, subsidiary-ready.* |

**30-second opener:** VPBank’s AI Factory must move from scattered PoCs to **measured production**: PD/risk models that protect asset quality, GenAI copilots that cut approval TAT without compliance drift, and reusable platform assets that subsidiaries can adopt — all under SBV-aligned governance.

---

## Slide 2 — Strategy (maps to JD §1 Strategic Leadership)

Five pillars aligned to the VPBank HoAI posting:

| Pillar | Objective (Year 1) | Measurable outcome |
|--------|-------------------|-------------------|
| **Business value** | Prioritize 3–5 use cases with ROI models before build | ≥2 pilots with signed business sponsor + baseline KPI |
| **Predictive AI** | PD, early-warning, anomaly detection in production path | 1 model in prod with AUC + champion/challenger + NPL link |
| **Generative AI** | Policy/credit copilot with RAG + guardrails (G1→G2) | Grounded answer rate ≥90% on golden set; human-in-loop for G3 |
| **Platform & reuse** | Feature store, vector DB, model registry, inference APIs | 1 shared platform sprint; 2+ teams reuse same RAG stack |
| **Governance** | Ethical AI, privacy, audit trail, model risk tiering | 100% use cases pass intake gate; zero PII in prompts/logs |

**Strategic principle:** *Value-led, platform-powered, governance-assured — expand to subsidiaries only after platform + governance pass.*

**Operating model (5 steps):**

1. **Intake** — BRD + problem statement + ROI hypothesis (apps/brd gate ≥80%)
2. **Prioritize** — Value × feasibility × risk tier (G1/G2/G3)
3. **Build** — Predictive (MLflow) or GenAI (RAG/agents); build vs buy decision logged
4. **Governance gate** — Model risk, privacy, SBV controls, eval harness
5. **Operate** — Monitor drift, retrain cadence, post-deployment ROI review

---

## Slide 3 — Portfolio wins (maps to JD §2 Model Development + §5 Business Partnership)

| Project | Business metric | Tech stack | VPBank relevance |
|---------|-----------------|------------|------------------|
| **Credit PD model** | AUC ≥0.75; link to NPL migration | Python · sklearn · SHAP · MLflow | Predictive AI — risk & asset quality |
| **Policy RAG copilot** | Grounded % ≥90%; citation on every answer | RAG · vector DB · eval golden set | GenAI — credit ops / RM productivity |
| **Policy agent (G2)** | Tool-call success; escalation to human | LangGraph · guardrails · audit log | Agents with safety guardrails |
| **BRD intake gate** | Quality score ≥80% before dev | Static app · checklist mirror | Factory intake — reduces rework |

**Build vs buy (one line each):**

| Use case | Decision | Rationale |
|----------|----------|-----------|
| PD scoring | **Build** | Proprietary features + model risk ownership |
| General LLM | **Buy** (API) + RAG | Speed; fine-tune only if ROI > cost of vendor + risk |
| Doc OCR | **Buy** + integrate | Mature vendors; focus on workflow + governance |

GitHub / demo links: `[your portfolio URLs]`

---

## Slide 4 — KPIs, platform & governance (maps to JD §3 Architecture + §4 Governance)

### KPI dashboard (steering committee view)

| KPI | Target Y1 | Owner |
|-----|-----------|-------|
| Time-to-value (idea → prod) | ≤90 days for G1 pilots | AI Factory PM |
| Post-deploy ROI measured | 100% of prod use cases | Business sponsor |
| Model governance pass rate | 100% at gate | Model risk / compliance liaison |
| Platform reuse | ≥2 squads on shared RAG/inference | Platform lead |
| Subsidiary readiness | 1 playbook exported | HoAI + IT |

### Risk tiers (from Week 28 governance)

| Tier | Examples | Controls |
|------|----------|----------|
| **G1** | Internal search, draft summaries | RAG + eval; no customer PII |
| **G2** | RM copilot with tool calls | Human review on actions; full audit |
| **G3** | Automated credit decisions | Model validation + SBV alignment + override |

### 90-day timeline (from Week 40 plan)

| Phase | Weeks | Deliverables |
|-------|-------|--------------|
| **Q1 — Foundation** | 1–12 | Intake process live; PD pilot baseline; platform MVP |
| **Q2 — Pilot** | 13–24 | Policy copilot G1→G2; first prod predictive model |
| **Q3 — Scale** | 25–36 | MLOps/LLMOps CI/CD; subsidiary playbook draft |
| **Q4 — Steer** | 37–52 | ROI review; headcount plan; Year 2 roadmap |

---

## Slide 5 — Ask (maps to JD §6 People + §1 Subsidiary expansion)

| Ask | Detail | Decision needed |
|-----|--------|-----------------|
| **Pilot sponsor** | Retail/corporate credit BU for policy copilot G1 | Name exec sponsor by [date] |
| **Headcount (Y1)** | +2 FTE: 1 ML engineer, 1 LLMOps/platform | Approve Q2 hiring |
| **Platform budget** | Vector DB + inference + eval tooling (cloud) | CapEx/Opex line item |
| **Subsidiary path** | Defer until 1 prod use case + governance pack proven | Agree gate criteria |

**Closing line:** *Approve G1 copilot pilot + Q2 platform hire — measurable ROI in 90 days, subsidiary rollout in Year 2.*

---

## 5-minute script (VPBank-tailored)

1. **Problem (30s):** PoCs don’t scale; risk of compliance drift with GenAI; subsidiaries need a **repeatable factory**, not one-off projects.
2. **Strategy (60s):** Five pillars — value, predictive, generative, platform, governance — one operating model from intake to monitor.
3. **Proof (90s):** PD model + policy copilot + BRD gate — evidence you can **ship and measure**, not slide-only.
4. **Plan (90s):** 90-day phases; G1→G2 copilot; MLOps gate; subsidiary playbook deferred until prod proof.
5. **Ask (30s):** Exec sponsor + 2 hires + platform budget; decision this quarter.

---

## Interview STAR seeds (if leadership loop)

| JD theme | Story angle |
|----------|-------------|
| C-level advisor | How you framed AI ROI in **bps / NPL / TAT** language, not model accuracy alone |
| Build vs buy | One decision matrix you used (cost, risk, latency, data sensitivity) |
| MLOps/LLMOps | CI/CD + versioning + monitoring for **both** PD model and RAG |
| People | How you’d structure squads: platform · use-case · governance (even as hypothetical) |
| Subsidiaries | “Platform + governance pack first, then white-label playbook” |

---

## Done when

- [ ] Exported PDF or 5-slide deck (copy sections above)
- [ ] Metrics replaced with **your** lab/portfolio numbers where available
- [ ] 5-min script rehearsed or recorded (Loom)
- [ ] Linked from `lab/projects/PORTFOLIO.md`
- [ ] Cross-read: [job-skills-adaptation.md §F.4](../../job-skills-adaptation.md#f4-vpbank--head-of-ai-factory-stretch--track-b)
