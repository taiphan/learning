/**
 * Platform navigation — same topbar + mobile tabs on Learning and BRD.
 */
(function () {
  const $ = (sel) => document.querySelector(sel);
  const $$ = (sel) => document.querySelectorAll(sel);

  const cfg = () => window.PLATFORM_CONFIG || window.LEARNING_CONFIG || {};
  const icons = () => window.LEARNING_ICONS || {};

  let state = {
    app: "learning",
    base: "",
    goTo: null,
    showWeek: null,
  };

  function navItems() {
    return cfg().NAV || [];
  }

  function mobileOrder() {
    return cfg().MOBILE_NAV || navItems().map((i) => i.id);
  }

  function itemById(id) {
    return navItems().find((i) => i.id === id);
  }

  function resolveHash(item) {
    if (!item.hash) return null;
    const hash = item.hash === "auth" ? "auth" : item.hash;
    return `${state.base}#${hash}`;
  }

  function resolvePageHref(item) {
    if (!item.href) return null;
    if (state.app === "brd" && item.appId === "brd") return null;
    if (state.app === "learning") return item.href;
    if (item.appId === "brd") return "./";
    return `${state.base}${item.href.replace(/^\//, "")}`;
  }

  function iconHtml(name) {
    const ic = icons()[name];
    return ic || "";
  }

  function linkLabel(item) {
    return `<span class="app-nav-label">${item.label}</span>`;
  }

  function isCurrentAppItem(item) {
    return state.app === "brd" && item.appId === "brd";
  }

  function renderTopNav() {
    const nav = $("#appNav");
    if (!nav) return;
    nav.innerHTML = "";

    navItems()
      .filter((item) => !item.mobileOnly)
      .forEach((item) => {
        const ic = iconHtml(item.icon);
        const label = ic + linkLabel(item);

        if (isCurrentAppItem(item)) {
          const el = document.createElement("span");
          el.className = "app-nav-link active";
          el.dataset.nav = item.id;
          el.setAttribute("aria-current", "page");
          el.innerHTML = label;
          nav.appendChild(el);
          return;
        }

        const pageHref = resolvePageHref(item);
        if (pageHref) {
          const a = document.createElement("a");
          a.className = "app-nav-link";
          a.href = pageHref;
          a.dataset.nav = item.id;
          if (item.appId === "brd") {
            a.title = "Open BRD intake (Week 1 bridge)";
          }
          a.innerHTML = label;
          nav.appendChild(a);
          return;
        }

        if (state.app === "learning" && item.hash) {
          const btn = document.createElement("button");
          btn.type = "button";
          btn.className = "app-nav-link";
          btn.dataset.nav = item.id;
          btn.setAttribute("aria-label", item.label);
          btn.innerHTML = label;
          btn.addEventListener("click", () => {
            const dest = item.id === "account" ? "auth" : item.id;
            state.goTo?.(dest);
          });
          nav.appendChild(btn);
          return;
        }

        const hashHref = resolveHash(item);
        if (hashHref) {
          const a = document.createElement("a");
          a.className = "app-nav-link";
          a.href = hashHref;
          a.dataset.nav = item.id;
          a.innerHTML = label;
          nav.appendChild(a);
        }
      });
  }

  function renderBreadcrumb(items) {
    const nav = document.getElementById("platformBreadcrumb");
    if (!nav || !items?.length) return;
    nav.hidden = items.length <= 1;
    nav.innerHTML = "";
    const ol = document.createElement("ol");
    ol.className = "breadcrumb-list";
    items.forEach((item, i) => {
      const li = document.createElement("li");
      const isLast = i === items.length - 1;
      if (isLast || (!item.href && !item.action)) {
        li.className = "breadcrumb-current";
        if (isLast) li.setAttribute("aria-current", "page");
        li.textContent = item.label;
      } else {
        const a = document.createElement("a");
        a.className = "breadcrumb-link";
        a.textContent = item.label;
        if (item.href) a.href = item.href;
        if (item.action) {
          a.href = item.href || "#";
          a.addEventListener("click", (e) => {
            e.preventDefault();
            item.action();
          });
        }
        li.appendChild(a);
      }
      ol.appendChild(li);
    });
    nav.appendChild(ol);
  }

  function defaultBrdBreadcrumb() {
    renderBreadcrumb([
      { label: "Home", href: `${state.base}#landing` },
      { label: "BRD" },
    ]);
  }

  function renderMobileNav() {
    const bar = $("#mobileNav");
    if (!bar) return;
    bar.innerHTML = "";

    mobileOrder().forEach((id) => {
      const item = itemById(id);
      if (!item) return;

      const pageHref = resolvePageHref(item);
      const hashHref = !pageHref && item.hash ? resolveHash(item) : null;

      if (isCurrentAppItem(item)) {
        const span = document.createElement("span");
        span.className = "mobile-nav-item active";
        span.dataset.mobileNav = item.id;
        span.setAttribute("aria-current", "page");
        span.innerHTML = `<span class="mobile-nav-icon">${iconHtml(item.icon)}</span><span>${item.label}</span>`;
        bar.appendChild(span);
        return;
      }

      if (item.mobileAction === "learn" && state.app === "learning") {
        const btn = document.createElement("button");
        btn.type = "button";
        btn.className = "mobile-nav-item";
        btn.dataset.mobileNav = "learn";
        btn.setAttribute("aria-label", item.label);
        btn.innerHTML = `<span class="mobile-nav-icon">${iconHtml(item.icon)}</span><span>${item.label}</span>`;
        btn.addEventListener("click", () => state.showWeek?.());
        bar.appendChild(btn);
        return;
      }

      if (item.id === "learn" && state.app === "brd") {
        const a = document.createElement("a");
        a.className = "mobile-nav-item";
        a.href = `${state.base}#week/1`;
        a.dataset.mobileNav = "learn";
        a.innerHTML = `<span class="mobile-nav-icon">${iconHtml(item.icon)}</span><span>${item.label}</span>`;
        bar.appendChild(a);
        return;
      }

      if (pageHref || hashHref) {
        const a = document.createElement("a");
        a.className = "mobile-nav-item";
        a.href = pageHref || hashHref;
        a.dataset.mobileNav = item.id;
        a.innerHTML = `<span class="mobile-nav-icon">${iconHtml(item.icon)}</span><span>${item.label}</span>`;
        bar.appendChild(a);
        return;
      }

      if (state.app === "learning" && item.hash) {
        const btn = document.createElement("button");
        btn.type = "button";
        btn.className = "mobile-nav-item";
        btn.dataset.mobileNav = item.id;
        btn.setAttribute("aria-label", item.label);
        btn.innerHTML = `<span class="mobile-nav-icon">${iconHtml(item.icon)}</span><span>${item.label}</span>`;
        btn.addEventListener("click", () => {
          const dest = item.id === "account" ? "auth" : item.id;
          state.goTo?.(dest);
        });
        bar.appendChild(btn);
      }
    });
  }

  function setActive(viewId) {
    const id = viewId === "auth" ? "account" : viewId;
    $$(".app-nav-link[data-nav]").forEach((el) => {
      const on = el.dataset.nav === id;
      el.classList.toggle("active", on);
      if (on) el.setAttribute("aria-current", "page");
      else el.removeAttribute("aria-current");
    });
    $$("[data-mobile-nav]").forEach((el) => {
      const on = el.dataset.mobileNav === id || (id === "week" && el.dataset.mobileNav === "learn");
      el.classList.toggle("active", on);
      if (on) el.setAttribute("aria-current", "page");
      else el.removeAttribute("aria-current");
    });
  }

  function init(opts = {}) {
    state = { ...state, ...opts };
    renderTopNav();
    renderMobileNav();
    if (state.app === "brd") {
      setActive("brd");
      defaultBrdBreadcrumb();
      applyBrandTagline();
    }
  }

  function applyBrandTagline() {
    const el = document.getElementById("brandTagline");
    if (!el) return;
    const pc = cfg();
    el.textContent =
      state.app === "brd" ? pc.TAGLINE_BRD || pc.TAGLINE : pc.TAGLINE;
  }

  function renderPlatformFooter() {
    const line = document.getElementById("platformVersionLine");
    if (!line) return;
    const v = cfg().APP_VERSION || "—";
    line.textContent =
      state.app === "brd"
        ? `Learning v${v} · BRD intake · Gate ≥ 80%`
        : `Learning v${v}`;
  }

  window.PlatformNav = {
    init,
    setActive,
    renderTopNav,
    renderMobileNav,
    renderBreadcrumb,
    renderPlatformFooter,
  };

  window.LearningNav = {
    init: (goTo, opts) =>
      PlatformNav.init({
        app: "learning",
        base: "",
        goTo,
        showWeek: opts?.showWeek,
      }),
    setActive: (id) => PlatformNav.setActive(id),
    renderNav: () => PlatformNav.renderTopNav(),
  };
})();
