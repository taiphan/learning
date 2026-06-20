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
  STORAGE_KEY: "fe-credit-ai-learning-progress",
};
