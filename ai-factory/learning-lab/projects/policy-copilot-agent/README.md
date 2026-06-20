# policy-copilot-agent (week 31)

Three tools: `policy_lookup`, `dti_calculator`, `escalate`.

```bash
python agent.py "Max DTI?"
python agent.py "calculate dti income"
```

## State diagram
```
START → RETRIEVE → (low confidence?) → ESCALATE
                 → ANSWER → END
```
