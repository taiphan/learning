# FE CREDIT — TÀI LIỆU YÊU CẦU NGHIỆP VỤ (BRD) / BUSINESS REQUIREMENTS DOCUMENT

**Mã tài liệu / Document ID:** BRD-YYYY-NNNN  
**Phiên bản / Version:** 1.0  
**Trạng thái / Status:** Nháp / Draft | Đang xem xét / Under Review | Đã phê duyệt / Approved  
**Phân loại / Classification:** Nội bộ / Internal

---

## Hướng dẫn / Instructions

| Tiếng Việt | English |
|------------|---------|
| Điền đầy đủ các mục **bắt buộc** trước khi gửi. | Complete all **mandatory** sections before submission. |
| Mô tả **cần gì** và **tại sao** — không mô tả cách IT xây dựng. | Describe **what** is needed and **why** — not how IT builds it. |
| Dùng ngôn ngữ rõ ràng, có thể kiểm thử được. | Use clear, testable language. |
| Xin **Người bảo trợ nghiệp vụ** ký duyệt trước khi gửi IT/BA. | Obtain **Business Sponsor** sign-off before IT/BA intake. |

---

## A. THÔNG TIN YÊU CẦU / REQUEST INFORMATION *(Bắt buộc / Mandatory)*

| Trường / Field | Giá trị / Value |
|----------------|-----------------|
| **Tên BRD / BRD Title** | |
| **Đơn vị nghiệp vụ / Business Unit** | ☐ Sales / POS ☐ Digital ☐ Thu hồi nợ / Collections ☐ Rủi ro / Risk ☐ Thẻ / Cards ☐ Vận hành / Ops ☐ Khác / Other |
| **Người yêu cầu / Requester** | |
| **Email** | |
| **Người bảo trợ (Giám đốc+) / Business Sponsor** | |
| **Ngày gửi / Date Submitted** | |
| **Ngày go-live mục tiêu / Target Go-Live** | |
| **Mức ưu tiên / Priority** | ☐ Pháp lý / Regulatory ☐ Doanh thu / Revenue ☐ Trải nghiệm KH / CX ☐ Hiệu quả / Efficiency ☐ Giảm rủi ro / Risk |

---

## B. TÓM TẮT ĐIỀU HÀNH / EXECUTIVE SUMMARY *(Bắt buộc / Mandatory)*

### Vấn đề nghiệp vụ / Business problem

**VI:**  
> _Ví dụ: "Nhân viên POS không thể xác nhận kế hoạch trả góp đã duyệt trong lúc khách hàng đang có mặt tại cửa hàng."_

**EN:**  
> _Example: "POS staff cannot confirm the approved installment plan while the customer is at the store."_

### Đối tượng bị ảnh hưởng / Who is impacted

**VI:**  
**EN:**

### Hậu quả nếu không làm / Impact if not addressed

**VI:** _(Số liệu: %, giờ, số KH, rủi ro tuân thủ)_  
**EN:** _(Quantify: %, hours, customers, compliance risk)_

### Kết quả mong muốn / Desired outcome (1 câu / one sentence)

**VI:**  
**EN:**

---

## C. MỤC TIÊU & CHỈ SỐ THÀNH CÔNG / OBJECTIVES & SUCCESS METRICS *(Bắt buộc)*

| # | Mục tiêu / Objective | Hiện tại / Baseline | Mục tiêu / Target | Cách đo / How measured | Người đo / Owner |
|---|----------------------|---------------------|-------------------|------------------------|------------------|
| 1 | | | | | |
| 2 | | | | | |

**Ví dụ / Examples:**
- Giảm tỷ lệ bỏ dở hồ sơ online từ 42% xuống 30% / Reduce digital drop-off from 42% to 30%
- Giảm thời gian giải ngân POS từ 24h xuống 4h / Reduce POS disbursement TAT from 24h to 4h

---

## D. HIỆN TRẠNG / CURRENT STATE *(Bắt buộc)*

### D.1 Quy trình hiện tại / Current process

| Bước / Step | Vai trò / Actor | Hoạt động / Activity | Hệ thống / System | Điểm đau / Pain point |
|-------------|-----------------|----------------------|---------------------|----------------------|
| 1 | | | | |
| 2 | | | | |

### D.2 Khối lượng / Volume

| Chỉ số / Metric | Giá trị / Value |
|-----------------|-----------------|
| Số người dùng / # users | |
| Số giao dịch hoặc hồ sơ/ngày / Transactions or cases per day | |
| Phạm vi / Scope | ☐ Toàn quốc / National ☐ Thí điểm / Pilot: ___ |

---

## E. TRẠNG THÁI MỤC TIÊU / TO-BE STATE *(Bắt buộc)*

> **VI:** Mô tả quy trình tương lai theo góc nhìn nghiệp vụ. Không ghi API, database, tên phần mềm kỹ thuật.  
> **EN:** Describe the future process from a business view. No API, database, or technical product names.

**VI:**  
**EN:**

---

## F. PHẠM VI / SCOPE *(Bắt buộc)*

### Trong phạm vi / In scope
- 
- 

### Ngoài phạm vi / Out of scope
- 
- 

### Giả định / Assumptions
- 

### Phụ thuộc / Dependencies
| Phụ thuộc / Dependency | Chủ sở hữu / Owner | Ảnh hưởng nếu trễ / Impact if delayed |
|------------------------|---------------------|--------------------------------------|
| | | |

---

## G. NGƯỜI DÙNG & BÊN LIÊN QUAN / USERS & STAKEHOLDERS *(Bắt buộc)*

| Vai trò / Role | Phòng ban / Dept | Số user / # users | Địa điểm / Location | Quyền / Access |
|----------------|------------------|-------------------|---------------------|----------------|
| | | | HQ / Chi nhánh / Branch / POS / Tại nhà / Remote | Xem / Tạo / Duyệt (View / Create / Approve) |

**Ảnh hưởng khách hàng / Customer impact:** ☐ Có / Yes ☐ Không / No  
**Ảnh hưởng đối tác / Partner impact:** ☐ Có / Yes ☐ Không / No

---

## H. QUY TẮC NGHIỆP VỤ / BUSINESS RULES *(Bắt buộc cho cho vay, thu hồi nợ, thẻ)*

> **VI:** IT và Rủi ro không được đoán quy tắc. Ghi rõ hoặc đính kèm quy định đã duyệt.  
> **EN:** IT and Risk must not guess rules. Document clearly or attach approved policy.

### H.1 Quy tắc đủ điều kiện / Eligibility rules

| Mã / ID | Quy tắc / Rule | Nguồn / Source |
|---------|----------------|----------------|
| BR-01 | | |
| BR-02 | | |

### H.2 Thẩm quyền phê duyệt / Approval authority

| Điều kiện / Condition | Người duyệt / Approver | Escalation |
|-----------------------|------------------------|------------|
| | | |

### H.3 Giờ cắt / Cut-off times

| Sự kiện / Event | Giờ cắt / Cut-off | Ngày nghỉ / Non-working day |
|-----------------|-------------------|----------------------------|
| | | |

### H.4 Liên lạc khách hàng / Customer communication

| Kích hoạt / Trigger | Kênh / Channel | Nội dung do / Content owner | Opt-out? |
|---------------------|----------------|----------------------------|----------|
| | SMS / Email / App | Legal / Marketing | ☐ Có / Yes ☐ Không / No |

---

## I. DỮ LIỆU & BẢO MẬT / DATA & SECURITY *(Bắt buộc)*

### Loại dữ liệu / Data types

☐ PII khách hàng / Customer PII (CCCD, SĐT, địa chỉ)  
☐ Dữ liệu tài chính / Financial data  
☐ CIC / Credit bureau  
☐ Thanh toán / thẻ / Payment / card  
☐ Nhân viên / Employee data

### Phân loại / Classification

☐ Công khai / Public ☐ Nội bộ / Internal ☐ Mật / Confidential ☐ Hạn chế / Restricted

### Truy cập từ xa / Remote access

☐ Không truy cập từ xa / No remote access  
☐ Chỉ thiết bị quản lý / Managed device only  
☐ Bắt buộc VDI / VDI required  
☐ Tải file về máy cá nhân — **cần phê duyệt Security / requires Security exception**

### Đồng ý khách hàng / Customer consent

☐ Cần đồng ý / Consent required  
☐ Cần Legal rà soát / Legal review required

---

## J. BÁO CÁO & KIỂM SOÁT / REPORTING & CONTROLS *(Bắt buộc)*

| Báo cáo / Report | Đối tượng / Audience | Tần suất / Frequency |
|------------------|----------------------|---------------------|
| | | |

| Kiểm soát / Control | Người tạo / Maker | Người duyệt / Checker |
|---------------------|-------------------|----------------------|
| | | |

---

## K. TRIỂN KHAI / IMPLEMENTATION *(Bắt buộc)*

☐ Thí điểm / Pilot: ___  
☐ Theo giai đoạn / Phased  
☐ Toàn quốc một lần / Big bang

### Đào tạo / Training

| Đối tượng / Audience | Loại / Type | Chủ trì / Owner |
|----------------------|-------------|-----------------|
| NV POS / POS staff | | |
| Tổng đài / Call center | | |

**Ngôn ngữ / Language:** ☐ Tiếng Việt ☐ English ☐ Song ngữ / Bilingual

---

## L. RỦI RO / RISKS *(Bắt buộc)*

| Loại / Type | Mô tả / Description | Khả năng / Likelihood | Tác động / Impact |
|-------------|---------------------|----------------------|-------------------|
| Vận hành / Operational | | L/M/H | L/M/H |
| Khách hàng / Customer | | | |
| Tuân thủ / Compliance | | | |

---

## M. TIÊU CHÍ NGHIỆM THU / ACCEPTANCE CRITERIA *(Bắt buộc — tối thiểu 5)*

| AC ID | Tiêu chí / Criterion |
|-------|----------------------|
| AC-01 | **Cho trước / Given** ___, **khi / when** ___, **thì / then** ___. |
| AC-02 | |
| AC-03 | |
| AC-04 | |
| AC-05 | |

---

## N. SÀNG LỌC TUÂN THỦ / COMPLIANCE SCREENING *(Bắt buộc)*

| # | Câu hỏi / Question | Có / Yes | Không / No |
|---|-------------------|----------|------------|
| 1 | Thay đổi cấp tín dụng / giải ngân? / Changes origination or disbursement? | ☐ | ☐ |
| 2 | Thay đổi lãi suất / phí / hợp đồng? / Changes interest, fees, or contract? | ☐ | ☐ |
| 3 | Gửi thông báo cho khách hàng? / Sends customer notifications? | ☐ | ☐ |
| 4 | Trao đổi dữ liệu bên thứ ba? / Third-party data exchange? | ☐ | ☐ |
| 5 | Ảnh hưởng thu hồi nợ / pháp lý? / Affects collections or legal recovery? | ☐ | ☐ |

**Nếu có "Có / Yes":** Chuyển Rủi ro / Tuân thủ trước khi triển khai. / Route to Risk / Compliance before build.

---

## O. PHÊ DUYỆT / APPROVALS *(Bắt buộc)*

| Vai trò / Role | Họ tên / Name | Ký / Signature | Ngày / Date |
|----------------|---------------|----------------|-------------|
| Người yêu cầu / Requester | | | |
| Người bảo trợ / Sponsor (Giám đốc+) | | | |
| Trưởng đơn vị / BU Head | | | |
| Rủi ro / Tuân thủ / Risk / Compliance (nếu cần) | | | |

---

## PHỤ LỤC / APPENDIX

- Sơ đồ quy trình / Process diagrams  
- Mẫu báo cáo / màn hình nghiệp vụ / Sample reports or business wireframes  
- Quy định tham chiếu / Reference policies  

---

*Mẫu song ngữ v1.0 / Bilingual template v1.0 | FE Credit BRD Training Package*
