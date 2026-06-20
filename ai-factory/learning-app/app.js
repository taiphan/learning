/**
 * 52-week learning app — loads learning-data.json, tracks progress in localStorage.
 */
(function () {
  const cfg = window.LEARNING_CONFIG;
  let data = null;
  let state = loadState();

  const $ = (sel) => document.querySelector(sel);
  const $$ = (sel) => document.querySelectorAll(sel);

  function loadState() {
    try {
      let raw = localStorage.getItem(cfg.STORAGE_KEY);
      if (!raw) raw = localStorage.getItem("fe-credit-ai-learning-progress");
      if (raw) return JSON.parse(raw);
    } catch (_) { /* ignore */ }
    return {
      completedWeeks: [],
      currentWeek: 1,
      notes: {},
      activeTab: "overview",
    };
  }

  function saveState() {
    localStorage.setItem(cfg.STORAGE_KEY, JSON.stringify(state));
    updateProgressUI();
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

  function nextIncompleteWeek() {
    for (const w of data.weeks) {
      if (!isComplete(w.week)) return w.week;
    }
    return 52;
  }

  function completedCount() {
    return state.completedWeeks.length;
  }

  function toast(msg) {
    const el = $("#toast");
    el.textContent = msg;
    el.classList.add("show");
    setTimeout(() => el.classList.remove("show"), 2200);
  }

  function route() {
    const hash = location.hash.slice(1) || "home";
    const weekMatch = hash.match(/^week\/(\d+)$/);
    if (weekMatch) {
      const n = parseInt(weekMatch[1], 10);
      if (n >= 1 && n <= 52) {
        showWeek(n);
        return;
      }
    }
    showHome();
  }

  function showHome() {
    $("#viewHome").hidden = false;
    $("#viewWeek").hidden = true;
    location.hash = "home";
    renderHome();
    highlightWeekInList(null);
  }

  function showWeek(n) {
    state.currentWeek = n;
    saveState();
    $("#viewHome").hidden = true;
    $("#viewWeek").hidden = false;
    location.hash = `week/${n}`;
    renderWeek(n);
    highlightWeekInList(n);
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
    $("#statProgress").textContent = `${pct}%`;
    $("#barProgress").style.width = `${pct}%`;
    $$(".week-link").forEach((btn) => {
      const w = parseInt(btn.dataset.week, 10);
      btn.classList.toggle("done", isComplete(w));
    });
    renderCheckpointsMini();
  }

  function renderHome() {
    const cur = weekByNum(state.currentWeek) || data.weeks[0];
    const next = nextIncompleteWeek();
    const nextW = weekByNum(next);

    $("#homeGreeting").textContent =
      completedCount() === 0 ? "Welcome — start your 52-week path" : "Welcome back";
    $("#homeLead").textContent =
      completedCount() === 0
        ? "Week 1 connects Python to BRD quality — the same gates you use at work."
        : `You have completed ${completedCount()} weeks. ${nextW ? `Next up: Week ${next} — ${nextW.title}.` : "You finished the path!"}`;

    $("#statCurrent").textContent = `Week ${cur.week}`;
    $("#statCurrentTitle").textContent = cur.title;

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
  }

  function renderPhaseGrid() {
    const grid = $("#phaseGrid");
    grid.innerHTML = "";
    data.phases.forEach((p) => {
      const el = document.createElement("article");
      el.className = "phase-card";
      el.style.borderLeftColor = cfg.PHASE_COLORS[p.id] || "var(--clay)";
      el.innerHTML = `<h4>${p.name}</h4><p>Weeks ${p.weeks} · ${p.theme}</p>`;
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
        <span class="week-link-title">${w.title}</span>`;
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
    const maxDone = Math.max(0, ...state.completedWeeks, 0);
    data.checkpoints.forEach((cp) => {
      const li = document.createElement("li");
      const pass = maxDone >= cp.after_week;
      li.className = pass ? "pass" : "";
      li.textContent = `${cp.id} (W${cp.after_week}): ${pass ? "✓" : "—"} ${cp.label.slice(0, 40)}…`;
      ul.appendChild(li);
    });
  }

  function setActiveTab(tab) {
    state.activeTab = tab;
    saveState();
    $$(".tab").forEach((t) => t.classList.toggle("active", t.dataset.tab === tab));
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
    $("#monthChip").textContent = `Month ${w.month}`;
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
    $("#phaseTip").textContent = `Phase tip: ${cfg.PHASE_TIPS[w.phase] || ""}`;

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
        `<strong>Week 1 bridge:</strong> Draft a BRD in the <a href="${brdHref}">Finance BRD app</a>, export `.md`, then run ` +
        `<code>python3 exercises/week01_brd_checklist.py your-export.md</code> from learning-lab.`;
    } else if (n === 2) {
      bridge.hidden = false;
      bridge.innerHTML =
        `<strong>Week 2 bridge:</strong> Loan rules in Python mirror Section H of ` +
        `<a href="https://github.com/taiphan/finance-brd-training/blob/main/examples/04a-brd-pos-lending.md" target="_blank" rel="noopener">examples/04a-brd-pos-lending.md</a>.`;
    } else if (n >= 25 && n <= 33) {
      bridge.hidden = false;
      bridge.innerHTML =
        `<strong>GenAI phase:</strong> Use BRDs you export from the intake app as RAG corpus (see <code>projects/policy-rag/ask.py</code>).`;
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
    [
      `Open \`${w.exercise}\` in Cursor`,
      `Run: \`${w.run}\` (from learning-lab/)`,
      `Output matches: ${w.deliverable}`,
      `Skill checkpoint: ${skill.checkpoint}`,
    ].forEach((step) => {
      const li = document.createElement("li");
      li.textContent = step;
      done.appendChild(li);
    });

    $("#weekNotes").value = state.notes[String(n)] || "";
    $("#completeWeek").checked = isComplete(n);

    $("#prevWeek").disabled = n <= 1;
    $("#nextWeek").textContent = n >= 52 ? "Finish path ✓" : "Next week →";

    setActiveTab(state.activeTab || "overview");
    updateProgressUI();
  }

  function bindEvents() {
    $("#menuToggle").addEventListener("click", () => {
      $("#sidebar").classList.toggle("open");
    });

    $("#continueBtn").addEventListener("click", () => showWeek(nextIncompleteWeek()));
    $("#homeContinue").addEventListener("click", () => showWeek(nextIncompleteWeek()));
    $("#homeWeek1").addEventListener("click", () => showWeek(1));

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
      const res = await fetch(cfg.DATA_URL);
      if (!res.ok) throw new Error(res.statusText);
      data = await res.json();
    } catch (err) {
      $("#main").innerHTML = `<div class="card"><h2>Could not load curriculum</h2><p>Run a local server from <code>ai-factory/learning-app</code> and ensure <code>learning-data.json</code> exists.</p><pre>${err.message}</pre></div>`;
      return;
    }

    renderPhaseFilter();
    renderWeekList("all");
    renderPhaseGrid();
    bindEvents();
    route();
  }

  init();
})();
