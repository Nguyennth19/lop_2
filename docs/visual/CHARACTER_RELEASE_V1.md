# Character Release V1.0.0 — Kiểm kê và QA

Đã sinh bản release cục bộ từ 5 character sheet được người dùng chốt: **Robot phong cách B, Bé nam ở nhà, Bé nam ở trường, Bé nữ ở nhà, Bé nữ ở trường**.

| Set | PNG | WebP | Duyệt sử dụng |
|---|---:|---:|---|
| ROBOT_MASCOT | 6 | 6 | REVIEW_REQUIRED |
| BOY_HOME | 6 | 6 | REVIEW_REQUIRED |
| BOY_SCHOOL | 6 | 6 | REVIEW_REQUIRED |
| GIRL_HOME | 6 | 6 | REVIEW_REQUIRED |
| GIRL_SCHOOL | 6 | 6 | REVIEW_REQUIRED |

Các pose gồm đứng, chào, viết, đọc, chỉ dẫn, ăn mừng hoặc biến thể đi học theo từng set. Tên file có cấu trúc KL_<ACTOR>_<SET>_<INDEX>_<POSE>_v1.0.0.(png|webp).

### Chất lượng
- Đã có alpha RGBA, cắt từ từng ô 3x2; file WebP alpha phục vụ app.
- Phải duyệt tay: cắt tay/tóc, dính vật thể ở biên, các phụ kiện và độ đồng nhất khuôn mặt. Chưa thể coi là sạch và sẵn sàng production.
- Tài liệu đầy đủ: `ASSET_MANIFEST.csv`, `ASSET_MANIFEST.json`, `QA_CONTACT_SHEET.png`, prompt từng nhóm và source sheet; thuộc bộ ZIP v1.0.0.
- Bản ZIP sha256 `80917390a3979b32175e9ced4024669ac1be345e655d96fc41707373ebad1a99`.

### Tài liệu nguồn
- [Style Lock](STYLE_LOCK_V1.md)
- [Storage Policy](ASSET_STORAGE_POLICY_V1.md)
- [Schema](../../assets/manifest.schema.json)

### Chưa hoàn thành
- Upload file nhị phân chính thức Drive + GitHub, read-back hai kho.
- Chốt QA từng nhân vật. Một phần crop có thể cần sửa tay.
- Kết nối GitHub ↔ Google Apps Script.


## Tình trạng xác minh bổ sung 27/10/2026
- 30 PNG + 30 WebP đã tải lên Drive và tải ngược, toàn bộ khớp byte với bản ZIP gốc. GitHub đã lưu đủ 30 mã, 60 file ID và SHA-256 PNG.
- Lưu trữ `SYNCED_VERIFIED` nhưng hình cắt vẫn `REVIEW_REQUIRED`. Xem [báo cáo chi tiết](DUAL_STORAGE_VERIFICATION_V1.md).
