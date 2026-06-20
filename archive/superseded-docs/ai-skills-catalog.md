# AI Skills Catalog — Definition, Sources, Practice, Exercise

**Companion to:** `exports/AI-Skills-Learning-Slides.pptx`  
**Full detail (links, steps, answers):** **[ai-skills-workbook.md](ai-skills-workbook.md)** ← start here for exercises  
**Use with:** [reading-path.md](reading-path.md) · [learning-lab-guide.md](learning-lab-guide.md)

Each skill follows the **4-step loop**: Define → Read → Practice → Exercise → **Checkpoint** (pass before moving on).

---

## Skill 1 — Python Fundamentals (Weeks 1–4)

| | |
|---|---|
| **Definition** | Read, write, and debug Python programs: variables, control flow, functions, file I/O, JSON/CSV parsing. |
| **Primary sources** | [Python.org tutorial §1–6](https://docs.python.org/3/tutorial/) · [Kaggle Learn Python](https://www.kaggle.com/learn/python) · [Automate the Boring Stuff Ch 1–6](https://automatetheboringstuff.com/) |
| **Book (optional)** | *Python Crash Course* (Matthes) Part I |
| **Practice** | Type every example without copy-paste. One virtualenv per project. Run scripts from terminal daily. |
| **Exercise** | `lab/exercises/week01_brd_checklist.py` · `week02_loan_rules.py` |
| **Checkpoint** | Write a 50-line script without the tutorial open; parse a CSV; push to GitHub |

---

## Skill 2 — Git Version Control (Weeks 3–4)

| | |
|---|---|
| **Definition** | Track code history with clone, branch, commit, push — your portfolio is proof of learning. |
| **Primary sources** | [GitHub Git Handbook](https://guides.github.com/introduction/git-handbook/) · [Pro Git Ch 1–3](https://git-scm.com/book/en/v2) (free) |
| **Practice** | Commit after every study session. Use conventional messages: `feat(week02): loan DTI rule`. |
| **Exercise** | Initialize `banking-ai-learning` repo · 10+ commits · README weekly log |
| **Checkpoint** | `git log` shows progress; you can revert one bad commit; public GitHub repo exists |

---

## Skill 3 — SQL for Analytics (Weeks 5–7)

| | |
|---|---|
| **Definition** | Query relational data: SELECT, JOIN, GROUP BY, aggregates, basic window functions. |
| **Primary sources** | [SQLBolt lessons 1–18](https://sqlbolt.com/) · [Kaggle Learn SQL](https://www.kaggle.com/learn/intro-to-sql) |
| **Book (optional)** | *Learning SQL* (Beaulieu) Ch 1–10 |
| **Practice** | Rewrite each SQLBolt lesson from memory. Connect SQLite from Python. |
| **Exercise** | `lab/sql/week05_queries.sql` — branches, roll rates, vintage |
| **Checkpoint** | JOIN two tables; GROUP BY month; explain query in plain English to a colleague |

---

## Skill 4 — pandas Data Wrangling (Week 8)

| | |
|---|---|
| **Definition** | Load, clean, merge, and group credit data using Python DataFrames. |
| **Primary sources** | [Kaggle Learn Pandas](https://www.kaggle.com/learn/pandas) · [10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html) · Géron *Hands-On ML* Ch 2 |
| **Practice** | Compute the same KPI in SQL then pandas — results must match. |
| **Exercise** | Notebook `01_lending_kpis.ipynb` — disbursement, approval rate, segments |
| **Checkpoint** | `read_csv`, `groupby`, `merge` on `customer_id`; one matplotlib chart |

---

## Skill 5 — EDA & Statistics Intuition (Weeks 9–12)

| | |
|---|---|
| **Definition** | Explore data, spot patterns, write business insights — intuition over proofs. |
| **Primary sources** | [StatQuest YouTube](https://www.youtube.com/@statquest) (5–8 videos) · [Give Me Some Credit](https://www.kaggle.com/c/GiveMeSomeCredit/data) data description |
| **Book (optional)** | *Naked Statistics* (Wheelan) |
| **Practice** | Every chart answers one business question. Write insights in BRD language. |
| **Exercise** | Notebook `02_eda_credit.ipynb` — 3 insights: segment, missingness, correlation |
| **Checkpoint** | 3 written insights with numbers; understand time-based split; no data leakage |

---

## Skill 6 — Classical Machine Learning (Weeks 13–20)

| | |
|---|---|
| **Definition** | Train classifiers (logistic regression, trees, RF, XGBoost) for credit default / PD proxy. |
| **Primary sources** | [Kaggle Intro + Intermediate ML](https://www.kaggle.com/learn/intro-to-machine-learning) · [scikit-learn tutorials](https://scikit-learn.org/stable/tutorial/index.html) |
| **Book ★** | Géron *Hands-On Machine Learning* Part I — Ch 1–9 |
| **Practice** | Baseline first, then tune. Document train/val/test. Use `class_weight` for imbalance. |
| **Exercise** | Repo `credit-pd-model/` — train → evaluate → save `model.pkl` |
| **Checkpoint** | AUC reported; beat baseline; reproducible pipeline script |

---

## Skill 7 — Model Metrics & Evaluation (Weeks 19–20)

| | |
|---|---|
| **Definition** | Measure models: AUC, precision/recall, calibration, confusion matrix, KS/Gini. |
| **Primary sources** | scikit-learn metrics docs · Géron Ch 3 · StatQuest ROC / precision-recall videos |
| **Practice** | Link each metric to business trade-off: false decline vs false approve. |
| **Exercise** | Comparison table baseline vs tuned; pick threshold for 90% approval rate |
| **Checkpoint** | Explain one metric to a BA; plot ROC; state business metric in README |

---

## Skill 8 — SHAP Explainability (Weeks 21–22)

| | |
|---|---|
| **Definition** | Explain individual predictions — why approved/declined — for audit and regulators. |
| **Primary sources** | [SHAP intro notebook](https://shap.readthedocs.io/en/latest/example_notebooks/overviews/An%20introduction%20to%20explainable%20AI%20with%20Shapley%20values.html) · Géron Ch 6 · [governance-mlops.md](governance-mlops.md) |
| **Practice** | One SHAP plot + 3-sentence plain-English decline narrative for a synthetic customer. |
| **Exercise** | Add `shap_summary.png` + `decline_story.md` to `credit-pd-model` repo |
| **Checkpoint** | SHAP for one row; top 3 features named; no PII in examples |

---

## Skill 9 — Embeddings & Vector Search (Weeks 25–26)

| | |
|---|---|
| **Definition** | Convert text to vectors; similarity search over policy document chunks. |
| **Primary sources** | [Hugging Face NLP course Ch 1–3](https://huggingface.co/learn/nlp-course/chapter1/1) · LangChain embedding docs · [ChromaDB](https://docs.trychroma.com/) |
| **Practice** | Embed 20 policy sentences; retrieve top-3 similar; measure latency. |
| **Exercise** | `embed_policies.py` — index chunks in Chroma; query with similarity score |
| **Checkpoint** | Chunk + embed pipeline; retrieval returns relevant chunk; cite source text |

---

## Skill 10 — RAG Pipeline (Weeks 27–34)

| | |
|---|---|
| **Definition** | Retrieve relevant docs → augment prompt → generate grounded answer with citation. |
| **Primary sources** | [DL.AI LangChain for LLM Apps](https://www.deeplearning.ai/short-courses/langchain-for-llm-application-development/) · [LangChain RAG tutorial](https://python.langchain.com/docs/tutorials/rag/) |
| **Practice** | Build chunk → embed → retrieve → generate. Log retrieved sources on every call. |
| **Exercise** | Repo `policy-rag/` — CLI Q&A over PDF chunks with source paragraph |
| **Checkpoint** | Answer from docs not memory; 20-question golden set started; refuse if no context |

---

## Skill 11 — LangGraph Agents (Weeks 35–38)

| | |
|---|---|
| **Definition** | Stateful multi-step agent with tools, memory, and human escalation when confidence is low. |
| **Primary sources** | [DL.AI AI Agents in LangGraph](https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/) · [LangGraph quickstart](https://langchain-ai.github.io/langgraph/tutorials/introduction/) |
| **Practice** | Tools: `policy_lookup`, `calculator`, `escalate_human`. Draw state diagram. |
| **Exercise** | Repo `policy-copilot-agent/` — LangGraph + 3 tools · architecture diagram |
| **Checkpoint** | Multi-step trace visible; escalation works; 5-min demo video |

---

## Skill 12 — LLM APIs & Structured Output (Weeks 31–32)

| | |
|---|---|
| **Definition** | Call Claude/OpenAI API; JSON schema output; system prompts; tool/function calling. |
| **Primary sources** | [Anthropic API docs](https://docs.anthropic.com/) · Anthropic prompt engineering guide |
| **Practice** | Extract structured fields from policy text using JSON schema validation. |
| **Exercise** | `extract_policy_fields.py` — paragraph → `{product, limit, dti_max}` |
| **Checkpoint** | API key in `.env` not code; valid JSON; graceful API error handling |

---

## Skill 13 — Eval Harness / LLMOps (Weeks 37–38)

| | |
|---|---|
| **Definition** | Golden Q&A set; measure grounded-response rate; catch regressions before production. |
| **Primary sources** | [ragas docs](https://docs.ragas.io/) · [governance-mlops.md](governance-mlops.md) · Anthropic eval best practices |
| **Practice** | 30–50 questions with expected sources. Score citation match + keyword overlap. |
| **Exercise** | `eval/golden.json` + `run_eval.py` — report % grounded; target ≥ 90% |
| **Checkpoint** | Automated eval script; score in README; CI fails if score drops |

---

## Skill 14 — FastAPI Production API (Weeks 39–40)

| | |
|---|---|
| **Definition** | REST API wrapping copilot: `/ask` endpoint, request validation, health check. |
| **Primary sources** | [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/) (first 5 sections) · Made With ML serving module |
| **Practice** | `POST /ask {question}` → `{answer, sources, confidence}`. OpenAPI at `/docs`. |
| **Exercise** | `policy-copilot-api/main.py` — uvicorn · curl test · pytest for `/health` |
| **Checkpoint** | API returns JSON; input validation; no secrets in logs |

---

## Skill 15 — Docker & Container Deploy (Weeks 41–42)

| | |
|---|---|
| **Definition** | Package app and dependencies; one-command deploy; reproducible environment. |
| **Primary sources** | [Docker Get Started](https://docs.docker.com/get-started/) · FastAPI in Docker docs |
| **Practice** | Dockerfile + docker-compose.yml; `.dockerignore`; env via `env_file` not `COPY .env`. |
| **Exercise** | `docker compose up` — API on localhost; document in README |
| **Checkpoint** | Another machine can run it; compose has api + optional chroma; healthcheck works |

---

## Skill 16 — Guardrails & Responsible AI (Weeks 43–44)

| | |
|---|---|
| **Definition** | PII redaction, policy blocks, audit trail, human escalation, risk tiers. |
| **Primary sources** | [governance-mlops.md](governance-mlops.md) (full) · Anthropic safety docs |
| **Practice** | Block national-ID patterns in logs. Escalate if confidence below threshold. |
| **Exercise** | `guardrails.py` — input/output filter · redacted `audit.log` · `model_card.md` |
| **Checkpoint** | PII never in logs; 3 governance gates documented; explain to auditor |

---

## Skill 17 — CI/CD & Eval Loop (Weeks 43–44)

| | |
|---|---|
| **Definition** | GitHub Actions: lint, test, eval on push — harness engineering for agents. |
| **Primary sources** | GitHub Actions Python workflow · Made With ML CI patterns |
| **Practice** | Nightly eval job. Separate verifier prompt grades agent output. |
| **Exercise** | `.github/workflows/ci.yml` — pytest + eval threshold · badge in README |
| **Checkpoint** | CI green on push; eval fails if grounded rate < 85%; postmortem template ready |

---

## Skill 18 — Banking AI Use Cases (Weeks 47–50)

| | |
|---|---|
| **Definition** | Map AI to CIR, TAT, NPL: policy copilot, AML triage, doc OCR, PD model. |
| **Primary sources** | `examples/04a-brd-pos-lending.md` · [job-skills-adaptation.md](job-skills-adaptation.md) |
| **Practice** | One-page value case: problem → baseline → target → measurement (BRD Section C). |
| **Exercise** | Second use case: AML triage agent OR doc classifier with one quantified metric |
| **Checkpoint** | Business metric in VND or bps; BRD-style problem statement; STAR story ready |

---

## Skill 19 — Portfolio & Interview Ready (Weeks 51–52)

| | |
|---|---|
| **Definition** | GitHub portfolio, English demo, CV, STAR stories — prove you can do the work. |
| **Primary sources** | [cv-cover-letter.md](cv-cover-letter.md) · [interview-kit.md](interview-kit.md) · [anthropic-career-adaptation.md](anthropic-career-adaptation.md) |
| **Practice** | 5-min demo video · architecture diagram · 90-second exec pitch. |
| **Exercise** | Update CV · apply OCB/NAB/Anthropic · 5 STAR stories |
| **Checkpoint** | 2 GitHub repos live; hire checklist complete; mock interview done |

---

## Regenerate slides

```bash
python3 curriculum/generate_ai_skills_slides.py
```

Output: `curriculum/exports/AI-Skills-Learning-Slides.pptx` (23 slides)
