from flask import Flask, jsonify, request
from service import create_app

app = create_app()

accounts = []
current_id = 1

@app.route('/accounts', methods=['POST'])
def create_account():
    global current_id
    data = request.get_json()
    account = {
        "id": current_id,
        "name": data.get("name"),
        "email": data.get("email"),
        "address": data.get("address")
    }
    accounts.append(account)
    current_id += 1
    return jsonify(account), 201

@app.route('/accounts', methods=['GET'])
def list_accounts():
    return jsonify(accounts), 200

@app.route('/accounts/<int:account_id>', methods=['GET'])
def get_account(account_id):
    for acc in accounts:
        if acc["id"] == account_id:
            return jsonify(acc), 200
    return jsonify({"error": "Not found"}), 404

@app.route('/accounts/<int:account_id>', methods=['PUT'])
def update_account(account_id):
    data = request.get_json()
    for acc in accounts:
        if acc["id"] == account_id:
            acc["name"] = data.get("name", acc["name"])
            acc["email"] = data.get("email", acc["email"])
            acc["address"] = data.get("address", acc["address"])
            return jsonify(acc), 200
    return jsonify({"error": "Not found"}), 404

@app.route('/accounts/<int:account_id>', methods=['DELETE'])
def delete_account(account_id):
    global accounts
    accounts = [acc for acc in accounts if acc["id"] != account_id]
    return jsonify({"message": "Deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)