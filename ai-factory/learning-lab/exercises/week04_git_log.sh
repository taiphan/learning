#!/bin/bash
# Week 4 — Git practice (run from your learning repo root)
set -e
echo "=== Recent commits ==="
git log --oneline -10 2>/dev/null || echo "Initialize repo: git init && git add . && git commit -m 'chore: week04 first commit'"
echo ""
echo "=== Status ==="
git status -sb 2>/dev/null || true
