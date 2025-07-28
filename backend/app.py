from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/submit", methods=["POST"])
def submit():
    data = request.form
    return jsonify({"message": f"Received {data['name']} - {data['email']} from Flask!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
