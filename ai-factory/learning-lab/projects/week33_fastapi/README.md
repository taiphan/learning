# FastAPI policy copilot (weeks 33–34)

```bash
cd learning-lab/projects/week33_fastapi
pip install fastapi uvicorn
uvicorn main:app --reload
curl http://127.0.0.1:8000/health
curl -X POST http://127.0.0.1:8000/ask -H 'Content-Type: application/json' -d '{"question":"Max DTI?"}'
pytest test_health.py
```
