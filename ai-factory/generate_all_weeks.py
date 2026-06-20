#!/usr/bin/env python3
"""Generate complete runnable code for all 52 weeks."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent  # ai-factory/
LAB = ROOT / "learning-lab"


def w(rel: str, content: str) -> None:
    p = ROOT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content.strip() + "\n", encoding="utf-8")
    print(f"  wrote {rel}")


def main() -> None:
    print("Generating all weeks...")
    lib = "learning-lab"
    sys_path = (
        "import sys\nfrom pathlib import Path\n"
        f"sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'lib'))\n"
    )

    w(f"{lib}/exercises/week01_brd_checklist.py", f'''#!/usr/bin/env python3
"""Week 1 — BRD section audit."""
import argparse
{sys_path}
from brd_utils import MANDATORY_SECTIONS, audit_brd, load_brd_text

SAMPLE = Path(__file__).resolve().parent.parent / "data" / "sample_brd_app_export.md"
DEFAULT = Path(__file__).resolve().parent.parent / "data" / "sample_brd_app_export.md"

def print_report(results, source):
    print("=== BRD Section Audit ===")
    print(f"Source: {{source}}\\n")
    missing = [s for s, ok in results.items() if not ok]
    for s, ok in results.items():
        print(f"  [{{'OK' if ok else 'MISSING'}}] {{s}}")
    print("\\nAction: add " + ", ".join(missing) if missing else "\\nAll mandatory sections present.")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("brd_file", nargs="?", type=Path)
    p.add_argument("--app-sample", action="store_true")
    a = p.parse_args()
    path = DEFAULT if a.app_sample else a.brd_file
    text = load_brd_text(path, "")
    if not text and not path:
        text = load_brd_text(None, "EXECUTIVE SUMMARY\\nOBJECTIVES\\nSCOPE\\nBUSINESS RULES")
    print_report(audit_brd(text), str(path or "inline"))
''')

    w(f"{lib}/exercises/week02_loan_rules.py", f'''#!/usr/bin/env python3
"""Week 2 — Loan rules from CSV."""
{sys_path}
from loan_utils import load_applications, evaluate

DATA = Path(__file__).resolve().parent.parent / "data" / "sample_loans.csv"

if __name__ == "__main__":
    apps = load_applications(DATA)
    print(f"Loaded {{len(apps)}} applications\\n")
    for row in apps:
        ok, reasons = evaluate(row)
        print(f"{{row['application_id']}}: {{'APPROVE' if ok else 'DECLINE'}}")
        for r in reasons:
            print(f"    - {{r}}")
''')

    w(f"{lib}/exercises/week03_brd_weighted_score.py", f'''#!/usr/bin/env python3
"""Week 3 — Weighted BRD quality score."""
import argparse
{sys_path}
from brd_utils import load_brd_text, audit_brd, weighted_score, MANDATORY_SECTIONS

DEFAULT = Path(__file__).resolve().parent.parent / "data" / "sample_brd_app_export.md"

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("brd_file", nargs="?", type=Path, default=DEFAULT)
    a = p.parse_args()
    text = load_brd_text(a.brd_file, "")
    results = audit_brd(text)
    score = weighted_score(results)
    print(f"Weighted BRD score: {{score:.1f}}%")
    for s in MANDATORY_SECTIONS:
        print(f"  [{{'OK' if results[s] else 'MISS'}}] {{s}} (weight applied)")
    print("Gate ≥80%:", "PASS" if score >= 80 else "FAIL — revise before export")
''')

    w(f"{lib}/exercises/week04_brd_scorecard.py", f'''#!/usr/bin/env python3
"""Week 4 — BRDScorecard class."""
import argparse
{sys_path}
from brd_utils import BRDScorecard, load_brd_text

DEFAULT = Path(__file__).resolve().parent.parent / "data" / "sample_brd_app_export.md"

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("brd_file", nargs="?", type=Path, default=DEFAULT)
    a = p.parse_args()
    card = BRDScorecard(load_brd_text(a.brd_file, ""))
    print(card.report())
''')

    w(f"{lib}/sql/week05_queries.sql", open(ROOT / "learning-lab/sql/week05_queries_solution.sql").read())

    w(f"{lib}/sql/week06_join.sql", """
-- Week 6 — JOIN customers and applications
SELECT c.customer_id, c.segment, a.application_id, a.loan_amount_vnd, a.region
FROM customers c
JOIN applications a ON a.customer_id = c.customer_id
ORDER BY a.loan_amount_vnd DESC;

SELECT c.region, COUNT(*) AS apps, SUM(a.loan_amount_vnd) AS total_loan
FROM customers c
JOIN applications a ON a.customer_id = c.customer_id
GROUP BY c.region;
""")

    w(f"{lib}/sql/week07_window.sql", """
-- Week 7 — Monthly disbursement trend (window)
SELECT application_month,
       SUM(loan_amount_vnd) AS month_total,
       SUM(SUM(loan_amount_vnd)) OVER (ORDER BY application_month) AS running_total
FROM applications
GROUP BY application_month
ORDER BY application_month;
""")

    w(f"{lib}/exercises/week08_lending_kpis.py", '''#!/usr/bin/env python3
"""Week 8 — pandas KPIs (run without Jupyter). pip install pandas matplotlib"""
import pandas as pd
from pathlib import Path

df = pd.read_csv(Path(__file__).resolve().parent.parent / "data" / "sample_loans.csv")
df["dti"] = df["existing_debt_vnd"] / df["monthly_income_vnd"]
print("=== Lending KPIs ===")
print(f"Total disbursement: {df['loan_amount_vnd'].sum():,} VND")
print(f"Avg loan: {df['loan_amount_vnd'].mean():,.0f} VND")
eligible = (df["monthly_income_vnd"] >= 15_000_000).mean()
print(f"Income-eligible rate: {eligible:.1%}")
print("\\nBy region:")
print(df.groupby("region")["loan_amount_vnd"].agg(["count", "sum", "mean"]).to_string())
try:
    import matplotlib.pyplot as plt
    df.groupby("region")["loan_amount_vnd"].sum().plot(kind="bar", title="Disbursement by region")
    out = Path(__file__).resolve().parent.parent / "outputs" / "week08_region_bar.png"
    out.parent.mkdir(exist_ok=True)
    plt.savefig(out)
    print(f"\\nChart saved: {out}")
except ImportError:
    print("\\nInstall matplotlib for chart: pip install matplotlib")
''')

    w(f"{lib}/exercises/week09_eda.py", '''#!/usr/bin/env python3
"""Weeks 9–11 — EDA on sample_loans (proxy for credit dataset). pip install pandas"""
import pandas as pd
from pathlib import Path

df = pd.read_csv(Path(__file__).resolve().parent.parent / "data" / "sample_loans.csv")
df["dti"] = df["existing_debt_vnd"] / df["monthly_income_vnd"]
df["high_dti"] = df["dti"] > 0.4

print("=== EDA Summary ===")
print(df.describe())
print("\\n=== Business insights (BRD language) ===")
by_region = df.groupby("region")["loan_amount_vnd"].mean()
top = by_region.idxmax()
print(f"1. Region {{top}} has highest avg loan ({{by_region[top]:,.0f}} VND) — prioritize capacity planning.")
print(f"2. {{df['high_dti'].mean():.0%}} of applications exceed 40% DTI — tighten policy segment.")
print(f"3. Employment <12mo: {{(df['employment_months']<12).sum()}} apps — align with week02 rules.")
''')

    w(f"{lib}/exercises/week12_train_test.py", '''#!/usr/bin/env python3
"""Week 12 — Time-ordered train/test split. pip install pandas scikit-learn"""
import pandas as pd
from pathlib import Path

df = pd.read_csv(Path(__file__).resolve().parent.parent / "data" / "sample_loans.csv")
df["dti"] = df["existing_debt_vnd"] / df["monthly_income_vnd"]
df["default_flag"] = ((df["dti"] > 0.35) | (df["employment_months"] < 12)).astype(int)
df = df.sort_values("application_id")
split = int(len(df) * 0.8)
train, test = df.iloc[:split], df.iloc[split:]
print(f"Train: {len(train)} rows | Test: {len(test)} rows")
print(f"Train default rate: {train['default_flag'].mean():.1%}")
print(f"Test default rate: {test['default_flag'].mean():.1%}")
print("No leakage: test rows are later application_ids only.")
''')

    w(f"{lib}/projects/credit-pd-model/train.py", '''#!/usr/bin/env python3
"""Weeks 13–16 — Credit PD model. pip install pandas scikit-learn joblib"""
import json
from pathlib import Path
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
import joblib

DATA = Path(__file__).resolve().parent.parent.parent / "data" / "sample_loans.csv"
OUT = Path(__file__).resolve().parent

df = pd.read_csv(DATA)
df["dti"] = df["existing_debt_vnd"] / df["monthly_income_vnd"]
df["default_flag"] = ((df["dti"] > 0.35) | (df["employment_months"] < 12)).astype(int)
features = ["customer_age", "monthly_income_vnd", "existing_debt_vnd", "loan_amount_vnd", "employment_months", "dti"]
X, y = df[features], df["default_flag"]
split = int(len(df) * 0.8)
X_train, X_test = X.iloc[:split], X.iloc[split:]
y_train, y_test = y.iloc[:split], y.iloc[split:]

baseline = LogisticRegression(max_iter=500).fit(X_train, y_train)
model = RandomForestClassifier(n_estimators=100, class_weight="balanced", random_state=42).fit(X_train, y_train)

b_auc = roc_auc_score(y_test, baseline.predict_proba(X_test)[:, 1])
m_auc = roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])
print(f"Baseline Logistic AUC: {b_auc:.3f}")
print(f"Random Forest AUC:     {m_auc:.3f}")

joblib.dump(model, OUT / "model.pkl")
metrics = {"baseline_auc": b_auc, "model_auc": m_auc, "features": features}
(OUT / "metrics.json").write_text(json.dumps(metrics, indent=2))
print(f"Saved {OUT / 'model.pkl'}")
''')

    w(f"{lib}/exercises/week17_metrics.py", '''#!/usr/bin/env python3
"""Weeks 17–19 — Metrics and threshold. pip install scikit-learn joblib matplotlib"""
import json
from pathlib import Path
import joblib
import pandas as pd
from sklearn.metrics import roc_auc_score, precision_score, recall_score, roc_curve

MODEL_DIR = Path(__file__).resolve().parent.parent / "projects" / "credit-pd-model"
DATA = Path(__file__).resolve().parent.parent / "data" / "sample_loans.csv"

df = pd.read_csv(DATA)
df["dti"] = df["existing_debt_vnd"] / df["monthly_income_vnd"]
df["default_flag"] = ((df["dti"] > 0.35) | (df["employment_months"] < 12)).astype(int)
features = json.loads((MODEL_DIR / "metrics.json").read_text())["features"]
X = df[features]
y = df["default_flag"]
model = joblib.load(MODEL_DIR / "model.pkl")
probs = model.predict_proba(X)[:, 1]
print(f"AUC: {roc_auc_score(y, probs):.3f}")

# Threshold for ~90% approval (top 90% by score)
import numpy as np
thresh = float(np.quantile(probs, 0.10))
preds = (probs >= thresh).astype(int)
print(f"Threshold (90% approve): {thresh:.3f}")
print(f"Precision: {precision_score(y, preds, zero_division=0):.3f}")
print(f"Recall:    {recall_score(y, preds, zero_division=0):.3f}")

try:
    import matplotlib.pyplot as plt
    fpr, tpr, _ = roc_curve(y, probs)
    plt.figure()
    plt.plot(fpr, tpr)
    plt.xlabel("False positive rate")
    plt.ylabel("True positive rate")
    out = Path(__file__).resolve().parent.parent / "outputs" / "week17_roc.png"
    out.parent.mkdir(exist_ok=True)
    plt.savefig(out)
    print(f"ROC saved: {out}")
except ImportError:
    pass
''')

    w(f"{lib}/exercises/week20_shap.py", '''#!/usr/bin/env python3
"""Week 20 — SHAP explainability. pip install shap scikit-learn joblib"""
from pathlib import Path
import json
import joblib
import pandas as pd

MODEL_DIR = Path(__file__).resolve().parent.parent / "projects" / "credit-pd-model"
OUT = Path(__file__).resolve().parent.parent / "outputs"
OUT.mkdir(exist_ok=True)

try:
    import shap
except ImportError:
    print("Install shap: pip install shap")
    raise SystemExit(1)

df = pd.read_csv(Path(__file__).resolve().parent.parent / "data" / "sample_loans.csv")
df["dti"] = df["existing_debt_vnd"] / df["monthly_income_vnd"]
features = json.loads((MODEL_DIR / "metrics.json").read_text())["features"]
X = df[features]
model = joblib.load(MODEL_DIR / "model.pkl")

explainer = shap.TreeExplainer(model)
sv = explainer.shap_values(X.iloc[[0]])
top = sorted(zip(features, sv[0]), key=lambda x: abs(x[1]), reverse=True)[:3]

story = Path(__file__).resolve().parent.parent / "outputs" / "decline_story.md"
lines = ["# Decline narrative (synthetic customer LN001)", ""]
lines.append("Application declined primarily due to:")
for name, val in top:
    lines.append(f"- **{name}** (SHAP {val:+.3f})")
lines.append("\\nRecommend revisit if DTI improves below 40%.")
story.write_text("\\n".join(lines))
print(story.read_text())
''')

    w(f"{lib}/exercises/week21_embed.py", f'''#!/usr/bin/env python3
"""Weeks 21–23 — TF-IDF policy similarity."""
import time
{sys_path}
from rag_simple import TfidfIndex, load_policy_chunks

POLICY = Path(__file__).resolve().parent.parent / "data" / "sample_policy.txt"

if __name__ == "__main__":
    chunks = load_policy_chunks(POLICY)
    index = TfidfIndex(chunks)
    query = "maximum DTI for motorbike loan"
    t0 = time.perf_counter()
    hits = index.search(query, top_k=3)
    ms = (time.perf_counter() - t0) * 1000
    print(f"Query: {{query}}\\nLatency: {{ms:.1f}} ms\\n")
    for i, score, text in hits:
        print(f"  [{{score:.3f}}] chunk {{i}}: {{text[:80]}}...")
''')

    w(f"{lib}/exercises/week24_doc_classifier.py", '''#!/usr/bin/env python3
"""Week 24 — Document type classifier. pip install scikit-learn"""
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

DOCS = [
    ("ID", "national id card copy cmnd citizen"),
    ("ID", "passport biometric identity document"),
    ("CONTRACT", "loan agreement contract signature disbursement"),
    ("CONTRACT", "credit contract terms and conditions"),
    ("COLLATERAL", "motorbike registration collateral asset"),
    ("COLLATERAL", "vehicle ownership certificate lien"),
    ("OTHER", "customer service complaint ticket"),
    ("OTHER", "branch visit feedback survey"),
]
TEST = [
    ("ID", "identity card verification"),
    ("CONTRACT", "signed loan contract appendix"),
    ("COLLATERAL", "collateral motorbike pink book"),
]

X_train = [t for _, t in DOCS]
y_train = [l for l, _ in DOCS]
vec = CountVectorizer()
Xv = vec.fit_transform(X_train)
clf = LogisticRegression(max_iter=500).fit(Xv, y_train)

Xt = vec.transform([t for _, t in TEST])
yt = [l for l, _ in TEST]
acc = accuracy_score(yt, clf.predict(Xt))
print(f"Holdout accuracy: {acc:.1%} ({'PASS' if acc >= 0.8 else 'FAIL'} ≥80%)")
''')

    w(f"{lib}/exercises/week25_rag_cli.py", f'''#!/usr/bin/env python3
"""Weeks 25–28 — CLI RAG over policy text."""
import argparse
{sys_path}
from rag_simple import TfidfIndex, load_policy_chunks

POLICY = Path(__file__).resolve().parent.parent / "data" / "sample_policy.txt"

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("question", nargs="?", default="Max DTI for POS motorbike loan?")
    a = p.parse_args()
    index = TfidfIndex(load_policy_chunks(POLICY))
    resp = index.answer(a.question)
    print("Answer:", resp["answer"])
    print("Confidence:", resp["confidence"])
    for s in resp["sources"]:
        print(f"  Source [{{s['index']}}] score={{s['score']}}: {{s['text'][:100]}}...")
''')

    w(f"{lib}/exercises/week29_structured_llm.py", '''#!/usr/bin/env python3
"""Week 29 — Extract structured policy fields (regex lab; optional API)."""
import json
import re

SAMPLE = """
POS motorbike installment product maximum loan 100 million VND.
Debt-to-income ratio must not exceed 40 percent for approval.
"""

def extract_regex(text: str) -> dict:
    limit = re.search(r"(\\d+)\\s*million\\s*VND", text, re.I)
    dti = re.search(r"(\\d+)\\s*percent", text, re.I)
    return {
        "product": "POS motorbike installment" if "motorbike" in text.lower() else "unknown",
        "limit_vnd": int(limit.group(1)) * 1_000_000 if limit else None,
        "dti_max": float(dti.group(1)) / 100 if dti else None,
    }

if __name__ == "__main__":
    data = extract_regex(SAMPLE)
    print(json.dumps(data, indent=2))
    print("\\nProduction: replace extract_regex with Claude API + JSON schema.")
''')

    w(f"{lib}/exercises/week30_langgraph.py", f'''#!/usr/bin/env python3
"""Week 30 — Simple agent state machine (LangGraph pattern)."""
{sys_path}
from rag_simple import TfidfIndex, load_policy_chunks

POLICY = Path(__file__).resolve().parent.parent / "data" / "sample_policy.txt"

def run_agent(question: str) -> list[str]:
    trace = ["START: understand question"]
    index = TfidfIndex(load_policy_chunks(POLICY))
    trace.append("RETRIEVE: search policy")
    resp = index.answer(question)
    if resp["confidence"] < 0.05:
        trace.append("ESCALATE: low confidence → human")
        return trace
    trace.append(f"ANSWER: {{resp['answer'][:60]}}...")
    trace.append("END")
    return trace

if __name__ == "__main__":
    for step in run_agent("Who approves above 100M?"):
        print(" →", step)
''')

    w(f"{lib}/exercises/week32_run_eval.py", f'''#!/usr/bin/env python3
"""Week 32 — Golden eval harness."""
import sys
{sys_path}
from rag_simple import TfidfIndex, load_policy_chunks, run_eval

POLICY = Path(__file__).resolve().parent.parent / "data" / "sample_policy.txt"
GOLDEN = Path(__file__).resolve().parent.parent / "data" / "eval_questions.json"

if __name__ == "__main__":
    index = TfidfIndex(load_policy_chunks(POLICY))
    result = run_eval(index, GOLDEN)
    print(f"Grounded rate: {{result['passed']}}/{{result['total']}} = {{result['grounded_rate']:.1%}}")
    if result["grounded_rate"] < 0.85:
        sys.exit(1)
    print("PASS ≥85%")
''')

    w(f"{lib}/exercises/week37_guardrails.py", '''#!/usr/bin/env python3
"""Week 37 — PII guardrails and audit log."""
import re
from pathlib import Path

ID_PATTERN = re.compile(r"\\b\\d{9,12}\\b")
BANNED = re.compile(r"bypass\\s+policy", re.I)
AUDIT = Path(__file__).resolve().parent.parent / "outputs" / "audit.log"

def redact(text: str) -> str:
    return ID_PATTERN.sub("[REDACTED_ID]", text)

def filter_input(text: str) -> tuple[bool, str]:
    if BANNED.search(text):
        return False, "Blocked: policy bypass request"
    return True, redact(text)

def filter_output(text: str) -> str:
    return redact(text)

if __name__ == "__main__":
    AUDIT.parent.mkdir(exist_ok=True)
    samples = [
        "Customer ID 123456789 asks loan limit",
        "Please bypass policy for VIP",
    ]
    with AUDIT.open("w") as f:
        for s in samples:
            ok, msg = filter_input(s)
            out = filter_output(msg) if ok else msg
            f.write(f"IN={redact(s)} | OK={ok} | OUT={out}\\n")
            print(out)
    print(f"Audit log: {AUDIT}")
''')

    w(f"{lib}/projects/week33_fastapi/main.py", '''"""Weeks 33–34 — FastAPI policy copilot. pip install fastapi uvicorn"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "lib"))
from rag_simple import TfidfIndex, load_policy_chunks

POLICY = Path(__file__).resolve().parent.parent.parent / "data" / "sample_policy.txt"
_index = TfidfIndex(load_policy_chunks(POLICY))

app = FastAPI(title="Policy Copilot Lab")

class AskRequest(BaseModel):
    question: str = Field(..., min_length=3, max_length=500)

class AskResponse(BaseModel):
    answer: str
    sources: list
    confidence: float

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/ask", response_model=AskResponse)
def ask(req: AskRequest):
    resp = _index.answer(req.question)
    return AskResponse(**resp)
''')

    w(f"{lib}/projects/week33_fastapi/test_health.py", '''from fastapi.testclient import TestClient
from main import app

def test_health():
    r = TestClient(app).get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"
''')

    w(f"{lib}/projects/policy-rag/ask.py", '''#!/usr/bin/env python3
"""Week 27 — Policy RAG CLI over repo BRD sample."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "lib"))
from rag_simple import TfidfIndex, chunk_text

REPO = Path(__file__).resolve().parents[3]
BRD = REPO / "examples" / "04a-brd-pos-lending.md"

if __name__ == "__main__":
    text = BRD.read_text(encoding="utf-8") if BRD.exists() else "No BRD found"
    index = TfidfIndex(chunk_text(text, max_words=100))
    q = sys.argv[1] if len(sys.argv) > 1 else "What is the business problem?"
    resp = index.answer(q)
    print(resp["answer"][:500])
''')

    w(f"{lib}/projects/policy-copilot-agent/agent.py", '''#!/usr/bin/env python3
"""Week 31 — Agent with lookup, calculator, escalate tools."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "lib"))
from rag_simple import TfidfIndex, load_policy_chunks

POLICY = Path(__file__).resolve().parent.parent.parent / "data" / "sample_policy.txt"

def policy_lookup(q: str):
    return TfidfIndex(load_policy_chunks(POLICY)).answer(q)

def dti_calculator(income: float, debt: float):
    return {"dti": round(debt / income, 3) if income else 1.0}

def escalate(reason: str):
    return {"escalated": True, "reason": reason}

def handle(question: str):
    if "dti" in question.lower() and "income" in question.lower():
        return dti_calculator(25_000_000, 8_000_000)
    resp = policy_lookup(question)
    if resp["confidence"] < 0.05:
        return escalate("low confidence")
    return resp

if __name__ == "__main__":
    print(handle(sys.argv[1] if len(sys.argv) > 1 else "Max DTI?"))
''')

    # Career templates — filled examples
    w(f"{lib}/exercises/week41_value_case.md", """# Week 41 — Value case (example)

| Field | Answer |
|-------|--------|
| Problem | POS staff cannot see loan approval during visit — 18% drop-off |
| Baseline | 82% same-day conversion; 45 min avg policy lookup |
| Target | 90% conversion; 10 min lookup via copilot |
| Measurement | Conversion rate monthly; grounded-rate eval ≥90% |
| Risk tier | Medium — human escalation for limit changes >100M VND |
""")

    w(f"{lib}/exercises/week47_star_stories.md", """# Week 47 — STAR stories (examples)

## Story 1 — BRD quality automation
- **S:** POS lending BRD missing acceptance criteria caused UAT rework.
- **T:** Define quality gate before IT intake.
- **A:** Built Python BRD auditor mirroring intake app scoring.
- **R:** Caught 3 missing sections pre-submission; reduced BA return rate.

## Story 2 — (add your own)
- **S:**
- **T:**
- **A:**
- **R:**
""")

    w(f"{lib}/projects/PORTFOLIO.md", """# Banking AI Portfolio

| Project | Metric | Link |
|---------|--------|------|
| credit-pd-model | AUC (see metrics.json) | learning-lab/projects/credit-pd-model/ |
| policy-rag | Grounded TF-IDF RAG | learning-lab/projects/policy-rag/ |
| policy-copilot-agent | 3 tools + escalation | learning-lab/projects/policy-copilot-agent/ |
| week33_fastapi | /health + /ask | learning-lab/projects/week33_fastapi/ |

## Architecture (Mermaid)

```mermaid
flowchart LR
  User --> API[FastAPI /ask]
  API --> RAG[TF-IDF RAG]
  RAG --> Policy[(Policy chunks)]
  API --> Agent[Agent tools]
  Agent --> Escalate[Human]
```

## Demo video
- [ ] Record 5-min English walkthrough
""")

    w(f"{lib}/projects/use-case-2/README.md", """# Use case 2 — AML alert triage (draft)

**Problem:** L2 analysts spend 12 min/alert on false positives.

**Target:** 30% reduction in manual review via AI triage + explainability.

**Metric:** FP rate, SAR filing TAT (baseline → target in bps).
""")

    w(f"{lib}/projects/model_card.md", """# Model card — credit-pd-model (lab)

## Purpose
Proxy default risk model for learning — not production credit decisioning.

## Limits
- Trained on 10-row synthetic lab data only.
- Not validated against SBV requirements.

## Governance gates
1. Human review for all declines in production.
2. SHAP narrative required for adverse action.
3. Monthly AUC drift monitoring.
""")

    w(f"{lib}/projects/week35_docker/Dockerfile", """FROM python:3.11-slim
WORKDIR /app
COPY ../week33_fastapi /app
COPY ../../lib /app/lib
COPY ../../data/sample_policy.txt /app/data/sample_policy.txt
RUN pip install --no-cache-dir fastapi uvicorn pydantic
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
""")

    w(f"{lib}/projects/week35_docker/docker-compose.yml", """services:
  api:
    build:
      context: ..
      dockerfile: week35_docker/Dockerfile
    ports:
      - "8000:8000"
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 10s
      retries: 3
""")

    w(f"{lib}/projects/week39_ci/.github/workflows/ci.yml", """name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install fastapi uvicorn pytest httpx pydantic scikit-learn pandas
      - run: python learning-lab/setup_db.py
      - run: python learning-lab/projects/credit-pd-model/train.py
      - run: pytest learning-lab/projects/week33_fastapi/test_health.py
      - run: python learning-lab/exercises/week32_run_eval.py
""")

    w(f"{lib}/requirements.txt", """pandas>=2.0
matplotlib>=3.7
scikit-learn>=1.3
joblib>=1.3
fastapi>=0.100
uvicorn>=0.23
pytest>=7.0
httpx>=0.24
# optional: shap xgboost
""")

    w(f"{lib}/data/eval_questions.json", """[
  {"id": "q01", "question": "Max DTI for POS motorbike loan?", "expected_contains": ["40"]},
  {"id": "q02", "question": "Who approves loans over 100M?", "expected_contains": ["regional", "director"]},
  {"id": "q03", "question": "Minimum employment months?", "expected_contains": ["12"]}
]
""")

    w(f"{lib}/exercises/week04_git_log.sh", """#!/bin/bash
# Week 4 — Git practice (run from your learning repo root)
set -e
echo "=== Recent commits ==="
git log --oneline -10 2>/dev/null || echo "Initialize repo: git init && git add . && git commit -m 'chore: week04 first commit'"
echo ""
echo "=== Status ==="
git status -sb 2>/dev/null || true
""")

    w(f"{lib}/exercises/week22_chunk_policy.py", f'''#!/usr/bin/env python3
"""Week 22 — Chunk policy text and write manifest JSON."""
import json
{sys_path}
from rag_simple import chunk_text, load_policy_chunks

POLICY = Path(__file__).resolve().parent.parent / "data" / "sample_policy.txt"
OUT = Path(__file__).resolve().parent.parent / "data" / "policy_chunks.json"

if __name__ == "__main__":
    chunks = load_policy_chunks(POLICY)
    manifest = [{{"id": i, "chars": len(c), "preview": c[:60]}} for i, c in enumerate(chunks)]
    OUT.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"Wrote {{len(chunks)}} chunks to {{OUT}}")
''')

    w(f"{lib}/exercises/week26_persist_index.py", f'''#!/usr/bin/env python3
"""Week 26 — Persist TF-IDF index to disk (Chroma substitute, no extra deps)."""
import json
{sys_path}
from rag_simple import TfidfIndex, load_policy_chunks

LAB = Path(__file__).resolve().parent.parent
POLICY = LAB / "data" / "sample_policy.txt"
STORE = LAB / "data" / "tfidf_index.json"

if __name__ == "__main__":
    chunks = load_policy_chunks(POLICY)
    index = TfidfIndex(chunks)
    STORE.write_text(json.dumps({{"docs": chunks}}, indent=2), encoding="utf-8")
    reloaded = TfidfIndex(json.loads(STORE.read_text())["docs"])
    hit = reloaded.search("DTI motorbike", top_k=1)[0]
    print(f"Persisted {{len(chunks)}} chunks → {{STORE}}")
    print(f"Reload test score: {{hit[1]:.3f}}")
''')

    w(f"{lib}/exercises/week45_portfolio_checklist.md", """# Week 45–52 — Hire-ready checklist

- [ ] CV updated with AUC + grounded-rate metrics
- [ ] GitHub: credit-pd-model public
- [ ] GitHub: policy-rag or week33_fastapi public
- [ ] 5-min demo video linked in PORTFOLIO.md
- [ ] 5 STAR stories in week47_star_stories.md
- [ ] 3 job applications logged
- [ ] Mock interview completed (week 48)
- [ ] All checkpoints CP0–CP6 passed
""")

    w(f"{lib}/projects/credit-pd-model/README.md", """# credit-pd-model (weeks 13–16)

Proxy PD model on lab `sample_loans.csv` — **not for production**.

## Run
```bash
pip install pandas scikit-learn joblib
python train.py
```

## Metrics
See `metrics.json` after training (baseline logistic vs random forest AUC).

## Business framing
- **False approve** → NPL cost
- **False decline** → lost revenue / CIR impact
- Target threshold tuned in `week17_metrics.py` for ~90% approval rate
""")

    w(f"{lib}/projects/policy-rag/README.md", """# policy-rag (weeks 27–28)

CLI RAG over repo BRD markdown.

```bash
python ask.py "What is the business problem?"
```

Returns grounded chunk or escalation message when confidence is low.
""")

    w(f"{lib}/projects/policy-copilot-agent/README.md", """# policy-copilot-agent (week 31)

Three tools: `policy_lookup`, `dti_calculator`, `escalate`.

```bash
python agent.py "Max DTI?"
python agent.py "calculate dti income"
```

## State diagram
```
START → RETRIEVE → (low confidence?) → ESCALATE
                 → ANSWER → END
```
""")

    w(f"{lib}/projects/week33_fastapi/README.md", """# FastAPI policy copilot (weeks 33–34)

```bash
cd learning-lab/projects/week33_fastapi
pip install fastapi uvicorn
uvicorn main:app --reload
curl http://127.0.0.1:8000/health
curl -X POST http://127.0.0.1:8000/ask -H 'Content-Type: application/json' -d '{"question":"Max DTI?"}'
pytest test_health.py
```
""")

    # Jupyter notebooks (weeks 8–11) — minimal runnable notebooks
    nb01 = {
        "cells": [
            {"cell_type": "markdown", "metadata": {}, "source": ["# Week 8 — Lending KPIs\\nRun cells or: `python exercises/week08_lending_kpis.py`"]},
            {"cell_type": "code", "metadata": {}, "source": [
                "import runpy\\n",
                "runpy.run_path('exercises/week08_lending_kpis.py')"
            ], "outputs": [], "execution_count": None},
        ],
        "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}},
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    nb02 = {
        "cells": [
            {"cell_type": "markdown", "metadata": {}, "source": ["# Weeks 9–11 — EDA\\nRun cells or: `python exercises/week09_eda.py`"]},
            {"cell_type": "code", "metadata": {}, "source": [
                "import runpy\\n",
                "runpy.run_path('exercises/week09_eda.py')"
            ], "outputs": [], "execution_count": None},
        ],
        "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}},
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    import json as _json
    (ROOT / lib / "notebooks").mkdir(parents=True, exist_ok=True)
    (ROOT / lib / "notebooks" / "01_lending_kpis.ipynb").write_text(
        _json.dumps(nb01, indent=1), encoding="utf-8"
    )
    (ROOT / lib / "notebooks" / "02_eda_credit.ipynb").write_text(
        _json.dumps(nb02, indent=1), encoding="utf-8"
    )
    print("  wrote learning-lab/notebooks/01_lending_kpis.ipynb")
    print("  wrote learning-lab/notebooks/02_eda_credit.ipynb")

    print("\\nDone. Run: python ai-factory/learning-lab/setup_db.py")
    print("Then: pip install -r learning-lab/requirements.txt")


if __name__ == "__main__":
    main()
