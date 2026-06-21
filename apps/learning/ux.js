/**
 * UX layer — breadcrumbs, loading shell, skip link, reduced-motion helpers.
 */
(function () {
  const $ = (sel) => document.querySelector(sel);

  function hideLoading() {
    const el = $("#appLoading");
    const app = $("#app");
    if (el) {
      el.hidden = true;
      el.setAttribute("aria-hidden", "true");
    }
    if (app) app.removeAttribute("aria-busy");
  }

  function showLoading() {
    const el = $("#appLoading");
    const app = $("#app");
    if (el) {
      el.hidden = false;
      el.setAttribute("aria-hidden", "false");
    }
    if (app) app.setAttribute("aria-busy", "true");
  }

  function renderBreadcrumb(items) {
    const nav = $("#breadcrumb");
    if (!nav || !items?.length) return;
    nav.innerHTML = "";
    nav.hidden = items.length <= 1;

    const ol = document.createElement("ol");
    ol.className = "breadcrumb-list";

    items.forEach((item, i) => {
      const li = document.createElement("li");
      const isLast = i === items.length - 1;
      if (isLast || !item.href) {
        li.className = "breadcrumb-current";
        if (isLast) li.setAttribute("aria-current", "page");
        li.textContent = item.label;
      } else {
        const a = document.createElement("a");
        a.href = item.href;
        a.className = "breadcrumb-link";
        a.textContent = item.label;
        if (item.action) {
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

  function initSkipLink() {
    const skip = $(".skip-link");
    const main = $("#main");
    if (!skip || !main) return;
    skip.addEventListener("click", (e) => {
      e.preventDefault();
      main.setAttribute("tabindex", "-1");
      main.focus({ preventScroll: false });
    });
  }

  function initMobileNav(navigate, showWeek) {
    const bar = $("#mobileNav");
    if (!bar) return;
    const icons = window.LEARNING_ICONS || {};
    bar.querySelectorAll("[data-icon]").forEach((el) => {
      const name = el.dataset.icon;
      if (icons[name]) el.innerHTML = icons[name];
    });
    bar.querySelectorAll("[data-mobile-nav]").forEach((btn) => {
      btn.addEventListener("click", () => {
        const dest = btn.dataset.mobileNav;
        if (dest === "learn") showWeek?.();
        else navigate?.(dest);
      });
    });
  }

  function setMobileActive(viewId) {
    $$("[data-mobile-nav]").forEach((el) => {
      el.classList.toggle("active", el.dataset.mobileNav === viewId);
    });
  }

  function injectSectionIcons() {
    const icons = window.LEARNING_ICONS || {};
    document.querySelectorAll(".section-nav-icon[data-icon]").forEach((el) => {
      const name = el.dataset.icon;
      if (icons[name]) el.innerHTML = icons[name];
    });
  }

  const $$ = (sel) => document.querySelectorAll(sel);

  window.LearningUX = {
    showLoading,
    hideLoading,
    renderBreadcrumb,
    setMobileActive,
    injectSectionIcons,
    init: (opts) => {
      initSkipLink();
      initMobileNav(opts?.navigate, opts?.showWeekContinue);
      injectSectionIcons();
    },
  };
})();
