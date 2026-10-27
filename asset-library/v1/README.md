# KidLearn – Character Asset Library V1.0 (Release Candidate)

30 hình PNG + 30 WebP tách độc lập từ 5 sheet, mỗi nhóm 6 pose. Giai đoạn 1B.

- `assets/robot/{png,webp,source_sheets}`
- `assets/boy_home/{png,webp,source_sheets}`
- `assets/boy_school/{png,webp,source_sheets}`
- `assets/girl_home/{png,webp,source_sheets}`
- `assets/girl_school/{png,webp,source_sheets}`
- `manifest/assets.v1.json` / `.csv`: 30 dòng, tên chuẩn, SHA-256, kích thước, QA, links.
- `docs/prompts/`: 5 prompt nhóm; `docs/STYLE_LOCK_V1.md`; `docs/STORAGE_POLICY.md`.

**Kỹ thuật:** File PNG có alpha min/max 0/255, chia theo mask alpha connected component để không lẫn hình liền kề. WebP tối ưu hóa để dùng trên web. Hình tách vẫn cần kiểm tra viền, đối chiếu mặt và kích cỡ hiển thị trước khi production.

**Trạng thái:** Người dùng khóa các set và style; từng ảnh chưa được đánh dấu `APPROVED_PRODUCTION`.

**Quản trị:** Google Drive = tài nguyên ảnh gốc, GitHub = mã nguồn, tài liệu, prompt, checksum và tình trạng; binary mirror GitHub phải xác minh trước khi tuyên bố hoàn tất lưu kép.
