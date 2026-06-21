/** Theme + phase tips — mirrors anthropic_theme.py */

window.LEARNING_CONFIG = {
  PHASE_COLORS: {
    foundation: "var(--clay)",
    ml: "var(--sky)",
    nlp: "var(--olive)",
    genai: "var(--fig)",
    production: "var(--cactus)",
    career: "var(--olive)",
  },
  PHASE_TIPS: {
    foundation: "Type every example yourself — no copy-paste. Commit when the script runs clean.",
    ml: "Connect every metric to business language: NPL, false decline, approval rate.",
    nlp: "Always log which source chunk grounded your answer.",
    genai: "Refuse when context is missing — escalation is a feature, not failure.",
    production: "If a friend cannot curl your API, it is not done.",
    career: "Quantify impact in VND or bps — hiring managers need numbers.",
  },
  DATA_URL: "learning-data.json",
  STORAGE_KEY: "learning-ai-learning-progress",
  /** Served at /decks/ on GitHub Pages; synced from exports/learning/ on generate */
  DECK_BASE: "decks/",
  REPO: "https://github.com/taiphan/learning",
  REPO_BLOB: "https://github.com/taiphan/learning/blob/main",
  DECKS: [
    { id: "master", label: "52-Week Master (165 slides)", file: "Learning-Master-Slides.pptx" },
    { id: "roadmap", label: "Zero-to-AI Roadmap", file: "Zero-to-AI-Expert-Roadmap-Slides.pptx" },
    { id: "trackb", label: "Track B — Head of AI (VPBank-aligned)", file: "Learning-Track-B-Slides.pptx" },
  ],
};
