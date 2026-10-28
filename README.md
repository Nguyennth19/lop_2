# KidLearn – Lớp 2

Hệ thống học tập hai môn **Toán** và **Tiếng Việt** lớp 2, dự kiến triển khai với GitHub, Google Apps Script và Google Drive.

## Quyết định đã khóa (27/10/2026)
- **Robot:** phong cách B – Chibi Hero Soft Shading; giữ giáp xanh, huy hiệu sách, mắt lớn, nổi bật vừa đủ.
- **Bé nam:** chibi sách học tập – tóc nâu ngắn, má hồng, mắt to, trang phục xanh/trắng.
- **Bé nữ:** chibi sách học tập – tóc nâu, nơ hồng, má hồng, mắt to, phối hồng/trắng/xanh.
- Nhân vật có hai biến thể **Ở nhà** và **Ở trường** (đồng phục); bộ tạo hình đã được lựa chọn về hướng phong cách, từng pose độc lập vẫn cần QA.
- Nội dung **LV1 = SGK; LV2 = VBT; LV3 = tài liệu tham khảo**; SGV chỉ dùng cho định hướng sư phạm; chia theo đầu bài và skill.

## Giai đoạn 1B – Character Asset Library
- Đã dựng 5 sheet, trích **30 PNG + 30 WebP**.
- Các hình có alpha thực, **chưa hoàn tất QA ranh giới**. Một số pose cần tách/chỉnh tay để loại vết cắt ở sát ô. Không dùng production trước khi duyệt.
- Bản ZIP hiện có: `KidLearn_Release_v1.zip`, **SHA-256 `80917390a3979b32175e9ced4024669ac1be345e655d96fc41707373ebad1a99`**. Bản ZIP và 60 hình PNG/WebP đã được lưu trên Google Drive. GitHub lưu chỉ mục và checksum, không lưu bản nhị phân.
- [Danh mục 30 pose](assets/RELEASE_INDEX_V1.csv) • [Phiên bản và QA](docs/visual/CHARACTER_RELEASE_V1.md) • [Prompt](docs/visual/PROMPT_REGISTRY_V1.md).

## Chính sách lưu trữ kép (bắt buộc)
1. Google Drive lưu gốc PNG/WebP/sheet. GitHub lưu code, manifest, prompt, checksum và lịch sử thay đổi.
2. Không gắn `SYNCED_VERIFIED` nếu chưa upload và kiểm tra lại **cả hai kho**.
3. Không ghi đè asset đã được duyệt; tạo phiên bản mới.
4. Không lưu token, khóa bí mật hoặc dữ liệu định danh học sinh trong repo.

Đọc: [ASSET_STORAGE_POLICY_V1.md](docs/visual/ASSET_STORAGE_POLICY_V1.md) và [định hướng Google Apps Script](docs/architecture/INTEGRATION.md).

**Tình trạng kết nối:** Mã và quy chuẩn đã có PR nháp; ZIP và 60/60 ảnh Drive đã được đọc lại và đối chiếu toàn vẹn. Chưa có tự động hóa Google Apps Script.

## Xác minh kho tài nguyên
[Báo cáo xác minh lưu trữ kép và QA](docs/visual/DUAL_STORAGE_VERIFICATION_V1.md): 60/60 ảnh khớp SHA-256/byte; lưu trữ `SYNCED_VERIFIED`, chất lượng nghệ thuật `REVIEW_REQUIRED`.
