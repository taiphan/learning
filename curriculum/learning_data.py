"""Single source of truth for AI learning curriculum — weeks, skills, links, slides."""

from __future__ import annotations

# Phase ids → anthropic_theme color keys (resolved in learning_loader)
# Y1 quarters align with career arc; post-Y1 path in CAREER_PATH
PHASES = [
    {
        "id": "y1q1",
        "name": "Y1 Q1 — Technologist",
        "color": "CLAY",
        "weeks": "1–12",
        "months": "1–3",
        "theme": "Python · Git · SQL · pandas · ML start",
        "career_year": 1,
        "career_quarter": 1,
        "career_gate": "Ship code + BRD bridge",
        "apply_target": None,
        "track_b": "H0 @ W8",
    },
    {
        "id": "y1q2",
        "name": "Y1 Q2 — ML hire signal",
        "color": "SKY",
        "weeks": "13–24",
        "months": "4–6",
        "theme": "PD model · metrics · SHAP · NLP · RAG start",
        "career_year": 1,
        "career_quarter": 2,
        "career_gate": "Portfolio piece 1 (classical ML)",
        "apply_target": None,
        "track_b": "H1 @ W16",
    },
    {
        "id": "y1q3",
        "name": "Y1 Q3 — GenAI production",
        "color": "FIG",
        "weeks": "25–36",
        "months": "7–9",
        "theme": "RAG · agents · FastAPI · Docker · CI",
        "career_year": 1,
        "career_quarter": 3,
        "career_gate": "Portfolio piece 2 (GenAI + API)",
        "apply_target": None,
        "track_b": "H2 @ W28",
    },
    {
        "id": "y1q4",
        "name": "Y1 Q4 — Apply",
        "color": "OLIVE",
        "weeks": "37–52",
        "months": "10–12",
        "theme": "Production gate · use case 2 · CV · interview",
        "career_year": 1,
        "career_quarter": 4,
        "career_gate": "Apply AI Engineer (VN banks)",
        "apply_target": "OCB · NAB · VPBank AI Engineer / Senior BA",
        "track_b": "H3 @ W40 · H4 @ W52",
    },
]

# Post–Year-1 career arc (study path ends at Y1 Q4; Y2–Y4 = on-the-job)
CAREER_PATH = [
    {
        "year": 1,
        "label": "Dual track (this repo)",
        "weeks": "1–52",
        "hours_per_week": 10,
        "role_target": "Graduate → apply AI Engineer",
        "deliverable": "2 portfolio repos + Track B H0–H4 + CP0–CP6",
        "quarters": ["y1q1", "y1q2", "y1q3", "y1q4"],
    },
    {
        "year": 2,
        "label": "AI Engineer",
        "weeks": "—",
        "hours_per_week": "40 (job)",
        "role_target": "OCB / NAB / VPBank AI Engineer",
        "deliverable": "2–3 production use cases with measured KPI",
        "quarters": [],
    },
    {
        "year": 3,
        "label": "Tech Lead / AI Product",
        "weeks": "—",
        "role_target": "Lead squad of 3–5",
        "deliverable": "Roadmap + hiring loop + stakeholder mgmt",
        "quarters": [],
    },
    {
        "year": 4,
        "label": "Head of AI Factory",
        "weeks": "—",
        "role_target": "Strategy + team + P&L",
        "deliverable": "Factory operating model · subsidiary rollout",
        "quarters": [],
    },
]

PHASE_CAREER = {p["id"]: p for p in PHASES}

CHECKPOINTS = [
    {"id": "CP0", "after_week": 4, "label": "Write 50-line script without googling every line", "career_quarter": "y1q1"},
    {"id": "CP1", "after_week": 8, "label": "SQL JOIN + pandas groupby without tutorial", "career_quarter": "y1q1"},
    {"id": "CP2", "after_week": 16, "label": "Train model, report AUC, explain one prediction", "career_quarter": "y1q2"},
    {"id": "CP3", "after_week": 24, "label": "RAG cites source chunk in answer", "career_quarter": "y1q2"},
    {"id": "CP4", "after_week": 32, "label": "LangGraph agent + 30-question eval ≥85%", "career_quarter": "y1q3"},
    {"id": "CP5", "after_week": 40, "label": "Friend runs your Docker API on their laptop", "career_quarter": "y1q4"},
    {"id": "CP6", "after_week": 48, "label": "30-min interview: business metric + tech stack", "career_quarter": "y1q4"},
]

# Track B — Head of AI Factory (2 hrs/week alongside technical track)
TRACK_B_CHECKPOINTS = [
    {"id": "H0", "after_week": 8, "label": "AI strategy on one page (5 pillars)", "career_quarter": "y1q1"},
    {"id": "H1", "after_week": 16, "label": "PD model value case with VND/bps metric", "career_quarter": "y1q2"},
    {"id": "H2", "after_week": 28, "label": "Policy copilot G1/G2/G3 governance checklist", "career_quarter": "y1q3"},
    {"id": "H3", "after_week": 40, "label": "90-day AI Factory pilot plan", "career_quarter": "y1q4"},
    {"id": "H4", "after_week": 52, "label": "5-slide steering deck + portfolio narrative", "career_quarter": "y1q4"},
]

TRACK_B_WEEKS = [8, 16, 28, 40, 52]

SKILLS = [
    {
        "id": 1,
        "name": "Python Fundamentals",
        "weeks": "1–4",
        "color": "CLAY",
        "definition": "Read, write, debug Python: variables, loops, functions, files, JSON/CSV.",
        "sources": "★ Python.org §1–6 · Kaggle Learn Python · Automate the Boring Stuff Ch 1–6",
        "practice": "Type every example. One venv per project. Run scripts from CLI daily.",
        "exercise": "week01_brd_checklist.py · week02_loan_rules.py · week03 · week04",
        "checkpoint": "✓ 50-line script · ✓ parse CSV · ✓ GitHub commit",
        "resource_urls": [
            ("Python tutorial", "https://docs.python.org/3/tutorial/"),
            ("Kaggle Python", "https://www.kaggle.com/learn/python"),
        ],
    },
    {
        "id": 2,
        "name": "Git Version Control",
        "weeks": "3–4",
        "color": "SKY",
        "definition": "Track code history: clone, branch, commit, push.",
        "sources": "★ GitHub Git Handbook · Pro Git Ch 1–3",
        "practice": "Commit after every session. Conventional messages.",
        "exercise": "week04_git_log.sh · banking-ai-learning repo",
        "checkpoint": "✓ public repo · ✓ 10+ commits",
        "resource_urls": [("Git Handbook", "https://guides.github.com/introduction/git-handbook/")],
    },
    {
        "id": 3,
        "name": "SQL for Analytics",
        "weeks": "5–7",
        "color": "CACTUS",
        "definition": "SELECT, JOIN, GROUP BY, window functions.",
        "sources": "★ SQLBolt 1–18 · Kaggle SQL",
        "practice": "Rewrite each lesson from memory.",
        "exercise": "sql/week05–07_queries.sql",
        "checkpoint": "✓ JOIN · ✓ GROUP BY month",
        "resource_urls": [
            ("SQLBolt", "https://sqlbolt.com/"),
            ("Kaggle SQL", "https://www.kaggle.com/learn/intro-to-sql"),
        ],
    },
    {
        "id": 4,
        "name": "pandas Data Wrangling",
        "weeks": "8",
        "color": "OLIVE",
        "definition": "Load, clean, merge, group credit data.",
        "sources": "★ Kaggle Pandas · 10 minutes to pandas",
        "practice": "Same KPI in SQL then pandas — must match.",
        "exercise": "notebooks/01_lending_kpis.ipynb",
        "checkpoint": "✓ read_csv · groupby · chart",
        "resource_urls": [("Kaggle Pandas", "https://www.kaggle.com/learn/pandas")],
    },
    {
        "id": 5,
        "name": "EDA & Statistics",
        "weeks": "9–12",
        "color": "FIG",
        "definition": "Explore data; business insights in BRD language.",
        "sources": "★ StatQuest · Give Me Some Credit dataset",
        "practice": "Every chart answers one business question.",
        "exercise": "notebooks/02_eda_credit.ipynb",
        "checkpoint": "✓ 3 insights · ✓ no leakage",
        "resource_urls": [("StatQuest", "https://www.youtube.com/@statquest")],
    },
    {
        "id": 6,
        "name": "Classical ML",
        "weeks": "13–16",
        "color": "SKY",
        "definition": "Train classifiers for credit default / PD proxy.",
        "sources": "★ Kaggle ML · sklearn · Géron Ch 1–9",
        "practice": "Baseline first; time-based split.",
        "exercise": "projects/credit-pd-model/",
        "checkpoint": "✓ AUC · beat baseline",
        "resource_urls": [("Kaggle Intro ML", "https://www.kaggle.com/learn/intro-to-machine-learning")],
    },
    {
        "id": 7,
        "name": "Metrics & SHAP",
        "weeks": "17–20",
        "color": "CLAY",
        "definition": "AUC, thresholds, SHAP explainability.",
        "sources": "★ sklearn metrics · SHAP docs",
        "practice": "Link metrics to false decline vs false approve.",
        "exercise": "week17_metrics.py · week20_shap.py",
        "checkpoint": "✓ ROC plot · decline story",
        "resource_urls": [("SHAP", "https://shap.readthedocs.io/")],
    },
    {
        "id": 8,
        "name": "Embeddings & NLP",
        "weeks": "21–24",
        "color": "CACTUS",
        "definition": "Text vectors, similarity, doc classification.",
        "sources": "★ HF NLP Ch 1–3 · LangChain embeddings",
        "practice": "Embed policy sentences; top-3 similar.",
        "exercise": "week21_embed.py · week24_doc_classifier.py",
        "checkpoint": "✓ chunk pipeline · classifier accuracy",
        "resource_urls": [("HF NLP", "https://huggingface.co/learn/nlp-course/chapter1/1")],
    },
    {
        "id": 9,
        "name": "RAG Pipeline",
        "weeks": "25–28",
        "color": "FIG",
        "definition": "Retrieve → augment → generate with citation.",
        "sources": "★ DL.AI LangChain · LangChain RAG tutorial",
        "practice": "Log sources every call.",
        "exercise": "week25_rag_cli.py · projects/policy-rag/",
        "checkpoint": "✓ grounded answer · refusal if no context",
        "resource_urls": [("LangChain RAG", "https://python.langchain.com/docs/tutorials/rag/")],
    },
    {
        "id": 10,
        "name": "LangGraph Agents",
        "weeks": "29–32",
        "color": "CLAY",
        "definition": "Stateful agent, tools, escalation.",
        "sources": "★ DL.AI LangGraph · LangGraph docs",
        "practice": "policy_lookup · escalate_human tools.",
        "exercise": "week29_agent.py · projects/policy-copilot-agent/",
        "checkpoint": "✓ eval ≥85% grounded",
        "resource_urls": [("DL.AI LangGraph", "https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/")],
    },
    {
        "id": 11,
        "name": "Production API",
        "weeks": "33–36",
        "color": "CACTUS",
        "definition": "FastAPI, Docker, health checks.",
        "sources": "★ FastAPI tutorial · Docker get-started",
        "practice": "POST /ask → JSON; docker compose up.",
        "exercise": "week33_fastapi/ · week35_docker/",
        "checkpoint": "✓ curl works · another machine runs it",
        "resource_urls": [("FastAPI", "https://fastapi.tiangolo.com/tutorial/")],
    },
    {
        "id": 12,
        "name": "Guardrails & CI",
        "weeks": "37–40",
        "color": "SKY",
        "definition": "PII redaction, eval in CI, governance gates.",
        "sources": "★ governance-mlops.md · ragas · GitHub Actions",
        "practice": "CI fails if eval score drops.",
        "exercise": "week37_guardrails.py · week39_ci/",
        "checkpoint": "✓ PII blocked · green CI",
        "resource_urls": [("ragas", "https://docs.ragas.io/")],
    },
    {
        "id": 13,
        "name": "Banking Use Cases",
        "weeks": "41–44",
        "color": "OLIVE",
        "definition": "Map AI to CIR, TAT, NPL; second use case.",
        "sources": "★ examples/04a-brd · job-skills-adaptation.md",
        "practice": "One-page value case with VND metric.",
        "exercise": "week41_value_case.md",
        "checkpoint": "✓ BRD problem · quantified metric",
        "resource_urls": [],
    },
    {
        "id": 14,
        "name": "Portfolio & Interview",
        "weeks": "45–52",
        "color": "FIG",
        "definition": "CV, demo video, STAR stories, apply.",
        "sources": "★ cv-templates.md · job-skills-adaptation.md",
        "practice": "5-min demo · 5 STAR stories.",
        "exercise": "week45_portfolio_checklist.md",
        "checkpoint": "✓ 2 repos · mock interview done",
        "resource_urls": [],
    },
]

# fmt: off — 52-week curriculum (single data source)
_W = lambda **k: k  # week record builder

def _build_weeks() -> list[dict]:
    items: list[dict] = []

    def add(
        n: int,
        title: str,
        phase: str,
        skill_id: int,
        study: str,
        exercise: str,
        run: str,
        deliverable: str,
        urls: list[tuple[str, str]] | None = None,
        checkpoint: str | None = None,
        track_b: dict | None = None,
    ):
        record = {
                "week": n,
                "title": title,
                "phase": phase,
                "skill_id": skill_id,
                "month": (n - 1) // 4 + 1,
                "career_year": PHASE_CAREER[phase]["career_year"],
                "career_quarter": PHASE_CAREER[phase]["career_quarter"],
                "career_gate": PHASE_CAREER[phase]["career_gate"],
                "study": study,
                "exercise": exercise,
                "run": run,
                "deliverable": deliverable,
                "resource_urls": urls or [],
                "checkpoint": checkpoint,
            }
        if track_b:
            record["track_b"] = track_b
        items.append(record)

    # Month 1 — Python
    add(1, "Python syntax — BRD audit", "y1q1", 1,
        "Python.org §1–4; Kaggle Python L1–3",
        "lab/exercises/week01_brd_checklist.py",
        "python3 week01_brd_checklist.py --app-sample",
        "Lists missing BRD sections",
        [("Python tutorial", "https://docs.python.org/3/tutorial/")])
    add(2, "Functions & CSV loan rules", "y1q1", 1,
        "§5–6; read docs/01-brd-template-en.md",
        "lab/exercises/week02_loan_rules.py",
        "python3 week02_loan_rules.py",
        "10 loans pass/fail correctly")
    add(3, "Dicts & weighted BRD score", "y1q1", 1,
        "Lists, dicts, JSON; docs/05 quality rubric",
        "lab/exercises/week03_brd_weighted_score.py",
        "python3 week03_brd_weighted_score.py",
        "Weighted score % printed")
    add(4, "OOP scorecard + Git", "y1q1", 2,
        "Classes basics; Git commit/push",
        "lab/exercises/week04_brd_scorecard.py",
        "python3 week04_brd_scorecard.py",
        "BRDScorecard class + GitHub repo", checkpoint="CP0")

    # Month 2 — SQL + pandas
    add(5, "SQL aggregates & filters", "y1q1", 3,
        "SQLBolt 1–6",
        "lab/sql/week05_queries.sql",
        "sqlite3 loans.db < sql/week05_queries.sql",
        "5 queries documented")
    add(6, "SQL JOINs", "y1q1", 3,
        "SQLBolt 7–12",
        "lab/sql/week06_join.sql",
        "Run join on customers + applications",
        "Join returns correct rows")
    add(7, "SQL windows & trends", "y1q1", 3,
        "SQLBolt 13–18",
        "lab/sql/week07_window.sql",
        "Monthly disbursement trend query",
        "Window function KPI")
    add(8, "pandas KPIs", "y1q1", 4,
        "Kaggle Pandas L1–4",
        "lab/notebooks/01_lending_kpis.ipynb",
        "jupyter notebook 01_lending_kpis.ipynb",
        "3 KPIs + 1 chart", checkpoint="CP1",
        track_b={
            "hours": 2,
            "title": "AI Factory strategy (1 page)",
            "study": "archive/head-of-ai-factory/strategy-and-roadmap.md §1–2",
            "template": "curriculum/templates/hoai/week08_ai_strategy.md",
            "action": "Complete strategy template for consumer finance scenario",
            "deliverable": "One-page AI strategy — 5 pillars + operating model sketch",
            "hoai_checkpoint": "H0",
        })

    # Months 3–4 — ML
    add(9, "Load credit dataset", "y1q1", 5,
        "Kaggle Give Me Some Credit description",
        "lab/notebooks/02_eda_credit.ipynb",
        "Start EDA notebook",
        "Dataset loaded; shape printed")
    add(10, "EDA histograms & missing", "y1q1", 5,
        "StatQuest stats fundamentals (3 videos)",
        "lab/notebooks/02_eda_credit.ipynb",
        "Complete missing-value analysis",
        "2 charts with captions")
    add(11, "Business insights write-up", "y1q1", 5,
        "StatQuest ML intro",
        "lab/notebooks/02_eda_credit.ipynb",
        "Write 3 insights in BRD language",
        "insights.md in notebook")
    add(12, "Train/test split — no leakage", "y1q1", 6,
        "Kaggle Intro ML L1–3",
        "lab/exercises/week12_train_test.py",
        "python3 week12_train_test.py",
        "Time-based split documented")
    add(13, "Logistic regression baseline", "y1q2", 6,
        "Kaggle Intro ML L4–7",
        "lab/projects/credit-pd-model/train.py",
        "python3 projects/credit-pd-model/train.py",
        "Baseline AUC printed")
    add(14, "Random Forest tune", "y1q2", 6,
        "Kaggle Intermediate ML",
        "lab/projects/credit-pd-model/train.py",
        "Beat baseline AUC",
        "Comparison table in README")
    add(15, "XGBoost + imbalance", "y1q2", 6,
        "XGBoost docs; class_weight",
        "lab/projects/credit-pd-model/train.py",
        "class_weight or scale_pos_weight",
        "README business metric")
    add(16, "Model README + metric", "y1q2", 6,
        "Géron Ch 3 metrics",
        "lab/projects/credit-pd-model/README.md",
        "Document AUC + decision use",
        "Repo public on GitHub", checkpoint="CP2",
        track_b={
            "hours": 2,
            "title": "PD model value case",
            "study": "archive/head-of-ai-factory/strategy-and-roadmap.md §7; credit-pd-model README",
            "template": "curriculum/templates/hoai/week16_pd_value_case.md",
            "action": "Quantify NPL/false-decline impact in VND or bps",
            "deliverable": "1-page value case linked to model README",
            "hoai_checkpoint": "H1",
        })
    add(17, "ROC & threshold", "y1q2", 7,
        "sklearn metrics; StatQuest ROC",
        "lab/exercises/week17_metrics.py",
        "python3 week17_metrics.py",
        "ROC plot saved")
    add(18, "Precision/recall trade-off", "y1q2", 7,
        "StatQuest precision-recall",
        "lab/exercises/week17_metrics.py",
        "Threshold for 90% approval rate",
        "Table in README")
    add(19, "Calibration intuition", "y1q2", 7,
        "Géron calibration concept",
        "lab/exercises/week17_metrics.py",
        "Reliability sketch",
        "1 paragraph for BA audience")
    add(20, "SHAP explainability", "y1q2", 7,
        "SHAP intro notebook",
        "lab/exercises/week20_shap.py",
        "python3 week20_shap.py",
        "decline_story.md + plot")

    # Months 5–6 — NLP
    add(21, "Sentence embeddings", "y1q2", 8,
        "HF NLP Ch 1–2",
        "lab/exercises/week21_embed.py",
        "python3 week21_embed.py",
        "Top-3 similar policy lines")
    add(22, "Chunk policy text", "y1q2", 8,
        "HF NLP Ch 3",
        "lab/data/sample_policy.txt",
        "Chunk into 500-token pieces",
        "chunk manifest JSON")
    add(23, "Cosine similarity search", "y1q2", 8,
        "LangChain embedding docs",
        "lab/exercises/week21_embed.py",
        "Query latency measured",
        "Sub-200ms local benchmark")
    add(24, "Document classifier", "y1q2", 8,
        "Text classification sklearn",
        "lab/exercises/week24_doc_classifier.py",
        "python3 week24_doc_classifier.py",
        "80%+ on tiny test set", checkpoint="CP3")

    # Months 7–8 — GenAI
    add(25, "LangChain RAG quickstart", "y1q3", 9,
        "DL.AI LangChain short course",
        "lab/exercises/week25_rag_cli.py",
        "python3 week25_rag_cli.py",
        "One Q&A with source cite")
    add(26, "Chroma vector store", "y1q3", 9,
        "ChromaDB docs",
        "lab/exercises/week25_rag_cli.py",
        "Persist index to ./chroma_db",
        "Reload index works")
    add(27, "PDF / markdown loader", "y1q3", 9,
        "LangChain document loaders",
        "lab/projects/policy-rag/",
        "Index examples/04a-brd-pos-lending.md",
        "CLI over repo BRD")
    add(28, "Refusal without context", "y1q3", 9,
        "RAG eval patterns",
        "lab/projects/policy-rag/",
        "Return escalate if no chunk",
        "10-question golden set started",
        track_b={
            "hours": 2,
            "title": "Copilot governance gates",
            "study": "curriculum/governance-mlops.md §1–3 risk tiering",
            "template": "curriculum/templates/hoai/week28_copilot_governance.md",
            "action": "Set risk tier + G1/G2/G3 pass criteria for policy copilot",
            "deliverable": "Governance checklist with named owners",
            "hoai_checkpoint": "H2",
        })
    add(29, "LLM structured JSON", "y1q3", 10,
        "Anthropic API docs",
        "lab/exercises/week29_structured_llm.py",
        "Extract policy fields to JSON",
        "Valid schema output")
    add(30, "LangGraph intro", "y1q3", 10,
        "DL.AI LangGraph course",
        "lab/exercises/week30_langgraph.py",
        "python3 week30_langgraph.py",
        "State diagram in README")
    add(31, "Agent tools", "y1q3", 10,
        "LangGraph tool calling",
        "lab/projects/policy-copilot-agent/",
        "3 tools: lookup, calc, escalate",
        "Multi-step trace logged")
    add(32, "Eval harness ≥85%", "y1q3", 10,
        "ragas; data/eval_questions.json",
        "lab/data/eval_questions.json",
        "python3 week32_run_eval.py",
        "Automated eval report", checkpoint="CP4")

    # Months 9–10 — Production
    add(33, "FastAPI /ask endpoint", "y1q3", 11,
        "FastAPI tutorial §1–5",
        "lab/projects/week33_fastapi/main.py",
        "uvicorn main:app --reload",
        "curl POST /ask works")
    add(34, "Pydantic validation", "y1q3", 11,
        "FastAPI body models",
        "lab/projects/week33_fastapi/main.py",
        "pytest test_health.py",
        "Invalid input rejected")
    add(35, "Dockerfile", "y1q3", 11,
        "Docker get-started",
        "lab/projects/week35_docker/Dockerfile",
        "docker build -t copilot .",
        "Image builds")
    add(36, "docker compose up", "y1q3", 11,
        "docker-compose reference",
        "lab/projects/week35_docker/docker-compose.yml",
        "docker compose up",
        "Healthcheck passes")
    add(37, "PII guardrails", "y1q4", 12,
        "governance-mlops.md",
        "lab/exercises/week37_guardrails.py",
        "python3 week37_guardrails.py",
        "Redacted audit.log")
    add(38, "Model card", "y1q4", 12,
        "Responsible AI template",
        "lab/projects/model_card.md",
        "Fill purpose, limits, risks",
        "3 governance gates documented")
    add(39, "GitHub Actions CI", "y1q4", 12,
        "GitHub Actions Python",
        "lab/projects/week39_ci/.github/workflows/ci.yml",
        "Push triggers pytest + eval",
        "CI badge green")
    add(40, "Eval gate in CI", "y1q4", 12,
        "Harness engineering",
        "lab/projects/week39_ci/",
        "Fail if grounded < 85%",
        "Friend runs Docker API", checkpoint="CP5",
        track_b={
            "hours": 2,
            "title": "90-day AI Factory plan",
            "study": "archive/head-of-ai-factory/strategy-and-roadmap.md §6",
            "template": "curriculum/templates/hoai/week40_ninety_day_plan.md",
            "action": "Draft listen → frame → deliver phases for pilot squad",
            "deliverable": "90-day plan with 1–2 quick wins + hiring sketch",
            "hoai_checkpoint": "H3",
        })

    # Months 11–12 — Career
    add(41, "Second use case BRD", "y1q4", 13,
        "examples/04a; job-skills-adaptation.md",
        "lab/exercises/week41_value_case.md",
        "Fill value case template",
        "1-page quantified metric")
    add(42, "AML triage OR doc OCR story", "y1q4", 13,
        "job-skills-adaptation.md",
        "lab/projects/use-case-2/README.md",
        "Pick and scope use case",
        "STAR outline draft")
    add(43, "Portfolio README", "y1q4", 13,
        "GitHub portfolio patterns",
        "lab/projects/PORTFOLIO.md",
        "Link all repos + metrics",
        "Single index page")
    add(44, "Architecture diagram", "y1q4", 13,
        "Mermaid / draw.io",
        "lab/projects/PORTFOLIO.md",
        "Copilot architecture diagram",
        "Diagram in README")
    add(45, "CV update", "y1q4", 14,
        "cv-templates.md",
        "curriculum/cv-templates.md",
        "Fill real project metrics",
        "CV draft v1")
    add(46, "Apply OCB / NAB / VPBank", "y1q4", 14,
        "job-skills-adaptation.md",
        "curriculum/job-skills-adaptation.md",
        "Submit 3 applications",
        "Application tracker")
    add(47, "STAR stories ×5", "y1q4", 14,
        "cv-templates.md §3",
        "lab/exercises/week47_star_stories.md",
        "Write 5 STAR stories",
        "Stories reviewed aloud")
    add(48, "Mock interview", "y1q4", 14,
        "job-skills-adaptation.md",
        "lab/exercises/week47_star_stories.md",
        "45-min mock with peer",
        "Feedback notes", checkpoint="CP6")
    add(49, "Demo video 5 min", "y1q4", 14,
        "Record Loom / OBS",
        "lab/projects/PORTFOLIO.md",
        "English demo of copilot",
        "Video link in README")
    add(50, "Anthropic stretch research", "y1q4", 14,
        "anthropic-career-adaptation.md",
        "curriculum/anthropic-career-adaptation.md",
        "Map skills to Claude roles",
        "Gap list")
    add(51, "Review weak weeks", "y1q4", 14,
        "Re-run failed checkpoints",
        "learning-data.json + workbook",
        "Fix lowest eval score week",
        "All CP0–CP6 passed")
    add(52, "Graduation checklist", "y1q4", 14,
        "ai-skills-workbook.md",
        "lab/WEEKS.md",
        "Verify 2 repos + CV + apply",
        "Hire-ready checklist ✓",
        track_b={
            "hours": 2,
            "title": "Steering committee deck",
            "study": "curriculum/head-of-ai-track.md · job-skills-adaptation.md §F.4 · templates/hoai/vpbank_steering_one_pager.md",
            "template": "curriculum/templates/hoai/week52_steering_deck.md",
            "action": "Build 5 slides (or use VPBank one-pager): strategy · portfolio · KPIs · 90-day · ask",
            "deliverable": "Deck + 5-min exec narrative (record or script)",
            "hoai_checkpoint": "H4",
        })

    assert len(items) == 52, f"Expected 52 weeks, got {len(items)}"
    return items


WEEKS = _build_weeks()

META = {
    "version": "1.2",
    "career_timeline": "curriculum/career-timeline.md",
    "hours_per_week": 10,
    "hours_track_a": 8,
    "hours_track_b": 2,
    "total_weeks": 52,
    "track_b_weeks": TRACK_B_WEEKS,
    "track_b_guide": "curriculum/head-of-ai-track.md",
    "track_b_delivery": "curriculum/track-b-delivery.md",
    "track_b_output_dir": "lab/delivery/track-b/",
    "track_b_demo_case": "curriculum/ai-factory-demo-case.md",
    "data_source": "curriculum/learning_data.py",
    "workbook": "curriculum/ai-skills-workbook.md",
    "repo_root_docs": "docs/",
    "lab_root": "lab/",
}
