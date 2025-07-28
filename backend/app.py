from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/submit", methods=["POST"])
def submit():
    data = request.form or request.json  # ✅ Accept both
    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return jsonify({"message": "Missing data"}), 400

    return jsonify({"message": f"Data received for {name} with email {email}"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
