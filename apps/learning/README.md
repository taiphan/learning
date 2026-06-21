# 52-Week Learning App

Browser cockpit for your **Y1 AI Engineer path** — dual track (8h Track A + 2h Track B), quarter gates, progress, and lab wiring.

**Live:** [taiphan.github.io/learning](https://taiphan.github.io/learning/) · **BRD app:** `/brd/`

**Step-by-step usage:** [docs/learning-requirements/LEARNING-REQUIREMENTS.md](../../docs/learning-requirements/LEARNING-REQUIREMENTS.md) (v2.0)

**Version control:** `curriculum/requirements_manifest.py` → `requirements-manifest.json` (footer in app)

**Google sign-in (optional):** [AUTH-SETUP.md](../../apps/learning/AUTH-SETUP.md) — sync progress with Firebase

**In-app guide:** First visit opens a 12-step tour; click **Guide** in the header to replay.

---

## How the system fits together

Three apps, one repo:

| App | Path | Role |
|-----|------|------|
| **Learning** (this) | `apps/learning/` | 52-week curriculum, progress, study/lab/leadership tabs |
| **BRD Intake** | `apps/brd/` | Week 1+ bridge — draft BRDs, export `.md` for Python exercises |
| **Lab** | `lab/` | Run commands from the Lab tab (`pip install -r requirements.txt`) |

**Data flow:**

```
curriculum/learning_data.py  →  learning-data.json  →  app.js (fetch)
                              ↘  slide decks (exports/learning/)
                              ↘  lab/exercises/week*.py
```

Progress is stored in **localStorage** only (`learning-ai-learning-progress`) — weeks complete, Track B milestones, notes, last tab.

---

## Your weekly loop (10 hrs)

1. Open **Continue** or `#week/N` from home.
2. **Overview** — deliverable + bridge banner (BRD app, quarter gate, Track B save path).
3. **Study** — readings and resources for the skill block.
4. **Lab** — open exercise in Cursor, run command from `lab/`, check “done when”.
5. **Leadership** (weeks 8, 16, 28, 40, 52) — fill HoAI template, save to `lab/delivery/track-b/h*.md`.
6. Mark week complete → next week.

**Y1 quarters (Track A):**

| Quarter | Weeks | Career gate |
|---------|-------|-------------|
| Q1 Technologist | 1–12 | Ship code + BRD bridge |
| Q2 ML hire signal | 13–24 | Portfolio piece 1 (classical ML) |
| Q3 GenAI production | 25–36 | Portfolio piece 2 (GenAI + API) |
| Q4 Apply | 37–52 | Apply AI Engineer (OCB · NAB · VPBank) |

**Track B (Head of AI Factory):** H0–H4 at weeks 8, 16, 28, 40, 52 — long-term Y4 target, not Y1 apply.

Full alignment: [`curriculum/career-timeline.md`](../../curriculum/career-timeline.md).

---

## Run locally

```bash
cd apps/learning
python3 -m http.server 8081
# http://localhost:8081
```

Use a local server (not `file://`) so `learning-data.json` loads.

---

## Regenerate curriculum

After editing `curriculum/learning_data.py`:

```bash
python3 curriculum/generate_all_learning.py
```

Or JSON only:

```bash
python3 -c "import sys; sys.path.insert(0,'curriculum'); from learning_loader import export_json; export_json()"
```

---

## Key files

| File | Purpose |
|------|---------|
| `app.js` | Routing, progress, week/home render |
| `config.js` | Phase colors, tips, deck URLs, Track B delivery filenames |
| `learning-data.json` | Exported curriculum (do not edit by hand) |
| `styles.css` | Layout and quarter / Track B styling |

---

## Related

- [Learning lab](../../lab/README.md)
- [Track B guide](../../curriculum/head-of-ai-track.md) · [Delivery playbook](../../curriculum/track-b-delivery.md)
- [Job skills / VPBank map](../../curriculum/job-skills-adaptation.md)
- Decks: `decks/Learning-Master-Slides.pptx`, `Zero-to-AI-Expert-Roadmap-Slides.pptx`, `Learning-Track-B-Slides.pptx`
