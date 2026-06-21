/**
 * Primary app navigation — topbar menu + active state + icons.
 */
(function () {
  let goTo = null;
  const icons = () => window.LEARNING_ICONS || {};

  function renderNav() {
    const nav = $("#appNav");
    const cfg = window.LEARNING_CONFIG;
    if (!nav || !cfg.NAV) return;
    nav.innerHTML = "";

    cfg.NAV.forEach((item) => {
      const btn = document.createElement("button");
      btn.type = "button";
      btn.className = "app-nav-link";
      btn.dataset.nav = item.id;
      btn.setAttribute("aria-label", item.label);
      const ic = icons()[item.icon];
      if (ic) btn.innerHTML = ic + `<span class="app-nav-label">${item.label}</span>`;
      else btn.textContent = item.label;
      btn.addEventListener("click", () => goTo?.(item.id));
      nav.appendChild(btn);
    });

    (cfg.NAV_EXTERNAL || []).forEach((item) => {
      const a = document.createElement("a");
      a.className = "app-nav-link app-nav-external";
      a.href = item.href;
      const ic = icons()[item.icon];
      if (ic) a.innerHTML = ic + `<span class="app-nav-label">${item.label}</span>`;
      else a.textContent = item.label;
      nav.appendChild(a);
    });
  }

  function setActive(viewId) {
    $$(".app-nav-link[data-nav]").forEach((el) => {
      const on = el.dataset.nav === viewId;
      el.classList.toggle("active", on);
      if (on) el.setAttribute("aria-current", "page");
      else el.removeAttribute("aria-current");
    });
  }

  function init(navigate) {
    goTo = navigate;
    renderNav();
  }

  const $ = (sel) => document.querySelector(sel);
  const $$ = (sel) => document.querySelectorAll(sel);

  window.LearningNav = { init, setActive, renderNav };
})();
