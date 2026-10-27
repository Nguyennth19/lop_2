# KidLearn – Lớp 2

Dự án ứng dụng hỗ trợ học **Toán** và **Tiếng Việt** lớp 2, dự kiến tích hợp **GitHub + Google Apps Script + Google Drive**.

> **Trạng thái 27/10/2026:** Giai đoạn 1B – thiết kế Character Master, chưa tạo đủ 12 ảnh nền trong, chưa triển khai Apps Script.

## Quyết định phong cách (đã được chủ dự án duyệt)
- **Robot:** phong cách B – Chibi Hero Soft Shading; giữ giáp xanh, mắt to, huy hiệu sách, vừa đủ nổi bật để dẫn dắt.
- **Bé nam:** theo thẻ Toán mẫu đã duyệt, tóc nâu ngắn, mắt tròn và má hồng, xanh–trắng; phong cách chibi tranh sách.
- **Bé nữ:** theo thẻ Tiếng Việt mẫu đã duyệt, tóc nâu, nơ hồng, mắt tròn và má hồng, hồng–trắng–xanh.
- **Đồng phục:** ý tưởng tùy chọn chưa được duyệt; không tự động thay trang phục gốc.
- Nội dung: **LV1 = SGK**, **LV2 = VBT**, **LV3 = tài liệu tham khảo**; sách giáo viên chỉ tham khảo sư phạm. Phân bài theo đầu bài, gắn mã kỹ năng, không ép theo tuần.

## Hồ sơ Giai đoạn 1B
- [Quy chuẩn khóa phong cách](docs/visual/STYLE_LOCK_V1.md)
- [Kế hoạch Character Master 12 hình](docs/visual/CHARACTER_MASTER_PHASE_1B.md)
- [Danh mục và trạng thái từng tài sản](docs/visual/ASSET_MANIFEST.csv)
- [Định hướng GitHub ↔ Drive ↔ Apps Script](docs/architecture/INTEGRATION.md)

## Nguyên tắc
Hai thẻ bài học đã duyệt là **mẫu mỹ thuật/bố cục**, không phải dữ liệu bài học đã kiểm chứng và không được coi là các nhân vật PNG riêng lẻ có nền trong. Ảnh chỉ chuyển sang trạng thái APPROVED sau khi kiểm tra tính nhất quán, nền alpha, quyền sử dụng, khả năng đọc trên điện thoại và ứng dụng.

**Bảo mật:** Không commit secret, OAuth token, thông tin riêng tư học sinh hay dữ liệu điểm số.
