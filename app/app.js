import { FECREDIT } from './config/fe-credit.js';

const STORAGE_KEY = 'fecredit-brd-draft';
let lang = 'en';
let currentStep = 0;

const i18n = {
  en: {
    subtitle: 'Business Requirements Document — first gate in IT delivery pipeline',
    pipelineTitle: 'Delivery pipeline',
    pipelineHint: 'You are here: BRD gate. After acceptance → FSD → Scrum → UAT → CAB ship.',
    routingTitle: 'Stakeholder routing',
    routingHint: 'IT-Governance, IT-Security, and GRC/Legal — updates as you complete the form.',
    gatesTitle: 'Hard gates',
    tipsTitle: 'Golden rule',
    goldenRule: 'Write the problem and business rules — not the system design.',
    frameworkLink: 'See IT Ops Framework and Application Landscape.',
    bucketWarn: 'This request type should use Service Desk — not a BRD. Redirect to ITSM for access/incidents.',
    bucketHint: 'Business bucket: you define rules and data. IT executes after approval.',
    newIntegration: 'Involves new system integration or architecture change?',
    exportTitle: 'Export BRD',
    exportDesc: 'Copy markdown or download. Includes delivery path and stakeholder routing.',
    copy: 'Copy',
    download: 'Download .md',
    close: 'Close',
    prev: 'Previous',
    next: 'Next',
    export: 'Export BRD',
    noRouting: 'Standard path: BA quality review → IT triage only.',
    coachMsg: 'Technical terms detected in to-be description. Consider rewriting as a business outcome (BA coaching tip).',
    steps: ['Request', 'Summary', 'Objectives', 'Current state', 'To-be & scope', 'Rules & data', 'Compliance', 'Acceptance'],
    panelDesc: {
      0: 'Classify request type, identify unit, sponsor, and timeline.',
      1: 'State the business problem and impact — not the IT solution.',
      2: 'Define measurable KPIs with baseline and target.',
      3: 'Document today’s process and which FE Credit systems are involved.',
      4: 'Describe the future process and clear scope boundaries.',
      5: 'Business rules and data classification — IT must not guess these.',
      6: 'FE Credit compliance screening — routes to IT-Security, GRC, or Legal.',
      7: 'Testable Given/When/Then criteria — become UAT scripts after FSD delivery.',
    },
  },
  vi: {
    subtitle: 'BRD — cổng đầu tiên trong quy trình giao hàng IT',
    pipelineTitle: 'Quy trình giao hàng',
    pipelineHint: 'Bạn đang ở: Cổng BRD. Sau khi chấp nhận → FSD → Scrum → UAT → CAB.',
    routingTitle: 'Luồng stakeholder',
    routingHint: 'IT-Governance, IT-Security, GRC/Pháp chế — cập nhật khi điền form.',
    gatesTitle: 'Cổng bắt buộc',
    tipsTitle: 'Nguyên tắc vàng',
    goldenRule: 'Viết vấn đề và quy tắc nghiệp vụ — không viết thiết kế hệ thống.',
    frameworkLink: 'Xem IT Ops Framework và Application Landscape.',
    bucketWarn: 'Loại yêu cầu này dùng Service Desk — không phải BRD.',
    bucketHint: 'Business bucket: nghiệp vụ định nghĩa quy tắc. IT thực hiện sau khi duyệt.',
    newIntegration: 'Có tích hợp hệ thống mới hoặc thay đổi kiến trúc?',
    exportTitle: 'Xuất BRD',
    exportDesc: 'Sao chép markdown hoặc tải về. Bao gồm quy trình giao hàng và routing.',
    copy: 'Sao chép',
    download: 'Tải .md',
    close: 'Đóng',
    prev: 'Quay lại',
    next: 'Tiếp theo',
    export: 'Xuất BRD',
    noRouting: 'Luồng chuẩn: BA rà soát → IT triage.',
    coachMsg: 'Phát hiện thuật ngữ kỹ thuật. Hãy viết lại thành kết quả nghiệp vụ (gợi ý từ BA).',
    steps: ['Yêu cầu', 'Tóm tắt', 'Mục tiêu', 'Hiện trạng', 'Mục tiêu & phạm vi', 'Quy tắc & dữ liệu', 'Tuân thủ', 'Nghiệm thu'],
    panelDesc: {
      0: 'Phân loại yêu cầu, đơn vị, sponsor và thời hạn.',
      1: 'Vấn đề nghiệp vụ và tác động — không phải giải pháp IT.',
      2: 'KPI đo lường được với hiện trạng và mục tiêu.',
      3: 'Quy trình hiện tại và hệ thống FE Credit liên quan.',
      4: 'Quy trình tương lai và ranh giới phạm vi.',
      5: 'Quy tắc nghiệp vụ và phân loại dữ liệu.',
      6: 'Sàng lọc tuân thủ — route IT-Security, GRC, Pháp chế.',
      7: 'Tiêu chí Cho trước / Khi / Thì — thành UAT sau khi FSD giao.',
    },
  },
};

const STEPS = 8;

function t(key) {
  return i18n[lang][key] ?? i18n.en[key] ?? key;
}

function lbl(obj) {
  return obj.label[lang] || obj.label.en;
}

function getFormData() {
  const form = document.getElementById('brdForm');
  const fd = new FormData(form);
  const data = Object.fromEntries(fd.entries());
  data.systems = fd.getAll('systems');
  data.dataTypes = fd.getAll('dataTypes');
  data.products = fd.getAll('products');
  data.acceptance = fd.getAll('acceptance');
  return data;
}

function computeRouting(data) {
  const routes = new Set();
  FECREDIT.complianceQuestions.forEach((q) => {
    if (data[q.id] === 'yes') q.routes.forEach((r) => routes.add(r));
  });
  if (data.dataClass === 'restricted') routes.add('it_security');
  if (data.remoteAccess === 'exception') routes.add('it_security');
  if (data.newIntegration === 'yes') routes.add('it_governance');
  if (data.q4 === 'yes') routes.add('it_security');
  return [...routes];
}

function getRequestTypeMeta(id) {
  return FECREDIT.requestTypes.find((r) => r.id === id);
}

function renderPipeline() {
  const list = document.getElementById('pipelineList');
  if (!list) return;
  list.innerHTML = FECREDIT.deliveryPhases
    .map((phase) => {
      const active = phase.id === 'brd' ? ' active' : '';
      const label = phase.label[lang] || phase.label.en;
      const owner = phase.owner[lang] || phase.owner.en;
      return `<li class="pipeline-step${active}"><span class="pipeline-label">${label}</span><span class="pipeline-owner">${owner}</span></li>`;
    })
    .join('');
}

function renderGates() {
  const list = document.getElementById('gatesList');
  if (!list) return;
  list.innerHTML = FECREDIT.hardGates
    .map((g) => `<li>${g[lang] || g.en}</li>`)
    .join('');
}

function renderRoutingGroups(routes) {
  const container = document.getElementById('routingGroups');
  if (!container) return;

  if (routes.length === 0) {
    container.innerHTML = `<p class="muted">${t('noRouting')}</p>`;
    return;
  }

  const grouped = { it_governance: [], it_security: [], compliance: [] };
  routes.forEach((r) => {
    const cat = FECREDIT.routeCategoryMap[r] || 'compliance';
    const label = FECREDIT.routeLabels[r]?.[lang] || r;
    grouped[cat].push(label);
  });

  container.innerHTML = Object.entries(grouped)
    .filter(([, items]) => items.length > 0)
    .map(([catId, items]) => {
      const cat = FECREDIT.routeCategories[catId];
      const title = cat[lang] || cat.en;
      const lis = items.map((l) => `<li>${l}</li>`).join('');
      return `<div class="route-group" data-cat="${catId}"><h3>${title}</h3><ul class="routing-list">${lis}</ul></div>`;
    })
    .join('');
}

function updateBucketWarning(data) {
  const meta = getRequestTypeMeta(data.requestType);
  const warn = document.getElementById('bucketWarn');
  const hint = document.getElementById('bucketHint');
  if (!warn || !hint) return;

  if (meta && !meta.needsBrd) {
    warn.textContent = meta.hint?.[lang] || meta.hint?.en || t('bucketWarn');
    warn.classList.add('visible');
    hint.classList.remove('visible');
  } else if (meta?.hint) {
    warn.classList.remove('visible');
    hint.textContent = meta.hint[lang] || meta.hint.en;
    hint.classList.add('visible');
  } else if (meta?.bucket === 'business') {
    warn.classList.remove('visible');
    hint.textContent = t('bucketHint');
    hint.classList.add('visible');
  } else {
    warn.classList.remove('visible');
    hint.classList.remove('visible');
  }
}

function computeScore(data) {
  let score = 0;
  const checks = [
    () => data.requestType,
    () => data.title?.trim(),
    () => data.businessUnit,
    () => data.sponsor?.trim(),
    () => data.problem?.trim()?.length >= 50,
    () => data.outcome?.trim(),
    () => data.objectives?.trim(),
    () => data.currentProcess?.trim(),
    () => (data.systems?.length ?? 0) > 0,
    () => data.toBe?.trim(),
    () => data.inScope?.trim() && data.outScope?.trim(),
    () => data.businessRules?.trim(),
    () => data.dataClass,
    () => (data.acceptance?.filter((a) => a?.trim()).length ?? 0) >= 5,
    () => FECREDIT.complianceQuestions.every((q) => data[q.id]),
  ];
  checks.forEach((fn) => {
    if (fn()) score += 100 / checks.length;
  });
  return Math.round(score);
}

function updateUI() {
  const data = getFormData();
  const score = computeScore(data);
  const badge = document.getElementById('scoreBadge');
  badge.textContent = `${score}%`;
  badge.classList.toggle('pass', score >= 80);
  badge.classList.toggle('fail', score < 80);

  const routes = computeRouting(data);
  renderRoutingGroups(routes);
  updateBucketWarning(data);
  renderPipeline();

  const toBe = (data.toBe || '').toLowerCase();
  const coach = document.getElementById('coachWarn');
  if (coach) {
    const hit = FECREDIT.technicalKeywords.some((k) => toBe.includes(k));
    coach.classList.toggle('visible', hit);
  }

  saveDraft(data);
}

function saveDraft(data) {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify({ data, currentStep, lang }));
  } catch (_) {}
}

function loadDraft() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) return;
    const { data, currentStep: step, lang: l } = JSON.parse(raw);
    if (l) lang = l;
    const form = document.getElementById('brdForm');
    Object.entries(data).forEach(([k, v]) => {
      if (k === 'systems' || k === 'dataTypes' || k === 'products') {
        (v || []).forEach((val) => {
          const el = form.querySelector(`[name="${k}"][value="${val}"]`);
          if (el) el.checked = true;
        });
      } else if (k === 'acceptance') {
        (v || []).forEach((val, i) => {
          const el = form.querySelector(`[name="acceptance"][data-idx="${i}"]`);
          if (el) el.value = val;
        });
      } else {
        const el = form.querySelector(`[name="${k}"]`);
        if (el) el.value = v;
      }
    });
    if (typeof step === 'number') currentStep = step;
  } catch (_) {}
}

function renderSystemsCheckboxes() {
  const groups = {};
  FECREDIT.applications.forEach((app) => {
    if (!groups[app.group]) groups[app.group] = [];
    groups[app.group].push(app);
  });
  return Object.entries(groups)
    .map(([groupId, apps]) => {
      const gTitle = FECREDIT.appGroups[groupId]?.[lang] || groupId;
      const items = apps
        .map(
          (app) => `
        <label title="${app.desc[lang] || ''}">
          <input type="checkbox" name="systems" value="${app.id}" />
          ${lbl(app)}
        </label>`
        )
        .join('');
      return `<div class="app-group-title">${gTitle}</div><div class="checkbox-grid">${items}</div>`;
    })
    .join('');
}

function renderComplianceRadios() {
  return FECREDIT.complianceQuestions
    .map(
      (q) => `
    <div class="field required">
      <label>${q.label[lang]}</label>
      <div class="radio-row">
        <label><input type="radio" name="${q.id}" value="yes" required /> ${lang === 'vi' ? 'Có' : 'Yes'}</label>
        <label><input type="radio" name="${q.id}" value="no" /> ${lang === 'vi' ? 'Không' : 'No'}</label>
        <label><input type="radio" name="${q.id}" value="na" /> N/A</label>
      </div>
    </div>`
    )
    .join('');
}

function renderForm() {
  const buOptions = FECREDIT.businessUnits
    .map((u) => `<option value="${u.id}">${lbl(u)}</option>`)
    .join('');
  const priOptions = FECREDIT.priorityCategories
    .map((p) => `<option value="${p.id}">${lbl(p)}</option>`)
    .join('');
  const prodChecks = FECREDIT.products
    .map((p) => `<label><input type="checkbox" name="products" value="${p.id}" /> ${lbl(p)}</label>`)
    .join('');
  const dataChecks = FECREDIT.dataTypes
    .map((d) => `<label><input type="checkbox" name="dataTypes" value="${d.id}" /> ${lbl(d)}</label>`)
    .join('');

  const acFields = [0, 1, 2, 3, 4]
    .map(
      (i) => `
    <div class="ac-row">
      <span class="ac-num">AC-${String(i + 1).padStart(2, '0')}</span>
      <textarea name="acceptance" data-idx="${i}" rows="2" placeholder="Given / When / Then"></textarea>
    </div>`
    )
    .join('');

  const reqTypeOptions = FECREDIT.requestTypes
    .map((r) => `<option value="${r.id}">${lbl(r)}</option>`)
    .join('');

  const form = document.getElementById('brdForm');
  form.innerHTML = `
    <div class="panel active" data-step="0">
      <h2>${t('steps')[0]}</h2>
      <p class="panel-desc">${t('panelDesc')[0]}</p>
      <div class="field required"><label>${lang === 'vi' ? 'Loại yêu cầu' : 'Request type'}</label><select name="requestType" required><option value="">—</option>${reqTypeOptions}</select></div>
      <div id="bucketWarn" class="bucket-warn"></div>
      <div id="bucketHint" class="bucket-hint"></div>
      <div class="field required"><label>${lang === 'vi' ? 'Tên BRD' : 'BRD title'}</label><input name="title" type="text" maxlength="120" /></div>
      <div class="grid-2">
        <div class="field required"><label>${lang === 'vi' ? 'Đơn vị' : 'Business unit'}</label><select name="businessUnit"><option value="">—</option>${buOptions}</select></div>
        <div class="field required"><label>${lang === 'vi' ? 'Ưu tiên' : 'Priority'}</label><select name="priority"><option value="">—</option>${priOptions}</select></div>
      </div>
      <div class="grid-2">
        <div class="field required"><label>${lang === 'vi' ? 'Người yêu cầu' : 'Requester'}</label><input name="requester" type="text" /></div>
        <div class="field required"><label>Email</label><input name="email" type="email" /></div>
      </div>
      <div class="field required"><label>${lang === 'vi' ? 'Sponsor (Giám đốc+)' : 'Business sponsor (Director+)'}</label><input name="sponsor" type="text" /></div>
      <div class="field"><label>${lang === 'vi' ? 'Sản phẩm liên quan' : 'Products involved'}</label><div class="checkbox-grid">${prodChecks}</div></div>
      <div class="grid-2">
        <div class="field required"><label>${lang === 'vi' ? 'Go-live mục tiêu' : 'Target go-live'}</label><input name="goLive" type="date" /></div>
        <div class="field"><label>${lang === 'vi' ? 'Hạn pháp lý' : 'Regulatory deadline'}</label><input name="regDeadline" type="date" /></div>
      </div>
    </div>

    <div class="panel" data-step="1">
      <h2>${t('steps')[1]}</h2>
      <p class="panel-desc">${t('panelDesc')[1]}</p>
      <div class="field required"><label>${lang === 'vi' ? 'Vấn đề nghiệp vụ' : 'Business problem'}</label><textarea name="problem" minlength="50"></textarea><p class="hint">min 50 characters</p></div>
      <div class="field"><label>${lang === 'vi' ? 'Ai bị ảnh hưởng' : 'Who is impacted'}</label><textarea name="impacted"></textarea></div>
      <div class="field"><label>${lang === 'vi' ? 'Hậu quả nếu không làm' : 'Impact if not addressed'}</label><textarea name="impact"></textarea></div>
      <div class="field required"><label>${lang === 'vi' ? 'Kết quả mong muốn' : 'Desired outcome (one sentence)'}</label><input name="outcome" type="text" /></div>
    </div>

    <div class="panel" data-step="2">
      <h2>${t('steps')[2]}</h2>
      <p class="panel-desc">${t('panelDesc')[2]}</p>
      <div class="field required"><label>${lang === 'vi' ? 'Mục tiêu & KPI' : 'Objectives & KPIs'}</label><textarea name="objectives" placeholder="Baseline → Target | How measured"></textarea></div>
    </div>

    <div class="panel" data-step="3">
      <h2>${t('steps')[3]}</h2>
      <p class="panel-desc">${t('panelDesc')[3]}</p>
      <div class="field required"><label>${lang === 'vi' ? 'Quy trình hiện tại' : 'Current process'}</label><textarea name="currentProcess"></textarea></div>
      <div class="field required"><label>${lang === 'vi' ? 'Hệ thống FE Credit' : 'FE Credit systems involved'}</label>${renderSystemsCheckboxes()}</div>
      <div class="grid-2">
        <div class="field"><label>${lang === 'vi' ? 'Số người dùng' : 'Users affected'}</label><input name="userCount" type="number" min="1" /></div>
        <div class="field"><label>${lang === 'vi' ? 'Giao dịch/tháng' : 'Transactions/month'}</label><input name="txMonth" type="number" min="0" /></div>
      </div>
    </div>

    <div class="panel" data-step="4">
      <h2>${t('steps')[4]}</h2>
      <p class="panel-desc">${t('panelDesc')[4]}</p>
      <div class="field required"><label>${lang === 'vi' ? 'Quy trình mục tiêu' : 'To-be process'}</label><textarea name="toBe"></textarea><div id="coachWarn" class="coach-warn">${t('coachMsg')}</div></div>
      <div class="field required"><label>${lang === 'vi' ? 'Trong phạm vi' : 'In scope'}</label><textarea name="inScope"></textarea></div>
      <div class="field required"><label>${lang === 'vi' ? 'Ngoài phạm vi' : 'Out of scope'}</label><textarea name="outScope"></textarea></div>
      <div class="field"><label>${lang === 'vi' ? 'Giả định' : 'Assumptions'}</label><textarea name="assumptions"></textarea></div>
      <div class="field"><label>${t('newIntegration')}</label>
        <div class="radio-row">
          <label><input type="radio" name="newIntegration" value="yes" /> ${lang === 'vi' ? 'Có' : 'Yes'}</label>
          <label><input type="radio" name="newIntegration" value="no" checked /> ${lang === 'vi' ? 'Không' : 'No'}</label>
        </div>
      </div>
    </div>

    <div class="panel" data-step="5">
      <h2>${t('steps')[5]}</h2>
      <p class="panel-desc">${t('panelDesc')[5]}</p>
      <div class="field required"><label>${lang === 'vi' ? 'Quy tắc nghiệp vụ' : 'Business rules'}</label><textarea name="businessRules"></textarea></div>
      <div class="field required"><label>${lang === 'vi' ? 'Phân loại dữ liệu' : 'Data classification'}</label>
        <select name="dataClass"><option value="">—</option>
          <option value="public">${lang === 'vi' ? 'Công khai' : 'Public'}</option>
          <option value="internal">${lang === 'vi' ? 'Nội bộ' : 'Internal'}</option>
          <option value="confidential">${lang === 'vi' ? 'Mật' : 'Confidential'}</option>
          <option value="restricted">${lang === 'vi' ? 'Hạn chế' : 'Restricted'}</option>
        </select>
      </div>
      <div class="field"><label>${lang === 'vi' ? 'Loại dữ liệu' : 'Data types'}</label><div class="checkbox-grid">${dataChecks}</div></div>
      <div class="field required"><label>${lang === 'vi' ? 'Truy cập từ xa' : 'Remote / home access'}</label>
        <select name="remoteAccess"><option value="none">${lang === 'vi' ? 'Không' : 'None'}</option>
          <option value="managed">${lang === 'vi' ? 'Thiết bị quản lý' : 'Managed device only'}</option>
          <option value="vdi">VDI</option>
          <option value="exception">${lang === 'vi' ? 'Cần ngoại lệ Security' : 'Security exception needed'}</option>
        </select>
      </div>
    </div>

    <div class="panel" data-step="6">
      <h2>${t('steps')[6]}</h2>
      <p class="panel-desc">${t('panelDesc')[6]}</p>
      ${renderComplianceRadios()}
      <div class="field"><label>${lang === 'vi' ? 'Rủi ro nếu triển khai sai' : 'Risks if implemented incorrectly'}</label><textarea name="risks"></textarea></div>
    </div>

    <div class="panel" data-step="7">
      <h2>${t('steps')[7]}</h2>
      <p class="panel-desc">${t('panelDesc')[7]}</p>
      ${acFields}
    </div>

    <div class="form-actions">
      <button type="button" class="btn btn-ghost" id="btnPrev">${t('prev')}</button>
      <div>
        <button type="button" class="btn btn-ghost" id="btnExport">${t('export')}</button>
        <button type="button" class="btn btn-primary" id="btnNext">${t('next')}</button>
      </div>
    </div>
  `;

  form.addEventListener('input', updateUI);
  form.addEventListener('change', updateUI);
  document.getElementById('btnPrev').addEventListener('click', () => goStep(currentStep - 1));
  document.getElementById('btnNext').addEventListener('click', () => {
    if (currentStep < STEPS - 1) goStep(currentStep + 1);
    else exportBRD();
  });
  document.getElementById('btnExport').addEventListener('click', exportBRD);
}

function renderStepNav() {
  const nav = document.getElementById('stepNav');
  nav.innerHTML = t('steps')
    .map(
      (label, i) =>
        `<button type="button" class="step-tab ${i === currentStep ? 'active' : ''} ${i < currentStep ? 'done' : ''}" data-step="${i}">${i + 1}. ${label}</button>`
    )
    .join('');
  nav.querySelectorAll('.step-tab').forEach((btn) => {
    btn.addEventListener('click', () => goStep(Number(btn.dataset.step)));
  });
}

function goStep(n) {
  currentStep = Math.max(0, Math.min(STEPS - 1, n));
  document.querySelectorAll('.panel').forEach((p) => {
    p.classList.toggle('active', Number(p.dataset.step) === currentStep);
  });
  renderStepNav();
  document.getElementById('btnPrev').disabled = currentStep === 0;
  document.getElementById('btnNext').textContent =
    currentStep === STEPS - 1 ? t('export') : t('next');
  saveDraft(getFormData());
}

function systemLabels(ids) {
  return (ids || [])
    .map((id) => FECREDIT.applications.find((a) => a.id === id))
    .filter(Boolean)
    .map((a) => lbl(a))
    .join(', ');
}

function exportBRD() {
  const d = getFormData();
  const id = `BRD-${new Date().getFullYear()}-${String(Math.floor(Math.random() * 9000) + 1000)}`;
  const score = computeScore(d);
  const routes = computeRouting(d);
  const bu = FECREDIT.businessUnits.find((u) => u.id === d.businessUnit);
  const reqMeta = getRequestTypeMeta(d.requestType);

  const routeByCategory = { 'IT-Governance': [], 'IT-Security': [], 'GRC / Legal': [] };
  routes.forEach((r) => {
    const cat = FECREDIT.routeCategoryMap[r] || 'compliance';
    const label = FECREDIT.routeLabels[r]?.en || r;
    if (cat === 'it_governance') routeByCategory['IT-Governance'].push(label);
    else if (cat === 'it_security') routeByCategory['IT-Security'].push(label);
    else routeByCategory['GRC / Legal'].push(label);
  });

  const deliveryPath = FECREDIT.deliveryPhases
    .map((p) => `${p.label.en} (${p.owner.en})`)
    .join(' → ');

  const md = `# FE CREDIT — BUSINESS REQUIREMENTS DOCUMENT

**Document ID:** ${id}
**Generated:** ${new Date().toISOString().slice(0, 10)}
**Quality preview score:** ${score}%
**Request type:** ${reqMeta ? lbl(reqMeta) : d.requestType || '—'}
**Bucket:** ${reqMeta?.bucket === 'it' ? 'IT Service Desk (not BRD path)' : 'Business — define & approve'}

---

## DELIVERY PATH (post-submission)

${deliveryPath}

| Phase | Owner | This BRD stage |
|-------|-------|----------------|
${FECREDIT.deliveryPhases.map((p) => `| ${p.label.en} | ${p.owner.en} | ${p.id === 'brd' ? '**YOU ARE HERE**' : '—'} |`).join('\n')}

### Hard gates
${FECREDIT.hardGates.map((g) => `- ${g.en}`).join('\n')}

### Stakeholder routing
${Object.entries(routeByCategory)
  .map(([cat, items]) => `**${cat}:** ${items.length ? items.join(', ') : 'None'}`)
  .join('\n')}

---

## A. REQUEST INFORMATION

| Field | Value |
|-------|-------|
| BRD Title | ${d.title || ''} |
| Request Type | ${reqMeta ? lbl(reqMeta) : d.requestType || ''} |
| Business Unit | ${bu ? lbl(bu) : d.businessUnit || ''} |
| Requester | ${d.requester || ''} |
| Email | ${d.email || ''} |
| Business Sponsor | ${d.sponsor || ''} |
| Priority | ${d.priority || ''} |
| Target Go-Live | ${d.goLive || ''} |
| Regulatory Deadline | ${d.regDeadline || 'N/A'} |
| Products | ${(d.products || []).join(', ')} |
| New integration / architecture | ${(d.newIntegration || 'no').toUpperCase()} |

## B. EXECUTIVE SUMMARY

**Business problem:** ${d.problem || ''}

**Who is impacted:** ${d.impacted || ''}

**Impact if not addressed:** ${d.impact || ''}

**Desired outcome:** ${d.outcome || ''}

## C. OBJECTIVES & KPIs

${d.objectives || ''}

## D. CURRENT STATE

**Current process:**
${d.currentProcess || ''}

**Systems involved:** ${systemLabels(d.systems)}

**Users affected:** ${d.userCount || '—'} | **Transactions/month:** ${d.txMonth || '—'}

## E. TO-BE & SCOPE

**To-be process:**
${d.toBe || ''}

**In scope:**
${d.inScope || ''}

**Out of scope:**
${d.outScope || ''}

**Assumptions:**
${d.assumptions || ''}

## H. BUSINESS RULES

${d.businessRules || ''}

## I. DATA & SECURITY

**Classification:** ${d.dataClass || ''}
**Data types:** ${(d.dataTypes || []).join(', ')}
**Remote access:** ${d.remoteAccess || ''}

## N. COMPLIANCE SCREENING

${FECREDIT.complianceQuestions.map((q) => `- ${q.label.en}: **${(d[q.id] || '').toUpperCase()}**`).join('\n')}

## L. RISKS

${d.risks || ''}

## M. ACCEPTANCE CRITERIA

${(d.acceptance || [])
  .filter((a) => a?.trim())
  .map((a, i) => `${i + 1}. ${a}`)
  .join('\n')}

---

*Exported from FE Credit BRD Intake App.*
*Next steps: Sponsor sign-off → BA quality gate (≥80%) → IT triage → FSD → Scrum → SIT → UAT → CAB ship.*
*Framework: docs/12-it-operations-stakeholder-framework.md*
`;

  document.getElementById('exportOutput').value = md;
  document.getElementById('exportDialog').showModal();
  document.getElementById('copyExport').onclick = () => navigator.clipboard.writeText(md);
  document.getElementById('downloadExport').onclick = () => {
    const blob = new Blob([md], { type: 'text/markdown' });
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = `${id}.md`;
    a.click();
  };
}

function applyI18n() {
  document.querySelectorAll('[data-i18n]').forEach((el) => {
    const key = el.dataset.i18n;
    if (key === 'goldenRule') {
      el.innerHTML =
        lang === 'vi'
          ? 'Viết <strong>vấn đề và quy tắc nghiệp vụ</strong> — không viết thiết kế hệ thống.'
          : 'Write the <strong>problem and business rules</strong> — not the system design.';
    } else if (key === 'frameworkLink') {
      el.innerHTML =
        lang === 'vi'
          ? 'Xem <a href="../docs/12-it-operations-stakeholder-framework.md">IT Ops Framework</a> và <a href="../docs/00-fe-credit-application-landscape.md">Application Landscape</a>.'
          : 'See <a href="../docs/12-it-operations-stakeholder-framework.md">IT Ops Framework</a> and <a href="../docs/00-fe-credit-application-landscape.md">Application Landscape</a>.';
    } else {
      el.textContent = t(key);
    }
  });
}

function init() {
  renderForm();
  loadDraft();
  renderStepNav();
  renderGates();
  renderPipeline();
  goStep(currentStep);
  applyI18n();
  updateUI();

  document.getElementById('langToggle').addEventListener('click', () => {
    lang = lang === 'en' ? 'vi' : 'en';
    const data = getFormData();
    renderForm();
    Object.entries(data).forEach(([k, v]) => {
      /* re-filled by loadDraft pattern - manually set */
    });
    const form = document.getElementById('brdForm');
    Object.entries(data).forEach(([k, v]) => {
      if (k === 'systems' || k === 'dataTypes' || k === 'products') {
        (v || []).forEach((val) => {
          const el = form.querySelector(`[name="${k}"][value="${val}"]`);
          if (el) el.checked = true;
        });
      } else if (k === 'acceptance') {
        (v || []).forEach((val, i) => {
          const el = form.querySelector(`[name="acceptance"][data-idx="${i}"]`);
          if (el) el.value = val;
        });
      } else {
        const el = form.querySelector(`[name="${k}"]`);
        if (el) {
          if (el.type === 'radio') {
            const r = form.querySelector(`[name="${k}"][value="${v}"]`);
            if (r) r.checked = true;
          } else el.value = v;
        }
      }
    });
    renderStepNav();
    renderGates();
    renderPipeline();
    goStep(currentStep);
    applyI18n();
    updateUI();
  });
}

init();
