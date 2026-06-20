# CV & Cover Letter — AI Engineer (Banking → Applied AI)

For **your** job search (OCB, NAB, VPBank, Anthropic stretch). Tailor placeholders `[...]` with real metrics from portfolio.

**Companion:** [job-skills-adaptation.md](job-skills-adaptation.md) · [anthropic-career-adaptation.md](anthropic-career-adaptation.md)

---

## 1. Applied AI Architect (Anthropic) — CV outline

Tailor for [Applied AI Architect, Commercial](https://job-boards.greenhouse.io/anthropic/jobs/5192805008). Full week map: [anthropic-career-adaptation.md](anthropic-career-adaptation.md).

### Header
`[Name]` · `[City, Country]` · `[Email]` · `[LinkedIn]` · `[GitHub — banking-ai-portfolio]` · **Open to relocation: San Francisco / New York**

### Professional summary (4–5 lines)
> Applied AI engineer and banking domain specialist with `[X]` years in `[credit/lending/BRD/regulated financial services]` and `[Y]` years building **production-shaped LLM systems** (RAG, **LangGraph** agents, **eval harnesses**, FastAPI/Docker). Shipped `[flagship: e.g. credit policy copilot with ≥90% grounded-response rate on golden set]` and documented **responsible-AI governance** (risk tiers, guardrails, audit trail). Combines **hands-on Python** with **customer discovery** — workshops, requirements translation, and measurable adoption metrics. Seeking to help enterprises deploy **Claude** safely in regulated industries.

### Core competencies (mirror JD)
- **Claude / LLM:** Claude API · tool use · RAG · agents · eval design · grounded-response metrics
- **Build:** Python · FastAPI · Docker · CI eval gates · reusable blueprints
- **Advisory:** Technical discovery · architecture workshops · executive + engineering audiences
- **Domain:** Banking credit/lending · compliance mindset · BRD-quality acceptance criteria
- **Safety:** Guardrails · PII handling · human escalation · governance gates ([governance-mlops.md](governance-mlops.md) patterns)

### Technical projects (lead with these — not buried)

**Credit Policy Copilot (Claude API + LangGraph)** · `[GitHub URL]` · `[Year]`
- Built RAG + **LangGraph** agent over synthetic credit policy corpus; **FastAPI** + **Docker** deploy.
- Designed **eval framework** (30–50 golden Q&A); achieved **`[%]` grounded-response rate**; CI runs eval on push.
- Implemented guardrails: PII redaction, low-confidence escalation, source citation for audit.
- **Blueprint:** architecture diagram + README for reuse across financial-services use cases.

**Credit PD Model (scikit-learn + SHAP)** · `[GitHub URL]`
- Trained classifier on public credit data; **AUC `[X]`**; SHAP narratives for decline explanations.
- Documented business metric linkage (false decline vs approval rate trade-off).

**BRD & AI Governance Toolkit** · `[This repo URL]`
- Authored BRD templates, quality gates, MLOps governance docs — proof of **safe deployment by design**.

### Professional experience

**`[Title]` — `[Bank / Company]` · `[Dates]`** *(target: OCB AI Engineer or NAB AIOps after month 12)*
- Embedded with `[credit ops / risk / lending]` to map workflow; shipped `[agent/copilot/pilot]` reducing `[TAT / handle time]` by **`[%]`**.
- Partnered with business + IT on requirements, UAT, and acceptance criteria (BRD Sections C, M).
- `[If applicable]` Deployed containerized API; established eval baseline before go-live.

**`[Prior BA / banking role]` — `[Company]` · `[Dates]`**
- Led BRD authoring / process analysis for `[lending/BPM/digital]`; `[N]` stakeholders across LOS/Core/CRM.
- Drove UAT E2E scenarios; improved `[delivery speed / defect rate / pass rate on quality gate]`.

### Education & certifications
- `[Degree]` — `[University]`
- `[Optional: AWS Cloud Practitioner / Azure AI fundamentals]`

### Links (required for Anthropic)
- GitHub (2+ repos above)
- **Demo video** (5–10 min, English): architecture + live policy Q&A
- Optional: blog post on eval harness or responsible AI in banking

---

## 2. Applied AI Architect — cover letter template

> Dear Anthropic Applied AI Team,
>
> I am applying for **Applied AI Architect, Commercial**. I combine **regulated-industry domain depth** (credit, lending, BRD, compliance) with **hands-on LLM engineering** — not slides-only architecture.
>
> In `[year/project]`, I built a **credit policy copilot** using **Claude API**, **LangGraph**, and a **golden-set eval harness** that achieved **`[%]` grounded responses**, served via **FastAPI/Docker**, with guardrails aligned to banking audit expectations. I documented the full path from business problem → eval criteria → deployment in a **reusable financial-services blueprint** — the same pattern I would use with your commercial customers.
>
> Before engineering, I spent `[X]` years as a banking `[BA/analyst]` translating operator workflows into testable requirements — the same discovery muscle your role needs from discovery through deployment. I am drawn to Anthropic because you treat **safety and capability as one problem**, which matches how I approach AI in regulated environments: **measure behavior, gate releases, escalate when uncertain**.
>
> I am **open to relocating** to San Francisco or New York and would welcome discussing how my banking + applied-AI background can help customers adopt Claude responsibly.
>
> Sincerely,  
> `[Name]`

### “Why Anthropic?” (application form — 200–400 words)

Structure:
1. **Hook:** One sentence — banking + building measurable Claude/LLM systems.
2. **Mission fit:** Responsible deployment is not optional in finance; Anthropic’s safety-first approach matches your governance work.
3. **Evidence:** One project metric (grounded rate, eval CI, escalation design).
4. **Contribution:** Help FS customers adopt Claude with eval discipline you already practice.
5. **Close:** Relocation readiness + excitement for pre-sales **building** (not only advising).

---

## 3. VN bank AI Engineer — CV bullets (OCB / NAB / VPBank)

Use [job-skills-adaptation.md](job-skills-adaptation.md) for JD-specific clusters. Lead every bullet with **business metric**, then tech.

| Theme | Example bullet |
|-------|----------------|
| RAG / agent | Shipped LangGraph policy copilot; **92% grounded** on 40-question golden set; escalates when confidence &lt; threshold |
| ML | Credit PD model **AUC 0.78**; SHAP explains top 3 decline drivers for branch staff |
| Domain | Translated POS lending BRD rules into executable Python policy engine (DTI 40%, tenure 12 mo) |
| Production | FastAPI + Docker; colleague ran `/ask` on laptop without setup doc |

---

## 4. Requirements → evidence map (Applied AI Architect)

| Anthropic requirement | Your evidence (after syllabus) |
|---|---|
| 3+ yrs SWE or SA with hands-on build | Portfolio repos + VN AI role |
| Python prototypes + eval frameworks | `policy-copilot-api` + golden set |
| Claude API / Claude Code | Week 31+ Claude migration; `claude-code-banking-lab` |
| Customer-facing advisory | BA workshops; mock enterprise workshop recording |
| Scalable cloud architecture | Docker + `[AWS module]` post-month 12 |
| LLM frameworks / ML background | LangGraph + `credit-pd-model` |
| Safety & beneficial use | `governance-mlops.md` + guardrails in API |
| Reusable blueprints | FS README template in flagship repo |
