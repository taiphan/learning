# credit-pd-model (weeks 13–16)

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
