# Learning Platform — Changelog

Versions are aligned across **requirements doc**, **app**, and **curriculum JSON**.

| Component | Source of truth |
|-----------|-----------------|
| Requirements | `docs/learning-requirements/LEARNING-REQUIREMENTS.md` |
| Versions | `curriculum/requirements_manifest.py` |
| App manifest | `apps/learning/requirements-manifest.json` (generated) |
| Curriculum | `curriculum/learning_data.py` → `learning-data.json` |

**Bump rule:** When you change behavior, update `requirements_manifest.py` (version + CHANGELOG entry) and run:

```bash
python3 curriculum/generate_all_learning.py
```

---

## 2.1.0 — 2026-06-21

| Layer | Version |
|-------|---------|
| Requirements | 2.0.0 |
| App | 2.1.0 |
| Curriculum | 1.3 |

- **Google sign-in** (Firebase Auth) + Firestore progress sync
- Setup: `apps/learning/AUTH-SETUP.md`
- Without Firebase config: **Local** pill, localStorage only (unchanged behavior)

---

## 2.0.0 — 2026-06-21

| Layer | Version |
|-------|---------|
| Requirements | 2.0.0 |
| App | 2.0.0 |
| Curriculum | 1.3 |

- Consolidated **LEARNING-REQUIREMENTS.md** (single doc: quick start → weekly loop → tracks → video → troubleshooting)
- Exported **requirements-manifest.json** to app; footer shows live versions
- In-app **Guide** tour (12 steps) + **Free video learning** card
- Video enrichment guide: `curriculum/video-learning-enrichment.md`
- Supersedes scattered copy in `docs/15-learning-app-usage-requirements.md`

---

## 1.2.0 — 2026-06-20

| Layer | Version |
|-------|---------|
| Requirements | 1.0.0 |
| App | 1.2.0 |
| Curriculum | 1.2 |

- Y1 quarters (Q1–Q4) aligned with career timeline
- Track B Head of AI milestones (H0–H4)
- Career path card on home
- First usage requirements doc (`docs/15-…`)

---

## 1.0.0 — 2026-06-19

| Layer | Version |
|-------|---------|
| Requirements | 1.0.0 |
| App | 1.0.0 |
| Curriculum | 1.0 |

- Initial learning app, BRD bridge, 52-week `learning_data.py`
