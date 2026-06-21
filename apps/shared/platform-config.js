/**
 * Shared navigation + brand — Learning app and BRD intake (single platform nav).
 */
window.PLATFORM_CONFIG = {
  APP_NAME: "Learning",
  APP_VERSION: "2.6.5",
  TAGLINE: "Y1 → AI Engineer · 10 hrs/week",
  TAGLINE_BRD: "Y1 → AI Engineer · BRD intake",
  /** Mobile tab order (includes learn — mobile only) */
  MOBILE_NAV: ["landing", "explore", "learn", "library", "brd", "account"],
  NAV: [
    { id: "landing", label: "Home", hash: "landing", icon: "home" },
    { id: "explore", label: "Explore", hash: "explore", icon: "explore" },
    { id: "library", label: "Library", hash: "library", icon: "library" },
    { id: "brd", label: "BRD", href: "brd/", icon: "brd", appId: "brd" },
    { id: "account", label: "Account", hash: "auth", icon: "account" },
    { id: "learn", label: "Learn", icon: "learn", mobileOnly: true, mobileAction: "learn" },
  ],
};
