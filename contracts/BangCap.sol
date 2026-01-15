// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract BangCap {
    // 1. Định nghĩa cấu trúc của một tấm bằng
    struct ThongTinBang {
        string tenSinhVien;     // Tên sinh viên
        string maSinhVien;      // Mã số SV
        string loaiBang;        // Giỏi/Khá...
        uint256 ngayCap;        // Ngày cấp bằng (số giây)
        address nguoiCap;       // Ví của nhà trường đã cấp
        bool laHopLe;           // Còn giá trị sử dụng không?
    }

    // 2. Nơi lưu trữ dữ liệu (Giống như Database)
    // mapping giúp tra cứu nhanh: Đưa vào mã Hash -> Trả về Thông tin bằng
    mapping(bytes32 => ThongTinBang) public danhSachBang;
    
    // Lưu địa chỉ ví của Admin (người tạo ra hợp đồng này)
    address public admin;

    // Sự kiện (Để báo hiệu cho bên ngoài biết khi có hành động)
    event DaCapBang(bytes32 indexed maHash, string maSinhVien);

    constructor() {
        admin = msg.sender; // Ai deploy contract này thì là Admin
    }

    // 3. Hàm cấp bằng (Chỉ ghi dữ liệu vào Blockchain)
    function capBang(
        bytes32 _maHash, 
        string memory _ten, 
        string memory _maSV, 
        string memory _loai
    ) public {
        // Chỉ cho phép Admin cấp (trong thực tế có thể thêm logic cho phép các trường)
        require(msg.sender == admin, "Ban khong phai Admin!");

        // Kiểm tra xem bằng này đã tồn tại chưa
        require(danhSachBang[_maHash].ngayCap == 0, "Bang nay da ton tai!");

        // Lưu thông tin vào Blockchain
        danhSachBang[_maHash] = ThongTinBang({
            tenSinhVien: _ten,
            maSinhVien: _maSV,
            loaiBang: _loai,
            ngayCap: block.timestamp, // Lấy thời gian hiện tại của block
            nguoiCap: msg.sender,
            laHopLe: true
        });

        // Phát loa thông báo: "Tôi vừa cấp bằng xong nhé!"
        emit DaCapBang(_maHash, _maSV);
    }

    // 4. Hàm tra cứu (Ai cũng xem được)
    function traCuuBang(bytes32 _maHash) public view returns (ThongTinBang memory) {
        return danhSachBang[_maHash];
    }
}