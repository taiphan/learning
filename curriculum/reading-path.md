# Step-by-Step Reading Path — Zero Python → AI Engineer (Banking)

**Profile:** Banking domain yes · Python zero · **10 hrs/week** · **12 months**  
**Rule:** Read one unit → do the matching exercise in [lab/](lab/) the same day.  
**Full lab guide:** [learning-lab-guide.md](learning-lab-guide.md)

---

## How to use this list

| Symbol | Meaning |
|---|---|
| **★ Primary** | Read/do this first — minimum to progress |
| **○ Optional** | Deepen understanding if you have extra time |
| **📦 After reading** | Exercise or deliverable before moving on |

Books are ordered. **Do not buy everything at once** — one phase at a time.

---

## STEP 1 — Python from zero (Weeks 1–4)

### Information (free — start here)

| Order | Resource | What to read | Time |
|---|---|---|---|
| 1 ★ | [Python.org Tutorial](https://docs.python.org/3/tutorial/) | **§1–4** (intro, types, control flow, functions) | Week 1 |
| 2 ★ | Same | **§5–6** (data structures, modules) | Week 2 |
| 3 ★ | [Kaggle Learn — Python](https://www.kaggle.com/learn/python) | All lessons | Week 1–2 parallel |
| 4 ★ | [Real Python — First Steps](https://realpython.com/python-first-steps/) | Setup, venv, running scripts | Day 1 |
| 5 ○ | [Automate the Boring Stuff](https://automatetheboringstuff.com/) (free online) | Ch. 1–6 | Week 3–4 |

### Book (optional buy — one is enough)

| Book | Read when | Chapters |
|---|---|---|
| **Python Crash Course** (Eric Matthes, 3rd ed.) | If you prefer a physical book | Part I (Basics), Part II (Projects) — stop before Django |
| *or* **Automate the Boring Stuff** (Al Sweigart) | Free online is enough | Ch 1–9 |

### Domain reading (same weeks)

| Order | Resource | Why |
|---|---|---|
| ★ | `docs/01-brd-template-en.md` (this repo) | Connect code to BRD sections |
| ★ | `docs/08` or quality rubric in `docs/` | Weights for scoring exercise |

📦 **After Step 1:** Complete [week01_brd_checklist.py](lab/exercises/week01_brd_checklist.py) + [week02_loan_rules.py](lab/exercises/week02_loan_rules.py)

**Checkpoint:** You can write a 50-line script without the tutorial open.

---

## STEP 2 — Git + SQL (Weeks 5–8)

### Information

| Order | Resource | What to read | Time |
|---|---|---|---|
| 1 ★ | [GitHub Git Handbook](https://guides.github.com/introduction/git-handbook/) | Full (short) | Week 5 |
| 2 ★ | [SQLBolt](https://sqlbolt.com/) | **Lessons 1–18** | Weeks 5–7 |
| 3 ★ | [Kaggle Learn — SQL](https://www.kaggle.com/learn/intro-to-sql) | All lessons | Week 6–7 |
| 4 ★ | [Kaggle Learn — Pandas](https://www.kaggle.com/learn/pandas) | Lessons 1–4 | Week 8 |
| 5 ○ | [pandas docs — 10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html) | One pass | Week 8 |

### Book (optional)

| Book | Read when | Chapters |
|---|---|---|
| **Learning SQL** (Alan Beaulieu, 3rd ed.) | Only if SQLBolt feels too thin | Ch 1–10 |

📦 **After Step 2:** [sql/week05_queries.sql](lab/sql/week05_queries.sql) + notebook `01_lending_kpis.ipynb`

**Checkpoint:** JOIN + GROUP BY + same KPI in pandas.

---

## STEP 3 — Data exploration & statistics intuition (Weeks 9–12)

### Information

| Order | Resource | What to read | Time |
|---|---|---|---|
| 1 ★ | [Kaggle — Give Me Some Credit](https://www.kaggle.com/c/GiveMeSomeCredit/data) | Read data description only first | Week 9 |
| 2 ★ | [StatQuest YouTube](https://www.youtube.com/@statquest) | Playlists: “Statistics fundamentals”, “Machine Learning” (pick 5–8 videos) | Weeks 9–10 |
| 3 ○ | [Seeing Theory](https://seeing-theory.brown.edu/) | Visual stats basics | Week 10 |

### Book (optional)

| Book | Chapters |
|---|---|
| **Naked Statistics** (Charles Wheelan) | Whole book — light read for intuition |
| *or* skip books — StatQuest videos are enough at this stage |

📦 **After Step 3:** Notebook `02_eda_credit.ipynb` — 3 business insights in BRD language

---

## STEP 4 — Machine learning (Weeks 13–20) ★ Core technical phase

### Information

| Order | Resource | What to read / do | Time |
|---|---|---|---|
| 1 ★ | [Kaggle Learn — Intro to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning) | **All lessons** | Weeks 13–14 |
| 2 ★ | [Kaggle Learn — Intermediate ML](https://www.kaggle.com/learn/intermediate-machine-learning) | All lessons | Weeks 15–16 |
| 3 ★ | [scikit-learn tutorials](https://scikit-learn.org/stable/tutorial/index.html) | Supervised learning chapter | Week 15 |
| 4 ★ | [SHAP documentation](https://shap.readthedocs.io/en/latest/example_notebooks/overviews/An%20introduction%20to%20explainable%20AI%20with%20Shapley%20values.html) | One notebook | Week 18 |
| 5 ○ | [XGBoost docs — Python intro](https://xgboost.readthedocs.io/en/stable/tutorials/index.html) | First tutorial | Week 17 |

### Book ★ (best single ML book for your path)

| Book | Author | Read when | What to read |
|---|---|---|---|
| **Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow** (3rd ed.) | Aurélien Géron | Weeks 13–20 | **Part I only:** Ch 1–9 (ignore deep learning chapters until Step 6) |

**Chapter map (Géron Part I):**

| Ch | Topic | Week |
|---|---|---|
| 1 | ML landscape | 13 |
| 2 | End-to-end project | 14 |
| 3 | Classification | 15 |
| 4 | Training models | 15 |
| 5 | Support Vector Machines | skip/skim |
| 6 | Decision Trees | 16 |
| 7 | Ensemble / Random Forest | 16 |
| 8 | Dimensionality reduction | skim |
| 9 | Unsupervised | skim |

### Domain reading

| Resource | Why |
|---|---|
| `examples/04a-brd-pos-lending.md` | Frame model as business problem |
| `governance-mlops.md` → model validation, bias | Interview + responsible AI |

📦 **After Step 4:** Repo `credit-pd-model/` — AUC + SHAP + README with business metric

**Checkpoint:** Train classifier, report AUC, explain one decline in plain English.

---

## STEP 5 — NLP, embeddings & RAG (Weeks 21–28)

### Information (courses > books for this phase)

| Order | Resource | What to complete | Time |
|---|---|---|---|
| 1 ★ | [Hugging Face NLP Course](https://huggingface.co/learn/nlp-course/chapter1/1) | **Ch 1–3** (embeddings, transformers intuition) | Weeks 21–22 |
| 2 ★ | [DeepLearning.AI — LangChain for LLM Application Development](https://www.deeplearning.ai/short-courses/langchain-for-llm-application-development/) | Full short course (~1 hr) | Week 23 |
| 3 ★ | [LangChain — RAG tutorial](https://python.langchain.com/docs/tutorials/rag/) | Build once alongside course | Week 24 |
| 4 ○ | [ChromaDB docs — getting started](https://docs.trychroma.com/docs/overview/getting-started) | Local vector store | Week 24 |

### Book (optional — skip if time tight)

| Book | Note |
|---|---|
| **Natural Language Processing with Transformers** (Tunstall et al.) | Read **Ch 1–2** only for intuition — not required for job path |

📦 **After Step 5:** `policy-rag/` — CLI Q&A over policy chunks with source citation

**Checkpoint:** Answer includes text from your document, not model memory.

---

## STEP 6 — Agents & LangGraph (Weeks 29–32) ★ Hire-critical for OCB / NAB

### Information

| Order | Resource | What to complete | Time |
|---|---|---|---|
| 1 ★ | [DeepLearning.AI — AI Agents in LangGraph](https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/) | Full course | Week 29 |
| 2 ★ | [LangGraph docs — quickstart](https://langchain-ai.github.io/langgraph/tutorials/introduction/) | Build agent with tools | Weeks 30–31 |
| 3 ★ | OpenAI or Azure OpenAI — API docs | Chat completions + function calling | Week 29 |
| 4 ○ | [LangChain — agent docs](https://python.langchain.com/docs/concepts/agents/) | Conceptual read | Week 30 |

### Book

**No book required** — LangGraph changes fast; courses + docs beat books here.

### Domain reading

| Resource | Why |
|---|---|
| `job-skills-adaptation.md` → OCB AI Engineer, NAB AIOps | Align project to JD language |
| `job-skills-adaptation.md` → use-case portfolio | Pick policy copilot / AML triage |

📦 **After Step 6:** `policy-copilot-agent/` — LangGraph + eval JSON (30 Q&A) + architecture diagram

**Checkpoint:** Agent escalates when confidence low; ≥85% grounded on eval set.

---

## STEP 7 — Production & MLOps (Weeks 33–40)

### Information

| Order | Resource | What to read | Time |
|---|---|---|---|
| 1 ★ | [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/) | First 5 sections | Weeks 33–34 |
| 2 ★ | [Docker — Get Started](https://docs.docker.com/get-started/) | Full guide | Weeks 35–36 |
| 3 ★ | `governance-mlops.md` (this repo) | Full — gates, monitoring, responsible AI | Week 37 |
| 4 ★ | [ragas docs](https://docs.ragas.io/en/stable/getstarted/) | RAG evaluation | Week 38 |
| 5 ○ | [Made With ML — MLOps lessons](https://madewithml.com/) | Deployment module | Week 39 |

### Book (optional — Part II of Géron now)

| Book | Chapters |
|---|---|
| **Hands-On ML** (Géron) **Part II** | Skim Ch 10–13 (TF/Keras intro) — **optional** unless you want deep learning later |

📦 **After Step 7:** `policy-copilot-api/` — `docker compose up` + eval in CI

**Checkpoint:** Someone else runs your Docker API on their machine.

---

## STEP 8 — Portfolio, jobs & interviews (Weeks 41–48)

### Information

| Order | Resource | Action |
|---|---|---|
| 1 ★ | [learning-lab-guide.md](learning-lab-guide.md) Part 4–5 | Finish exercise catalog |
| 2 ★ | [job-skills-adaptation.md](job-skills-adaptation.md) | Pick 3 target roles (NAB BA data, OCB AI, etc.) |
| 3 ★ | [cv-templates.md](cv-templates.md) | Fill with real project metrics |
| 4 ★ | [job-skills-adaptation.md](job-skills-adaptation.md) | Prepare 5 STAR stories |
| 5 ○ | Target bank JD pages | Mirror keywords in CV |

### Books

**No new technical books** — polish GitHub README and practice explaining projects aloud.

📦 **After Step 8:** Apply · mock interviews · refine portfolio

---

## Minimum book list (if you buy only 2)

| # | Book | When |
|---|---|---|
| 1 | **Python Crash Course** *or* use free Automate the Boring Stuff | Month 1 |
| 2 | **Hands-On Machine Learning** (Géron) — Part I | Months 4–5 |

Everything else: **free docs + DeepLearning.AI short courses + this repo**.

---

## One-page reading calendar (10 hrs/week)

| Month | Read / study | Book chapter |
|---|---|---|
| 1 | Python.org §1–6, Kaggle Python | Crash Course Part I *or* Automate Ch 1–6 |
| 2 | SQLBolt, Kaggle SQL + Pandas | — |
| 3 | StatQuest + EDA on Kaggle dataset | Géron Ch 1–2 |
| 4 | Kaggle Intro + Intermediate ML | Géron Ch 3–7 |
| 5 | SHAP, XGBoost docs | Géron Ch 8–9 skim |
| 6 | HF NLP Ch 1–3 | — |
| 7 | DL.AI LangChain + RAG docs | — |
| 8 | DL.AI LangGraph + LangGraph docs | — |
| 9 | FastAPI + Docker + governance-mlops.md | — |
| 10 | ragas, job docs, interview prep | — |

---

## What NOT to read early (common mistakes)

| Too early | Read instead when |
|---|---|
| Deep learning textbooks | Month 6+ optional (Géron Part II skim) |
| Kubernetes books | After Docker works (Month 9+) |
| Statistics PhD-level texts | StatQuest + Kaggle ML is enough |
| 5 Python books at once | One tutorial + Kaggle Learn |
| Research papers | After you have one working RAG agent |

---

## Your next 3 actions

1. **Today:** Python.org tutorial §1 + start [week01_brd_checklist.py](lab/exercises/week01_brd_checklist.py)
2. **This week:** Finish §1–4 + Kaggle Python lessons 1–3
3. **This month:** Finish Step 1 checkpoint before opening any ML book
