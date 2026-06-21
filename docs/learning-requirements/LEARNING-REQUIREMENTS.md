# Learning Platform Requirements

**Version:** 2.0.0 · **App:** 2.0.0 · **Curriculum:** 1.3 · **Updated:** 2026-06-21

| | |
|---|---|
| **Live app** | [taiphan.github.io/learning](https://taiphan.github.io/learning/) |
| **BRD app** | [/brd/](https://taiphan.github.io/learning/brd/) |
| **Changelog** | [CHANGELOG.md](./CHANGELOG.md) |
| **Video enrichment** | [video-learning-enrichment.md](../../curriculum/video-learning-enrichment.md) |

---

## How to read this doc

Follow **top to bottom once**, then use **§4 Weekly loop** every week.

| Section | When to use |
|---------|-------------|
| §1 Quick start | First day |
| §2 System map | Once — understand 3 parts |
| §3 Setup | Once — Python + lab |
| §4 Weekly loop | **Every week** |
| §5 Track B | Milestone weeks 8, 16, 28, 40, 52 |
| §6 Week 1 | First week only |
| §7 Progress | When checking gates |
| §8 Video | Optional 2–3h/week |
| §9 In-app guide | First visit / click **Guide** |
| §10 Done right | Self-check |
| §11 Fix problems | When stuck |

**Version check:** App footer shows `Req · App · Curr` versions. They must match this header. If not, hard-refresh or redeploy ([§11](#11-troubleshooting)).

---

## 1. Quick start (5 minutes)

1. Open the [Learning app](https://taiphan.github.io/learning/).
2. Complete the **12-step Guide tour** (or click **Skip**, then **Take the guided tour** later).
3. Click **Start at Week 1** or **Continue**.
4. Read **Overview** → do **Lab** → mark week complete.

**Time budget:** 10 h/week = **~8h Track A** (every week) + **~2h Track B** (weeks 8, 16, 28, 40, 52 only).

---

## 2. System map (three parts)

```
Learning app     →  plan, progress, tabs
      ↓
BRD app (/brd/)  →  export .md for Week 1+ exercises
      ↓
lab/             →  run commands from Lab tab
```

| Part | Path | You do |
|------|------|--------|
| Learning | `apps/learning/` | Study, track weeks, Track B templates |
| BRD | `apps/brd/` | Draft BRDs, export Markdown |
| Lab | `lab/` | Python exercises + portfolio + `delivery/track-b/` |

---

## 3. One-time setup

| # | Requirement | Verify |
|---|-------------|--------|
| P1 | Browser (Chrome, Safari, Firefox, Edge) | App loads |
| P2 | Repo cloned | `learning/` on disk |
| P3 | Python 3.11+ | `python3 --version` |
| P4 | Lab deps | `cd lab && pip install -r requirements.txt` |
| P5 | SQLite (weeks 5–7) | `cd lab && python3 setup_db.py` |
| P6 | IDE (Cursor) | Open `lab/exercises/` |
| P7 | **Optional** Google sync | [AUTH-SETUP.md](../../apps/learning/AUTH-SETUP.md) — Firebase + Sign in |

**Progress storage:** Without P7, header shows **Local** (browser only). With Google sign-in, progress merges to Firestore.

**Local app (if Pages is stale):**

```bash
cd apps/learning && python3 -m http.server 8081
```

**Regenerate after curriculum edits:**

```bash
python3 curriculum/generate_all_learning.py
```

---

## 4. Weekly loop (repeat every week)

| Step | Tab / action | Time | Done when |
|------|----------------|------|-----------|
| 1 | **Continue** or pick week in sidebar | — | Right week open |
| 2 | **Overview** — deliverable + bridge banner | 15 min | You know the deliverable |
| 3 | **Study** — readings + links | 2–3 h | Ready for lab |
| 4 | **Lab** — run command from `lab/` | 4–5 h | Output matches **Done when** |
| 5 | **Leadership** — only on milestone weeks | 0–2 h | See [§5](#5-track-b--head-of-ai) |
| 6 | **Notes** — optional | — | Saved in browser |
| 7 | Footer — **Mark week complete** | — | Pill `x / 52` updates |
| 8 | **Next week →** | — | — |

**Rule:** Do not mark complete until the lab deliverable passes. Video alone does not count.

---

## 5. Track B — Head of AI

Track B is **leadership rehearsal** (Y4 Head of AI Factory), **not** Y1 job apply.

| Week | ID | Save to |
|------|-----|---------|
| 8 | H0 AI strategy | `lab/delivery/track-b/h0-ai-strategy.md` |
| 16 | H1 PD value case | `lab/delivery/track-b/h1-pd-value-case.md` |
| 28 | H2 Copilot governance | `lab/delivery/track-b/h2-copilot-governance.md` |
| 40 | H3 90-day plan | `lab/delivery/track-b/h3-ninety-day-plan.md` |
| 52 | H4 Steering deck | `lab/delivery/track-b/h4-steering-deck.md` |

**Milestone week:** Leadership tab → fill template → save file → mark Track B complete.  
**Other weeks:** Leadership tab shows next milestone only; focus on Track A.

---

## 6. Week 1 (BRD bridge)

1. **Learning app** → Week 1 → Overview bridge.
2. **BRD app** → draft BRD → **Export** `.md`.
3. **Lab:**

```bash
cd lab
python3 exercises/week01_brd_checklist.py /path/to/your-export.md
```

4. Fix until checklist passes → mark Week 1 complete.

---

## 7. Progress & Y1 gates

**Browser storage:** weeks done, Track B done, notes (`localStorage` — this device only).

| UI | Meaning |
|----|---------|
| `x / 52` | Weeks complete |
| `B x/5` | Track B milestones |
| Sidebar checkpoints | CP0–CP6 technical gates |
| Quarter bar | Weeks done in current Y1 quarter |

| Quarter | Weeks | Career gate |
|---------|-------|-------------|
| Y1 Q1 | 1–12 | Ship code + BRD bridge |
| Y1 Q2 | 13–24 | Portfolio piece 1 (ML) |
| Y1 Q3 | 25–36 | Portfolio piece 2 (GenAI + API) |
| Y1 Q4 | 37–52 | Apply AI Engineer (OCB · NAB · VPBank) |

Full timeline: [career-timeline.md](../../curriculum/career-timeline.md).

---

## 8. Free video (optional)

**2–3 h/week max** — supplement Study tab, never replace Lab.

- App Home → **Free video learning** (by quarter)
- Full list: [video-learning-enrichment.md](../../curriculum/video-learning-enrichment.md)

**Priority free stack:** Kaggle Learn → StatQuest (YouTube) → DeepLearning.AI short courses → Class Central free Coursera list.

---

## 9. In-app guide

| Feature | How |
|---------|-----|
| First visit | Auto 12-step tour |
| Replay | Header **Guide** |
| Cheat sheet | Home **How to use this app** card |
| Written doc | This file |

---

## 10. Acceptance criteria

| # | You are on track when… |
|---|------------------------|
| AC1 | Each week starts from Continue or `#week/N` |
| AC2 | Lab command runs from `lab/` before week marked complete |
| AC3 | Track B files exist on weeks 8, 16, 28, 40, 52 |
| AC4 | Week 1 BRD passed `week01_brd_checklist.py` |
| AC5 | You know current quarter gate (header chip + sidebar) |
| AC6 | Portfolio repos progress in Q2–Q3 ([PORTFOLIO.md](../../lab/projects/PORTFOLIO.md)) |
| AC7 | Y1 Q4 = apply AI Engineer; H4 deck is for leadership practice, not HoAI apply |

---

## 11. Troubleshooting

| Problem | Fix |
|---------|-----|
| Blank app / JSON error | Use http server or GitHub Pages, not `file://` |
| No Track B / old phases | Hard-refresh; footer versions should be **2.0.0 / 2.0.0 / 1.3** |
| Version mismatch banner | Run `generate_all_learning.py` + redeploy Pages |
| Progress lost | Browser data cleared — re-mark weeks; Git lab work is source of truth |
| Lab fails | `cd lab` first; reinstall `requirements.txt` |

**Maintainers — deploy:**

```bash
gh workflow run deploy-pages.yml --ref main
```

---

## 12. Version control (maintainers)

| File | Role |
|------|------|
| `curriculum/requirements_manifest.py` | **Bump versions here** + CHANGELOG entry |
| `curriculum/learning_data.py` | Week content (`META.version` = curriculum) |
| `apps/learning/config.js` | `APP_VERSION` must match manifest |
| `apps/learning/requirements-manifest.json` | Generated — do not edit by hand |
| `docs/learning-requirements/CHANGELOG.md` | Human-readable history |

**Release checklist:**

1. Edit `requirements_manifest.py` (versions + CHANGELOG[0] or new entry).
2. Update this doc header if requirements changed.
3. Run `python3 curriculum/generate_all_learning.py`.
4. Verify app footer versions match.
5. Commit + deploy Pages.

---

*Requirements **2.0.0** · App **2.0.0** · Curriculum **1.3***
