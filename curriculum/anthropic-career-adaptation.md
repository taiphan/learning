# Anthropic Career Adaptation — 3 Roles × 12-Month Syllabus

**Profile:** Banking domain (BRD, credit, compliance) · Zero Python today · Vietnam-based  
**North star:** Work on **Claude** at Anthropic (Applied AI / Claude Code / eval harness)  
**Strategy:** Use **12-month syllabus** + **VN bank job** (OCB/NAB) as stepping stones — same portfolio serves both.

**Official apply:** [anthropic.com/careers/jobs](https://www.anthropic.com/careers/jobs) · verify `@anthropic.com` only

**Companion docs:** [zero-to-ai-expert-syllabus.md](zero-to-ai-expert-syllabus.md) · [job-skills-adaptation.md](job-skills-adaptation.md) · [reading-path.md](reading-path.md) · [cv-templates.md](cv-templates.md#1-applied-ai-architect-anthropic--cv-outline)

---

## Three target roles (tiered)

| Tier | Role | Location | Experience bar | Realistic horizon | Greenhouse |
|---|---|---|---|---|---|
| **1 — Primary** | **Applied AI Architect, Commercial** | SF / NYC (hybrid) | 3+ yrs SWE + customer-facing | **18–24 mo** (after VN AI role + portfolio) | [5192805008](https://job-boards.greenhouse.io/anthropic/jobs/5192805008) |
| **2 — Bridge** | **Technical Specialist, Claude Code** | SF / NYC (hybrid) | 3–7 yrs customer-facing technical | **12–18 mo** (strong demo + enablement story) | [5197597008](https://job-boards.greenhouse.io/anthropic/jobs/5197597008) |
| **3 — Stretch (harness/loop)** | **Staff SWE, Dev Productivity (CI/CD) — Claude Code** | SF / NYC | 7+ yrs dev-infra / CI/CD at scale | **3–5 yrs** | [5271428008](https://job-boards.greenhouse.io/anthropic/jobs/5271428008) |

**APAC alternative (later):** [Solutions Architect, Applied AI — Bangalore](https://job-boards.greenhouse.io/anthropic/jobs/5117581008) (10+ yrs pre-sales, India/APAC enterprises). Requires relocation; Japanese Tokyo role needs native Japanese — skip unless fluent.

---

## How Anthropic roles map to VN bank adaptation

```
  YOUR PATH (recommended)
  ─────────────────────
  Months 1–12     Syllabus + portfolio (this repo)
       │
       ▼
  Months 12–24    OCB AI Engineer OR NAB AIOps/Business BA  ← job-skills-adaptation §A / §H
       │          (production LangGraph + eval + banking metric)
       ▼
  Months 18–24    Apply Anthropic Tier 2 (Technical Specialist) OR Tier 1 (Applied AI Architect)
       │
       ▼
  Years 3–5       Tier 3 (Claude Code platform / loop & harness engineering)
```

| VN adaptation section | Builds toward Anthropic |
|---|---|
| **§A OCB AI Engineer** | LangGraph, RAG, FastAPI, Docker, eval harness → Tier 1 & 2 |
| **§H NAB AIOps/MLOps Nexus** | Production agents + K8s → Tier 1 architecture stories |
| **§B / §H Senior BA** | Stakeholder discovery, BRD, UAT → Tier 1 pre-sales discovery |
| **§ governance-mlops.md** | Safety, gates, audit → Anthropic mission alignment |
| **Harness / loop engineering** | Eval CI, verifier agents → Tier 3 |

---

## Role 1 — Applied AI Architect, Commercial

### Skills extracted (from JD)

| Category | Must-have | Nice-to-have |
|---|---|---|
| Pre-sales / advisory | Discovery → eval → deployment journey; translate business ↔ technical | Workshop facilitation, executive comms |
| Builder | Ship prototypes, near-production examples, **eval frameworks** | Reusable blueprints across customers |
| Technical | **Python**, Claude API, Claude Code, Claude for Enterprise | Cloud architecture, enterprise integration |
| LLM | RAG/agents patterns, measure Claude for specific use cases | LangChain/LangGraph familiarity |
| Mindset | Systems thinking (“one thing serves ten customers”); safety-first | Early-stage ambiguity |
| Experience | **3+ yrs** SWE + customer exposure **OR** 3+ yrs SA/SE/TAM + hands-on build | ML/data science background |

### Skill-relationship map

```
   CUSTOMER OUTCOME (adoption + measured value)
              ▲
              │ proves
   ┌──────────┴──────────┐
   │ EVAL + ARCHITECTURE  │◄─── governance-mlops.md (your repo)
   │ golden set · metrics │     responsible deployment story
   └──────────┬──────────┘
              │ wraps
   ┌──────────▼──────────┐
   │ HANDS-ON BUILD       │
   │ API · RAG · agents   │◄─── same cluster as OCB §A
   │ FastAPI · Docker     │
   └──────────┬──────────┘
              │ explained to
   ┌──────────▼──────────┐
   │ DISCOVERY + TRUST    │◄─── your BA superpower
   │ workshops · BRD lang │
   └─────────────────────┘
```

### Adaptation plan

1. **Months 1–12:** Complete syllabus flagship **`policy-copilot-api`** (RAG + LangGraph + eval + Docker) on **banking synthetic data**.
2. **Months 12–18:** Land **OCB AI Engineer** or **NAB AIOps** — get *real* production-adjacent story (even internal pilot).
3. **Portfolio add-ons for Anthropic:**
   - **Reusable blueprint:** “Financial services policy copilot” (architecture diagram + eval template + 5-min demo video).
   - **Customer-style narrative:** Write a case study as if you deployed for a bank (problem → eval design → grounded-rate metric → governance).
   - **Claude-specific:** Rebuild flagship using **Claude API** (not only OpenAI) — show Claude tool-use + citations.
4. **Gap to close:** Enterprise cloud (AWS/Azure), multi-stakeholder pre-sales — simulate with 2 mock “workshop” recordings in English.
5. **Relocation:** Role is SF/NYC hybrid (25%+ in office). Plan visa path; Anthropic sponsors for eligible roles.

---

## Role 2 — Technical Specialist, Claude Code

### Skills extracted

| Category | Must-have |
|---|---|
| Claude Code depth | Subagents, hooks, MCP, headless mode, managed settings |
| Customer enablement | 90-day adoption window; demos; reference implementations |
| Builder | Ship demo apps over a weekend; live agent steering |
| Background | 3–7 yrs SA / sales engineering / devrel / technical consulting |
| Identity | Uses Claude Code daily as core infrastructure |

### Skill-relationship map

```
   ADOPTION DEPTH (developers actually using Claude Code)
              ▲
   ┌──────────┴──────────┐
   │ ENABLEMENT           │  live demos · workshops · reference repos
   └──────────┬──────────┘
              │
   ┌──────────▼──────────┐
   │ CLAUDE CODE HARNESS  │  hooks · MCP · subagents · /loop patterns
   └──────────┬──────────┘
              │
   ┌──────────▼──────────┐
   │ DOMAIN PROOF         │  banking repo automation (BRD checker, eval loop)
   └─────────────────────┘
```

### Adaptation plan

1. **Months 7–10:** Use **Cursor + Claude** daily for all syllabus coding (document in README).
2. **Month 10 deliverable:** **`claude-code-banking-lab`** repo — hooks that run BRD linter + eval on save; MCP tool for policy lookup.
3. **Month 11–12:** Record **3 enablement assets:** (a) 10-min Claude Code walkthrough, (b) banking agent demo, (c) “eval harness in CI” snippet.
4. **Bridge from BA:** Frame past work as *“helped business + IT adopt new workflow”* — same muscle as driving Claude Code adoption.
5. **Apply earlier than Tier 1** if enablement portfolio is strong — Tier 2 cares less about deep ML, more about **Claude Code fluency + teaching**.

---

## Role 3 — Staff SWE, Developer Productivity (CI/CD) — Claude Code

### Skills extracted

| Category | Must-have |
|---|---|
| CI/CD at scale | PR → merge queue → deploy; gates; incident postmortems |
| Languages | **Python** + Go or Rust |
| Loop / harness | Pre-push validation; AI-assisted review; fast inner loop |
| Experience | **7+ yrs** backend or dev-infra |
| Influence | Cross-team pipeline standards |

### Adaptation plan (long-term)

1. **Months 9–12:** GitHub Actions eval-on-push for policy copilot (syllabus Phase 5).
2. **Year 2:** At VN bank, own **CI/CD for ML/agent pipeline** — document “time from PR to eval green.”
3. **Year 3+:** Contribute to OSS (pytest plugin, eval runner) or write public post on **verifier-agent in CI** (loop engineering).
4. **Not a Year-1 target** — requires years of infra experience Anthropic expects.

---

## 52-week syllabus → Anthropic skills map

**Legend:** ● = primary week for that role · ○ = supporting · — = not focus

| Week | Syllabus focus | Deliverable | Tier 1 Commercial | Tier 2 Claude Code | Tier 3 CI/CD |
|---|---|---|---|---|---|
| **1–2** | Python syntax | `week01_brd_checklist.py` | ○ | ● hooks later | — |
| **3–4** | Functions, OOP, Git | `week02_loan_rules.py` | ○ | ● | — |
| **5–8** | SQL + pandas | KPI queries + notebook | ○ | ○ | — |
| **9–12** | EDA + stats | `02_eda_credit.ipynb` | ○ customer metrics | ○ | — |
| **13–16** | pandas + leakage | Time-based split | ● feature thinking | — | — |
| **17–20** | Logistic / trees | Baseline PD model | ● ML credibility | — | — |
| **21–24** | XGBoost + SHAP | `credit-pd-model` | ● explainability story | — | — |
| **25–26** | Embeddings | Similarity demo | ● RAG foundation | ○ | — |
| **27–28** | Vector DB | Chroma policy chunks | ● | ○ MCP source | — |
| **29–30** | Doc classifier | `loan-doc-classifier` | ● doc intelligence | ○ | — |
| **31–32** | LLM APIs, JSON | Structured extraction | ● **switch to Claude API** | ● daily driver | — |
| **33–34** | RAG pipeline | Policy Q&A | ● flagship core | ● demo script | — |
| **35–36** | **LangGraph** | Escalation agent | ● same as OCB §A | ● subagent pattern | — |
| **37–38** | Golden eval set | ≥90% grounded rate | ● **Anthropic evals language** | ● | ○ |
| **39–40** | FastAPI | `/ask` endpoint | ● near-production | ● reference impl | ○ |
| **41–42** | Docker | `docker compose up` | ● | ● | ● container basics |
| **43–44** | GitHub Actions | Lint + test on push | ● eval in CI | ● hook automation | ● **core Tier 3** |
| **45–46** | Guardrails + audit | PII redaction logs | ● safety alignment | ○ | ○ |
| **47–50** | 2nd use case | AML triage agent | ● FS blueprint | ● 2nd demo | ○ |
| **51–52** | Portfolio + apply | CV + STAR + **Anthropic app** | ● apply Tier 1* | ● apply Tier 2* | — |

\*Apply after **6–12 months production experience** at VN bank unless enablement portfolio is exceptional for Tier 2.

### Phase summary (12 months)

| Month | Syllabus phase | Anthropic capability unlocked |
|---|---|---|
| 1–2 | Python + SQL | Can read/write integration code; BRD → automation narrative |
| 3–4 | Data + EDA | Customer metric design (eval success criteria) |
| 5–6 | Classical ML + SHAP | Credible ML generalist; “why declined” demos |
| 7–8 | NLP + RAG | Core Applied AI technical interview topics |
| 9–10 | LangGraph + eval | **Highest-value Anthropic differentiator** |
| 11–12 | API + Docker + CI + 2nd use case | Production-shaped; Tier 1 & 2 ready |

---

## Parallel track: VN banks vs Anthropic (same work, dual purpose)

| Syllabus week block | OCB/NAB proof (adaptation §A/§H) | Anthropic proof |
|---|---|---|
| 31–38 | LangGraph policy copilot | Claude API + eval framework (Tier 1 JD verbatim) |
| 39–46 | FastAPI/Docker/guardrails | Near-production examples + reusable blueprint |
| 43–44 | LLMOps gate | CI eval — “catch regressions before ship” (Tier 3 seed) |
| 47–50 | AML triage (CIR metric) | Financial services vertical demo for Commercial team |
| All | `governance-mlops.md` | Safety-first mission alignment in cover letter |

---

## Recommended sequencing

| When | Action |
|---|---|
| **Now → Month 12** | Execute [zero-to-ai-expert-syllabus.md](zero-to-ai-expert-syllabus.md); apply **OCB/NAB** per [job-skills-adaptation.md](job-skills-adaptation.md) rank 1–5 |
| **Month 10** | Rebuild flagship on **Claude API**; start **`claude-code-banking-lab`** |
| **Month 12** | Draft Anthropic CV (§5 in cv-templates.md); 200–400 word “Why Anthropic?” |
| **Month 12–18** | VN bank role; 1 internal Claude/agent pilot if possible |
| **Month 18** | Apply **Technical Specialist, Claude Code** (Tier 2) |
| **Month 24** | Apply **Applied AI Architect, Commercial** (Tier 1) with bank production story |
| **Year 3+** | Tier 3 if you pivot to platform/CI/CD leadership |

---

## Interview prep (Anthropic-specific)

| Round | Tier 1 Commercial | Tier 2 Claude Code | Prepare from syllabus |
|---|---|---|---|
| Recruiter | Mission + relocation + visa | Same + Claude Code daily use | governance-mlops.md “why safe AI” |
| Technical | Live Python: extend RAG prototype | Live demo: agent completes banking task | Weeks 33–36 projects |
| System design | Enterprise Claude deployment + eval | Customer 90-day adoption plan | Architecture diagram from Phase 4 |
| Behavioral | Embedded with customer; trade-offs | Teaching developers; shipped demos | STAR from BA + portfolio |

**Anthropic note:** They allow AI in application process with [published guidelines](https://www.anthropic.com/careers) — use Claude honestly; disclose as required on form.

---

## Gap checklist before Tier 1 application

- [ ] **Claude API** flagship (not OpenAI-only)
- [ ] **Eval framework** documented (golden set + grounded-rate metric)
- [ ] **English** demo video (5–10 min) — architecture + live Q&A
- [ ] **Financial services** case study (synthetic OK if labeled)
- [ ] **3+ years** SWE narrative (include intensive portfolio year + bank role)
- [ ] **Customer-facing** evidence (BA workshops count — position explicitly)
- [ ] **Relocation** plan (SF or NYC)
- [ ] **Why Anthropic** essay (200–400 words, safety + banking governance angle)

---

## Related Anthropic roles (watch list)

| Role | ID | When to consider |
|---|---|---|
| Engineering Manager, Agent Prompts & Evals | [5159608008](https://job-boards.greenhouse.io/anthropic/jobs/5159608008) | After 8+ yrs eng + 3 yrs mgmt + eval platform ownership |
| Applied AI Architect, Industries (FS customers) | Search careers | After Tier 1 + FS vertical depth |
| ML/Research Engineer, Safeguards | Search careers | If you deepen policy/red-team track |
| Solutions Architect, Applied AI (Bangalore) | [5117581008](https://job-boards.greenhouse.io/anthropic/jobs/5117581008) | APAC relocation; 10+ yrs pre-sales |
