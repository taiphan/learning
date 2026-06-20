# Learning Lab — Materials, Syllabus, Exercises & How to Learn

**For:** Banking domain expert · **zero Python** today · goal = applied AI engineer in banking.  
**Companion files:**
- Timeline overview → [zero-to-ai-expert-syllabus.md](zero-to-ai-expert-syllabus.md)
- Visual deck → `exports/Zero-to-AI-Expert-Roadmap-Slides.pptx`
- **Runnable exercises** → [lab/exercises/](lab/exercises/)

---

## Part 1 — How to learn (method that actually builds skills)

### The 4-step loop (use every study session)

```
1. READ   (20%)  → one concept only (15–30 min video or docs)
2. TYPE   (50%)  → rewrite example yourself — no copy-paste
3. APPLY  (20%)  → banking exercise in lab/
4. SHIP   (10%)  → git commit + one-line README note
```

**Rules**
- **No passive binge.** If you watched 30 min, you must code 30 min the same day.
- **One concept per session.** “Today = Python functions” not “today = Python everything”.
- **Banking lens always.** After each concept, ask: *how would this help credit ops / BRD / risk?*
- **Fail in public (GitHub).** Commit broken code early; fix in next commit — shows progress.
- **Explain aloud.** Pretend you’re telling a BA colleague why your script matters (builds interview skill).

### Environment setup (Day 1 — 45 minutes)

```bash
# macOS
brew install python@3.11 git
mkdir -p ~/projects/banking-ai-learning
cd ~/projects/banking-ai-learning
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install jupyter pandas matplotlib

# Clone or copy exercises from this repo
cp -r /path/to/finance/curriculum/learning-lab ./lab
git init && git add . && git commit -m "chore: day 1 setup"
```

**Tools:** VS Code or Cursor · Jupyter Lab · GitHub account · (later) Docker Desktop.

### How to do an exercise (step-by-step)

1. Open the exercise file in `lab/exercises/`.
2. Read the **TASK** and **TODO** comments only — don’t peek at solutions online first.
3. Try 20–30 min alone; then check Python docs or Kaggle hint.
4. Run: `python3 weekXX_....py` — fix errors until it passes.
5. **Stretch:** change one business rule (e.g. DTI 0.40 → 0.35) and re-run.
6. Commit: `git commit -m "feat(week02): loan rules with DTI check"`.

### When you’re stuck

| Problem | Fix |
|---|---|
| Syntax error | Read the line number; google exact error message |
| `ModuleNotFoundError` | `pip install <package>` inside activated venv |
| Logic wrong | Print variables (`print(income, debt)`) — smallest debug |
| Overwhelmed | Drop to smaller task; finish one TODO only |
| No motivation | Do 25 min timer; banking exercises feel more real than generic |

---

## Part 2 — Curated materials (free-first)

### Phase 0 — Python & Git (Weeks 1–8)

| Material | Type | URL | Use for |
|---|---|---|---|
| **Python official tutorial** | Docs | https://docs.python.org/3/tutorial/ | Weeks 1–4 (§1–9) |
| **Real Python — basics** | Articles | https://realpython.com/python-first-steps/ | Setup, venv, scripts |
| **Kaggle Learn — Python** | Interactive | https://www.kaggle.com/learn/python | Daily micro-exercises |
| **freeCodeCamp Python** | Video | YouTube “Python for Beginners” (~4h) | Week 1 background |
| **Git handbook** | Docs | https://guides.github.com/introduction/git-handbook/ | Week 3–4 |
| **SQLBolt** | Interactive | https://sqlbolt.com/ | Weeks 5–8 (lessons 1–18) |
| **Kaggle Learn — Pandas** | Interactive | https://www.kaggle.com/learn/pandas | Week 7–8 |
| **This repo — BRD template** | Domain | `docs/01-brd-template-en.md` | Week 1–2 exercises |

### Phase 1 — Data & statistics (Weeks 9–16)

| Material | Type | URL | Use for |
|---|---|---|---|
| **Kaggle Learn — Intro to ML** | Course | https://www.kaggle.com/learn/intro-to-machine-learning | Week 13 preview |
| **StatQuest (YouTube)** | Video | Search “StatQuest ML playlist” | Intuition without heavy math |
| **Dataset — Give Me Some Credit** | Data | https://www.kaggle.com/c/GiveMeSomeCredit/data | Credit default modelling |
| **Dataset — German Credit (UCI)** | Data | Small starter set if Kaggle heavy | Week 9 EDA |
| **pandas docs** | Reference | https://pandas.pydata.org/docs/ | Daily reference |

### Phase 2 — Classical ML (Weeks 17–24)

| Material | Type | URL | Use for |
|---|---|---|---|
| **scikit-learn tutorials** | Docs | https://scikit-learn.org/stable/tutorial/index.html | Core algorithms |
| **scikit-learn — classification** | Docs | User guide → Supervised learning | PD / default model |
| **XGBoost docs** | Docs | https://xgboost.readthedocs.io/ | Better AUC |
| **SHAP docs** | Docs | https://shap.readthedocs.io/ | Explainability |
| ***Hands-On ML* (book)** | Book | Aurélien Géron — ch. 1–6 optional | Deep dive if you want |
| **Imbalanced-learn** | Docs | For rare default class | Banking reality |

### Phase 3 — NLP & embeddings (Weeks 25–30)

| Material | Type | URL | Use for |
|---|---|---|---|
| **Hugging Face NLP course** | Course | https://huggingface.co/learn/nlp-course/chapter1/1 | Embeddings intro |
| **LangChain docs — RAG** | Docs | https://python.langchain.com/docs/tutorials/rag/ | Week 27+ |
| **ChromaDB docs** | Docs | https://docs.trychroma.com/ | Local vector store |

### Phase 4 — GenAI & agents (Weeks 31–38)

| Material | Type | URL | Use for |
|---|---|---|---|
| **DeepLearning.AI — LangChain** | Course | https://www.deeplearning.ai/short-courses/langchain-for-llm-application-development/ | RAG patterns |
| **DeepLearning.AI — LangGraph** | Course | https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/ | **Required for OCB/NAB** |
| **LangGraph docs** | Docs | https://langchain-ai.github.io/langgraph/ | Agent state, tools |
| **OpenAI / Azure OpenAI docs** | API | Platform docs for your API key | Production patterns |

### Phase 5 — Production (Weeks 39–46)

| Material | Type | URL | Use for |
|---|---|---|---|
| **FastAPI tutorial** | Docs | https://fastapi.tiangolo.com/tutorial/ | REST API |
| **Docker getting started** | Docs | https://docs.docker.com/get-started/ | Container deploy |
| **GitHub Actions — Python** | Docs | CI template | Automated test |
| **This repo — governance** | Domain | `governance-mlops.md` | Guardrails narrative |
| **ragas (eval)** | Library | https://docs.ragas.io/ | RAG quality metrics |

### Phase 6–7 — Banking AI & jobs

| Material | Type | Use for |
|---|---|---|
| `job-skills-adaptation.md` | Target roles OCB/NAB/VPBank | Interview focus |
| `interview-kit.md` | STAR / technical prompts | Mock interviews |
| `examples/04a-brd-pos-lending.md` | Gold BRD sample | Domain stories |

---

## Part 3 — Week-by-week syllabus + exercises

**Default pace:** 10 hrs/week · **12 months** to job-ready.  
**Legend:** 📖 = study · ✍️ = exercise in `lab/` · 📦 = portfolio deliverable

### Month 1 — Python foundations

| Week | Study (📖) | Practice (✍️) | Deliverable (📦) |
|---|---|---|---|
| **1** | Python tutorial §1–4; Kaggle Python L1–3 | `week01_brd_checklist.py` — complete TODOs | Script runs; lists missing BRD sections |
| **2** | §5–6 functions, modules; read `docs/01-brd-template-en.md` | Extend week01: read BRD from **file path** arg | `python3 week01_brd_checklist.py path/to/brd.md` |
| **3** | Lists, dicts, JSON; Real Python data structures | Map section → weight from quality rubric (`docs/`) | Print score % (weighted) |
| **4** | Classes (basic); logging | `class BRDScorecard` with `.score()` method | Week 4 commit on GitHub |

**Week 1 exercise (start now):**
```bash
cd curriculum/lab/exercises
python3 week01_brd_checklist.py   # will fail until you complete TODOs
```

**Week 2 exercise:**
```bash
python3 week02_loan_rules.py      # implement evaluate() rules
```

**Self-test Week 4:** Explain to someone why BRD Section H (business rules) maps to `if` statements in code.

---

### Month 2 — SQL + pandas

| Week | Study | Practice | Deliverable |
|---|---|---|---|
| **5** | SQLBolt 1–6 | Write 5 queries: count apps, avg income by region | `sql/week05_queries.sql` |
| **6** | SQLBolt 7–12; JOINs | Join customers ↔ applications (create 2nd CSV) | Join query returns correct rows |
| **7** | SQLBolt 13–18; windows | Monthly disbursement trend (window function) | KPI query documented |
| **8** | Kaggle Pandas L1–4 | Same KPIs in pandas from `sample_loans.csv` | Notebook `01_lending_kpis.ipynb` |

**Exercise — SQL (Week 5):**
```sql
-- File: lab/sql/week05_queries.sql
-- Q1: How many applications per region?
-- Q2: Average loan_amount_vnd where employment_months >= 12
-- Q3: Applications with debt/income > 0.4 (high DTI)
```

**Exercise — pandas (Week 8):**
```python
import pandas as pd
df = pd.read_csv("data/sample_loans.csv")
df["dti"] = df["existing_debt_vnd"] / df["monthly_income_vnd"]
# TODO: groupby region, plot bar chart of avg loan amount
```

---

### Months 3–4 — Machine learning

| Week | Study | Practice | Deliverable |
|---|---|---|---|
| **9–10** | Kaggle Intro ML L1–3; pandas EDA | Load Give Me Some Credit; missing values, histograms | `notebooks/02_eda_credit.ipynb` |
| **11–12** | Logistic regression, train/test split | Baseline model; **time-based split** (no leakage) | AUC printed |
| **13–14** | Random Forest, XGBoost | Beat baseline; tune one hyperparameter | Comparison table |
| **15–16** | Metrics (AUC, KS); SHAP | Explain 3 declined cases | `credit-pd-model/` repo + README |

**Exercise — ML (Week 12):**
```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

# X = features, y = SeriousDlqin2yrs (default label)
# TODO: fit, predict_proba, print AUC
# WRITE IN README: what business decision this supports (approval policy)
```

**Banking write-up (required):** One paragraph in BRD language — problem, baseline metric, target metric, how measured.

---

### Months 5–6 — NLP & documents

| Week | Study | Practice | Deliverable |
|---|---|---|---|
| **17–18** | HF NLP ch.1–2 | Embed 10 sentences; cosine similarity | Notebook `03_embeddings.ipynb` |
| **19–20** | LangChain RAG quickstart | Chunk 5 policy paragraphs; retrieve top-3 | CLI asks one question |
| **21–22** | Text classification | Labels: `ID`, `CONTRACT`, `COLLATERAL`, `OTHER` | `doc-classifier/` |
| **23–24** | Review + refactor | Add tests for classifier | 80%+ accuracy on tiny test set |

**Exercise — RAG (Week 20):** Use synthetic policy text from `lab/data/sample_policy.txt` (create 1-page markdown of fake credit rules).

---

### Months 7–8 — LangGraph agent (hire-critical)

| Week | Study | Practice | Deliverable |
|---|---|---|---|
| **25–26** | DL.AI LangChain short course | Prompt + JSON output for structured answers | Structured Q&A |
| **27–28** | DL.AI LangGraph course | Graph: retrieve → generate → check confidence | Diagram in README |
| **29–30** | Tool calling | Tool: `search_policy(query)`, `escalate_to_human(reason)` | Agent demo |
| **31–32** | Eval | 30 golden Q&A pairs; score grounded rate | ≥85% grounded |

**Exercise — golden eval format (`lab/data/eval_questions.json`):**
```json
[
  {"question": "Max DTI for POS motorbike loan?", "expected_contains": ["40%", "DTI"], "must_not_contain": ["I don't know"]},
  {"question": "Who approves loans over 100M?", "expected_contains": ["regional", "director"]}
]
```

---

### Months 9–10 — Production

| Week | Study | Practice | Deliverable |
|---|---|---|---|
| **33–34** | FastAPI tutorial | `POST /ask` `{ "question": "..." }` | Running API |
| **35–36** | Docker get-started | Dockerfile + docker-compose | `docker compose up` |
| **37–38** | Guardrails; governance doc | Redact national ID patterns in logs | Audit log sample |
| **39–40** | CI + eval in pipeline | GitHub Action runs eval on push | Green CI badge |

---

### Months 11–12 — Portfolio & apply

| Week | Action |
|---|---|
| **41–42** | Second use case: AML triage **OR** propensity model |
| **43–44** | Single GitHub portfolio README linking all projects |
| **45–46** | CV (`cv-cover-letter.md`), apply NAB BA data + OCB AI |
| **47–48** | Mock interviews; refine STAR stories |

---

## Part 4 — Exercise catalog (by skill)

| Skill | Exercise file / project | Pass criteria |
|---|---|---|
| Python basics | `week01_brd_checklist.py` | All sections detected correctly |
| Business rules in code | `week02_loan_rules.py` | 10/10 sample loans evaluated |
| SQL | `sql/week05_queries.sql` | Queries match hand-calculated answers |
| pandas | `01_lending_kpis.ipynb` | 3 KPIs + 1 chart |
| ML model | `credit-pd-model/` | AUC > 0.65 on holdout; README with metric |
| Explainability | SHAP notebook | Explain 1 approval + 1 decline |
| RAG | `policy-rag/` | Answers from docs only (no hallucination on eval) |
| LangGraph | `policy-copilot-agent/` | Escalates when confidence low |
| API | FastAPI `/ask` | curl returns JSON in <3s local |
| Docker | `docker compose up` | Health check passes |
| Governance | Guardrail module | Blocks PII in test prompts |

---

## Part 5 — Skill checkpoints (am I ready to move on?)

| Checkpoint | After | You must be able to… |
|---|---|---|
| **CP0** | Week 4 | Write 50-line script without googling syntax every line |
| **CP1** | Week 8 | SQL JOIN + pandas groupby without tutorial open |
| **CP2** | Week 16 | Train sklearn model, report AUC, explain 1 prediction |
| **CP3** | Week 24 | Build RAG that cites source chunk in answer |
| **CP4** | Week 32 | LangGraph agent with 2 tools + 30-question eval |
| **CP5** | Week 40 | Friend runs your API via Docker on their laptop |
| **CP6** | Week 48 | 30-min interview: explain one project business metric + tech stack |

**Do not skip checkpoints.** Jumping to LangGraph without Python = frustration and “PoC only” skills.

---

## Part 6 — First 7 days (concrete schedule)

| Day | Hours | Do exactly this |
|---|---|---|
| **D1** | 2 | Install Python, venv, Git; clone repo; run `week01` (expect fail) |
| **D2** | 2 | Python tutorial §1–2; print hello; variables |
| **D3** | 2 | §3 control flow; complete `brd_has_section()` TODO |
| **D4** | 1.5 | Complete `audit_brd()`; week01 passes |
| **D5** | 2 | §4 functions; add CLI arg for file path |
| **D6** | 2 | Read `docs/01-brd-template-en.md`; add 2 sections to MANDATORY list |
| **D7** | 1 | Git commit; write 5-line README in learning-lab |

---

## Part 7 — Folder structure (your GitHub repo)

```
banking-ai-learning/
├── README.md                 # Portfolio index (update monthly)
├── lab/                      # copy from curriculum/lab/
│   ├── data/
│   ├── exercises/
│   ├── sql/
│   └── notebooks/
├── credit-pd-model/          # month 4
├── policy-copilot-agent/     # month 8
└── policy-copilot-api/       # month 10
```

---

## Quick links in this repo

| Path | What |
|---|---|
| [lab/exercises/week01_brd_checklist.py](lab/exercises/week01_brd_checklist.py) | **Start here — Week 1** |
| [lab/exercises/week02_loan_rules.py](lab/exercises/week02_loan_rules.py) | Week 2 — rules engine |
| [lab/data/sample_loans.csv](lab/data/sample_loans.csv) | Practice loan data |
| [zero-to-ai-expert-syllabus.md](zero-to-ai-expert-syllabus.md) | 12-month timeline |
| [job-skills-adaptation.md](job-skills-adaptation.md) | Target banks & roles |

**Your next action:** open `week01_brd_checklist.py`, complete TODO 1, run it. That is Day 1 done.
