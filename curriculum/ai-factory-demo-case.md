# AI Factory Demo Case — Policy Copilot (filled example)

Use this as a **reference** when completing Track B templates. Replace numbers with your lab results.

---

## Use case intake (G1)

| Field | Value |
|-------|-------|
| **Name** | Credit Policy Copilot |
| **Business owner** | Head of Credit Policy |
| **Problem** | Branch staff spend **12–15 min** per complex case searching PDF policy + asking seniors |
| **Baseline** | ~400 lookups/day × 12 min ≈ **80 staff-hours/day** |
| **Target** | **&lt;2 min** median lookup; **≥90%** answers cite source chunk |
| **Risk tier** | **High** (influences credit decisions; human approves final action) |
| **Data** | Internal policy markdown, approved BRD exports, `sample_policy.txt` |

---

## Value case (H1 style)

| Metric | Baseline | Target (12 mo) | Assumption |
|--------|----------|----------------|------------|
| Lookup time | 12 min | 2 min | 80% adoption on pilot branches |
| Senior escalations | 120/day | 60/day | Copilot resolves tier-1 policy questions |
| Annual savings | — | ~**4.5B VND** equiv. | 80h/day × 250 days × loaded cost (illustrative) |

**Model link:** N/A (GenAI); **eval link:** grounded-response rate from `week32_run_eval.py`

---

## Governance (H2 summary)

| Gate | Pass criteria |
|------|----------------|
| G1 Intake | Value case signed by Policy owner |
| G2 Pre-deploy | Eval ≥85% grounded; PII redaction; escalation path tested |
| G3 In-life | Weekly eval sample; re-index on policy change |

**Escalation:** No source chunk → “Cannot answer — escalate to regional credit desk.”

---

## 90-day pilot (H3 excerpt)

| Phase | Deliverable |
|-------|-------------|
| 0–30 | 10-branch pilot; baseline time study |
| 30–60 | FastAPI `/ask` + audit log; governance sign-off |
| 60–90 | Expand to 50 branches; hire 1 LLM engineer |

---

## Steering ask (H4 slide 5)

- **Approve:** 50-branch pilot Q2
- **Fund:** 1 FTE LLM engineer + vector DB hosting
- **Metric:** Review grounded rate monthly with Risk committee

---

## Connect to your lab

| Artifact | Path |
|----------|------|
| RAG CLI | `lab/exercises/week25_rag_cli.py` |
| Policy RAG project | `lab/projects/policy-rag/` |
| Agent | `lab/projects/policy-copilot-agent/` |
| API | `lab/projects/week33_fastapi/` |
| BRD corpus | Export from [apps/brd/](../apps/brd/) |

Update this file with **your** eval % and dates as you progress.
