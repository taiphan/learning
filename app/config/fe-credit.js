/** FE Credit BRD intake — application landscape & form config */
export const FECREDIT = {
  org: {
    name: 'FE Credit',
    legalName: 'SMBC Vietnam Prosperity Bank Finance Company Limited',
    formerName: 'VPBank Finance / FECredit',
  },

  businessUnits: [
    { id: 'digital', label: { en: 'Digital & Customer Experience', vi: 'Kỹ thuật số & Trải nghiệm KH' } },
    { id: 'sales', label: { en: 'Sales / Partner Network (POS)', vi: 'Kinh doanh / Đối tác (POS)' } },
    { id: 'credit', label: { en: 'Credit & Risk', vi: 'Tín dụng & Rủi ro' } },
    { id: 'collections', label: { en: 'Collections & Recovery', vi: 'Thu hồi nợ & Xử lý nợ' } },
    { id: 'cards', label: { en: 'Cards', vi: 'Thẻ tín dụng' } },
    { id: 'cx', label: { en: 'Customer Service / Call Center', vi: 'Chăm sóc KH / Tổng đài' } },
    { id: 'ops', label: { en: 'Operations / Back Office', vi: 'Vận hành / Hậu phương' } },
    { id: 'finance', label: { en: 'Finance & Accounting', vi: 'Tài chính & Kế toán' } },
    { id: 'hr', label: { en: 'HR & Admin', vi: 'Nhân sự' } },
    { id: 'other', label: { en: 'Other', vi: 'Khác' } },
  ],

  products: [
    { id: 'cash_loan', label: { en: 'Personal cash loan', vi: 'Vay tiền mặt' } },
    { id: 'twowheeler', label: { en: 'Two-wheeler installment', vi: 'Vay mua xe máy' } },
    { id: 'durable', label: { en: 'Consumer durable (phone, electronics)', vi: 'Vay tiêu dùng (điện thoại, điện máy)' } },
    { id: 'card', label: { en: 'Credit card', vi: 'Thẻ tín dụng' } },
    { id: 'insurance', label: { en: 'Insurance (SHIELD)', vi: 'Bảo hiểm (SHIELD)' } },
    { id: 'na', label: { en: 'Not product-specific', vi: 'Không gắn sản phẩm cụ thể' } },
  ],

  applications: [
    {
      id: 'fe_online',
      group: 'customer',
      label: { en: 'FE ONLINE 2.0', vi: 'FE ONLINE 2.0' },
      desc: { en: 'Customer mobile app — loans, cards, loan management', vi: 'App khách hàng — vay, thẻ, quản lý khoản vay' },
    },
    {
      id: 'nap',
      group: 'customer',
      label: { en: '$NAP', vi: '$NAP' },
      desc: { en: 'Digital lending — apply, approval, credit tools', vi: 'Cho vay số — đăng ký, duyệt, công cụ tín dụng' },
    },
    {
      id: 'shield',
      group: 'customer',
      label: { en: 'SHIELD', vi: 'SHIELD' },
      desc: { en: 'Loan, card, insurance mobile', vi: 'App vay, thẻ, bảo hiểm' },
    },
    {
      id: 'pos_los',
      group: 'channel',
      label: { en: 'Partner POS / LOS tablet', vi: 'POS / LOS đối tác' },
      desc: { en: 'In-store origination at partner points', vi: 'Bán hàng tại điểm đối tác' },
    },
    {
      id: 'finacle_lms',
      group: 'core',
      label: { en: 'Finacle LMS', vi: 'Finacle LMS' },
      desc: { en: 'Loan management — accounts, disbursement, repayment', vi: 'Quản lý khoản vay — giải ngân, thu nợ' },
    },
    {
      id: 'finacle_cif',
      group: 'core',
      label: { en: 'Finacle CIF', vi: 'Finacle CIF' },
      desc: { en: 'Customer information file / KYC master', vi: 'Hồ sơ khách hàng / KYC' },
    },
    {
      id: 'finacle_assure',
      group: 'core',
      label: { en: 'Finacle Assure', vi: 'Finacle Assure' },
      desc: { en: 'Finacle assurance module', vi: 'Module Assure' },
    },
    {
      id: 'firstvision',
      group: 'core',
      label: { en: 'Card platform (FirstVision)', vi: 'Hệ thống thẻ (FirstVision)' },
      desc: { en: 'Credit card issuance and servicing', vi: 'Phát hành và vận hành thẻ' },
    },
    {
      id: 'collections',
      group: 'ops',
      label: { en: 'Collections platform', vi: 'Hệ thống thu hồi nợ' },
      desc: { en: 'DPD, reminders, recovery', vi: 'DPD, nhắc nợ, thu hồi' },
    },
    {
      id: 'crm',
      group: 'ops',
      label: { en: 'Call center / CRM', vi: 'Tổng đài / CRM' },
      desc: { en: 'Tickets, inbound/outbound contact', vi: 'Phiếu yêu cầu, gọi đi/đến' },
    },
    {
      id: 'chatbot',
      group: 'customer',
      label: { en: 'AI Chatbot', vi: 'Chatbot AI' },
      desc: { en: '24/7 digital customer support', vi: 'Hỗ trợ KH 24/7' },
    },
    {
      id: 'esign',
      group: 'ops',
      label: { en: 'eSign', vi: 'eSign' },
      desc: { en: 'Electronic contract signing', vi: 'Ký hợp đồng điện tử' },
    },
    {
      id: 'workflow',
      group: 'ops',
      label: { en: 'Workflow / BPM', vi: 'Workflow / BPM' },
      desc: { en: 'Approval chains and process automation', vi: 'Luồng phê duyệt' },
    },
    {
      id: 'bi',
      group: 'ops',
      label: { en: 'BI / Reporting', vi: 'BI / Báo cáo' },
      desc: { en: 'Dashboards and management reports', vi: 'Dashboard và báo cáo' },
    },
    {
      id: 'sms',
      group: 'ops',
      label: { en: 'SMS / Email gateway', vi: 'Cổng SMS / Email' },
      desc: { en: 'Customer notifications', vi: 'Thông báo khách hàng' },
    },
    {
      id: 'other',
      group: 'ops',
      label: { en: 'Other (specify in notes)', vi: 'Khác (ghi rõ trong ghi chú)' },
      desc: { en: '', vi: '' },
    },
  ],

  appGroups: {
    customer: { en: 'Customer channels', vi: 'Kênh khách hàng' },
    channel: { en: 'Sales channels', vi: 'Kênh bán hàng' },
    core: { en: 'Core systems', vi: 'Hệ thống lõi' },
    ops: { en: 'Operations & support', vi: 'Vận hành & hỗ trợ' },
  },

  priorityCategories: [
    { id: 'regulatory', label: { en: 'Regulatory / Audit', vi: 'Pháp lý / Kiểm toán' } },
    { id: 'revenue', label: { en: 'Revenue / Growth', vi: 'Doanh thu / Tăng trưởng' } },
    { id: 'cx', label: { en: 'Customer experience', vi: 'Trải nghiệm khách hàng' } },
    { id: 'efficiency', label: { en: 'Operational efficiency', vi: 'Hiệu quả vận hành' } },
    { id: 'risk', label: { en: 'Risk reduction', vi: 'Giảm rủi ro' } },
  ],

  dataTypes: [
    { id: 'pii', label: { en: 'Customer PII (CCCD, phone, address)', vi: 'PII khách hàng (CCCD, SĐT, địa chỉ)' } },
    { id: 'financial', label: { en: 'Loan / account financial data', vi: 'Dữ liệu tài chính khoản vay' } },
    { id: 'cic', label: { en: 'CIC / credit bureau', vi: 'CIC / bureau tín dụng' } },
    { id: 'payment', label: { en: 'Payment / card data', vi: 'Thanh toán / dữ liệu thẻ' } },
    { id: 'employee', label: { en: 'Employee data', vi: 'Dữ liệu nhân viên' } },
  ],

  complianceQuestions: [
    {
      id: 'q1',
      label: {
        en: 'Changes loan origination, approval, or disbursement?',
        vi: 'Thay đổi cấp tín dụng / duyệt / giải ngân?',
      },
      routes: ['credit_policy', 'risk'],
    },
    {
      id: 'q2',
      label: {
        en: 'Changes interest, fees, or contract terms?',
        vi: 'Thay đổi lãi suất, phí, hoặc hợp đồng?',
      },
      routes: ['legal', 'finance'],
    },
    {
      id: 'q3',
      label: { en: 'Sends customer notifications (SMS/email/push)?', vi: 'Gửi thông báo cho khách hàng?' },
      routes: ['legal'],
    },
    {
      id: 'q4',
      label: { en: 'Third-party or partner data exchange?', vi: 'Trao đổi dữ liệu bên thứ ba / đối tác?' },
      routes: ['vendor_risk', 'legal'],
    },
    {
      id: 'q5',
      label: { en: 'Affects collections or legal recovery?', vi: 'Ảnh hưởng thu hồi nợ / pháp lý?' },
      routes: ['collections_compliance', 'risk'],
    },
    {
      id: 'q6',
      label: { en: 'Requires audit trail for regulator / internal audit?', vi: 'Cần audit trail cho NHNN / kiểm toán?' },
      routes: ['risk'],
    },
    {
      id: 'q7',
      label: { en: 'Exposes customer data on POS or field devices?', vi: 'Hiển thị dữ liệu KH trên POS / thiết bị hiện trường?' },
      routes: ['it_security'],
    },
  ],

  routeLabels: {
    it_governance: { en: 'IT-Governance (CAB / standards)', vi: 'IT-Governance (CAB / tiêu chuẩn)' },
    it_security: { en: 'IT-Security', vi: 'IT-Security' },
    credit_policy: { en: 'Credit Policy', vi: 'Chính sách tín dụng' },
    risk: { en: 'Risk / GRC', vi: 'Rủi ro / GRC' },
    legal: { en: 'Legal', vi: 'Pháp chế' },
    finance: { en: 'Finance', vi: 'Tài chính' },
    vendor_risk: { en: 'Vendor Risk', vi: 'Rủi ro đối tác' },
    collections_compliance: { en: 'Collections Compliance', vi: 'Tuân thủ thu hồi nợ' },
    security: { en: 'IT-Security (legacy)', vi: 'IT-Security' },
  },

  routeCategories: {
    it_governance: { en: 'IT-Governance', vi: 'IT-Governance', color: '#1a2b4a' },
    it_security: { en: 'IT-Security', vi: 'IT-Security', color: '#c00000' },
    compliance: { en: 'GRC / Legal', vi: 'GRC / Pháp chế', color: '#2e75b6' },
  },

  /** Maps route id → sidebar category */
  routeCategoryMap: {
    it_governance: 'it_governance',
    it_security: 'it_security',
    security: 'it_security',
    credit_policy: 'compliance',
    risk: 'compliance',
    legal: 'compliance',
    finance: 'compliance',
    vendor_risk: 'compliance',
    collections_compliance: 'compliance',
  },

  requestTypes: [
    {
      id: 'business_change',
      label: { en: 'Business rule / process change', vi: 'Thay đổi quy tắc / quy trình nghiệp vụ' },
      bucket: 'business',
      needsBrd: true,
    },
    {
      id: 'new_capability',
      label: { en: 'New system capability / feature', vi: 'Tính năng / năng lực hệ thống mới' },
      bucket: 'business',
      needsBrd: true,
    },
    {
      id: 'data_import',
      label: { en: 'Bulk data import / mass update', vi: 'Import dữ liệu / cập nhật hàng loạt' },
      bucket: 'business',
      needsBrd: true,
      hint: {
        en: 'Business prepares and approves the file. IT executes after BRD + maker-checker.',
        vi: 'Nghiệp vụ chuẩn bị và duyệt file. IT thực hiện sau BRD + maker-checker.',
      },
    },
    {
      id: 'report_definition',
      label: { en: 'Report / KPI definition', vi: 'Định nghĩa báo cáo / KPI' },
      bucket: 'business',
      needsBrd: true,
    },
    {
      id: 'access_incident',
      label: { en: 'Access / password / incident', vi: 'Truy cập / mật khẩu / sự cố' },
      bucket: 'it',
      needsBrd: false,
      hint: {
        en: 'Use Service Desk — not this BRD form. No business rule definition needed.',
        vi: 'Dùng Service Desk — không dùng form BRD này.',
      },
    },
  ],

  deliveryPhases: [
    { id: 'intake', label: { en: 'Receive req', vi: 'Tiếp nhận' }, owner: { en: 'ITSM', vi: 'ITSM' } },
    { id: 'brd', label: { en: 'BRD gate', vi: 'Cổng BRD' }, owner: { en: 'Business + BA', vi: 'Nghiệp vụ + BA' } },
    { id: 'triage', label: { en: 'IT triage', vi: 'IT triage' }, owner: { en: 'IT Product', vi: 'IT Product' } },
    { id: 'fsd', label: { en: 'FSD / FRD', vi: 'FSD / FRD' }, owner: { en: 'BA + IT', vi: 'BA + IT' } },
    { id: 'sprint', label: { en: 'Sprint build', vi: 'Sprint' }, owner: { en: 'Dev (Scrum)', vi: 'Dev (Scrum)' } },
    { id: 'sit', label: { en: 'SIT test', vi: 'SIT' }, owner: { en: 'QA', vi: 'QA' } },
    { id: 'uat', label: { en: 'UAT', vi: 'UAT' }, owner: { en: 'Business', vi: 'Nghiệp vụ' } },
    { id: 'ship', label: { en: 'Ship (CAB)', vi: 'Ship (CAB)' }, owner: { en: 'IT Ops + IT-Gov', vi: 'IT Ops + IT-Gov' } },
    { id: 'ops', label: { en: 'Ops support', vi: 'Vận hành' }, owner: { en: 'IT Ops', vi: 'IT Ops' } },
  ],

  hardGates: [
    {
      en: 'No FSD / sprint work without accepted BRD (≥ 80%)',
      vi: 'Không FSD / sprint nếu BRD chưa đạt ≥ 80%',
    },
    {
      en: 'No production deploy without UAT sign-off + CAB (IT-Governance)',
      vi: 'Không deploy prod nếu chưa UAT + CAB (IT-Governance)',
    },
    {
      en: 'IT-Security review required for Restricted data or access exceptions',
      vi: 'IT-Security bắt buộc với dữ liệu Hạn chế hoặc ngoại lệ truy cập',
    },
  ],

  technicalKeywords: ['api', 'kafka', 'rabbitmq', 'microservice', 'aws lambda', 'database', 'redis', 'docker', 'kubernetes'],
};
