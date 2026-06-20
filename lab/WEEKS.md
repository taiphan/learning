# 52-Week Learning Index

Edit `curriculum/learning_data.py` — regenerate with scaffold.

| Week | Phase | Title | Exercise | Run |
|------|-------|-------|----------|-----|
| 1 | foundation | Python syntax — BRD audit | `lab/exercises/week01_brd_checklist.py` | `python3 week01_brd_checklist.py --app-sample` |
| 2 | foundation | Functions & CSV loan rules | `lab/exercises/week02_loan_rules.py` | `python3 week02_loan_rules.py` |
| 3 | foundation | Dicts & weighted BRD score | `lab/exercises/week03_brd_weighted_score.py` | `python3 week03_brd_weighted_score.py` |
| 4 | foundation | OOP scorecard + Git | `lab/exercises/week04_brd_scorecard.py` | `python3 week04_brd_scorecard.py` |
| 5 | foundation | SQL aggregates & filters | `lab/sql/week05_queries.sql` | `sqlite3 loans.db < sql/week05_queries.sql` |
| 6 | foundation | SQL JOINs | `lab/sql/week06_join.sql` | `Run join on customers + applications` |
| 7 | foundation | SQL windows & trends | `lab/sql/week07_window.sql` | `Monthly disbursement trend query` |
| 8 | foundation | pandas KPIs | `lab/notebooks/01_lending_kpis.ipynb` | `jupyter notebook 01_lending_kpis.ipynb` |
| 9 | ml | Load credit dataset | `lab/notebooks/02_eda_credit.ipynb` | `Start EDA notebook` |
| 10 | ml | EDA histograms & missing | `lab/notebooks/02_eda_credit.ipynb` | `Complete missing-value analysis` |
| 11 | ml | Business insights write-up | `lab/notebooks/02_eda_credit.ipynb` | `Write 3 insights in BRD language` |
| 12 | ml | Train/test split — no leakage | `lab/exercises/week12_train_test.py` | `python3 week12_train_test.py` |
| 13 | ml | Logistic regression baseline | `lab/projects/credit-pd-model/train.py` | `python3 projects/credit-pd-model/train.py` |
| 14 | ml | Random Forest tune | `lab/projects/credit-pd-model/train.py` | `Beat baseline AUC` |
| 15 | ml | XGBoost + imbalance | `lab/projects/credit-pd-model/train.py` | `class_weight or scale_pos_weight` |
| 16 | ml | Model README + metric | `lab/projects/credit-pd-model/README.md` | `Document AUC + decision use` |
| 17 | ml | ROC & threshold | `lab/exercises/week17_metrics.py` | `python3 week17_metrics.py` |
| 18 | ml | Precision/recall trade-off | `lab/exercises/week17_metrics.py` | `Threshold for 90% approval rate` |
| 19 | ml | Calibration intuition | `lab/exercises/week17_metrics.py` | `Reliability sketch` |
| 20 | ml | SHAP explainability | `lab/exercises/week20_shap.py` | `python3 week20_shap.py` |
| 21 | nlp | Sentence embeddings | `lab/exercises/week21_embed.py` | `python3 week21_embed.py` |
| 22 | nlp | Chunk policy text | `lab/data/sample_policy.txt` | `Chunk into 500-token pieces` |
| 23 | nlp | Cosine similarity search | `lab/exercises/week21_embed.py` | `Query latency measured` |
| 24 | nlp | Document classifier | `lab/exercises/week24_doc_classifier.py` | `python3 week24_doc_classifier.py` |
| 25 | genai | LangChain RAG quickstart | `lab/exercises/week25_rag_cli.py` | `python3 week25_rag_cli.py` |
| 26 | genai | Chroma vector store | `lab/exercises/week25_rag_cli.py` | `Persist index to ./chroma_db` |
| 27 | genai | PDF / markdown loader | `lab/projects/policy-rag/` | `Index examples/04a-brd-pos-lending.md` |
| 28 | genai | Refusal without context | `lab/projects/policy-rag/` | `Return escalate if no chunk` |
| 29 | genai | LLM structured JSON | `lab/exercises/week29_structured_llm.py` | `Extract policy fields to JSON` |
| 30 | genai | LangGraph intro | `lab/exercises/week30_langgraph.py` | `python3 week30_langgraph.py` |
| 31 | genai | Agent tools | `lab/projects/policy-copilot-agent/` | `3 tools: lookup, calc, escalate` |
| 32 | genai | Eval harness ≥85% | `lab/data/eval_questions.json` | `python3 week32_run_eval.py` |
| 33 | production | FastAPI /ask endpoint | `lab/projects/week33_fastapi/main.py` | `uvicorn main:app --reload` |
| 34 | production | Pydantic validation | `lab/projects/week33_fastapi/main.py` | `pytest test_health.py` |
| 35 | production | Dockerfile | `lab/projects/week35_docker/Dockerfile` | `docker build -t copilot .` |
| 36 | production | docker compose up | `lab/projects/week35_docker/docker-compose.yml` | `docker compose up` |
| 37 | production | PII guardrails | `lab/exercises/week37_guardrails.py` | `python3 week37_guardrails.py` |
| 38 | production | Model card | `lab/projects/model_card.md` | `Fill purpose, limits, risks` |
| 39 | production | GitHub Actions CI | `lab/projects/week39_ci/.github/workflows/ci.yml` | `Push triggers pytest + eval` |
| 40 | production | Eval gate in CI | `lab/projects/week39_ci/` | `Fail if grounded < 85%` |
| 41 | career | Second use case BRD | `lab/exercises/week41_value_case.md` | `Fill value case template` |
| 42 | career | AML triage OR doc OCR story | `lab/projects/use-case-2/README.md` | `Pick and scope use case` |
| 43 | career | Portfolio README | `lab/projects/PORTFOLIO.md` | `Link all repos + metrics` |
| 44 | career | Architecture diagram | `lab/projects/PORTFOLIO.md` | `Copilot architecture diagram` |
| 45 | career | CV update | `curriculum/cv-cover-letter.md` | `Fill real project metrics` |
| 46 | career | Apply OCB / NAB / VPBank | `curriculum/interview-kit.md` | `Submit 3 applications` |
| 47 | career | STAR stories ×5 | `lab/exercises/week47_star_stories.md` | `Write 5 STAR stories` |
| 48 | career | Mock interview | `lab/exercises/week47_star_stories.md` | `45-min mock with peer` |
| 49 | career | Demo video 5 min | `lab/projects/PORTFOLIO.md` | `English demo of copilot` |
| 50 | career | Anthropic stretch research | `curriculum/anthropic-career-adaptation.md` | `Map skills to Claude roles` |
| 51 | career | Review weak weeks | `learning-data.json + workbook` | `Fix lowest eval score week` |
| 52 | career | Graduation checklist | `lab/WEEKS.md` | `Verify 2 repos + CV + apply` |

## Checkpoints

- **CP0** after week 4: Write 50-line script without googling every line
- **CP1** after week 8: SQL JOIN + pandas groupby without tutorial
- **CP2** after week 16: Train model, report AUC, explain one prediction
- **CP3** after week 24: RAG cites source chunk in answer
- **CP4** after week 32: LangGraph agent + 30-question eval ≥85%
- **CP5** after week 40: Friend runs your Docker API on their laptop
- **CP6** after week 48: 30-min interview: business metric + tech stack
