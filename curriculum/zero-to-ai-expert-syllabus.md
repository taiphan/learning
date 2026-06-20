# Zero to AI Expert — Syllabus & Timeline

**Your profile:** Strong **banking domain** (credit, ops, BRD, compliance) · **Zero Python** today.  
**Target:** Hire-ready **AI Engineer / applied AI expert** in banking (OCB, NAB, VPBank, Techcombank track).  
**Honest horizon:** **12 months** focused study → job-ready portfolio · **2–3 years** production work → industry “expert.”

**Companion deck:** `exports/Zero-to-AI-Expert-Roadmap-Slides.pptx` (generate below).

**Hands-on lab:** [learning-lab-guide.md](learning-lab-guide.md) — materials, exercises, how to learn · start at [lab/exercises/week01_brd_checklist.py](lab/exercises/week01_brd_checklist.py)

---

## Your unfair advantage

| You already have | AI candidates often lack |
|---|---|
| Credit / lending / collections process | Why a model matters to the business |
| BRD, acceptance criteria, UAT thinking | What “production ready” means to regulators |
| Banking compliance mindset | Stakeholder language (CIR, TAT, NPL) |
| This repo (BRD + AI Factory governance) | Responsible AI by design |

**Strategy:** Learn Python/ML **through banking problems**, not abstract tutorials. Every phase ends with a **banking artifact**.

---

## Time commitment → timeline

| Hours/week | Job-ready AI Engineer | Notes |
|---|---|---|
| **5 hrs** | ~18 months | Slow but steady |
| **10 hrs** | **12 months** (recommended) | Default plan below |
| **15 hrs** | ~9 months | Aggressive |
| **20+ hrs** | ~6–7 months | Bootcamp pace — burnout risk |

---

## 12-month master timeline

| Month | Phase | Theme | Deliverable (proof) |
|---|---|---|---|
| **1** | 0 | Python foundations | Script: BRD quality checker |
| **2** | 0–1 | Python + SQL | SQL: loan portfolio KPI queries |
| **3** | 1 | Data + pandas | Notebook: clean credit dataset |
| **4** | 2 | Classical ML | Model: credit default / PD proxy |
| **5** | 2 | ML evaluation | Report: AUC, calibration, SHAP |
| **6** | 3 | NLP + embeddings | Doc classifier for loan files |
| **7** | 4 | RAG fundamentals | Policy Q&A over PDF chunks |
| **8** | 4 | LangGraph agents | Agent: policy lookup + escalate |
| **9** | 5 | FastAPI + Docker | API serving your copilot |
| **10** | 5 | Eval + guardrails | 90%+ grounded-response test suite |
| **11** | 6 | Banking use case #2 | AML triage OR NBO scoring story |
| **12** | 7 | Portfolio + apply | GitHub + CV + 3 interview STAR stories |

---

## Phase 0 — Python from zero (Weeks 1–8)

**Goal:** Read, write, and debug Python; use Git; run notebooks.

### Weeks 1–2: Core syntax

| Topic | Learn | Banking exercise |
|---|---|---|
| Variables, types, `if/for/while` | Python.org tutorial §1–4 | Parse a BRD checklist (yes/no fields) |
| Functions, modules, `import` | Real Python basics | Function: score BRD completeness % |
| Files, JSON, CSV | Read/write files | Load `examples/` BRD markdown metadata |
| venv, pip, Jupyter | Setup | One notebook per week |

**Resources:** [Python.org tutorial](https://docs.python.org/3/tutorial/), Kaggle Learn “Python”, freeCodeCamp Python (YouTube, sections 1–6).

**Exit test:** Write a 100-line script that reads a CSV of fake loan applications and prints pass/fail by simple rules.

### Weeks 3–4: Intermediate Python

| Topic | Learn | Banking exercise |
|---|---|---|
| Lists, dicts, comprehensions | Data structures | Map BRD sections → weights (quality rubric) |
| Classes (basic OOP) | One simple class | `class BRDScorecard` with methods |
| Error handling, logging | `try/except`, `logging` | Log validation errors without crashing |
| Git: clone, commit, push | GitHub | Public repo `banking-ai-learning` |

**Exit test:** BRD quality scorer CLI — input markdown path → output score + missing sections.

### Weeks 5–8: SQL + Python together

| Topic | Learn | Banking exercise |
|---|---|---|
| SQL SELECT, JOIN, GROUP BY | SQLBolt or Mode SQL | “Top 10 branches by disbursement” |
| Window functions | Advanced SQL | Monthly churn / roll rates |
| Python + DB (`sqlite3` or `psql`) | Connect from Python | Export query results to CSV |
| pandas intro | `read_csv`, `groupby` | Same KPIs in pandas |

**Resources:** SQLBolt, Kaggle Learn SQL, pandas “10 minutes to pandas”.

**Exit deliverable:** **`phase0-brd-scorer`** + **`phase0-lending-kpis`** repos on GitHub.

---

## Phase 1 — Data science foundations (Weeks 9–16)

**Goal:** Exploratory analysis and feature thinking on credit data.

| Week | Topic | Banking exercise |
|---|---|---|
| 9–10 | pandas deep dive | Missing values, dtypes, merges on customer ID |
| 11–12 | Visualization (matplotlib/seaborn) | PD by segment, vintage curves |
| 13–14 | Statistics refresher | Mean, variance, correlation, hypothesis intuition |
| 15–16 | Train/validation split, leakage | No future data in features; time-based split |

**Dataset:** [Kaggle Give Me Some Credit](https://www.kaggle.com/c/GiveMeSomeCredit) or UCI German Credit (start small).

**Exit deliverable:** EDA notebook with **3 business insights** written in BRD language (problem → metric → implication).

---

## Phase 2 — Classical machine learning (Weeks 17–24)

**Goal:** Build, evaluate, and explain a credit-style model.

| Week | Topic | Tool | Banking exercise |
|---|---|---|---|
| 17–18 | Logistic regression, decision trees | scikit-learn | Baseline PD model |
| 19–20 | Random forest, XGBoost | xgboost | Beat baseline AUC |
| 21–22 | Metrics: AUC, KS, Gini, confusion matrix | sklearn metrics | Model comparison table |
| 23–24 | Explainability (SHAP / feature importance) | shap | “Why declined?” narrative for 1 customer |

**Concepts (light math):** bias-variance, overfitting, cross-validation, class imbalance (`class_weight`).

**Resources:** scikit-learn docs, Kaggle Learn Intro to ML, *Hands-On ML* ch. 1–6 (optional).

**Exit deliverable:** **`credit-pd-model`** — README with business metric (“reduce false declines X% at fixed approval rate”).

---

## Phase 3 — NLP & document intelligence (Weeks 25–30)

**Goal:** Text + embeddings for banking documents.

| Week | Topic | Banking exercise |
|---|---|---|
| 25–26 | Tokenization, embeddings concept | Compare two policy sentences similarity |
| 27–28 | Vector DB (Chroma or pgvector) | Index 20 policy PDF chunks |
| 29–30 | Document classification | Loan doc type: ID / contract / collateral |

**Resources:** Hugging Face NLP course (ch. 1–3), LangChain embedding docs.

**Exit deliverable:** **`loan-doc-classifier`** — ties to Senior BA “AI/OCR” differentiator.

---

## Phase 4 — Generative AI & agents (Weeks 31–38)

**Goal:** RAG + LangGraph agent — **core hire signal** for OCB / NAB AIOps roles.

| Week | Topic | Banking exercise |
|---|---|---|
| 31–32 | LLM APIs, prompts, JSON output | Structured extraction from policy text |
| 33–34 | RAG pipeline (chunk, retrieve, generate) | Credit policy Q&A |
| 35–36 | **LangGraph**: state, tools, multi-step | Agent: retrieve → answer → escalate if low confidence |
| 37–38 | Eval: golden Q&A set (20–50 questions) | Measure grounded-response rate |

**Resources:** DeepLearning.AI “LangChain for LLM Application Development”, LangGraph docs, LangChain RAG tutorial.

**Exit deliverable:** **`policy-copilot-agent`** — demo video + architecture diagram.

---

## Phase 5 — Production & LLMOps (Weeks 39–46)

**Goal:** Not a notebook — a **served, monitored** system.

| Week | Topic | Banking exercise |
|---|---|---|
| 39–40 | FastAPI REST API | `/ask` endpoint for copilot |
| 41–42 | Docker + docker-compose | One-command local deploy |
| 43–44 | CI (GitHub Actions) | Lint + test on push |
| 45–46 | Guardrails + logging | PII redaction; no secrets in logs; audit trail |

**Optional stretch:** MLflow experiments, basic Prometheus metrics, OpenTelemetry trace IDs.

**Exit deliverable:** **`policy-copilot-api`** — `docker compose up` works; eval report in `/docs`.

---

## Phase 6 — Second banking use case (Weeks 47–50)

Pick **one** to show breadth:

| Option | Skills | Metric |
|---|---|---|
| **A. AML alert triage agent** | Classification + LangGraph | Analyst minutes saved |
| **B. Next-best-offer (propensity)** | ML + business rules | Conversion lift |
| **C. Collections script assist** | RAG over playbooks | Handle time reduction |

**Exit deliverable:** Second repo or second module in monorepo — **`banking-ai-portfolio`**.

---

## Phase 7 — Expert polish & job hunt (Weeks 51–52+)

| Task | Output |
|---|---|
| Consolidate GitHub README (architecture, metrics, governance) | 1 portfolio page |
| Update `cv-cover-letter.md` with real projects | English CV |
| 5 STAR stories (embed, ship, metric) | Interview doc |
| Apply: NAB BA data focus + OCB AI Engineer + VPBank AI | 3 applications/week |
| Mock interviews | LangGraph + ML + banking domain |

---

## Weekly syllabus template (10 hrs/week)

| Day | Hours | Activity |
|---|---|---|
| Mon | 2 | Course/video + notes |
| Tue | 2 | Code exercises (same topic) |
| Wed | 1 | Banking exercise (apply to domain) |
| Thu | 2 | Project work toward deliverable |
| Fri | 1 | Git commit + README update |
| Sat | 2 | Project / debug / optional Kaggle |
| Sun | — | Rest |

**Rule:** Never watch without coding the same day. **Domain rule:** Every month, tie output to a BRD or ops metric.

---

## Tools to install (Week 1)

```bash
# macOS — install once
brew install python@3.11 git
python3 -m venv ~/venvs/ai-learn
source ~/venvs/ai-learn/bin/activate
pip install jupyter pandas scikit-learn xgboost matplotlib sqlalchemy
```

Add later: `langchain langgraph chromadb fastapi uvicorn docker`

---

## What “expert” means (levels)

| Level | Timeline | Evidence |
|---|---|---|
| **Beginner** | Month 1–3 | Python + SQL + pandas |
| **Practitioner** | Month 4–6 | ML model with metrics + explainability |
| **Applied AI engineer** | Month 7–10 | RAG + LangGraph + API |
| **Job-ready** | Month 11–12 | 2 banking AI projects + governance story |
| **Industry expert** | Year 2–3+ | Production systems at scale with measured ROI |

You skip **years** of “what problem are we solving?” because you have banking domain. You must **not** skip Python fundamentals — 8 weeks minimum.

---

## First 30 days — start tomorrow

| Week | Do this |
|---|---|
| **1** | Install Python, Git, VS Code/Cursor; finish Python.org tutorial §1–4; create GitHub repo |
| **2** | Functions + files; build BRD section checker (hardcode 5 sections) |
| **3** | SQLBolt lessons 1–12; SQLite + Python query |
| **4** | pandas `read_csv`; plot one KPI from sample credit data |

**Generate slides:**

```bash
python3 curriculum/generate_ai_roadmap_slides.py
```

Output: `curriculum/exports/Zero-to-AI-Expert-Roadmap-Slides.pptx`
