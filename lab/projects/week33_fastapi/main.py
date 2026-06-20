"""Weeks 33–34 — FastAPI policy copilot. pip install fastapi uvicorn"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "lib"))
from rag_simple import TfidfIndex, load_policy_chunks

POLICY = Path(__file__).resolve().parent.parent.parent / "data" / "sample_policy.txt"
_index = TfidfIndex(load_policy_chunks(POLICY))

app = FastAPI(title="Policy Copilot Lab")

class AskRequest(BaseModel):
    question: str = Field(..., min_length=3, max_length=500)

class AskResponse(BaseModel):
    answer: str
    sources: list
    confidence: float

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/ask", response_model=AskResponse)
def ask(req: AskRequest):
    resp = _index.answer(req.question)
    return AskResponse(**resp)
