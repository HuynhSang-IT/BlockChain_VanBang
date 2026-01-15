import json
from web3 import Web3

# --- 1. CẤU HÌNH KẾT NỐI ---
# Kết nối vào mạng Cronos Testnet
cronos_rpc = "https://evm-t3.cronos.org/"
web3 = Web3(Web3.HTTPProvider(cronos_rpc))

# Kiểm tra kết nối
if web3.is_connected():
    print("✅ Đã kết nối thành công với Cronos Testnet!")
else:
    print("❌ Không thể kết nối!")

# --- 2. THIẾT LẬP HỢP ĐỒNG ---
address = "0xc2EDa0FDe7DF24dfd8d7B6E7ba2Ac71c614d41AC" # Địa chỉ bạn vừa deploy
with open("abi.json", "r") as f:
    abi_data = json.load(f)["abi"] # Lấy phần 'abi' trong file json

# Tạo đối tượng hợp đồng để Python điều khiển
contract = web3.eth.contract(address=address, abi=abi_data)

# --- 3. HÀM TRA CỨU (Đọc dữ liệu) ---
def tra_cuu_bang(ma_hash):
    try:
        # Gọi hàm 'traCuuBang' từ Smart Contract
        result = contract.functions.traCuuBang(ma_hash).call()
        
        # Nếu ngày cấp = 0 nghĩa là không tồn tại
        if result[3] == 0:
            print("⚠️ Văn bằng này KHÔNG tồn tại trên hệ thống!")
        else:
            print("\n=== 🎓 THÔNG TIN VĂN BẰNG TÌM THẤY ===")
            print(f"👤 Sinh viên: {result[0]}")
            print(f"🆔 Mã SV:     {result[1]}")
            print(f"📜 Loại bằng: {result[2]}")
            print(f"📅 Ngày cấp:  {result[3]}")
            print(f"🏛️ Người cấp: {result[4]}")
            print("=======================================")
    except Exception as e:
        print(f"Lỗi: {e}")

# --- CHẠY THỬ ---
# Vì chưa cấp bằng nào, ta thử tra cứu một mã bừa xem nó báo gì
ma_hash_test = "0xb33caacf4d2dbf4bea6103974673dd74f376e72a9d5511c4845cbd6ffdf0b62d"
tra_cuu_bang(ma_hash_test)