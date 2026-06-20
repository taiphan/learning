# Finance BRD Cheat Sheet / Phiếu hướng dẫn nhanh BRD

---

## Tiếng Việt (cho NV POS / hiện trường)

### 8 bước viết BRD tốt
1. **Bắt đầu bằng vấn đề** — không bắt đầu bằng "cần hệ thống X"
2. **Có số liệu** — %, giờ, số khách hàng, doanh thu ảnh hưởng
3. **Ghi rõ ai dùng** — vai trò, số người, địa điểm (POS/chi nhánh/HQ)
4. **Quy tắc nghiệp vụ** — ai duyệt, giờ cắt, ngoại lệ
5. **Trong phạm vi + ngoài phạm vi** — tránh mở rộng dự án
6. **Dữ liệu & tuân thủ** — PII, CIC, SMS, đối tác
7. **Tiêu chí nghiệm thu** — Cho trước / Khi / Thì (tối thiểu 5)
8. **Xin Sponsor ký** — Giám đốc+ trước khi gửi IT

### Công thức mô tả vấn đề
> **[Vai trò] không thể [làm gì] vì [rào cản], gây [ảnh hưởng].**

**Ví dụ:** Nhân viên POS không thể xác nhận khoản vay đã duyệt trong lúc khách đang có mặt, gây mất 18% hồ sơ đã pre-approve.

### Trước khi gửi — tự kiểm tra
- ☐ IT có thể hiểu mà không phải đoán quy tắc?
- ☐ UAT có thể kiểm tra được thành công?
- ☐ Risk/Audit hiểu tác động kiểm soát?
- ☐ Đã có Sponsor ký?

### Không ghi trong BRD
- Tên API, Kafka, database
- "Làm gấp" không có lý do
- Yêu cầu tắt bảo mật (MFA, DLP)
- Dùng máy cá nhân / Gmail / Dropbox cho dữ liệu KH

---

## English (for HQ / Digital / Collections)

### 8 steps to a good BRD
1. Start with the **problem**, not the system
2. **Quantify** impact (%, hours, customers, VND)
3. Define **who** uses it (role, count, location)
4. Document **business rules** (approval, cut-off, exceptions)
5. Write **in-scope AND out-of-scope**
6. Complete **data & compliance** honestly
7. Add **acceptance criteria** (Given/When/Then, min 5)
8. Get **Sponsor sign-off** before IT intake

### Problem statement formula
> **[Role] cannot [task] because [constraint], causing [impact].**

### Before submit — self-check
- ☐ Can IT build without guessing rules?
- ☐ Can UAT verify success objectively?
- ☐ Can Risk/Audit assess control impact?
- ☐ Sponsor signed?

### Do not put in BRD
- API names, middleware, vendor technical design
- "ASAP" without business driver
- Requests to disable security controls
- BYOD / personal cloud for customer data

---

## Quick reference — Finance compliance triggers

| If your BRD includes… | Route to |
|------------------------|----------|
| Loan approval / disbursement change | Risk + Credit Policy |
| Interest / fees / contract change | Legal + Finance |
| Customer SMS / email | Legal (template) |
| Third-party data sharing | Vendor Risk + Legal |
| Collections / legal process | Compliance |
| Data on POS / home device | Security |

---

*Print double-sided: Vietnamese on front, English on back | v1.0*
