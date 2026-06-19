#!/usr/bin/env python3
"""Generate Word and PowerPoint deliverables from FE Credit BRD training package."""

from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Inches, Pt
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches as PInches, Pt as PPt
from pptx.dml.color import RGBColor

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "exports"
OUTPUT.mkdir(exist_ok=True)


def add_heading(doc, text, level=1):
    doc.add_heading(text, level=level)


def generate_brd_template_docx():
    src = ROOT / "docs" / "01-brd-template-en.md"
    doc = Document()
    doc.add_heading("FE CREDIT — BUSINESS REQUIREMENTS DOCUMENT (BRD)", 0)
    p = doc.add_paragraph()
    p.add_run("Template v1.0 | Internal use only").italic = True
    doc.add_paragraph(
        "Instructions: Complete all mandatory sections. Write what the business needs and why — "
        "not how IT should build it. Obtain Business Sponsor sign-off before IT/BA intake."
    )

    sections = [
        ("A. REQUEST INFORMATION", [
            "BRD Title:", "Business Unit:", "Requester Name:", "Requester Email:",
            "Business Sponsor (Director+):", "Date Submitted:", "Target Go-Live Date:",
            "Priority Category:", "Regulatory Deadline (if applicable):",
        ]),
        ("B. EXECUTIVE SUMMARY", [
            "Business problem:", "Who is impacted:", "Business impact if not addressed:",
            "Proposed business outcome (one sentence):",
        ]),
        ("C. BUSINESS OBJECTIVES & SUCCESS METRICS", [
            "Objective 1 — Baseline / Target / Measurement:",
            "Objective 2 — Baseline / Target / Measurement:",
            "Objective 3 — Baseline / Target / Measurement:",
        ]),
        ("D. BACKGROUND & CURRENT STATE", [
            "Current process (step-by-step):", "Current systems involved:",
            "Volume and frequency:",
        ]),
        ("E. PROPOSED TO-BE STATE", [
            "Desired future process (business view only):", "Expected changes:",
        ]),
        ("F. SCOPE", ["In scope:", "Out of scope:", "Assumptions:", "Dependencies:"]),
        ("G. STAKEHOLDERS & USERS", ["Role / Department / # users / Location / Access:"]),
        ("H. BUSINESS RULES", [
            "Eligibility rules:", "Approval authority:", "Pricing/fees (business level):",
            "Exception handling:", "Cut-off times:", "Customer communication rules:",
        ]),
        ("I. DATA & SECURITY REQUIREMENTS", [
            "Data types:", "Classification:", "Data sharing:", "Retention:",
            "Audit requirements:", "Customer consent:", "Remote access implications:",
        ]),
        ("J. REPORTING & CONTROLS", [
            "Reports required:", "Control points:", "Reconciliation:", "Fraud/risk controls:",
        ]),
        ("K. IMPLEMENTATION & ROLLOUT", [
            "Rollout approach:", "Training needs:", "Language:", "Business continuity fallback:",
        ]),
        ("L. RISKS", ["Operational / Customer / Financial / Compliance risks:"]),
        ("M. ACCEPTANCE CRITERIA (min 5)", [
            "AC-01: Given / When / Then",
            "AC-02: Given / When / Then",
            "AC-03: Given / When / Then",
            "AC-04: Given / When / Then",
            "AC-05: Given / When / Then",
        ]),
        ("N. COMPLIANCE SCREENING", [
            "Changes origination/disbursement? Y/N",
            "Changes interest/fees/contract? Y/N",
            "Sends customer notifications? Y/N",
            "Third-party data exchange? Y/N",
            "Affects collections/legal? Y/N",
            "Audit trail required? Y/N",
            "Exposes data on POS/field devices? Y/N",
        ]),
        ("O. APPROVALS", [
            "Business Requester:", "Business Sponsor:", "Business Unit Head:",
            "Risk/Compliance (if required):", "Data Owner (if required):",
        ]),
    ]

    for title, fields in sections:
        add_heading(doc, title, level=1)
        for field in fields:
            doc.add_paragraph(field)
            doc.add_paragraph("_" * 60)

    out = OUTPUT / "FE-Credit-BRD-Template.docx"
    doc.save(out)
    print(f"Created {out}")
    return out


def generate_cheat_sheet_docx():
    doc = Document()
    doc.add_heading("FE Credit BRD Cheat Sheet", 0)

    for lang_title, items in [
        ("Tiếng Việt (POS / hiện trường)", [
            "Bắt đầu bằng vấn đề — không bắt đầu bằng hệ thống",
            "Có số liệu: %, giờ, số KH",
            "Ghi rõ ai dùng: vai trò, số người, địa điểm",
            "Quy tắc nghiệp vụ: ai duyệt, giờ cắt, ngoại lệ",
            "Trong phạm vi + ngoài phạm vi",
            "Dữ liệu & tuân thủ: PII, CIC, SMS",
            "Tiêu chí nghiệm thu: Cho trước / Khi / Thì (≥5)",
            "Xin Sponsor (Giám đốc+) ký trước khi gửi IT",
        ]),
        ("English (HQ / Digital / Collections)", [
            "Start with the problem, not the system",
            "Quantify impact: %, hours, customers, VND",
            "Define who uses it: role, count, location",
            "Document business rules: approval, cut-off, exceptions",
            "Write in-scope AND out-of-scope",
            "Complete data & compliance section honestly",
            "Add acceptance criteria: Given/When/Then (min 5)",
            "Get Sponsor sign-off before IT intake",
        ]),
    ]:
        add_heading(doc, lang_title, level=1)
        for i, item in enumerate(items, 1):
            doc.add_paragraph(f"{i}. {item}", style="List Number")

    add_heading(doc, "Compliance triggers → Route to", level=1)
    table = doc.add_table(rows=1, cols=2)
    table.style = "Table Grid"
    hdr = table.rows[0].cells
    hdr[0].text = "If BRD includes..."
    hdr[1].text = "Route to"
    rows = [
        ("Loan approval / disbursement change", "Risk + Credit Policy"),
        ("Interest / fees / contract change", "Legal + Finance"),
        ("Customer SMS / email", "Legal (template)"),
        ("Third-party data sharing", "Vendor Risk + Legal"),
        ("Collections / legal process", "Compliance"),
        ("Data on POS / home device", "Security"),
    ]
    for a, b in rows:
        row = table.add_row().cells
        row[0].text = a
        row[1].text = b

    out = OUTPUT / "FE-Credit-BRD-Cheat-Sheet.docx"
    doc.save(out)
    print(f"Created {out}")
    return out


SLIDES = [
    ("FE Credit BRD Training", "Write requirements IT can deliver — without rework\nSession 1 of 4"),
    ("Learning Objectives", "• Write a complete BRD using FE Credit template\n• Separate business need from technical solution\n• Define testable acceptance criteria\n• Pass BRD quality gate (≥ 80%)"),
    ("Why We Are Here", "• High volume of IT requests from business\n• Rework costs: delay, UAT defects, compliance risk\n• Goal: faster triage, predictable delivery"),
    ("What Is a BRD?", "Document describing:\n• Business problem\n• Outcomes and KPIs\n• Business rules and scope\n\nNOT: technical design, vendor selection, project plan"),
    ("BRD vs Other Documents", "BRD → Business owns\nFRD → BA + IT\nTechnical Design → IT\nUAT → Business + QA"),
    ("FE Credit Context", "• FE ONLINE 2.0, $NAP, SHIELD (customer apps)\n• Finacle LMS, CIF, Assure on AWS\n• POS/LOS, FirstVision cards, Collections\n• ~13k POS, SBV compliance expectations"),
    ("Request Journey", "Business BRD → BA review → IT triage → Risk (if needed)\n→ FRD → Build → UAT → Go-live"),
    ("Good vs Bad Request", "BAD: 'Build Kafka API to Finacle'\nGOOD: 'POS needs same-day approval visibility during customer visit'"),
    ("The Golden Rule", "Write the PROBLEM and RULES,\nnot the SYSTEM DESIGN."),
    ("Problem Statement Formula", "[Role] cannot [task] because [constraint],\ncausing [impact].\n\nExample: POS staff cannot confirm approved installment plan during customer visit, causing 18% drop-off."),
    ("Objectives Must Be Measurable", "WEAK: Improve customer experience\nSTRONG: Reduce disbursement TAT from 24h to 4h for POS motorbike loans"),
    ("Scope: In AND Out", "In scope: what this project delivers\nOut of scope: prevents scope creep\n\nAlways write both."),
    ("Business Rules — IT Must Not Guess", "• Eligibility\n• Approval authority\n• Cut-off times\n• Exceptions\n• Customer communication"),
    ("Acceptance Criteria", "Given [context]\nWhen [action]\nThen [expected result]\n\nMinimum 5 per BRD → becomes UAT tests"),
    ("Data & Compliance", "• Classify data: Public / Internal / Confidential / Restricted\n• Complete Section N screening\n• Route to Risk if customer data on POS or notifications"),
    ("Top 10 BRD Mistakes", "1. Solution not need\n2. No KPI baseline\n3. Missing business rules\n4. No out-of-scope\n5. Multiple projects in one BRD\n6. No acceptance criteria\n7. No sponsor\n8. Ignoring POS training\n9. No data classification\n10. Vendor brochure copy-paste"),
    ("BRD Quality Gate", "• Score ≥ 80% on quality rubric\n• Sponsor sign-off\n• All mandatory sections complete\n• Then → IT triage"),
    ("Certification: BRD Ready", "• Attend all 4 sessions\n• Submit 1 BRD scoring ≥ 80%\n• Sponsor sign-off\n• BA coach confirms readiness"),
    ("Next Steps", "• Use template on Confluence\n• Office hours: weekly BA support\n• Submit via ServiceNow/Jira BRD form\n• Questions: BA team"),
]


def _add_content_slide(prs, title, body):
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = title
    slide.placeholders[1].text = body
    return slide


def _add_pipeline_slide(prs, title, stages, subtitle=None):
    """Horizontal pipeline diagram with rounded boxes."""
    slide = prs.slides.add_slide(prs.slide_layouts[5])  # Title Only
    slide.shapes.title.text = title
    if subtitle:
        box = slide.shapes.add_textbox(PInches(0.5), PInches(1.15), PInches(12.3), PInches(0.4))
        box.text_frame.text = subtitle
        box.text_frame.paragraphs[0].font.size = PPt(14)
        box.text_frame.paragraphs[0].font.color.rgb = RGBColor(0x55, 0x55, 0x55)

    n = len(stages)
    total_w = 12.0
    box_w = min(1.55, (total_w - 0.3 * (n - 1)) / n)
    gap = 0.3
    start_x = (13.333 - (box_w * n + gap * (n - 1))) / 2
    y = PInches(3.0)
    h = PInches(0.95)
    colors = [
        RGBColor(0x1F, 0x4E, 0x79),
        RGBColor(0x2E, 0x75, 0xB6),
        RGBColor(0x5B, 0x9B, 0xD5),
        RGBColor(0x70, 0xAD, 0x47),
        RGBColor(0xED, 0x7D, 0x31),
        RGBColor(0xA5, 0xA5, 0xA5),
        RGBColor(0x44, 0x72, 0xC4),
        RGBColor(0x70, 0x30, 0xA0),
    ]

    for i, label in enumerate(stages):
        x = PInches(start_x + i * (box_w + gap))
        shape = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE, x, y, PInches(box_w), h
        )
        shape.fill.solid()
        shape.fill.fore_color.rgb = colors[i % len(colors)]
        shape.line.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        tf = shape.text_frame
        tf.text = label
        p = tf.paragraphs[0]
        p.font.size = PPt(11)
        p.font.bold = True
        p.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        p.alignment = 1  # center
        tf.word_wrap = True

        if i < n - 1:
            ax = x + PInches(box_w)
            arrow = slide.shapes.add_shape(
                MSO_SHAPE.RIGHT_ARROW, ax, PInches(3.25), PInches(gap), PInches(0.35)
            )
            arrow.fill.solid()
            arrow.fill.fore_color.rgb = RGBColor(0xBF, 0xBF, 0xBF)
            arrow.line.fill.background()

    return slide


def _add_dual_track_slide(prs):
    """Governance track (top) + Agile delivery track (bottom)."""
    slide = prs.slides.add_slide(prs.slide_layouts[5])
    slide.shapes.title.text = "Dual-Track: Governance + Agile Delivery"

    tracks = [
        ("Governance & assurance (parallel)", [
            "BRD gate", "GRC / Legal", "IT-Security", "ARB", "CAB", "Audit evidence",
        ], 1.8, RGBColor(0xC0, 0x00, 0x00)),
        ("Agile delivery (Scrum)", [
            "FSD", "Sprint plan", "Build", "SIT", "UAT", "Ship", "Hypercare",
        ], 3.6, RGBColor(0x00, 0x70, 0x50)),
    ]
    n_boxes = 7
    box_w = 1.55
    gap = 0.22
    start_x = (13.333 - (box_w * n_boxes + gap * (n_boxes - 1))) / 2

    for track_name, stages, y_in, accent in tracks:
        lbl = slide.shapes.add_textbox(PInches(0.4), PInches(y_in - 0.35), PInches(4), PInches(0.3))
        lbl.text_frame.text = track_name
        lbl.text_frame.paragraphs[0].font.bold = True
        lbl.text_frame.paragraphs[0].font.size = PPt(13)
        lbl.text_frame.paragraphs[0].font.color.rgb = accent

        for i, label in enumerate(stages):
            x = PInches(start_x + i * (box_w + gap))
            shape = slide.shapes.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE,
                x, PInches(y_in), PInches(box_w), PInches(0.75),
            )
            shape.fill.solid()
            shape.fill.fore_color.rgb = accent
            shape.line.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
            tf = shape.text_frame
            tf.text = label
            p = tf.paragraphs[0]
            p.font.size = PPt(10)
            p.font.bold = True
            p.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
            p.alignment = 1

    note = slide.shapes.add_textbox(PInches(0.5), PInches(5.0), PInches(12.3), PInches(1.2))
    note.text_frame.text = (
        "Governance track can run in parallel — it does not wait for sprint end.\n"
        "Delivery track runs in 2-week sprints; Ship only when BOTH tracks are green."
    )
    note.text_frame.paragraphs[0].font.size = PPt(14)
    return slide


def _add_scrum_cycle_slide(prs):
    """Scrum ceremony ring mapped to delivery phases."""
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = "Scrum Ceremonies Inside Delivery"
    slide.placeholders[1].text = (
        "SPRINT N (typically 2 weeks)\n"
        "──────────────────────────────────────────────────\n"
        "Mon     Sprint Planning     Pull stories from FSD → sprint backlog\n"
        "        Gate: BRD accepted, FSD linked, flags clear\n"
        "Daily   Stand-up (15 min)   Dev + SM + Ops (deploy blockers)\n"
        "        Wed   Mid-sprint      BA clarification; no new scope without change\n"
        "Fri     Code complete       Unit tests + SIT entry\n"
        "──────────────────────────────────────────────────\n"
        "SPRINT N+1 or Release sprint\n"
        "Mon     SIT / QA regression QA exit criteria\n"
        "Wed     UAT window          Business tests BRD acceptance criteria\n"
        "Thu     Sprint Review       Demo to Sponsor delegate\n"
        "Fri     Retrospective       Process improvement\n"
        "──────────────────────────────────────────────────\n"
        "RELEASE WEEK (may align with sprint boundary)\n"
        "        Release readiness   Ops checklist + CAB (IT-Governance)\n"
        "        Ship to production  Deploy + verify + hypercare handover"
    )
    return slide


IT_DELIVERY_SLIDES = [
    (
        "FE Credit IT Delivery Framework",
        "Requirement → BRD → FSD → Test → UAT → Ship → Operations Support\n"
        "Governed delivery with Agile/Scrum internal process",
    ),
    (
        "Learning Objectives",
        "• Map the end-to-end IT delivery pipeline and mandatory gates\n"
        "• Align Scrum ceremonies with BRD / FSD / release governance\n"
        "• Clarify roles: Business, Dev, IT Ops, IT-Governance, IT-Security, GRC\n"
        "• Apply evidence chain from requirement intake to operations support",
    ),
    (
        "Document Chain — Who Owns What",
        "BRD (Business Requirements)     → Business writes, Sponsor signs\n"
        "FSD / FRD (Functional Spec)     → BA + IT Product; derived from BRD\n"
        "User Stories & Tasks            → BA + Dev; traceable to FSD + BRD AC\n"
        "Test Cases (SIT)                → QA; mapped to acceptance criteria\n"
        "UAT Scripts                     → Business; from BRD Section M\n"
        "Change Request (CR)             → IT Ops + IT-Governance (CAB)\n\n"
        "Rule: each document links upward — full traceability for Audit",
    ),
    (
        "Three Lanes Operating Model",
        "LANE 1 — DEMAND (Business + BA)\n"
        "  Define need → BRD → Sponsor → BA quality ≥80% → compliance routing → triage\n\n"
        "LANE 2 — DELIVERY (IT Product + Dev + Ops)\n"
        "  FSD → Scrum sprints → SIT → UAT support → CAB → Ship → Hypercare\n\n"
        "LANE 3 — ASSURANCE (IT-Gov + IT-Sec + GRC + Audit)\n"
        "  Architecture standards, security review, regulatory control, evidence pack",
    ),
    (
        "Stakeholder Map",
        "BUSINESS          Sponsor, requesters, UAT owners\n"
        "IT DELIVERY       Ops Manager, BA, IT Product, Dev, Service Desk\n"
        "IT-GOVERNANCE     CAB, ARB, CMDB, intake policy, change control\n"
        "IT-SECURITY       Security architecture, IAM, exceptions, secure SDLC\n"
        "GRC / LEGAL       Business compliance, contracts, collections\n"
        "AUDIT / BOD       Evidence, material risk reporting",
    ),
    (
        "Routing Rule — IT-Gov vs IT-Sec vs GRC",
        "IT process & change control     → IT-Governance\n"
        "Security, access, data protection → IT-Security\n"
        "Business & regulatory controls  → Risk / GRC / Legal\n\n"
        "All three may apply to one BRD — route early, run in parallel",
    ),
    (
        "Phase 1 — Receive Requirement",
        "Channel: ServiceNow / Jira BRD catalog (not email for projects)\n\n"
        "1. Classify: standard IT ticket vs business change vs build request\n"
        "2. Wrong bucket? → redirect to BRD (business must define first)\n"
        "3. Assign: Service Desk | BA | IT Product\n\n"
        "Ops Manager: enforce one front door; log informal requests",
    ),
    (
        "Phase 2 — BRD & Quality Gate",
        "Business drafts BRD → Sponsor (Director+) signs\n"
        "BA quality review (≤2 business days)\n"
        "  • Score ≥ 80% on quality rubric\n"
        "  • Mandatory sections complete\n"
        "  • Compliance Section N → auto-route GRC / IT-Security\n"
        "Outcome: Accepted to triage | Returned | Deferred",
    ),
    (
        "Phase 3 — IT Triage & Product Backlog",
        "IT Product / Portfolio (≤5 business days)\n"
        "  • Fit with strategy and capacity\n"
        "  • Priority vs regulatory / revenue / risk\n"
        "  • Decision: Approved for FSD | Deferred | Rejected (with reason)\n\n"
        "Approved BRD → Product Backlog item (Epic) in Jira",
    ),
    (
        "Phase 4 — FSD (Functional Specification / FRD)",
        "BA + IT Product create FSD from accepted BRD\n"
        "FSD contains:\n"
        "  • Functional flows mapped to BRD to-be state\n"
        "  • Interface & system touchpoints (FE ONLINE, Finacle, LOS…)\n"
        "  • Story breakdown with traceability ID → BRD-xxx\n"
        "  • Non-functional: performance, security, audit trail\n\n"
        "Gate: no sprint planning without FSD linked to BRD",
    ),
    (
        "Agile / Scrum — Where It Fits",
        "Governance gates are OUTSIDE the sprint (BRD, FSD, CAB).\n"
        "Scrum runs INSIDE build & test phases.\n\n"
        "Epic     = Accepted BRD\n"
        "Feature  = FSD capability group\n"
        "Story    = Implementable unit with AC\n"
        "Task     = Dev work item\n\n"
        "2-week sprints typical; release may span 1–2 sprints + UAT window",
    ),
    (
        "Scrum Roles at FE Credit",
        "Product Owner (IT Product)    Prioritizes backlog; accepts sprint output\n"
        "Scrum Master (Dev Lead)       Facilitates ceremonies; removes blockers\n"
        "Development Team            Build, unit test, support SIT fixes\n"
        "BA                          FSD, story refinement, UAT support\n"
        "IT Ops Manager                Release discipline, CAB, hypercare\n"
        "Business Sponsor              UAT accountability; go-live sign-off",
    ),
    (
        "Backlog Hierarchy",
        "Product Backlog (prioritized by IT Product)\n"
        "  └── Epic [BRD-2026-0042] POS lending visibility\n"
        "        └── Feature [FSD-3.2] Approval status API to POS\n"
        "              └── Story [US-101] Display pre-approved amount\n"
        "              └── Story [US-102] Handle expired pre-approval\n"
        "                    └── Tasks: dev, test, docs\n\n"
        "Every story must reference BRD acceptance criteria IDs",
    ),
    (
        "Sprint Planning — Entry Checklist",
        "☐ BRD accepted (score ≥ 80%) and linked\n"
        "☐ FSD approved for this epic / feature\n"
        "☐ GRC / Legal review complete (if flagged)\n"
        "☐ IT-Security review complete (if Restricted / integration)\n"
        "☐ Stories have clear AC and testable outcomes\n"
        "☐ Team capacity confirmed; no conflicting release\n"
        "☐ Ops aware of target UAT / deploy window",
    ),
    (
        "Definition of Done — Development Team",
        "☐ Code complete + peer review\n"
        "☐ Unit tests pass; coverage per team standard\n"
        "☐ Traceability: story → BRD AC → test case\n"
        "☐ SIT-ready build deployed to test environment\n"
        "☐ Release notes draft for Ops\n"
        "☐ No open Critical/High defects for in-scope stories\n"
        "☐ Security scan clean or exception recorded (IT-Security)",
    ),
    (
        "Phase 5 — Test (SIT / QA)",
        "QA executes SIT against FSD + BRD acceptance criteria\n\n"
        "Flow: Unit tests (Dev) → SIT (QA) → Regression → Defect fix loop\n\n"
        "Exit criteria:\n"
        "  • All in-scope test cases Pass\n"
        "  • No open Sev-1 / Sev-2 defects\n"
        "  • Test summary report attached to release record\n\n"
        "Then → UAT environment ready for Business",
    ),
    (
        "Phase 6 — UAT (Business Validation)",
        "Business executes UAT scripts derived from BRD Section M\n"
        "  Given / When / Then — objective pass/fail\n\n"
        "IT provides: UAT environment, test data, defect fixes\n"
        "Business provides: testers, sign-off, edge-case validation\n\n"
        "Gate: Sponsor (or delegate) signs UAT record\n"
        "IT does NOT accept on behalf of business",
    ),
    (
        "Phase 7 — Ship (Release to Production)",
        "1. Release readiness review (Ops checklist)\n"
        "2. Change Request submitted — linked BRD, FSD, UAT sign-off\n"
        "3. CAB approval (IT-Governance) — IT-Security if flagged\n"
        "4. Deploy via approved pipeline / runbook\n"
        "5. Post-deploy verification (smoke test + monitoring)\n"
        "6. CMDB / release record updated\n\n"
        "Hard gate: no production deploy without UAT + CAB",
    ),
    (
        "Phase 8 — Operations Support",
        "HYPERCARE (T+1 to T+14)\n"
        "  • Ops war room for Critical releases\n"
        "  • Dev on standby for defects\n"
        "  • Daily check with Business Sponsor\n\n"
        "BAU HANDOVER\n"
        "  • Service Desk knowledge article\n"
        "  • Monitoring & alerting configured\n"
        "  • Incident routing defined\n"
        "  • Evidence pack closed for Audit (13 artifacts)",
    ),
    (
        "Release Readiness — Go / No-Go",
        "☐ BRD accepted and linked\n"
        "☐ FSD complete; stories closed\n"
        "☐ SIT exit criteria met\n"
        "☐ UAT signed by Business Sponsor\n"
        "☐ CAB approved (IT-Governance)\n"
        "☐ IT-Security sign-off (if required)\n"
        "☐ Rollback plan tested\n"
        "☐ Comms & training complete (BRD Section K)\n"
        "☐ Hypercare roster assigned",
    ),
    (
        "Hard Gates — Non-Negotiable",
        "1. No FSD / sprint work without accepted BRD (≥ 80%)\n"
        "2. No story without traceability to BRD acceptance criteria\n"
        "3. No UAT skip — business signs, not IT\n"
        "4. No production deploy without CAB (IT-Governance)\n"
        "5. No security bypass without IT-Security exception register\n"
        "6. Email / chat is not intake for projects",
    ),
    (
        "Audit Evidence Pack (per release)",
        "1. BRD (+ versions)  2. BA scorecard  3. Sponsor approval\n"
        "4. IT-Security sign-off (if flagged)  5. GRC/Legal (if flagged)\n"
        "6. FSD linked to BRD  7. SIT results  8. UAT sign-off\n"
        "9. CR + CAB approval  10. Deployment log  11. Post-deploy verify\n"
        "12. Security scan / pen test (if required)  13. RCA (if incident)",
    ),
    (
        "Key Metrics — Ops & Leadership Dashboard",
        "BRD first-pass acceptance rate          Target ≥ 60%\n"
        "BRD → triage decision time              Target < 5 days\n"
        "Deployments without linked BRD          Target 0\n"
        "UAT sign-off before production          Target 100%\n"
        "Emergency prod changes / month          Target ≤ 2\n"
        "Open IT-Security prod exceptions        Target 0",
    ),
    (
        "Escalation Paths",
        "Skip BRD pressure       → Ops → IT-Governance policy → IT Director\n"
        "GRC hold + deploy rush  → Document hold → GRC Manager → no deploy\n"
        "Security review open    → Ops blocks CR → IT-Security lead\n"
        "Scope dispute           → BA → IT Product → Sponsor\n"
        "CAB rejection           → IT-Governance → IT Product → Sponsor\n"
        "Material incident       → IT-Security IR → CIO → EXCO / BOD",
    ),
    (
        "Summary",
        "DEMAND: Business defines in BRD — IT does not guess rules\n"
        "DELIVER: Scrum builds from FSD with traceability to BRD\n"
        "ASSURE: IT-Governance + IT-Security + GRC run in parallel\n"
        "SHIP: CAB + UAT — then hypercare → BAU support\n\n"
        "Docs: docs/12-it-operations-stakeholder-framework.md\n"
        "      docs/11-operations-manager-checklist.md",
    ),
    (
        "Next Steps",
        "• Publish framework on Confluence (FECBRD space)\n"
        "• Configure Jira: Epic = BRD, Feature = FSD, link fields mandatory\n"
        "• Train dev leads on sprint planning gate checklist\n"
        "• Align CAB charter with IT-Governance + IT-Security\n"
        "• Weekly Ops metrics to IT leadership",
    ),
]


def generate_it_delivery_framework_pptx():
    prs = Presentation()
    prs.slide_width = PInches(13.333)
    prs.slide_height = PInches(7.5)

    # Slide 1 — title (content)
    _add_content_slide(prs, *IT_DELIVERY_SLIDES[0])
    # Slide 2 — objectives
    _add_content_slide(prs, *IT_DELIVERY_SLIDES[1])

    # Slide 3 — VISUAL: end-to-end pipeline
    _add_pipeline_slide(
        prs,
        "End-to-End Delivery Pipeline",
        [
            "Receive\nReq",
            "BRD\nGate",
            "Triage\n& FSD",
            "Sprint\nBuild",
            "SIT\nTest",
            "UAT",
            "Ship\n(CAB)",
            "Ops\nSupport",
        ],
        subtitle="Governed pipeline with Agile/Scrum inside Build → SIT phases",
    )

    # Slides 4–10 content (documents through FSD)
    for item in IT_DELIVERY_SLIDES[2:9]:
        _add_content_slide(prs, *item)

    # Slide 11 — VISUAL: Agile overlay pipeline
    _add_pipeline_slide(
        prs,
        "Agile/Scrum Inside the Pipeline",
        [
            "Product\nBacklog",
            "Sprint\nPlanning",
            "Daily\nBuild",
            "SIT in\nSprint",
            "Sprint\nReview",
            "UAT\nWindow",
            "Release\nCAB",
            "Retro",
        ],
        subtitle="FSD feeds Product Backlog; Ship requires governance gates green",
    )

    for item in IT_DELIVERY_SLIDES[9:14]:
        _add_content_slide(prs, *item)

    # Scrum ceremonies visual
    _add_scrum_cycle_slide(prs)

    for item in IT_DELIVERY_SLIDES[14:20]:
        _add_content_slide(prs, *item)

    # Dual-track diagram
    _add_dual_track_slide(prs)

    for item in IT_DELIVERY_SLIDES[20:]:
        _add_content_slide(prs, *item)

    out = OUTPUT / "FE-Credit-IT-Delivery-Framework-Slides.pptx"
    prs.save(out)
    print(f"Created {out}")
    return out


def generate_pptx():
    prs = Presentation()
    prs.slide_width = PInches(13.333)
    prs.slide_height = PInches(7.5)

    for title, body in SLIDES:
        slide = prs.slides.add_slide(prs.slide_layouts[1])  # Title and Content
        slide.shapes.title.text = title
        slide.placeholders[1].text = body

    out = OUTPUT / "FE-Credit-BRD-Training-Slides.pptx"
    prs.save(out)
    print(f"Created {out}")
    return out


if __name__ == "__main__":
    generate_brd_template_docx()
    generate_cheat_sheet_docx()
    generate_pptx()
    generate_it_delivery_framework_pptx()
    print("Done.")
