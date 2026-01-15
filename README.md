🎓 HỆ THỐNG QUẢN LÝ & XÁC THỰC VĂN BẰNG TRÊN BLOCKCHAIN (CRONOS)
Tác giả: [Trần Huỳnh Sang] Mô tả: Ứng dụng phi tập trung (DApp) giúp các trường đại học cấp bằng và doanh nghiệp tra cứu văn bằng minh bạch, chống giả mạo bằng công nghệ Blockchain.

🛠 1. Công Cụ & Công Nghệ Sử Dụng
Hệ thống được xây dựng theo mô hình 3 lớp (3-Tier Architecture):

Blockchain (Lớp dữ liệu):

Mạng lưới: Cronos Testnet (EVM Compatible).

Ngôn ngữ: Solidity (Viết Smart Contract).

Framework: Hardhat (Biên dịch & Triển khai hợp đồng).

Ví: MetaMask (Quản lý tài khoản & Phí Gas).

Backend (Lớp xử lý):

Ngôn ngữ: Python.

Thư viện chính: Flask (Tạo API Server), Web3.py (Kết nối Blockchain).

Frontend (Lớp giao diện):

Ngôn ngữ: HTML5, CSS3, Javascript (Vanilla).

Thư viện: SweetAlert2 (Thông báo đẹp), html2canvas & jspdf (Xuất file PDF).

🚀 2. Quy Trình Thực Hiện (Step-by-Step)
Chúng ta đã xây dựng dự án qua 3 giai đoạn chính:

Giai đoạn 1: Xây dựng "Trái Tim" (Smart Contract)
Mục tiêu: Tạo ra một "cuốn sổ cái" không thể tẩy xóa để lưu thông tin văn bằng.

Cách làm:

Viết file BangCap.sol bằng ngôn ngữ Solidity.

Định nghĩa cấu trúc Bang gồm: Tên SV, Mã SV, Loại bằng, Ngày cấp, Người cấp.

Sử dụng mapping để gán mỗi văn bằng với một mã Hash độc nhất.

Triển khai (Deploy) lên mạng Cronos Testnet bằng Hardhat.

Kết quả: Có được địa chỉ hợp đồng (Contract Address) để giao tiếp.

Giai đoạn 2: Xây dựng "Cầu Nối" (Python Backend)
Mục tiêu: Giúp máy tính giao tiếp được với Blockchain (vì trình duyệt web không làm trực tiếp việc này an toàn).

Cách làm:

Cấu hình môi trường (.env) chứa Private Key và Contract Address.

Dùng Web3.py để kết nối tới RPC của Cronos.

Tạo API /cap-bang: Nhận thông tin -> Ký giao dịch bằng Private Key -> Gửi lên Blockchain.

Tạo API /tra-cuu: Nhận mã Hash -> Đọc dữ liệu từ Blockchain -> Trả về JSON.

Giai đoạn 3: Xây dựng "Giao Diện" (Frontend Web)
Mục tiêu: Tạo trang web thân thiện cho người dùng (Admin và Sinh viên/Nhà tuyển dụng).

Cách làm:

Thiết kế giao diện 2 Tab: Tra Cứu và Admin.

Chức năng Tra Cứu: Nhập mã Hash -> Gọi API Python -> Hiển thị tấm bằng Visual đẹp mắt.

Chức năng Admin: Nhập thông tin -> Gọi API Python để cấp bằng mới -> Lưu lịch sử vào LocalStorage.

Tính năng nâng cao: Tích hợp xuất bằng ra file PDF chuẩn A4.

🌟 3. Các Tính Năng Nổi Bật
Chống giả mạo tuyệt đối: Dữ liệu nằm trên Blockchain, hacker không thể sửa điểm hay ngày cấp.

Minh bạch: Bất kỳ ai có mã Hash đều có thể kiểm tra nguồn gốc văn bằng.

Giao diện trực quan: Mô phỏng tấm bằng thực tế thay vì chỉ hiện dòng chữ khô khan.

Xuất PDF chuẩn: Hỗ trợ tải văn bằng về máy để in ấn với độ nét cao.

Thông báo thông minh: Hệ thống phản hồi tức thì (Loading, Thành công, Thất bại) giúp người dùng dễ thao tác.

📖 4. Hướng Dẫn Cài Đặt & Chạy
Để chạy dự án này trên máy local, làm theo các bước sau:

Bước 1: Khởi động Backend Mở Terminal tại thư mục Python-App và chạy lệnh:

Bash

python api.py
(Hoặc click đúp file START.bat nếu đã tạo). Server sẽ chạy tại: http://127.0.0.1:5000

Bước 2: Mở Giao diện

Vào thư mục Python-App.

Mở file index.html bằng trình duyệt Chrome/Edge.

Bước 3: Sử dụng

Cấp bằng: Vào tab Admin, điền thông tin -> Bấm Cấp bằng -> Copy mã Hash.

Kiểm tra: Vào tab Tra cứu, dán mã Hash -> Xem kết quả -> Tải PDF.

📝 5. Tổng Kết
Dự án đã chứng minh khả năng ứng dụng thực tế của Blockchain trong giáo dục. Từ những dòng code Solidity đầu tiên đến một giao diện web hoàn chỉnh, hệ thống đảm bảo tính: Toàn vẹn dữ liệu - Bảo mật - Dễ sử dụng.
