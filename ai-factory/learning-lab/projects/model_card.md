# Model card — credit-pd-model (lab)

## Purpose
Proxy default risk model for learning — not production credit decisioning.

## Limits
- Trained on 10-row synthetic lab data only.
- Not validated against SBV requirements.

## Governance gates
1. Human review for all declines in production.
2. SHAP narrative required for adverse action.
3. Monthly AUC drift monitoring.
