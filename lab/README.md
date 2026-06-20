# Learning Lab — 52 weeks, runnable code

All exercises are **generated from** `curriculum/learning_data.py` via:

```bash
python3 curriculum/generate_all_weeks.py      # lab code only
python3 curriculum/generate_all_learning.py   # JSON + lab + all slide decks
```

## Setup (once)

```bash
cd curriculum/learning-lab
python3 --version          # 3.11+
python3 -m pip install -r requirements.txt
python3 setup_db.py        # SQLite for weeks 5–7
```

## Quick smoke test

```bash
python3 exercises/week01_brd_checklist.py --app-sample
python3 exercises/week02_loan_rules.py
python3 exercises/week25_rag_cli.py "Max DTI?"
python3 exercises/week32_run_eval.py
python3 projects/credit-pd-model/train.py
cd projects/week33_fastapi && python3 -m pytest test_health.py
```

## Week map

| Weeks | Focus | Key files |
|-------|-------|-----------|
| 1–4 | Python + Git | `exercises/week01`–`week04`, `week04_git_log.sh` |
| 5–7 | SQL | `sql/week05`–`week07`, `loans.db` |
| 8–11 | pandas / EDA | `week08_lending_kpis.py`, `week09_eda.py`, `notebooks/` |
| 12–20 | ML + SHAP | `week12_train_test.py`, `projects/credit-pd-model/` |
| 21–24 | NLP | `week21_embed.py`, `week22_chunk_policy.py`, `week24_doc_classifier.py` |
| 25–32 | RAG + agents | `week25_rag_cli.py`, `week26_persist_index.py`, `week32_run_eval.py` |
| 33–40 | Production | `projects/week33_fastapi/`, Docker, CI, `week37_guardrails.py` |
| 41–52 | Career | `week41_value_case.md`, `week45_portfolio_checklist.md`, `PORTFOLIO.md` |

Full index: [WEEKS.md](WEEKS.md)

## Learning app (browser)

```bash
cd curriculum/learning-app && python3 -m http.server 8081
# http://localhost:8081 — week-by-week UI, progress saved locally
```

See [learning-app/README.md](../learning-app/README.md).

## Shared libraries

- `lib/brd_utils.py` — BRD audit, weighted score, scorecard
- `lib/loan_utils.py` — loan rule engine
- `lib/rag_simple.py` — TF-IDF RAG (no API keys)

## Solutions (optional peek)

`exercises/solutions/` — week 1–2 reference implementations.
