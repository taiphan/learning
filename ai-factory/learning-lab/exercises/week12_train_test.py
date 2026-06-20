#!/usr/bin/env python3
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
