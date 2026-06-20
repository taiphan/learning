#!/usr/bin/env python3
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
lines.append("\nRecommend revisit if DTI improves below 40%.")
story.write_text("\n".join(lines))
print(story.read_text())
