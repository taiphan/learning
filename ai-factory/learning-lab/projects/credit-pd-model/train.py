#!/usr/bin/env python3
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
