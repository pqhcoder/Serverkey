from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# Admin token để tạo/xóa key
ADMIN_TOKEN = "mat_khau_admin"

# Bộ nhớ key (lưu trên RAM cho demo, triển khai thực tế thì dùng MySQL hoặc file JSON)
keys_db = {}

# API tạo key (chỉ admin)
@app.route("/admin/create_key", methods=["POST"])
def create_key():
    token = request.headers.get("X-ADMIN-TOKEN")
    if token != ADMIN_TOKEN:
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()
    role = data.get("role", "free")

    key_id = str(uuid.uuid4())
    secret = str(uuid.uuid4())

    keys_db[key_id] = {
        "secret": secret,
        "role": role
    }

    return jsonify({"key_id": key_id, "secret": secret, "role": role})

# API xóa key
@app.route("/admin/delete_key", methods=["POST"])
def delete_key():
    token = request.headers.get("X-ADMIN-TOKEN")
    if token != ADMIN_TOKEN:
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()
    key_id = data.get("key_id")

    if key_id in keys_db:
        del keys_db[key_id]
        return jsonify({"message": "Key deleted"})
    return jsonify({"error": "Key not found"}), 404

# API kiểm tra key
@app.route("/check_key", methods=["POST"])
def check_key():
    data = request.get_json()
    key_id = data.get("key_id")
    secret = data.get("secret")

    if key_id in keys_db and keys_db[key_id]["secret"] == secret:
        return jsonify({"valid": True, "role": keys_db[key_id]["role"]})
    return jsonify({"valid": False}), 401

@app.route("/")
def home():
    return "🔑 Key Management Server is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
