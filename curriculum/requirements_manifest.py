"""Single source for requirements, app, and curriculum version alignment."""

from __future__ import annotations

REQUIREMENTS_VERSION = "2.0.0"
APP_VERSION = "2.6.3"
CURRICULUM_VERSION = "1.3"

DOCS = {
    "primary": "docs/learning-requirements/LEARNING-REQUIREMENTS.md",
    "changelog": "docs/learning-requirements/CHANGELOG.md",
    "video_enrichment": "curriculum/video-learning-enrichment.md",
    "career_timeline": "curriculum/career-timeline.md",
    "app_usage_legacy": "docs/15-learning-app-usage-requirements.md",
    "auth_setup": "apps/learning/AUTH-SETUP.md",
}

CHANGELOG: list[dict] = [
    {
        "version": "2.6.3",
        "date": "2026-06-21",
        "requirements": "2.0.0",
        "app": "2.6.3",
        "curriculum": "1.3",
        "changes": [
            "Shared app-shell.css — topbar, buttons, cards, forms for Learning + BRD",
            "Higher contrast text tokens (--text-secondary, darker links, solid topbar text)",
            "BRD header matches Learning homepage (topbar, brand-dot, step tabs)",
            "Risk/score badges use theme CSS classes instead of inline colors",
        ],
    },
    {
        "version": "2.6.0",
        "date": "2026-06-21",
        "requirements": "2.0.0",
        "app": "2.6.0",
        "curriculum": "1.3",
        "changes": [
            "Unified Home — landing and dashboard merged with progress stats and section nav",
            "Consistent page-hero layout across Home, Explore, Library, Account",
            "Top nav simplified: Home, Explore, Library, Account (+ mobile Account)",
            "#dashboard and #home redirect to #landing",
        ],
    },
    {
        "version": "2.5.0",
        "date": "2026-06-21",
        "requirements": "2.0.0",
        "app": "2.5.0",
        "curriculum": "1.3",
        "changes": [
            "UI/UX Pro Max pass — focus rings, skip link, breadcrumbs, loading shell",
            "SVG nav icons + mobile bottom navigation bar",
            "Micro-interactions, contrast, reduced-motion, no layout-shift hovers",
        ],
    },
    {
        "version": "2.4.0",
        "date": "2026-06-21",
        "requirements": "2.0.0",
        "app": "2.4.0",
        "curriculum": "1.3",
        "changes": [
            "Landing page at #landing with quick-start cards",
            "Main menu: Home · Dashboard · Explore · Library · Account · BRD",
            "Explore view — quarters, career path, videos, decks, library link",
            "Dashboard slimmed to progress + Track B summary",
        ],
    },
    {
        "version": "2.3.0",
        "date": "2026-06-21",
        "requirements": "2.0.0",
        "app": "2.3.0",
        "curriculum": "1.3",
        "changes": [
            "Dedicated account page at #auth — Google sign-in, profile, sync stats",
            "Header Account button replaces inline sign-in controls",
        ],
    },
    {
        "version": "2.2.0",
        "date": "2026-06-21",
        "requirements": "2.0.0",
        "app": "2.2.0",
        "curriculum": "1.3",
        "changes": [
            "apps/learning/data/ — JSON manifests in one folder",
            "Library view — browse all curriculum, lab, deck, and doc files",
            "app-files-manifest.json generated from repo on build",
        ],
    },
    {
        "version": "2.1.0",
        "date": "2026-06-21",
        "requirements": "2.0.0",
        "app": "2.1.0",
        "curriculum": "1.3",
        "changes": [
            "Google sign-in via Firebase Auth (optional)",
            "Firestore progress sync across devices",
            "AUTH-SETUP.md + GitHub Actions Firebase secrets",
        ],
    },
    {
        "version": "2.0.0",
        "date": "2026-06-21",
        "requirements": "2.0.0",
        "app": "2.0.0",
        "curriculum": "1.3",
        "changes": [
            "Consolidated LEARNING-REQUIREMENTS.md (one doc to follow)",
            "requirements-manifest.json synced to app on generate",
            "App version footer + manifest mismatch warning",
            "In-app guide tour + free video enrichment card",
        ],
    },
    {
        "version": "1.2.0",
        "date": "2026-06-20",
        "requirements": "1.0.0",
        "app": "1.2.0",
        "curriculum": "1.2",
        "changes": [
            "Y1 quarters (y1q1–y1q4) replace six technical phases",
            "Track B H0–H4 on weeks 8, 16, 28, 40, 52",
            "Career path Y1–Y4 in app home",
            "docs/15-learning-app-usage-requirements.md (superseded by 2.0)",
        ],
    },
    {
        "version": "1.0.0",
        "date": "2026-06-19",
        "requirements": "1.0.0",
        "app": "1.0.0",
        "curriculum": "1.0",
        "changes": [
            "Initial 52-week learning app + learning_data.py",
            "Six-phase curriculum (foundation → career)",
        ],
    },
]


def manifest_dict() -> dict:
    latest = CHANGELOG[0]
    return {
        "requirements_version": REQUIREMENTS_VERSION,
        "app_version": APP_VERSION,
        "curriculum_version": CURRICULUM_VERSION,
        "updated": latest["date"],
        "docs": DOCS,
        "repo": "https://github.com/taiphan/learning",
        "live_url": "https://taiphan.github.io/learning/",
        "changelog": CHANGELOG,
    }
