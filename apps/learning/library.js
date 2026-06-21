/**
 * Library — browse all repo files from app-files-manifest.json
 */
(function () {
  const cfg = window.LEARNING_CONFIG;
  let manifest = null;
  let filterCategory = "all";
  let searchQuery = "";
  let onWeekClick = null;

  const $ = (sel) => document.querySelector(sel);

  function kindLabel(kind) {
    const map = {
      python: "Python",
      markdown: "MD",
      deck: "PPTX",
      sql: "SQL",
      json: "JSON",
      javascript: "JS",
      data: "Data",
      notebook: "Notebook",
    };
    return map[kind] || kind;
  }

  function linkFor(file) {
    if (file.local_url && file.kind === "deck") {
      return { href: file.local_url, label: "Download", download: true };
    }
    return { href: file.url, label: "GitHub", external: true };
  }

  function filteredFiles() {
    if (!manifest?.files) return [];
    const q = searchQuery.trim().toLowerCase();
    return manifest.files.filter((f) => {
      if (filterCategory !== "all" && f.category !== filterCategory) return false;
      if (!q) return true;
      const hay = `${f.path} ${f.label} ${f.name} ${f.description || ""}`.toLowerCase();
      return hay.includes(q);
    });
  }

  function renderStats(count) {
    const el = $("#libraryStats");
    if (!el) return;
    const total = manifest?.total || 0;
    el.textContent =
      count === total
        ? `${total} files · open on GitHub or download decks locally`
        : `Showing ${count} of ${total} files`;
  }

  function renderCategoryOptions() {
    const sel = $("#libraryCategory");
    if (!sel || !manifest) return;
    const current = filterCategory;
    sel.innerHTML = `<option value="all">All categories</option>`;
    Object.entries(manifest.categories || {}).forEach(([id, label]) => {
      const opt = document.createElement("option");
      opt.value = id;
      opt.textContent = `${label} (${manifest.counts?.[id] || 0})`;
      sel.appendChild(opt);
    });
    sel.value = current;
  }

  function renderBody() {
    const body = $("#libraryBody");
    if (!body || !manifest) return;

    const files = filteredFiles();
    renderStats(files.length);
    body.replaceChildren();

    if (!files.length) {
      const empty = document.createElement("div");
      empty.className = "card library-empty";
      const p = document.createElement("p");
      p.textContent = "No files match your filter.";
      empty.appendChild(p);
      body.appendChild(empty);
      return;
    }

    const groups = new Map();
    files.forEach((f) => {
      if (!groups.has(f.category)) groups.set(f.category, []);
      groups.get(f.category).push(f);
    });

    const order = Object.keys(manifest.categories || {});
    const sortedKeys = [...groups.keys()].sort(
      (a, b) => (order.indexOf(a) === -1 ? 99 : order.indexOf(a)) - (order.indexOf(b) === -1 ? 99 : order.indexOf(b))
    );

    sortedKeys.forEach((cat) => {
      const section = document.createElement("section");
      section.className = "card library-group";

      const h3 = document.createElement("h3");
      h3.className = "library-group-title";
      const titleText = manifest.categories[cat] || cat;
      h3.appendChild(document.createTextNode(titleText + " "));
      const countSpan = document.createElement("span");
      countSpan.className = "library-group-count";
      countSpan.textContent = String(groups.get(cat).length);
      h3.appendChild(countSpan);
      section.appendChild(h3);

      const list = document.createElement("ul");
      list.className = "library-list";

      groups.get(cat).forEach((f) => {
        const li = document.createElement("li");
        li.className = "library-item";

        const meta = document.createElement("div");
        meta.className = "library-item-meta";

        const kindSpan = document.createElement("span");
        kindSpan.className = "library-kind";
        kindSpan.textContent = kindLabel(f.kind);
        meta.appendChild(kindSpan);

        if (f.week) {
          const weekBtn = document.createElement("button");
          weekBtn.type = "button";
          weekBtn.className = "library-week";
          weekBtn.dataset.week = String(f.week);
          weekBtn.textContent = `W${String(f.week).padStart(2, "0")}`;
          meta.appendChild(weekBtn);
        }

        const pathCode = document.createElement("code");
        pathCode.className = "library-path";
        pathCode.textContent = f.path;
        meta.appendChild(pathCode);

        const main = document.createElement("div");
        main.className = "library-item-main";
        const labelStrong = document.createElement("strong");
        labelStrong.textContent = f.label;
        main.appendChild(labelStrong);
        if (f.description) {
          const desc = document.createElement("p");
          desc.className = "hint";
          desc.textContent = f.description;
          main.appendChild(desc);
        }

        const actions = document.createElement("div");
        actions.className = "library-item-actions";
        const link = linkFor(f);
        const a = document.createElement("a");
        a.href = link.href;
        a.className = "btn btn-ghost btn-sm";
        a.textContent = link.label;
        if (link.external) {
          a.target = "_blank";
          a.rel = "noopener noreferrer";
        }
        if (link.download) a.setAttribute("download", f.name);
        actions.appendChild(a);

        if (f.week && onWeekClick) {
          meta.querySelector(".library-week")?.addEventListener("click", (e) => {
            e.preventDefault();
            onWeekClick(f.week);
          });
        }

        li.appendChild(main);
        li.appendChild(meta);
        li.appendChild(actions);
        list.appendChild(li);
      });

      section.appendChild(list);
      body.appendChild(section);
    });
  }

  function bindControls() {
    const search = $("#librarySearch");
    const cat = $("#libraryCategory");
    if (search) {
      search.value = searchQuery;
      search.oninput = (e) => {
        searchQuery = e.target.value;
        renderBody();
      };
    }
    if (cat) {
      cat.onchange = (e) => {
        filterCategory = e.target.value;
        renderBody();
      };
    }
  }

  function init(filesManifest, callbacks) {
    manifest = filesManifest;
    onWeekClick = callbacks?.onWeekClick || null;
    filterCategory = "all";
    searchQuery = "";
    renderCategoryOptions();
    bindControls();
    renderBody();
  }

  function refresh() {
    renderCategoryOptions();
    renderBody();
  }

  window.LearningLibrary = { init, refresh };
})();
