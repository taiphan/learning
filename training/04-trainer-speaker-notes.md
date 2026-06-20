# FE Credit BRD Training — Detailed Speaker Notes

Companion to slide deck. Use with `exports/FE-Credit-BRD-Training-Slides.pptx` and `03-trainer-slide-outline.md`.

---

## Session 1 — Why BRD Matters (2 hours)

### Slide: Learning Objectives
**Say:** "By the end of this program you will submit BRDs that BA can accept on first review — meaning your project enters IT backlog faster."

**Ask:** "How many have had a project delayed because IT came back with 20 questions?" (show of hands)

---

### Slide: Good vs Bad Request
**Story (FE Credit):**  
Regional Sales asked IT to "add a dashboard." After 6 weeks IT built the wrong metrics. Root cause: no KPI, no definition of "approval status." Rewrote as BRD with conversion rate target → delivered in 8 weeks with correct scope.

**Activity debrief:** Praise outcomes, not systems. Redirect "use AI/OCR/Kafka" to "customer cannot upload photo of payslip."

---

### Slide: Golden Rule
**Facilitator tip:** Post this on wall for Sessions 2–4:  
**"Problem + Rules, not System Design."**

---

## Session 2 — How to Write Each Section (3 hours)

### Section B — Executive Summary
**Exercise (10 min):** Give slip: *"Collections needs automation."*  
Pairs rewrite using formula. Share 2 examples.

**Common fix:** Replace "implement RPA" with "team lead spends 2 hours daily on manual export."

---

### Section C — KPIs
**FE Credit examples to write on board:**
- Digital: completion rate 58% → 68%
- POS: conversion 72% → 80%
- Collections: DPD30 roll-forward 38% → 34%

**Trap:** "Improve efficiency" — ask "How many hours? Whose hours? Measured how?"

---

### Section H — Business Rules
**Say:** "This is the section that prevents UAT fights. If you don't write the cut-off time, IT will guess 17:00 or 18:00 — and one of you will be wrong."

**Call out:** POS masking of CCCD, collections SMS frequency caps, approval authority matrix.

---

### Section M — Acceptance Criteria
**Live build (15 min):** Take volunteer use case. Write 3 AC together on whiteboard.  
Test: "Could QA run this tomorrow without calling you?"

---

### Activity 2 — Pair draft
**Coach circulation:** Check for missing **out of scope** and **baseline KPI**.  
**Time:** 40 min draft + 15 min share.

---

## Session 3 — Data, Risk & Compliance (2 hours)

### Co-present with Risk
**Risk owns:** Section N interpretation, data classification, escalation paths.

**Case study:** Hypothetical — "Upload customer list to personal Google Sheet for campaign." Walk through why BRD would be rejected and what alternative to offer.

---

### Remote access slide
**Link to bank policy:** Managed device, no personal cloud. BRD stating "sales download loan file to home PC" auto-triggers Security — explain this is not blocker, it's routing to controlled options (VDI, browser view).

---

### Activity 3
Hand out printed compliance screening from 3 samples (POS, eKYC, Collections). Groups decide routing.  
**Answer key:** All three need some form of Risk; eKYC also Security; Collections also Legal template.

---

## Session 4 — Workshop & Certification (3 hours)

### Peer review protocol
1. Presenter: 5 min problem + 3 min scope + 2 min AC
2. Peers: silent scoring on checklist (5 min)
3. BA coach: top 3 improvements (2 min)
4. No debating technology

**Certification:** Score ≥ 80% on real BRD + sponsor sign-off + attendance.

---

### Closing script
> "Starting [date], IT will not start FRD without an accepted BRD. You now have templates, samples, office hours, and a form. Your sponsor is part of this — not IT blocking you."

---

## Facilitator FAQ — quick answers

| Question | Answer |
|----------|--------|
| "How long should BRD be?" | 5–15 pages typical; completeness over length |
| "Can I submit in Vietnamese?" | Yes — use bilingual template; AC can be VI |
| "Who is my sponsor?" | Your Director+ who owns budget/outcome |
| "IT said no — can I skip BRD?" | No for project work; use BRD for exception path too |
| "Small change — still need BRD?" | Use change request threshold: <5 days dev may use lite form (define locally) |

---

## Materials checklist (per session)

- [ ] Slide deck loaded
- [ ] Printed cheat sheets (count = attendees)
- [ ] Quality checklist handout
- [ ] Sample BRDs (1 per table)
- [ ] Whiteboard markers
- [ ] ServiceNow form URL on last slide
- [ ] Sign-in sheet for certification attendance

---

*Speaker notes v1.0 | FE Credit BRD Training Package*
