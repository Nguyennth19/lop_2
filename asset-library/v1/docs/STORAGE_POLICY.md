# KidLearn – Khóa nguyên tắc lưu trữ đồng bộ kép (V1.0)

**Người dùng đã yêu cầu GitHub + Google Drive là hai hệ thống lưu trữ quản lý chính.** Không xem tệp đính kèm trong chat hay sandbox là bản lưu chính.

## Tách vai trò nhưng cùng manifest
- **Google Drive:** nguồn gốc ảnh raster PNG/WebP, tờ tổng hợp, tài liệu duyệt. File Drive phải lưu mã asset ở tên tệp.
- **GitHub:** manifest, style-lock, prompt, script xác minh, README, lịch sử và trạng thái duyệt. Khi khả thi lưu luôn PNG/WebP bản tối ưu hoặc sử dụng Git LFS/GitHub Releases, nhưng không tuyên bố binary ở hai nơi khi chưa xác thực.

## Giao thức giao dịch (2-phase)
1. Sinh file staging, tính SHA-256 PNG/WebP và so với manifest local.
2. Đưa PNG/WebP và sheet lên Drive trong thư mục version cố định, đọc lại ID/link.
3. Ghi GitHub manifest với Drive IDs, checksum, trạng thái staging và ảnh nguồn; bổ sung prompt, quy tắc, bảng QA.
4. Nếu binary cũng lên GitHub, kiểm tra SHA tương ứng; nếu chưa tải binary lên GitHub thì ghi rõ `github_binary_status=NOT_MIRRORED` và coi GitHub là catalog/metadata mirror.
5. Cuối cùng mới đặt `sync_status=VERIFIED` khi hai nơi được kiểm tra và chính sách lưu file đã định nghĩa được đáp ứng.
6. Không xóa file Drive cũ khi cập nhật; đưa asset mới vào v1.1/v2; commit/tag release riêng.

## Đặt tên và version
`KL2_<CHARACTER>_<VARIANT>_<NN>_<POSE>_v1.png|webp`. Ví dụ: `KL2_BOY_HOME_03_WRITE_v1.png`.
Một asset_id không được trỏ tới hai file có checksum khác nhau trong cùng version.

## Bảo mật và quyền sử dụng
- Không lưu tokens, credentials, dữ liệu trẻ em ở GitHub hay file public.
- Chỉ công bố ảnh được chủ dự án duyệt; nhóm hiện tại `SET_APPROVED_AWAITING_ASSET_QA`.
- Drive URLs không đảm bảo dùng làm CDN; frontend dùng bản phát hành ổn định sau khi QA.
- Mọi thay đổi prompt/style cần PR và lịch sử; API credentials Apps Script qua GitHub Secrets.
