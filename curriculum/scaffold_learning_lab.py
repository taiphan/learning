#!/usr/bin/env python3
"""Scaffold lab files from learning_data.py (idempotent — skips existing)."""

from __future__ import annotations

from repo_paths import LAB


def _lab_path(rel: str):
    return LAB / rel.removeprefix("lab/")


STUBS: dict[str, str] = {
    "lab/exercises/week03_brd_weighted_score.py": '''#!/usr/bin/env python3
"""Week 3 — Weighted BRD score (see docs/05-brd-quality-checklist.md)."""
# TODO: reuse week01 audit; multiply by weights; print total %
''',
    "lab/exercises/week04_brd_scorecard.py": '''#!/usr/bin/env python3
"""Week 4 — class BRDScorecard with .score() and .missing_sections()."""
# TODO: implement class; argparse file path
''',
    "lab/sql/week06_join.sql": "-- Week 6 — JOIN customers ↔ applications\n-- TODO\n",
    "lab/sql/week07_window.sql": "-- Week 7 — monthly trend window function\n-- TODO\n",
    "lab/exercises/week12_train_test.py": "# Week 12 — time-based split\n# TODO\n",
    "lab/exercises/week17_metrics.py": "# Week 17–19 — ROC, threshold\n# TODO\n",
    "lab/exercises/week20_shap.py": "# Week 20 — SHAP\n# TODO\n",
    "lab/exercises/week21_embed.py": "# Week 21–23 — embeddings\n# TODO\n",
    "lab/exercises/week24_doc_classifier.py": "# Week 24 — doc classifier\n# TODO\n",
    "lab/exercises/week25_rag_cli.py": "# Week 25–28 — RAG CLI\n# TODO\n",
    "lab/exercises/week29_structured_llm.py": "# Week 29 — structured LLM JSON\n# TODO\n",
    "lab/exercises/week30_langgraph.py": "# Week 30 — LangGraph\n# TODO\n",
    "lab/exercises/week32_run_eval.py": "# Week 32 — eval harness\n# TODO\n",
    "lab/exercises/week37_guardrails.py": "# Week 37 — guardrails\n# TODO\n",
    "lab/data/sample_policy.txt": """Max DTI for POS motorbike loan: 40%.
Branch manager approves up to 100,000,000 VND.
Regional director required above 100M VND.
Min employment: 12 months.
""",
    "lab/data/eval_questions.json": '[{"id":"q01","question":"Max DTI?","expected_contains":["40"],"expected_source":"sample_policy.txt"}]\n',
    "lab/data/sample_customers.csv": "customer_id,region\nC001,HCM\nC002,HN\n",
    "lab/exercises/week41_value_case.md": "# Week 41 value case\n\n| Problem | |\n",
    "lab/exercises/week47_star_stories.md": "# STAR stories\n\n## Story 1\n",
    "lab/projects/credit-pd-model/train.py": "# TODO train model\n",
    "lab/projects/credit-pd-model/README.md": "# credit-pd-model\n",
    "lab/projects/policy-rag/README.md": "# policy-rag\n",
    "lab/projects/policy-copilot-agent/README.md": "# policy-copilot-agent\n",
    "lab/projects/week33_fastapi/main.py": "from fastapi import FastAPI\napp=FastAPI()\n@app.get('/health')\ndef health(): return {'status':'ok'}\n",
    "lab/projects/week33_fastapi/test_health.py": "def test_health(): pass  # TODO\n",
    "lab/projects/week35_docker/Dockerfile": "FROM python:3.11-slim\n",
    "lab/projects/week35_docker/docker-compose.yml": "services:\n  api:\n    build: .\n",
    "lab/projects/week39_ci/.github/workflows/ci.yml": "name: CI\non: [push]\njobs:\n  test:\n    runs-on: ubuntu-latest\n",
    "lab/projects/model_card.md": "# Model card\n",
    "lab/projects/PORTFOLIO.md": "# Portfolio\n",
    "lab/projects/use-case-2/README.md": "# Use case 2\n",
}


def scaffold(force: bool = False) -> list[str]:
    created = []
    for rel, content in STUBS.items():
        path = _lab_path(rel)
        if path.exists() and not force:
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        created.append(str(path.relative_to(LAB.parent)))

    from learning_data import CHECKPOINTS, WEEKS

    lines = ["# 52-Week Learning Index", "", "Edit `curriculum/learning_data.py` — regenerate with scaffold.", ""]
    lines.append("| Week | Phase | Title | Exercise | Run |")
    lines.append("|------|-------|-------|----------|-----|")
    for w in WEEKS:
        lines.append(f"| {w['week']} | {w['phase']} | {w['title']} | `{w['exercise']}` | `{w['run']}` |")
    lines.append("\n## Checkpoints\n")
    for cp in CHECKPOINTS:
        lines.append(f"- **{cp['id']}** after week {cp['after_week']}: {cp['label']}")
    (LAB / "WEEKS.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    created.append("lab/WEEKS.md")
    return created


if __name__ == "__main__":
    print(f"Scaffolded {len(scaffold())} files")
