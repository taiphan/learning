"""Lightweight TF-IDF RAG — no API keys required (weeks 21, 25, 32)."""

from __future__ import annotations

import json
import math
import re
from collections import Counter
from pathlib import Path


def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z0-9%]+", text.lower())


def chunk_text(text: str, max_words: int = 80) -> list[str]:
    words = text.split()
    chunks: list[str] = []
    for i in range(0, len(words), max_words):
        chunks.append(" ".join(words[i : i + max_words]))
    return [c for c in chunks if c.strip()]


class TfidfIndex:
    def __init__(self, docs: list[str]):
        self.docs = docs
        self.doc_tokens = [tokenize(d) for d in docs]
        self.df: Counter[str] = Counter()
        for toks in self.doc_tokens:
            self.df.update(set(toks))
        self.n = len(docs)

    def _tfidf_vec(self, tokens: list[str]) -> dict[str, float]:
        tf = Counter(tokens)
        vec: dict[str, float] = {}
        for term, count in tf.items():
            idf = math.log((1 + self.n) / (1 + self.df[term])) + 1
            vec[term] = count * idf
        return vec

    @staticmethod
    def _cosine(a: dict[str, float], b: dict[str, float]) -> float:
        keys = set(a) | set(b)
        dot = sum(a.get(k, 0) * b.get(k, 0) for k in keys)
        na = math.sqrt(sum(v * v for v in a.values()))
        nb = math.sqrt(sum(v * v for v in b.values()))
        return dot / (na * nb) if na and nb else 0.0

    def search(self, query: str, top_k: int = 3) -> list[tuple[int, float, str]]:
        qv = self._tfidf_vec(tokenize(query))
        scored = []
        for i, toks in enumerate(self.doc_tokens):
            score = self._cosine(qv, self._tfidf_vec(toks))
            scored.append((i, score, self.docs[i]))
        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[:top_k]

    def answer(self, query: str, min_score: float = 0.05) -> dict:
        hits = self.search(query, top_k=3)
        if not hits or hits[0][1] < min_score:
            return {
                "answer": "I don't know — escalate to policy team.",
                "sources": [],
                "confidence": 0.0,
            }
        best = hits[0]
        return {
            "answer": best[2],
            "sources": [{"index": i, "score": round(s, 3), "text": t[:200]} for i, s, t in hits],
            "confidence": round(best[1], 3),
        }


def load_policy_chunks(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    return chunk_text(text)


def run_eval(index: TfidfIndex, questions_path: Path) -> dict:
    items = json.loads(questions_path.read_text(encoding="utf-8"))
    passed = 0
    for item in items:
        resp = index.answer(item["question"])
        text = resp["answer"].lower()
        ok = all(k.lower() in text for k in item.get("expected_contains", []))
        if ok and resp["confidence"] > 0:
            passed += 1
    rate = passed / len(items) if items else 0.0
    return {"total": len(items), "passed": passed, "grounded_rate": rate}
