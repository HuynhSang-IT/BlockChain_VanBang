from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os
from web3 import Web3
from dotenv import load_dotenv

# --- CẤU HÌNH ---
app = Flask(__name__)
CORS(app) # Cho phép mọi người kết nối
load_dotenv()

# Kết nối Blockchain
cronos_rpc = "https://evm-t3.cronos.org/"
web3 = Web3(Web3.HTTPProvider(cronos_rpc))
contract_address = os.getenv("CONTRACT_ADDRESS")
private_key = os.getenv("PRIVATE_KEY")
my_address = web3.eth.account.from_key(private_key).address

# Load ABI
with open("abi.json", "r") as f:
    abi_data = json.load(f)["abi"]

contract = web3.eth.contract(address=contract_address, abi=abi_data)

# --- TRANG CHỦ ---
@app.route('/')
def home():
    return "<h1>🚀 SERVER BLOCKCHAIN ĐANG CHẠY NGON LÀNH!</h1>"

# --- API 1: TRA CỨU VĂN BẰNG ---
# Cách dùng: Truy cập http://localhost:5000/tra-cuu/<mã_hash>
@app.route('/tra-cuu/<path:ma_hash>', methods=['GET'])
def api_tra_cuu(ma_hash):
    try:
        print(f"🔍 Đang tra cứu: {ma_hash}")
        result = contract.functions.traCuuBang(ma_hash).call()
        
        # Kiểm tra nếu ngày cấp = 0 là không có
        if result[3] == 0:
            return jsonify({"status": "error", "message": "Van bang khong ton tai!"}), 404
        
        # Trả về dữ liệu đẹp đẽ
        data = {
            "status": "success",
            "sinh_vien": result[0],
            "ma_sv": result[1],
            "loai_bang": result[2],
            "ngay_cap": result[3],
            "nguoi_cap": result[4]
        }
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# --- API 2: CẤP BẰNG MỚI ---
# Cách dùng: Gửi dữ liệu JSON vào đường dẫn này
@app.route('/cap-bang', methods=['POST'])
def api_cap_bang():
    try:
        # Lấy dữ liệu người dùng gửi lên
        data = request.json
        ten_sv = data.get('ten_sv')
        ma_sv = data.get('ma_sv')
        loai_bang = data.get('loai_bang')

        print(f"📝 Đang cấp bằng cho: {ten_sv}")

        # 1. Tạo Hash
        ma_hash = Web3.solidity_keccak(['string'], [ma_sv])
        
        # 2. Tính toán Gas
        nonce = web3.eth.get_transaction_count(my_address)
        gas_price = web3.eth.gas_price
        adjusted_gas = int(gas_price * 1.2)

        # 3. Tạo giao dịch
        tx_data = contract.functions.capBang(
            ma_hash, ten_sv, ma_sv, loai_bang
        ).build_transaction({
            'chainId': 338,
            'gas': 3000000,
            'gasPrice': adjusted_gas,
            'nonce': nonce,
        })

        # 4. Ký và Gửi
        signed_tx = web3.eth.account.sign_transaction(tx_data, private_key)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)
        
        # 5. Chờ xác nhận
        receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

        return jsonify({
            "status": "success", 
            "message": "Cap bang thanh cong!",
            "tx_hash": web3.to_hex(tx_hash),
            "ma_hash_bang": ma_hash.hex()
        }), 200

    except Exception as e:
        print("Lỗi:", e)
        return jsonify({"status": "error", "message": str(e)}), 500

# --- CHẠY SERVER ---
if __name__ == '__main__':
    app.run(debug=True, port=5000)