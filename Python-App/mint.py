import json
import os
from web3 import Web3
from dotenv import load_dotenv

# 1. Nạp cấu hình từ file .env (Bảo mật)
load_dotenv()
contract_address = os.getenv("CONTRACT_ADDRESS")
private_key = os.getenv("PRIVATE_KEY")

# 2. Kết nối mạng Cronos
cronos_rpc = "https://evm-t3.cronos.org/"
web3 = Web3(Web3.HTTPProvider(cronos_rpc))
account = web3.eth.account.from_key(private_key) # Khôi phục ví từ khóa bí mật
my_address = account.address

print(f"🔗 Đang kết nối từ ví: {my_address}")

# 3. Lấy ABI (Bản vẽ)
with open("abi.json", "r") as f:
    abi_data = json.load(f)["abi"]

contract = web3.eth.contract(address=contract_address, abi=abi_data)

# --- HÀM CẤP BẰNG (ĐÃ SỬA LỖI GAS) ---
def cap_bang_moi(ten_sv, ma_sv, loai_bang):
    print(f"\n⏳ Đang xử lý cấp bằng cho: {ten_sv}...")

    # A. Tạo mã Hash
    ma_hash = Web3.solidity_keccak(['string'], [ma_sv])
    print(f"🔑 Mã Hash tạo ra: {ma_hash.hex()}")

    # B. Chuẩn bị giao dịch
    nonce = web3.eth.get_transaction_count(my_address)

    # --- SỬA ĐỔI QUAN TRỌNG TẠI ĐÂY ---
    # 1. Lấy giá gas hiện tại của mạng lưới
    gas_price = web3.eth.gas_price
    # 2. Tăng thêm 20% để đảm bảo giao dịch đi nhanh (tránh bị kẹt)
    adjusted_gas_price = int(gas_price * 1.2)
    
    print(f"⛽ Giá Gas hiện tại: {gas_price} -> Đề xuất trả: {adjusted_gas_price}")

    tx_data = contract.functions.capBang(
        ma_hash,
        ten_sv,
        ma_sv,
        loai_bang
    ).build_transaction({
        'chainId': 338,
        'gas': 3000000,           # Tăng giới hạn Gas lên 3 triệu cho chắc
        'gasPrice': adjusted_gas_price, # Dùng giá tự động thay vì số '10' cũ
        'nonce': nonce,
    })
    # -------------------------------------

    # C. Ký tên
    print("✍️  Đang ký điện tử...")
    signed_tx = web3.eth.account.sign_transaction(tx_data, private_key)

    # D. Gửi
    print("🚀 Đang gửi lên Blockchain...")
    tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)

    # E. Chờ
    print(f"⏳ Đang chờ xác nhận (Tx Hash: {web3.to_hex(tx_hash)})...")
    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

    print("✅ CẤP BẰNG THÀNH CÔNG!")
    print("========================================")
    return ma_hash.hex()

# --- CHẠY THỬ ---
if __name__ == "__main__":
    # Điền thông tin sinh viên muốn cấp
    ma_hash_vua_tao = cap_bang_moi(
        ten_sv="Nguyen Van A",
        ma_sv="SV2024001",
        loai_bang="Ky Su Gioi"
    )

    print(f"👉 Hãy copy mã này để tra cứu: {ma_hash_vua_tao}")