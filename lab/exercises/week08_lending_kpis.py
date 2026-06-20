#!/usr/bin/env python3
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
print("\nBy region:")
print(df.groupby("region")["loan_amount_vnd"].agg(["count", "sum", "mean"]).to_string())
try:
    import matplotlib.pyplot as plt
    df.groupby("region")["loan_amount_vnd"].sum().plot(kind="bar", title="Disbursement by region")
    out = Path(__file__).resolve().parent.parent / "outputs" / "week08_region_bar.png"
    out.parent.mkdir(exist_ok=True)
    plt.savefig(out)
    print(f"\nChart saved: {out}")
except ImportError:
    print("\nInstall matplotlib for chart: pip install matplotlib")
