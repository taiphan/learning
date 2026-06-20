#!/usr/bin/env python3
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
