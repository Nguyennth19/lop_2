# KidLearn – Chính sách lưu trữ kép V1.0 (LOCKED)

Ngày thiết lập: 2026-10-27. Áp dụng cho tất cả tài sản hình mới.

## Nguồn sự thật và vai trò
- **Google Drive:** giữ sheet gốc, PNG master, WebP đã duyệt, chứng từ QA, và các bản phát hành nguyên vẹn.
- **GitHub:** code, README, phiên bản, manifest ID/hash/Drive URL, prompt, lịch sử commit, quy tắc QA, chương trình đồng bộ; file nhị phân được phép đặt trong repo nếu kích thước và giấy phép phù hợp.
- **Backup:** ZIP theo phiên bản với SHA-256; không dựa vào lịch sử hội thoại.

## Quy trình mỗi lần bổ sung/sửa ảnh
1. Tạo asset độc lập, alpha thật, file gốc và mã tài sản duy nhất.
2. Gắn trạng thái REVIEW_REQUIRED đến khi duyệt ranh giới, nét, khuôn mặt, phụ kiện, nguồn quyền sử dụng, hiển thị điện thoại/A4.
3. Upload lên Drive; đọc lại ID, URL và checksum thực tế.
4. Commit manifest với cùng ID, phiên bản, SHA-256, Drive ID, prompt liên quan lên GitHub bằng Pull Request.
5. Chỉ ghi SYNCED_VERIFIED sau khi đọc xác minh cả hai nơi; đối chiếu hash và số lượng.
6. Khi thay hình, không ghi đè phiên bản đã phát hành: tăng phiên bản, cập nhật manifest rồi duyệt lại.

## Quy tắc tên
KL_<ACTOR>_<SET>_<2-DIGIT-INDEX>_<POSE>_vMAJOR.MINOR.PATCH.png
Ví dụ: KL_ROBOT_MASCOT_02_wave_step_v1.0.0.png.

## Trạng thái
REVIEW_REQUIRED → APPROVED_LOCAL → DRIVE_STORED → GITHUB_INDEXED → SYNCED_VERIFIED.
Nếu một nhánh lỗi, không được tự tuyên bố đồng bộ hoàn tất.

## Bảo mật / triển khai
Không commit token, service account key, clasp credentials, điểm số hay thông tin riêng của trẻ. Không lấy Google Drive share URL làm CDN phục vụ giao diện. Apps Script kết nối GitHub ở giai đoạn cấu hình riêng, cần kiểm tra quyền và bảo vệ secret.

## Phát hành v1.0.0 này
Bản ZIP gốc có SHA-256: `80917390a3979b32175e9ced4024669ac1be345e655d96fc41707373ebad1a99`.
**Đã xác nhận Drive lưu 30 PNG + 30 WebP và ZIP gốc; tải ngược 60/60 ảnh và ZIP khớp byte/SHA-256 với bản phát hành tại chỗ. GitHub lưu chỉ mục 30 asset IDs / 60 Drive file IDs, không lưu nhị phân.** Không ghi status SYNCED_VERIFIED cho đến khi xác minh.

## Xác minh ngày 27/10/2026
Báo cáo [DUAL_STORAGE_VERIFICATION_V1.md](DUAL_STORAGE_VERIFICATION_V1.md). Drive cũng lưu [bản báo cáo](https://drive.google.com/file/d/1POewCpboLyw1USHrhKH8taP7ZL1J_-G4/view). `SYNCED_VERIFIED` nghĩa là bản lưu trữ và metadata đã xác minh; không phải duyệt chất lượng ảnh. `REVIEW_REQUIRED` giữ nguyên đối với hình đã tách.
