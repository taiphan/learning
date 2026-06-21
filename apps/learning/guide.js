/**
 * First-visit onboarding + replayable spotlight tour.
 */
(function () {
  const cfg = window.LEARNING_CONFIG;
  let stepIndex = 0;
  let active = false;
  let api = null;

  const $ = (sel) => document.querySelector(sel);

  function isCompleted() {
    return localStorage.getItem(cfg.GUIDE_STORAGE_KEY) === "1";
  }

  function markCompleted() {
    localStorage.setItem(cfg.GUIDE_STORAGE_KEY, "1");
  }

  function isHomeCardDismissed() {
    return localStorage.getItem(cfg.GUIDE_HOME_CARD_KEY) === "1";
  }

  function dismissHomeCard() {
    localStorage.setItem(cfg.GUIDE_HOME_CARD_KEY, "1");
    const card = $("#gettingStartedCard");
    if (card) card.hidden = true;
  }

  function renderHomeCard() {
    const card = $("#gettingStartedCard");
    if (!card || isHomeCardDismissed()) {
      if (card) card.hidden = true;
      return;
    }
    card.hidden = false;
  }

  function runBefore(hook) {
    if (!hook || !api) return;
    switch (hook) {
      case "openSidebar":
        $("#sidebar")?.classList.add("open");
        break;
      case "goWeek1":
        api.showWeek(1);
        break;
      case "showOverviewTab":
        api.setActiveTab("overview");
        break;
      case "flashLabTab":
        api.setActiveTab("lab");
        break;
      default:
        break;
    }
  }

  function prepareStep(step) {
    if (step.view === "home") api.showHome();
    else if (step.view === "week") api.showWeek(step.week || 1);
    if (step.before) runBefore(step.before);
  }

  function positionSpotlight(el) {
    const ring = $("#guideSpotlight");
    if (!el || !ring) {
      if (ring) ring.hidden = true;
      return null;
    }
    el.scrollIntoView({ behavior: "smooth", block: "nearest", inline: "nearest" });
    const rect = el.getBoundingClientRect();
    const pad = 8;
    ring.hidden = false;
    ring.style.top = `${Math.max(0, rect.top - pad)}px`;
    ring.style.left = `${Math.max(0, rect.left - pad)}px`;
    ring.style.width = `${rect.width + pad * 2}px`;
    ring.style.height = `${rect.height + pad * 2}px`;
    return rect;
  }

  function positionCard(rect) {
    const card = $("#guideCard");
    if (!card) return;
    card.classList.toggle("guide-card-center", !rect);
    if (!rect) {
      card.style.top = "";
      card.style.left = "";
      card.style.right = "";
      card.style.bottom = "";
      return;
    }
    const margin = 12;
    const cardW = Math.min(360, window.innerWidth - 24);
    let top = rect.bottom + margin;
    let left = rect.left;
    if (top + 220 > window.innerHeight) top = Math.max(margin, rect.top - 220);
    if (left + cardW > window.innerWidth) left = window.innerWidth - cardW - margin;
    left = Math.max(margin, left);
    card.style.top = `${top}px`;
    card.style.left = `${left}px`;
    card.style.right = "auto";
    card.style.bottom = "auto";
    card.style.maxWidth = `${cardW}px`;
  }

  function renderStep() {
    const steps = cfg.GUIDE_STEPS || [];
    const step = steps[stepIndex];
    if (!step) return closeGuide(true);

    prepareStep(step);

    requestAnimationFrame(() => {
      const overlay = $("#guideOverlay");
      const title = $("#guideTitle");
      const body = $("#guideBody");
      const tip = $("#guideTip");
      const back = $("#guideBack");
      const next = $("#guideNext");
      const progress = $("#guideProgress");

      if (!overlay) return;

      title.textContent = step.title;
      body.innerHTML = step.body;
      if (step.tip) {
        tip.hidden = false;
        tip.innerHTML = step.tip;
      } else {
        tip.hidden = true;
      }

      back.disabled = stepIndex === 0;
      next.textContent = stepIndex >= steps.length - 1 ? "Start learning" : "Next";

      progress.textContent = `${stepIndex + 1} / ${steps.length}`;

      let rect = null;
      if (step.type === "spotlight" && step.target) {
        const el = $(step.target);
        rect = positionSpotlight(el);
        if (!el) {
          body.innerHTML += `<p class="guide-warn">Could not highlight <code>${step.target}</code> — continue anyway.</p>`;
        }
      } else {
        $("#guideSpotlight").hidden = true;
      }
      positionCard(rect);
    });
  }

  function openGuide(fromStart) {
    if (active) return;
    active = true;
    stepIndex = fromStart ? 0 : stepIndex;
    const overlay = $("#guideOverlay");
    if (overlay) {
      overlay.hidden = false;
      document.body.classList.add("guide-open");
    }
    renderStep();
  }

  function closeGuide(completed) {
    active = false;
    const overlay = $("#guideOverlay");
    if (overlay) overlay.hidden = true;
    document.body.classList.remove("guide-open");
    $("#guideSpotlight").hidden = true;
    if (completed) {
      markCompleted();
      dismissHomeCard();
    }
    $("#sidebar")?.classList.remove("open");
  }

  function nextStep() {
    const steps = cfg.GUIDE_STEPS || [];
    if (stepIndex >= steps.length - 1) {
      closeGuide(true);
      api.showWeek(1);
      api.toast("Tour complete — start Week 1!");
      return;
    }
    stepIndex += 1;
    renderStep();
  }

  function prevStep() {
    if (stepIndex > 0) {
      stepIndex -= 1;
      renderStep();
    }
  }

  function bindGuideEvents() {
    $("#guideSkip")?.addEventListener("click", () => closeGuide(true));
    $("#guideBack")?.addEventListener("click", prevStep);
    $("#guideNext")?.addEventListener("click", nextStep);
    $("#guideClose")?.addEventListener("click", () => closeGuide(false));
    $("#openGuideBtn")?.addEventListener("click", () => {
      stepIndex = 0;
      openGuide(true);
    });
    $("#startTourBtn")?.addEventListener("click", () => {
      stepIndex = 0;
      openGuide(true);
    });
    $("#dismissHomeCardBtn")?.addEventListener("click", dismissHomeCard);

    window.addEventListener("resize", () => {
      if (!active) return;
      const step = cfg.GUIDE_STEPS[stepIndex];
      if (step?.type === "spotlight" && step.target) {
        positionSpotlight($(step.target));
        positionCard($(step.target)?.getBoundingClientRect());
      }
    });

    document.addEventListener("keydown", (e) => {
      if (!active || $("#guideOverlay")?.hidden) return;
      if (e.key === "Escape") closeGuide(true);
      if (e.key === "ArrowRight") nextStep();
      if (e.key === "ArrowLeft") prevStep();
    });
  }

  function initGuide(handlers) {
    api = handlers;
    bindGuideEvents();
    renderHomeCard();
    if (!isCompleted()) {
      setTimeout(() => openGuide(true), 400);
    }
  }

  window.LearningGuide = { initGuide, openGuide, renderHomeCard, isCompleted };
})();
