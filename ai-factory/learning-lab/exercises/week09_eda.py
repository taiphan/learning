#!/usr/bin/env python3
"""Weeks 9–11 — EDA on sample_loans (proxy for credit dataset). pip install pandas"""
import pandas as pd
from pathlib import Path

df = pd.read_csv(Path(__file__).resolve().parent.parent / "data" / "sample_loans.csv")
df["dti"] = df["existing_debt_vnd"] / df["monthly_income_vnd"]
df["high_dti"] = df["dti"] > 0.4

print("=== EDA Summary ===")
print(df.describe())
print("\n=== Business insights (BRD language) ===")
by_region = df.groupby("region")["loan_amount_vnd"].mean()
top = by_region.idxmax()
print(f"1. Region {{top}} has highest avg loan ({{by_region[top]:,.0f}} VND) — prioritize capacity planning.")
print(f"2. {{df['high_dti'].mean():.0%}} of applications exceed 40% DTI — tighten policy segment.")
print(f"3. Employment <12mo: {{(df['employment_months']<12).sum()}} apps — align with week02 rules.")
