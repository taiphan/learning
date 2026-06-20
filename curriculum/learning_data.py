"""Single source of truth for AI learning curriculum — weeks, skills, links, slides."""

from __future__ import annotations

# Phase ids → anthropic_theme color keys (resolved in learning_loader)
PHASES = [
    {"id": "foundation", "name": "Foundation", "color": "CLAY", "weeks": "1–8", "theme": "Python · Git · SQL · pandas"},
    {"id": "ml", "name": "Classical ML", "color": "SKY", "weeks": "9–20", "theme": "EDA · sklearn · SHAP"},
    {"id": "nlp", "name": "NLP & Docs", "color": "OLIVE", "weeks": "21–24", "theme": "Embeddings · chunking · classify"},
    {"id": "genai", "name": "GenAI & Agents", "color": "FIG", "weeks": "25–32", "theme": "RAG · LangGraph · eval"},
    {"id": "production", "name": "Production", "color": "CACTUS", "weeks": "33–40", "theme": "FastAPI · Docker · CI"},
    {"id": "career", "name": "Career", "color": "OLIVE", "weeks": "41–52", "theme": "Portfolio · apply · interview"},
]

CHECKPOINTS = [
    {"id": "CP0", "after_week": 4, "label": "Write 50-line script without googling every line"},
    {"id": "CP1", "after_week": 8, "label": "SQL JOIN + pandas groupby without tutorial"},
    {"id": "CP2", "after_week": 16, "label": "Train model, report AUC, explain one prediction"},
    {"id": "CP3", "after_week": 24, "label": "RAG cites source chunk in answer"},
    {"id": "CP4", "after_week": 32, "label": "LangGraph agent + 30-question eval ≥85%"},
    {"id": "CP5", "after_week": 40, "label": "Friend runs your Docker API on their laptop"},
    {"id": "CP6", "after_week": 48, "label": "30-min interview: business metric + tech stack"},
]

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
    ):
        items.append(
            {
                "week": n,
                "title": title,
                "phase": phase,
                "skill_id": skill_id,
                "month": (n - 1) // 4 + 1,
                "study": study,
                "exercise": exercise,
                "run": run,
                "deliverable": deliverable,
                "resource_urls": urls or [],
                "checkpoint": checkpoint,
            }
        )

    # Month 1 — Python
    add(1, "Python syntax — BRD audit", "foundation", 1,
        "Python.org §1–4; Kaggle Python L1–3",
        "lab/exercises/week01_brd_checklist.py",
        "python3 week01_brd_checklist.py --app-sample",
        "Lists missing BRD sections",
        [("Python tutorial", "https://docs.python.org/3/tutorial/")])
    add(2, "Functions & CSV loan rules", "foundation", 1,
        "§5–6; read docs/01-brd-template-en.md",
        "lab/exercises/week02_loan_rules.py",
        "python3 week02_loan_rules.py",
        "10 loans pass/fail correctly")
    add(3, "Dicts & weighted BRD score", "foundation", 1,
        "Lists, dicts, JSON; docs/05 quality rubric",
        "lab/exercises/week03_brd_weighted_score.py",
        "python3 week03_brd_weighted_score.py",
        "Weighted score % printed")
    add(4, "OOP scorecard + Git", "foundation", 2,
        "Classes basics; Git commit/push",
        "lab/exercises/week04_brd_scorecard.py",
        "python3 week04_brd_scorecard.py",
        "BRDScorecard class + GitHub repo", checkpoint="CP0")

    # Month 2 — SQL + pandas
    add(5, "SQL aggregates & filters", "foundation", 3,
        "SQLBolt 1–6",
        "lab/sql/week05_queries.sql",
        "sqlite3 loans.db < sql/week05_queries.sql",
        "5 queries documented")
    add(6, "SQL JOINs", "foundation", 3,
        "SQLBolt 7–12",
        "lab/sql/week06_join.sql",
        "Run join on customers + applications",
        "Join returns correct rows")
    add(7, "SQL windows & trends", "foundation", 3,
        "SQLBolt 13–18",
        "lab/sql/week07_window.sql",
        "Monthly disbursement trend query",
        "Window function KPI")
    add(8, "pandas KPIs", "foundation", 4,
        "Kaggle Pandas L1–4",
        "lab/notebooks/01_lending_kpis.ipynb",
        "jupyter notebook 01_lending_kpis.ipynb",
        "3 KPIs + 1 chart", checkpoint="CP1")

    # Months 3–4 — ML
    add(9, "Load credit dataset", "ml", 5,
        "Kaggle Give Me Some Credit description",
        "lab/notebooks/02_eda_credit.ipynb",
        "Start EDA notebook",
        "Dataset loaded; shape printed")
    add(10, "EDA histograms & missing", "ml", 5,
        "StatQuest stats fundamentals (3 videos)",
        "lab/notebooks/02_eda_credit.ipynb",
        "Complete missing-value analysis",
        "2 charts with captions")
    add(11, "Business insights write-up", "ml", 5,
        "StatQuest ML intro",
        "lab/notebooks/02_eda_credit.ipynb",
        "Write 3 insights in BRD language",
        "insights.md in notebook")
    add(12, "Train/test split — no leakage", "ml", 6,
        "Kaggle Intro ML L1–3",
        "lab/exercises/week12_train_test.py",
        "python3 week12_train_test.py",
        "Time-based split documented")
    add(13, "Logistic regression baseline", "ml", 6,
        "Kaggle Intro ML L4–7",
        "lab/projects/credit-pd-model/train.py",
        "python3 projects/credit-pd-model/train.py",
        "Baseline AUC printed")
    add(14, "Random Forest tune", "ml", 6,
        "Kaggle Intermediate ML",
        "lab/projects/credit-pd-model/train.py",
        "Beat baseline AUC",
        "Comparison table in README")
    add(15, "XGBoost + imbalance", "ml", 6,
        "XGBoost docs; class_weight",
        "lab/projects/credit-pd-model/train.py",
        "class_weight or scale_pos_weight",
        "README business metric")
    add(16, "Model README + metric", "ml", 6,
        "Géron Ch 3 metrics",
        "lab/projects/credit-pd-model/README.md",
        "Document AUC + decision use",
        "Repo public on GitHub", checkpoint="CP2")
    add(17, "ROC & threshold", "ml", 7,
        "sklearn metrics; StatQuest ROC",
        "lab/exercises/week17_metrics.py",
        "python3 week17_metrics.py",
        "ROC plot saved")
    add(18, "Precision/recall trade-off", "ml", 7,
        "StatQuest precision-recall",
        "lab/exercises/week17_metrics.py",
        "Threshold for 90% approval rate",
        "Table in README")
    add(19, "Calibration intuition", "ml", 7,
        "Géron calibration concept",
        "lab/exercises/week17_metrics.py",
        "Reliability sketch",
        "1 paragraph for BA audience")
    add(20, "SHAP explainability", "ml", 7,
        "SHAP intro notebook",
        "lab/exercises/week20_shap.py",
        "python3 week20_shap.py",
        "decline_story.md + plot")

    # Months 5–6 — NLP
    add(21, "Sentence embeddings", "nlp", 8,
        "HF NLP Ch 1–2",
        "lab/exercises/week21_embed.py",
        "python3 week21_embed.py",
        "Top-3 similar policy lines")
    add(22, "Chunk policy text", "nlp", 8,
        "HF NLP Ch 3",
        "lab/data/sample_policy.txt",
        "Chunk into 500-token pieces",
        "chunk manifest JSON")
    add(23, "Cosine similarity search", "nlp", 8,
        "LangChain embedding docs",
        "lab/exercises/week21_embed.py",
        "Query latency measured",
        "Sub-200ms local benchmark")
    add(24, "Document classifier", "nlp", 8,
        "Text classification sklearn",
        "lab/exercises/week24_doc_classifier.py",
        "python3 week24_doc_classifier.py",
        "80%+ on tiny test set", checkpoint="CP3")

    # Months 7–8 — GenAI
    add(25, "LangChain RAG quickstart", "genai", 9,
        "DL.AI LangChain short course",
        "lab/exercises/week25_rag_cli.py",
        "python3 week25_rag_cli.py",
        "One Q&A with source cite")
    add(26, "Chroma vector store", "genai", 9,
        "ChromaDB docs",
        "lab/exercises/week25_rag_cli.py",
        "Persist index to ./chroma_db",
        "Reload index works")
    add(27, "PDF / markdown loader", "genai", 9,
        "LangChain document loaders",
        "lab/projects/policy-rag/",
        "Index examples/04a-brd-pos-lending.md",
        "CLI over repo BRD")
    add(28, "Refusal without context", "genai", 9,
        "RAG eval patterns",
        "lab/projects/policy-rag/",
        "Return escalate if no chunk",
        "10-question golden set started")
    add(29, "LLM structured JSON", "genai", 10,
        "Anthropic API docs",
        "lab/exercises/week29_structured_llm.py",
        "Extract policy fields to JSON",
        "Valid schema output")
    add(30, "LangGraph intro", "genai", 10,
        "DL.AI LangGraph course",
        "lab/exercises/week30_langgraph.py",
        "python3 week30_langgraph.py",
        "State diagram in README")
    add(31, "Agent tools", "genai", 10,
        "LangGraph tool calling",
        "lab/projects/policy-copilot-agent/",
        "3 tools: lookup, calc, escalate",
        "Multi-step trace logged")
    add(32, "Eval harness ≥85%", "genai", 10,
        "ragas; data/eval_questions.json",
        "lab/data/eval_questions.json",
        "python3 week32_run_eval.py",
        "Automated eval report", checkpoint="CP4")

    # Months 9–10 — Production
    add(33, "FastAPI /ask endpoint", "production", 11,
        "FastAPI tutorial §1–5",
        "lab/projects/week33_fastapi/main.py",
        "uvicorn main:app --reload",
        "curl POST /ask works")
    add(34, "Pydantic validation", "production", 11,
        "FastAPI body models",
        "lab/projects/week33_fastapi/main.py",
        "pytest test_health.py",
        "Invalid input rejected")
    add(35, "Dockerfile", "production", 11,
        "Docker get-started",
        "lab/projects/week35_docker/Dockerfile",
        "docker build -t copilot .",
        "Image builds")
    add(36, "docker compose up", "production", 11,
        "docker-compose reference",
        "lab/projects/week35_docker/docker-compose.yml",
        "docker compose up",
        "Healthcheck passes")
    add(37, "PII guardrails", "production", 12,
        "governance-mlops.md",
        "lab/exercises/week37_guardrails.py",
        "python3 week37_guardrails.py",
        "Redacted audit.log")
    add(38, "Model card", "production", 12,
        "Responsible AI template",
        "lab/projects/model_card.md",
        "Fill purpose, limits, risks",
        "3 governance gates documented")
    add(39, "GitHub Actions CI", "production", 12,
        "GitHub Actions Python",
        "lab/projects/week39_ci/.github/workflows/ci.yml",
        "Push triggers pytest + eval",
        "CI badge green")
    add(40, "Eval gate in CI", "production", 12,
        "Harness engineering",
        "lab/projects/week39_ci/",
        "Fail if grounded < 85%",
        "Friend runs Docker API", checkpoint="CP5")

    # Months 11–12 — Career
    add(41, "Second use case BRD", "career", 13,
        "examples/04a; job-skills-adaptation.md",
        "lab/exercises/week41_value_case.md",
        "Fill value case template",
        "1-page quantified metric")
    add(42, "AML triage OR doc OCR story", "career", 13,
        "job-skills-adaptation.md",
        "lab/projects/use-case-2/README.md",
        "Pick and scope use case",
        "STAR outline draft")
    add(43, "Portfolio README", "career", 13,
        "GitHub portfolio patterns",
        "lab/projects/PORTFOLIO.md",
        "Link all repos + metrics",
        "Single index page")
    add(44, "Architecture diagram", "career", 13,
        "Mermaid / draw.io",
        "lab/projects/PORTFOLIO.md",
        "Copilot architecture diagram",
        "Diagram in README")
    add(45, "CV update", "career", 14,
        "cv-templates.md",
        "curriculum/cv-templates.md",
        "Fill real project metrics",
        "CV draft v1")
    add(46, "Apply OCB / NAB / VPBank", "career", 14,
        "job-skills-adaptation.md",
        "curriculum/job-skills-adaptation.md",
        "Submit 3 applications",
        "Application tracker")
    add(47, "STAR stories ×5", "career", 14,
        "cv-templates.md §3",
        "lab/exercises/week47_star_stories.md",
        "Write 5 STAR stories",
        "Stories reviewed aloud")
    add(48, "Mock interview", "career", 14,
        "job-skills-adaptation.md",
        "lab/exercises/week47_star_stories.md",
        "45-min mock with peer",
        "Feedback notes", checkpoint="CP6")
    add(49, "Demo video 5 min", "career", 14,
        "Record Loom / OBS",
        "lab/projects/PORTFOLIO.md",
        "English demo of copilot",
        "Video link in README")
    add(50, "Anthropic stretch research", "career", 14,
        "anthropic-career-adaptation.md",
        "curriculum/anthropic-career-adaptation.md",
        "Map skills to Claude roles",
        "Gap list")
    add(51, "Review weak weeks", "career", 14,
        "Re-run failed checkpoints",
        "learning-data.json + workbook",
        "Fix lowest eval score week",
        "All CP0–CP6 passed")
    add(52, "Graduation checklist", "career", 14,
        "ai-skills-workbook.md",
        "lab/WEEKS.md",
        "Verify 2 repos + CV + apply",
        "Hire-ready checklist ✓")

    assert len(items) == 52, f"Expected 52 weeks, got {len(items)}"
    return items


WEEKS = _build_weeks()

META = {
    "version": "1.0",
    "hours_per_week": 10,
    "total_weeks": 52,
    "data_source": "curriculum/learning_data.py",
    "workbook": "curriculum/ai-skills-workbook.md",
    "repo_root_docs": "docs/",
    "lab_root": "lab/",
}
