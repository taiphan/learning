/**
 * 52-week learning app — loads learning-data.json, tracks progress in localStorage.
 */
(function () {
  const cfg = window.LEARNING_CONFIG;
  let data = null;
  let manifest = null;
  let filesManifest = null;
  let state = loadState();

  const $ = (sel) => document.querySelector(sel);
  const $$ = (sel) => document.querySelectorAll(sel);

  function loadState() {
    try {
      let raw = localStorage.getItem(cfg.STORAGE_KEY);
      if (!raw) raw = localStorage.getItem("finance-ai-learning-progress");
      if (!raw) raw = localStorage.getItem("fe-credit-ai-learning-progress");
      if (raw) {
        const parsed = JSON.parse(raw);
        if (!parsed.trackBCompleted) parsed.trackBCompleted = [];
        return parsed;
      }
    } catch (_) { /* ignore */ }
    return {
      completedWeeks: [],
      trackBCompleted: [],
      currentWeek: 1,
      notes: {},
      activeTab: "overview",
    };
  }

  function saveState() {
    localStorage.setItem(cfg.STORAGE_KEY, JSON.stringify(state));
    updateProgressUI();
    if (window.LearningAuth?.syncProgress) {
      window.LearningAuth.syncProgress(state);
    }
  }

  function applyCloudProgress(merged) {
    state.completedWeeks = merged.completedWeeks || [];
    state.trackBCompleted = merged.trackBCompleted || [];
    state.currentWeek = merged.currentWeek || 1;
    state.notes = merged.notes || {};
    if (merged.activeTab) state.activeTab = merged.activeTab;
    localStorage.setItem(cfg.STORAGE_KEY, JSON.stringify(state));
    updateProgressUI();
    if (!$("#viewWeek").hidden) renderWeek(state.currentWeek);
    else if (!$("#viewLanding").hidden) renderHome();
  }

  function trackBCompletedCount() {
    return (state.trackBCompleted || []).length;
  }

  function deckUrl(file) {
    return `${cfg.DECK_BASE}${file}`;
  }

  function repoPathUrl(path) {
    return `${cfg.REPO_BLOB}/${path}`;
  }

  function renderDeckLinks() {
    const ul = $("#deckLinks");
    if (!ul || !cfg.DECKS) return;
    ul.innerHTML = "";
    cfg.DECKS.forEach((d) => {
      const li = document.createElement("li");
      const a = document.createElement("a");
      a.href = deckUrl(d.file);
      a.textContent = d.label;
      a.setAttribute("download", d.file);
      li.appendChild(a);
      ul.appendChild(li);
    });
  }

  function renderTrackBLinks(w) {
    const el = $("#trackBLinks");
    if (!el) return;
    el.innerHTML = "";
    const tb = w?.track_b;
    if (!tb) return;
    const links = [
      ["Delivery playbook", repoPathUrl("curriculum/track-b-delivery.md")],
      ["Track B guide", repoPathUrl("curriculum/head-of-ai-track.md")],
      ["Template (GitHub)", repoPathUrl(tb.template.replace(/^curriculum\//, "curriculum/"))],
      ["Save to", repoPathUrl("lab/delivery/track-b/README.md")],
      ["Track B slides (PPTX)", deckUrl("Learning-Track-B-Slides.pptx")],
    ];
    if (w.week === 52) {
      links.push([
        "VPBank steering one-pager",
        repoPathUrl("curriculum/templates/hoai/vpbank_steering_one_pager.md"),
      ]);
    }
    links.forEach(([label, url]) => {
      const a = document.createElement("a");
      a.href = url;
      a.target = "_blank";
      a.rel = "noopener";
      a.textContent = label;
      el.appendChild(a);
    });
  }

  function skillById(id) {
    return data.skills.find((s) => s.id === id);
  }

  function phaseById(id) {
    return data.phases.find((p) => p.id === id);
  }

  function weekByNum(n) {
    return data.weeks.find((w) => w.week === n);
  }

  function studyBullets(study) {
    for (const sep of [" · ", "; ", " ·", ";"]) {
      if (study.includes(sep)) {
        return study.split(sep).map((s) => s.trim()).filter(Boolean);
      }
    }
    return [study];
  }

  function isComplete(n) {
    return state.completedWeeks.includes(n);
  }

  function isTrackBComplete(n) {
    return (state.trackBCompleted || []).includes(n);
  }

  function maxCompletedWeek() {
    return state.completedWeeks.length ? Math.max(...state.completedWeeks) : 0;
  }

  function nextIncompleteWeek() {
    for (const w of data.weeks) {
      if (!isComplete(w.week)) return w.week;
    }
    return 52;
  }

  function completedCount() {
    return state.completedWeeks.length;
  }

  function quarterProgress(phaseId) {
    const weeks = data.weeks.filter((w) => w.phase === phaseId);
    const done = weeks.filter((w) => isComplete(w.week)).length;
    return { done, total: weeks.length, weeks };
  }

  function currentQuarterPhase() {
    const cur = weekByNum(state.currentWeek) || data.weeks[0];
    return phaseById(cur.phase);
  }

  function trackBDeliveryPath(hoaiId) {
    const file = cfg.TRACK_B_DELIVERY?.[hoaiId];
    if (!file) return null;
    return `lab/delivery/track-b/${file}`;
  }

  function updateQuarterProgressUI() {
    const phase = currentQuarterPhase();
    if (!phase) return;
    const qp = quarterProgress(phase.id);
    const pct = qp.total ? Math.round((qp.done / qp.total) * 100) : 0;

    const qLabel = $("#statQuarter");
    const qSub = $("#statQuarterLabel");
    if (qLabel) qLabel.textContent = `Q${phase.career_quarter || "?"}`;
    if (qSub) {
      qSub.textContent = `${phase.name.split("—")[1]?.trim() || phase.theme} · W${state.currentWeek} · ${qp.done}/${qp.total}`;
    }
    const barQ = $("#barQuarter");
    if (barQ) barQ.style.width = `${pct}%`;

    const gate = $("#quarterMiniGate");
    const count = $("#quarterMiniCount");
    const barSide = $("#barQuarterSidebar");
    if (gate) gate.textContent = phase.career_gate || phase.theme;
    if (count) count.textContent = `${qp.done} of ${qp.total} weeks · gate: ${phase.career_gate || "—"}`;
    if (barSide) barSide.style.width = `${pct}%`;
  }

  function renderVersionFooter() {
    const line = $("#versionLine");
    if (!line) return;
    const req = manifest?.requirements_version || data?.meta?.requirements_version || cfg.REQUIREMENTS_VERSION;
    const app = manifest?.app_version || cfg.APP_VERSION;
    const curr = data?.meta?.curriculum_version || data?.meta?.version || cfg.CURRICULUM_VERSION;
    const updated = manifest?.updated || data?.meta?.manifest_updated || "";
    line.textContent = `Req ${req} · App ${app} · Curr ${curr}${updated ? ` · ${updated}` : ""}`;
    const reqLink = $("#versionRequirements");
    const clLink = $("#versionChangelog");
    if (reqLink && manifest?.docs?.primary) {
      reqLink.href = `${cfg.REPO_BLOB}/${manifest.docs.primary}`;
    }
    if (clLink && manifest?.docs?.changelog) {
      clLink.href = `${cfg.REPO_BLOB}/${manifest.docs.changelog}`;
    }
  }

  function checkVersionAlignment() {
    const banner = $("#versionBanner");
    if (!banner || !manifest) return;
    const appMismatch = manifest.app_version && manifest.app_version !== cfg.APP_VERSION;
    const currMismatch =
      data?.meta?.curriculum_version &&
      manifest.curriculum_version &&
      data.meta.curriculum_version !== manifest.curriculum_version;
    if (appMismatch || currMismatch) {
      banner.hidden = false;
      const exp = $("#versionExpected");
      const loaded = $("#versionLoaded");
      if (exp) exp.textContent = `app ${manifest.app_version}, curr ${manifest.curriculum_version}`;
      if (loaded) loaded.textContent = `app ${cfg.APP_VERSION}, curr ${data?.meta?.curriculum_version || "?"}`;
    } else {
      banner.hidden = true;
    }
  }

  function toast(msg) {
    const el = $("#toast");
    el.textContent = msg;
    el.classList.add("show");
    setTimeout(() => el.classList.remove("show"), 2200);
  }

  function setLayoutMode(mode) {
    const layout = $("#layout");
    const toggle = $("#menuToggle");
    if (!layout) return;
    layout.classList.toggle("layout--full", mode === "full");
    layout.classList.toggle("layout--sidebar", mode === "sidebar");
    if (toggle) toggle.hidden = mode === "full";
  }

  function setNavActive(viewId) {
    window.LearningNav?.setActive(viewId);
  }

  function updateBreadcrumb(view, meta = {}) {
    const home = { label: "Home", href: "#landing", action: () => showLanding() };
    const items = [home];
    switch (view) {
      case "landing":
        break;
      case "explore":
        items.push({ label: "Explore" });
        break;
      case "library":
        items.push({ label: "Library" });
        break;
      case "account":
        items.push({ label: "Account" });
        break;
      case "week":
        items.push({ label: meta.title || `Week ${meta.n}` });
        break;
      default:
        break;
    }
    window.LearningUX?.renderBreadcrumb(items);
    const mobileId = view === "week" ? "learn" : view === "auth" ? "account" : view;
    window.LearningUX?.setMobileActive(mobileId);
  }

  function navigateTo(viewId) {
    if (viewId === "dashboard" || viewId === "home") {
      showLanding();
      return;
    }
    switch (viewId) {
      case "landing":
        showLanding();
        break;
      case "explore":
        showExplore();
        break;
      case "library":
        showLibrary();
        break;
      case "account":
        showAuth();
        break;
      default:
        showLanding();
    }
  }

  let activeRoute = null;

  function normalizeRoute(raw) {
    const hash = (raw || "").replace(/^#/, "") || "landing";
    if (hash === "home" || hash === "dashboard") return "landing";
    if (hash === "account") return "auth";
    return hash;
  }

  /** Update URL hash; hashchange → route() → renderForRoute (single render). */
  function setRoute(raw) {
    const normalized = normalizeRoute(raw);
    if (normalizeRoute(location.hash.slice(1)) === normalized) {
      renderForRoute(normalized);
      return;
    }
    location.hash = normalized;
  }

  function route() {
    let normalized = normalizeRoute(location.hash.slice(1));
    if (!location.hash.slice(1)) {
      history.replaceState(null, "", "#landing");
      normalized = "landing";
      activeRoute = null;
    }
    renderForRoute(normalized);
  }

  function renderForRoute(routeKey) {
    if (activeRoute === routeKey) return;
    activeRoute = routeKey;

    const weekMatch = routeKey.match(/^week\/(\d+)$/);
    if (weekMatch) {
      const n = parseInt(weekMatch[1], 10);
      if (n >= 1 && n <= 52) {
        renderWeekView(n);
        return;
      }
    }

    switch (routeKey) {
      case "landing":
        renderLandingView();
        break;
      case "explore":
        renderExploreView();
        break;
      case "library":
        renderLibraryView();
        break;
      case "auth":
        renderAuthView();
        break;
      default:
        activeRoute = null;
        renderForRoute("landing");
        break;
    }
  }

  function hideAllViews() {
    $("#viewLanding").hidden = true;
    $("#viewExplore").hidden = true;
    $("#viewWeek").hidden = true;
    $("#viewLibrary").hidden = true;
    $("#viewAuth").hidden = true;
  }

  function renderHomeSummary() {
    const prog = $("#landingProgress");
    const done = completedCount();
    if (prog) {
      if (done > 0) {
        prog.hidden = false;
        const next = nextIncompleteWeek();
        prog.textContent = `${done} / 52 weeks complete · next up: Week ${next}`;
      } else {
        prog.hidden = true;
      }
    }
    const cont = $("#landingContinue");
    if (cont) cont.hidden = done === 0;
  }

  function renderHome() {
    renderHomeSummary();

    const cur = weekByNum(state.currentWeek) || data.weeks[0];
    const phase = phaseById(cur.phase);
    const next = nextIncompleteWeek();
    const nextW = weekByNum(next);
    const meta = data.meta || {};

    const done = completedCount();
    $("#homeGreeting").textContent = done === 0 ? "Banking BA → AI Engineer" : "Welcome back";
    $("#homeLead").textContent =
      done === 0
        ? `Y1 quarters · Track B Head of AI · ${meta.hours_per_week || 10} hrs/week · OCB · NAB · VPBank`
        : `${done} weeks complete. ${nextW ? `Next: Week ${next} — ${nextW.title}.` : "You finished Y1!"}` +
          (phase?.career_gate ? ` Quarter gate: ${phase.career_gate}.` : "");

    const cpPending = data.checkpoints.find((cp) => {
      const maxDone = state.completedWeeks.length ? Math.max(...state.completedWeeks) : 0;
      return maxDone < cp.after_week;
    });
    if (cpPending) {
      $("#statCheckpoint").textContent = cpPending.id;
      $("#statCheckpointLabel").textContent = `After week ${cpPending.after_week}: ${cpPending.label}`;
    } else {
      $("#statCheckpoint").textContent = "Done";
      $("#statCheckpointLabel").textContent = "All checkpoints passed";
    }

    updateProgressUI();
    renderHoaiHome();
    if (window.LearningGuide) window.LearningGuide.renderHomeCard();
  }

  function renderLandingView() {
    hideAllViews();
    setLayoutMode("full");
    $("#viewLanding").hidden = false;
    renderHome();
    highlightWeekInList(null);
    setNavActive("landing");
    updateBreadcrumb("landing");
    window.LearningUX?.injectSectionIcons?.();
  }

  function renderExploreView() {
    hideAllViews();
    setLayoutMode("full");
    $("#viewExplore").hidden = false;
    renderExplore();
    highlightWeekInList(null);
    setNavActive("explore");
    updateBreadcrumb("explore");
  }

  function renderLibraryView() {
    hideAllViews();
    setLayoutMode("full");
    $("#viewLibrary").hidden = false;
    highlightWeekInList(null);
    setNavActive("library");
    updateBreadcrumb("library");
    if (window.LearningLibrary && filesManifest) {
      window.LearningLibrary.init(filesManifest, { onWeekClick: showWeek });
    }
  }

  function renderAuthView() {
    hideAllViews();
    setLayoutMode("full");
    $("#viewAuth").hidden = false;
    highlightWeekInList(null);
    setNavActive("account");
    updateBreadcrumb("account");
    window.LearningAuth?.renderPage?.();
  }

  function renderWeekView(n) {
    state.currentWeek = n;
    saveState();
    hideAllViews();
    setLayoutMode("sidebar");
    $("#viewWeek").hidden = false;
    const w = weekByNum(n);
    renderWeek(n);
    highlightWeekInList(n);
    setNavActive("landing");
    updateBreadcrumb("week", { n, title: w ? `W${String(n).padStart(2, "0")} · ${w.title}` : `Week ${n}` });
  }

  function showLanding() {
    setRoute("landing");
  }

  function showExplore() {
    setRoute("explore");
  }

  function showLibrary() {
    setRoute("library");
  }

  function showAuth() {
    setRoute("auth");
  }

  function showWeek(n) {
    setRoute(`week/${n}`);
  }

  function showHome() {
    showLanding();
  }

  function highlightWeekInList(n) {
    $$(".week-link").forEach((btn) => {
      const w = parseInt(btn.dataset.week, 10);
      btn.classList.toggle("active", w === n);
    });
  }

  function updateProgressUI() {
    const total = 52;
    const done = completedCount();
    const pct = Math.round((done / total) * 100);
    $("#progressPill").textContent = `${done} / ${total}`;
    const tbDone = trackBCompletedCount();
    const tbTotal = (data.track_b_checkpoints || []).length || 5;
    const pill = $("#trackBPill");
    if (pill) {
      pill.textContent = `B ${tbDone}/${tbTotal}`;
      pill.classList.toggle("complete", tbDone >= tbTotal);
    }
    $("#statProgress").textContent = `${pct}%`;
    $("#barProgress").style.width = `${pct}%`;
    $$(".week-link").forEach((btn) => {
      const w = parseInt(btn.dataset.week, 10);
      btn.classList.toggle("done", isComplete(w));
    });
    renderCheckpointsMini();
    renderHoaiCheckpointsMini();
    updateQuarterProgressUI();
    if ($("#viewLanding") && !$("#viewLanding").hidden) renderHomeSummary();
  }

  function renderEnrichment() {
    const grid = $("#enrichmentGrid");
    if (!grid || !cfg.ENRICHMENT) return;
    grid.innerHTML = "";
    const phase = currentQuarterPhase();
    const qNum = phase?.career_quarter || 1;
    cfg.ENRICHMENT.forEach((block, i) => {
      const el = document.createElement("article");
      el.className = "enrichment-block" + (i + 1 === qNum ? " active" : "");
      const ul = document.createElement("ul");
      block.items.forEach((item) => {
        const li = document.createElement("li");
        const a = document.createElement("a");
        a.href = item.url;
        a.target = "_blank";
        a.rel = "noopener";
        a.textContent = item.label;
        li.innerHTML = `<span class="enrichment-tag">${item.tag}</span> `;
        li.appendChild(a);
        ul.appendChild(li);
      });
      el.innerHTML = `<h4>${block.quarter} <span class="enrichment-weeks">W${block.weeks}</span></h4>`;
      el.appendChild(ul);
      grid.appendChild(el);
    });
  }

  function renderExplore() {
    renderPhaseGrid();
    renderCareerPath();
    renderEnrichment();
    renderDeckLinks();
    const libHint = $("#libraryHomeHint");
    if (libHint && filesManifest?.total) {
      libHint.textContent = `${filesManifest.total} files indexed — curriculum, lab, Track B, decks, and docs.`;
    }
  }

  function renderHoaiHome() {
    const ul = $("#hoaiHomeProgress");
    if (!ul || !data.track_b_checkpoints) return;
    ul.innerHTML = "";
    data.track_b_checkpoints.forEach((cp) => {
      const li = document.createElement("li");
      const done = isTrackBComplete(cp.after_week);
      li.className = done ? "pass" : "";
      li.innerHTML = `<strong>${cp.id}</strong> W${cp.after_week}: ${done ? "✓" : "—"} ${cp.label}`;
      li.addEventListener("click", () => showWeek(cp.after_week));
      li.style.cursor = "pointer";
      ul.appendChild(li);
    });
  }

  function renderCareerPath() {
    const ul = $("#careerPathList");
    if (!ul || !data.career_path) return;
    ul.innerHTML = "";
    data.career_path.forEach((y) => {
      const el = document.createElement("article");
      el.className = "career-year" + (y.year === 1 ? " active" : "");
      const weeks = y.weeks && y.weeks !== "—" ? `Weeks ${y.weeks}` : "On the job";
      el.innerHTML = `
        <div class="career-year-head"><strong>Y${y.year}</strong> · ${y.label}</div>
        <p class="career-year-role">${y.role_target}</p>
        <p class="career-year-meta">${weeks} · ${y.deliverable || ""}</p>`;
      if (y.year === 1) {
        el.addEventListener("click", () => {
          const q1 = data.phases.find((p) => p.id === "y1q1");
          if (q1) {
            const first = data.weeks.find((w) => w.phase === q1.id);
            if (first) showWeek(first.week);
          }
        });
        el.style.cursor = "pointer";
      }
      ul.appendChild(el);
    });
  }

  function renderPhaseGrid() {
    const grid = $("#phaseGrid");
    grid.innerHTML = "";
    data.phases.forEach((p) => {
      const el = document.createElement("article");
      el.className = "phase-card";
      el.style.borderLeftColor = cfg.PHASE_COLORS[p.id] || "var(--clay)";
      const tb = p.track_b ? `<span class="phase-track-b">${p.track_b}</span>` : "";
      const apply = p.apply_target ? `<span class="phase-apply">Apply: ${p.apply_target}</span>` : "";
      el.innerHTML = `<h4>${p.name}</h4>
        <p class="phase-gate">${p.career_gate || ""}</p>
        <p>Weeks ${p.weeks} · M${p.months || ""} · ${p.theme}</p>
        ${tb}${apply}`;
      el.addEventListener("click", () => {
        const first = data.weeks.find((w) => w.phase === p.id);
        if (first) showWeek(first.week);
      });
      grid.appendChild(el);
    });
  }

  function renderWeekList(filterPhase) {
    const list = $("#weekList");
    list.innerHTML = "";
    data.weeks.forEach((w) => {
      if (filterPhase !== "all" && w.phase !== filterPhase) return;
      const btn = document.createElement("button");
      btn.type = "button";
      btn.className = "week-link" + (isComplete(w.week) ? " done" : "");
      btn.dataset.week = w.week;
      const color = cfg.PHASE_COLORS[w.phase] || "var(--ivory)";
      btn.innerHTML = `
        <span class="week-num" style="background:${isComplete(w.week) ? "var(--olive)" : color};color:${isComplete(w.week) ? "#fff" : "var(--slate)"}">W${String(w.week).padStart(2, "0")}</span>
        <span class="week-link-title">${w.title}${w.track_b ? '<span class="hoai-dot" title="Track B milestone">◆</span>' : ""}</span>`;
      btn.addEventListener("click", () => {
        showWeek(w.week);
        $("#sidebar").classList.remove("open");
      });
      list.appendChild(btn);
    });
  }

  function renderPhaseFilter() {
    const sel = $("#phaseFilter");
    data.phases.forEach((p) => {
      const opt = document.createElement("option");
      opt.value = p.id;
      opt.textContent = `${p.name} (${p.weeks})`;
      sel.appendChild(opt);
    });
    sel.addEventListener("change", () => renderWeekList(sel.value));
  }

  function renderCheckpointsMini() {
    const ul = $("#checkpointList");
    ul.innerHTML = "";
    const maxDone = maxCompletedWeek();
    data.checkpoints.forEach((cp) => {
      const li = document.createElement("li");
      const pass = maxDone >= cp.after_week;
      li.className = pass ? "pass" : "";
      li.textContent = `${cp.id} (W${cp.after_week}): ${pass ? "✓" : "—"} ${cp.label.slice(0, 40)}…`;
      ul.appendChild(li);
    });
  }

  function renderHoaiCheckpointsMini() {
    const ul = $("#hoaiCheckpointList");
    if (!ul || !data.track_b_checkpoints) return;
    ul.innerHTML = "";
    data.track_b_checkpoints.forEach((cp) => {
      const li = document.createElement("li");
      const pass = isTrackBComplete(cp.after_week);
      li.className = pass ? "pass" : "";
      li.textContent = `${cp.id} (W${cp.after_week}): ${pass ? "✓" : "—"} ${cp.label.slice(0, 36)}…`;
      ul.appendChild(li);
    });
  }

  function nextTrackBMilestone(fromWeek) {
    if (!data?.track_b_checkpoints) return null;
    const cur = fromWeek ?? state.currentWeek;
    return data.track_b_checkpoints.find((cp) => cur <= cp.after_week) || null;
  }

  function renderTrackBIdleList() {
    const ul = $("#trackBIdleList");
    if (!ul || !data.track_b_checkpoints) return;
    ul.innerHTML = "";
    const next = nextTrackBMilestone();
    data.track_b_checkpoints.forEach((cp) => {
      const li = document.createElement("li");
      const done = isTrackBComplete(cp.after_week);
      const isNext = next && cp.after_week === next.after_week;
      li.className = done ? "pass" : isNext ? "next" : "";
      li.innerHTML =
        `<strong>${cp.id}</strong> Week ${cp.after_week}: ${done ? "✓ " : isNext ? "→ " : "— "}${cp.label}`;
      li.addEventListener("click", () => showWeek(cp.after_week));
      li.style.cursor = "pointer";
      ul.appendChild(li);
    });
  }

  function renderLeadershipPanel(w) {
    const tb = w.track_b;
    const active = $("#trackBActive");
    const idle = $("#trackBIdle");
    const banner = $("#trackBBanner");
    if (!tb) {
      active.hidden = true;
      idle.hidden = false;
      const next = nextTrackBMilestone(w.week);
      banner.textContent = next
        ? `Track B — next milestone ${next.id} at Week ${next.after_week}`
        : "Track B — Head of AI Factory (milestone weeks)";
      renderTrackBIdleList();
      return;
    }
    active.hidden = false;
    idle.hidden = true;
    banner.textContent = `${tb.hoai_checkpoint || "Track B"} · ~${tb.hours || 2}h · ${tb.title}`;
    $("#trackBTitle").textContent = tb.title;
    $("#trackBStudy").textContent = tb.study;
    $("#trackBTemplate").textContent = tb.template;
    $("#trackBAction").textContent = tb.action;
    const savePath = trackBDeliveryPath(tb.hoai_checkpoint);
    const saveEl = $("#trackBSavePath");
    if (saveEl) saveEl.textContent = savePath || "lab/delivery/track-b/";
    $("#trackBDeliverable").textContent = tb.deliverable;
    $("#completeTrackB").checked = isTrackBComplete(w.week);
    renderTrackBLinks(w);
  }

  function setActiveTab(tab) {
    state.activeTab = tab;
    saveState();
    $$(".tab").forEach((t) => {
      const on = t.dataset.tab === tab;
      t.classList.toggle("active", on);
      t.setAttribute("aria-selected", on ? "true" : "false");
    });
    $$(".tab-panel").forEach((p) => {
      const on = p.dataset.panel === tab;
      p.classList.toggle("active", on);
      p.hidden = !on;
    });
  }

  function renderWeek(n) {
    const w = weekByNum(n);
    if (!w) return;
    const skill = skillById(w.skill_id);
    const phase = phaseById(w.phase);

    $("#weekBadge").textContent = `W${String(n).padStart(2, "0")}`;
    $("#phaseChip").textContent = phase.name;
    $("#phaseChip").style.background = cfg.PHASE_COLORS[w.phase] || "var(--ivory)";
    $("#monthChip").textContent = `Month ${w.month} · Y1 Q${w.career_quarter || phase.career_quarter || "?"}`;
    const cg = $("#careerGateChip");
    if (cg && (w.career_gate || phase.career_gate)) {
      cg.hidden = false;
      cg.textContent = w.career_gate || phase.career_gate;
    } else if (cg) {
      cg.hidden = true;
    }
    $("#weekTitle").textContent = w.title;
    $("#skillLine").textContent = `Skill ${skill.id}: ${skill.name}`;

    $("#deliverableBanner").textContent = `Deliverable: ${w.deliverable}`;
    $("#deliverableBanner").style.background = cfg.PHASE_COLORS[w.phase] || "var(--clay)";

    const bullets = $("#studyBullets");
    bullets.innerHTML = "";
    studyBullets(w.study).forEach((b) => {
      const li = document.createElement("li");
      li.textContent = b;
      bullets.appendChild(li);
    });

    $("#skillDefinition").textContent = skill.definition;
    $("#phaseTip").textContent = `Quarter tip: ${cfg.PHASE_TIPS[w.phase] || ""}`;
    const ct = $("#careerTip");
    if (ct && phase.career_gate) {
      ct.hidden = false;
      const apply = phase.apply_target ? ` · Apply target: ${phase.apply_target}` : "";
      ct.textContent = `Career gate (Y${phase.career_year || 1} Q${phase.career_quarter || "?"}): ${phase.career_gate}${apply}`;
    } else if (ct) {
      ct.hidden = true;
    }

    const cpEl = $("#checkpointCallout");
    if (w.checkpoint) {
      cpEl.hidden = false;
      $("#checkpointText").textContent = w.checkpoint;
    } else {
      cpEl.hidden = true;
    }

    const bridge = $("#weekBridge");
    const brdHref = location.pathname.includes("/brd") ? "../brd/" : "brd/";
    if (n === 1) {
      bridge.hidden = false;
      bridge.innerHTML =
        `<strong>Week 1 bridge (Y1 Q1):</strong> Draft a BRD in the <a href="${brdHref}">Learning BRD app</a>, export `.md`, then run ` +
        `<code>python3 exercises/week01_brd_checklist.py your-export.md</code> from <code>lab/</code>.`;
    } else if (n === 2) {
      bridge.hidden = false;
      bridge.innerHTML =
        `<strong>Week 2 bridge (Y1 Q1):</strong> Loan rules in Python mirror Section H of ` +
        `<a href="https://github.com/taiphan/learning/blob/main/examples/04a-brd-pos-lending.md" target="_blank" rel="noopener">examples/04a-brd-pos-lending.md</a>.`;
    } else if (phase.id === "y1q2" && n === 13) {
      bridge.hidden = false;
      bridge.innerHTML =
        `<strong>Y1 Q2 start:</strong> Classical ML quarter — portfolio piece 1 is the gate. Review ` +
        `<a href="https://github.com/taiphan/learning/blob/main/lab/projects/PORTFOLIO.md" target="_blank" rel="noopener">lab/projects/PORTFOLIO.md</a>.`;
    } else if (phase.id === "y1q3" && n >= 25 && n <= 36) {
      bridge.hidden = false;
      bridge.innerHTML =
        `<strong>Y1 Q3 (GenAI production):</strong> Use BRDs from the intake app as RAG corpus (see <code>lab/projects/policy-rag/ask.py</code>).`;
    } else if (phase.id === "y1q4" && n === 37) {
      bridge.hidden = false;
      bridge.innerHTML =
        `<strong>Y1 Q4 — Apply quarter:</strong> Gate is AI Engineer / Senior BA at OCB, NAB, or VPBank. See ` +
        `<a href="https://github.com/taiphan/learning/blob/main/curriculum/job-skills-adaptation.md" target="_blank" rel="noopener">job-skills-adaptation.md</a>.`;
    } else if (w.track_b) {
      bridge.hidden = false;
      const save = trackBDeliveryPath(w.track_b.hoai_checkpoint) || "lab/delivery/track-b/";
      bridge.innerHTML =
        `<strong>Track B (${w.track_b.hoai_checkpoint}):</strong> ~2h leadership — open the <em>Leadership</em> tab, fill the template, save to ` +
        `<code>${save}</code>.`;
    } else {
      bridge.hidden = true;
    }

    $("#studyText").textContent = w.study;
    $("#skillSources").textContent = skill.sources;
    $("#skillPractice").textContent = skill.practice;
    $("#skillCheckpoint").textContent = skill.checkpoint;

    const links = $("#resourceLinks");
    links.innerHTML = "";
    const urls = w.resource_urls?.length ? w.resource_urls : skill.resource_urls || [];
    if (urls.length === 0) {
      links.innerHTML = "<li>No external links — see workbook and repo docs.</li>";
    } else {
      urls.forEach(([label, url]) => {
        const li = document.createElement("li");
        const a = document.createElement("a");
        a.href = url;
        a.target = "_blank";
        a.rel = "noopener";
        a.textContent = label;
        li.appendChild(a);
        links.appendChild(li);
      });
    }

    $("#exercisePath").textContent = w.exercise;
    $("#runCommand").textContent = w.run;

    const done = $("#doneList");
    done.innerHTML = "";
    const steps = [
      `Open \`${w.exercise}\` in Cursor`,
      `Run: \`${w.run}\` (from lab/)`,
      `Output matches: ${w.deliverable}`,
      `Skill checkpoint: ${skill.checkpoint}`,
    ];
    if (w.track_b) {
      const save = trackBDeliveryPath(w.track_b.hoai_checkpoint) || "lab/delivery/track-b/";
      steps.push(
        `Track B (~2h): fill \`${w.track_b.template}\``,
        `Save leadership deliverable to \`${save}\``,
        `Mark Track B milestone on Leadership tab`
      );
    }
    steps.forEach((step) => {
      const li = document.createElement("li");
      li.textContent = step;
      done.appendChild(li);
    });

    $("#weekNotes").value = state.notes[String(n)] || "";
    $("#completeWeek").checked = isComplete(n);

    renderLeadershipPanel(w);

    $$(".tab").forEach((tab) => {
      tab.classList.toggle("milestone", tab.dataset.tab === "leadership" && !!w.track_b);
    });

    $("#prevWeek").disabled = n <= 1;
    $("#nextWeek").textContent = n >= 52 ? "Finish path ✓" : "Next week →";

    setActiveTab(state.activeTab || "overview");
    updateProgressUI();
  }

  function bindGotoHandlers() {
    document.addEventListener("click", (e) => {
      const btn = e.target.closest("[data-goto]");
      if (!btn) return;
      const dest = btn.dataset.goto;
      if (dest === "week") {
        showWeek(parseInt(btn.dataset.week || "1", 10));
        return;
      }
      navigateTo(dest);
    });
  }

  function bindEvents() {
    $("#menuToggle").addEventListener("click", () => {
      $("#sidebar").classList.toggle("open");
    });

    $("#brandHome")?.addEventListener("click", () => showLanding());
    $("#continueBtn").addEventListener("click", () => showWeek(nextIncompleteWeek()));
    $("#landingStart")?.addEventListener("click", () => showWeek(1));
    $("#landingContinue")?.addEventListener("click", () => showWeek(nextIncompleteWeek()));
    $("#landingTour")?.addEventListener("click", () => window.LearningGuide?.openGuide?.());
    $("#libraryBackHome")?.addEventListener("click", () => showLanding());
    $("#homeOpenLibrary")?.addEventListener("click", () => showLibrary());
    $("#openAuthBtn")?.addEventListener("click", () => showAuth());
    bindGotoHandlers();

    $$(".tab").forEach((tab) => {
      tab.addEventListener("click", () => setActiveTab(tab.dataset.tab));
    });

    $("#prevWeek").addEventListener("click", () => {
      if (state.currentWeek > 1) showWeek(state.currentWeek - 1);
    });

    $("#nextWeek").addEventListener("click", () => {
      if (state.currentWeek < 52) showWeek(state.currentWeek + 1);
      else toast("Congratulations — 52 weeks complete!");
    });

    $("#completeWeek").addEventListener("change", (e) => {
      const n = state.currentWeek;
      if (e.target.checked) {
        if (!state.completedWeeks.includes(n)) state.completedWeeks.push(n);
        state.completedWeeks.sort((a, b) => a - b);
        toast(`Week ${n} marked complete`);
      } else {
        state.completedWeeks = state.completedWeeks.filter((w) => w !== n);
      }
      saveState();
      renderWeek(n);
    });

    $("#completeTrackB").addEventListener("change", (e) => {
      const n = state.currentWeek;
      if (!state.trackBCompleted) state.trackBCompleted = [];
      if (e.target.checked) {
        if (!state.trackBCompleted.includes(n)) state.trackBCompleted.push(n);
        state.trackBCompleted.sort((a, b) => a - b);
        toast(`Track B milestone (W${n}) marked complete`);
      } else {
        state.trackBCompleted = state.trackBCompleted.filter((w) => w !== n);
      }
      saveState();
      renderWeek(n);
    });

    $("#weekNotes").addEventListener("input", (e) => {
      state.notes[String(state.currentWeek)] = e.target.value;
      saveState();
    });

    $("#copyRun").addEventListener("click", async () => {
      const w = weekByNum(state.currentWeek);
      try {
        await navigator.clipboard.writeText(w.run);
        toast("Run command copied");
      } catch (_) {
        toast("Copy failed — select command manually");
      }
    });

    window.addEventListener("hashchange", route);
  }

  async function init() {
    try {
      const [dataRes, manifestRes, filesRes] = await Promise.all([
        fetch(cfg.DATA_URL),
        fetch(cfg.MANIFEST_URL).catch(() => null),
        fetch(cfg.FILES_URL).catch(() => null),
      ]);
      if (!dataRes.ok) throw new Error(dataRes.statusText);
      data = await dataRes.json();
      if (manifestRes?.ok) manifest = await manifestRes.json();
      if (filesRes?.ok) filesManifest = await filesRes.json();
    } catch (err) {
      window.LearningUX?.hideLoading();
      $("#main").innerHTML = `<div class="card"><h2>Could not load curriculum</h2><p>Run a local server from <code>apps/learning</code> and ensure <code>data/learning-data.json</code> exists.</p><pre>${err.message}</pre></div>`;
      return;
    }

    renderPhaseFilter();
    renderWeekList("all");
    renderPhaseGrid();
    window.LearningUX?.init({
      navigate: navigateTo,
      showWeekContinue: () => showWeek(nextIncompleteWeek()),
    });
    window.LearningNav?.init(navigateTo);
    bindEvents();
    route();
    renderVersionFooter();
    checkVersionAlignment();
    if (window.LearningGuide) {
      window.LearningGuide.initGuide({
        showHome,
        showWeek,
        setActiveTab,
        toast,
      });
    }
    window.__learningToast = toast;
    window.__learningShowHome = showHome;
    window.__learningShowAuth = showAuth;
    window.__learningAuthGetProgress = () => ({
      completedWeeks: [...state.completedWeeks],
      trackBCompleted: [...(state.trackBCompleted || [])],
      currentWeek: state.currentWeek,
      notes: { ...state.notes },
      activeTab: state.activeTab,
    });
    window.__learningAuthApplyProgress = applyCloudProgress;
    window.LearningAuth?.init?.();
    window.LearningUX?.hideLoading();
  }

  init();
})();
