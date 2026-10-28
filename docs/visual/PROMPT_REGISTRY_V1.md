# KidLearn – Prompt Registry V1.0

**Mục tiêu:** tái tạo đúng nhận diện từ source master. Prompt dưới đây là **mô tả chuẩn hóa**, không phải bản transcript hoàn chỉnh của mọi câu lệnh sinh ảnh trước đây. Không cam kết tái tạo 100% hình giống nhau chỉ từ prompt.

## ROBOT_MASCOT
Robot chibi xanh điện/cyan, giáp đầu và thân nhiều mảng, mắt xanh to, huy hiệu sách trên trán, bút/thước hai bên mũ. Nét viền xanh than, bóng mềm vừa phải: **phương án B đã khóa**, không sáng bóng như A, không làm phẳng như C. Tư thế: đứng chính diện, chào, chỉ tay, cầm sách, cầm bút/nháy mắt, ăn mừng. Hình độc lập nền alpha thật, không khung/bong bóng chữ.

## BOY_HOME
Bé trai lớp 2 chibi sách thiếu nhi, tóc nâu hơi bồng, mắt đen tròn, má hồng, áo trắng tay xanh có hình gấu, quần ngắn xanh. Các tư thế: đứng, chào, ngồi viết ở bàn, đọc sách, chỉ dẫn, ăn mừng. Giữ một khuôn mặt/tóc xuyên suốt.

## BOY_SCHOOL
Cùng nhân vật BOY_HOME; đồng phục áo trắng cổ viền xanh, quần xanh navy, tất trắng, giày xanh, ba lô xanh-vàng. Các tư thế: đứng đeo ba lô, giơ tay, ôm sách, ngồi học viết, cầm que chỉ, bước đi đến trường.

## GIRL_HOME
Bé gái lớp 2 chibi sách thiếu nhi, tóc nâu có mái và nơ hồng hai bên, mắt đen tròn, má hồng. Ở nhà: áo trắng tay hồng họa tiết thỏ, quần hồng hoa nhỏ, dép thỏ. Các tư thế: đứng, chào, ngồi viết, đọc, chỉ dẫn, ăn mừng.

## GIRL_SCHOOL
Cùng nhân vật GIRL_HOME; đồng phục áo trắng viền xanh, váy xanh, giày hồng, tất trắng, ba lô hồng, giữ tóc và nơ. Các tư thế: đeo cặp đứng, giơ tay, ôm sách, ngồi học, cầm que chỉ, bước đi.

## Constraints dùng chung
Nhân vật độc lập full body trên true-alpha; cạnh sạch, không halo trắng, không chữ hay phép tính, không nền hay shadow plate; tỉ lệ đầu lớn/chibi, nét sách thiếu nhi có tô khối mềm, cùng ánh sáng; đối chiếu trực quan với sheet được chủ dự án duyệt; kiểm tra số ngón tay và đạo cụ.

## Từ mẫu đến bản phát hành
Mỗi asset cần: character_id, source_sheet, prompt_id, creation timestamp/model nếu biết, phiên bản, SHA-256, QA, Drive file ID, GitHub commit ref. Mọi chi tiết không xác định nên ghi UNKNOWN, không tự suy diễn.
