# Week 28 — Policy Copilot Governance (Track B · H2)

**Time:** ~2 hours · **Read:** `curriculum/governance-mlops.md` §1–3

---

## Use case

| Field | Value |
|-------|-------|
| System | Policy RAG / copilot |
| Users | Branch staff, credit officers |
| Decision impact | Supports credit decisions (not auto-approve) |
| **Risk tier** | ☐ Low ☐ Medium ☑ High ☐ Critical |

---

## Gate G1 — Intake (before build)

| Criterion | Pass? | Owner | Evidence |
|-----------|-------|-------|----------|
| Business value case | | Credit Policy | Week 16-style metric |
| Data availability | | | `sample_policy.txt` + BRD exports |
| Legal basis / consent | | Legal | |
| Risk tier assigned | | GRC | This doc |

---

## Gate G2 — Pre-deploy (before prod)

| Criterion | Pass? | Owner | Evidence |
|-----------|-------|-------|----------|
| Validation / eval ≥85% grounded | | Model owner | `week32_run_eval.py` |
| Bias / fairness review | | Risk | |
| Security & PII | | IT Security | Week 37 guardrails |
| Explainability / citations | | | Source chunk in answer |

---

## Gate G3 — In-life (continuous)

| Criterion | Cadence | Owner | Tool |
|-----------|---------|-------|------|
| Performance vs baseline | Weekly | MLOps | Eval harness |
| Drift in policy corpus | On change | Policy | Re-index job |
| Cost (tokens) | Monthly | Platform | Dashboard |
| Audit trail | Always | GRC | Logs |

---

## Escalation rule

When confidence &lt; ___ or no source chunk → **human escalation** (not silent guess).

---

## Done when

- [ ] All G1 rows filled
- [ ] G2 linked to your eval % from lab
- [ ] Saved beside `projects/policy-rag/README.md`
