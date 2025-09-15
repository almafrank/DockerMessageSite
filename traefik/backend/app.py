
from flask import Flask, request, jsonify
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route("/api", methods=["GET"])
def api():
    return jsonify({"message": "Hello from Python backend!"})

@app.route("/submit", methods=["POST"])
def submit():
    data = request.json
    if not data or "message" not in data:
        return jsonify({"error": "Missing message"}), 400
    r.lpush("messages", data["message"])
    return jsonify({"status": "ok"})

@app.route("/messages", methods=["GET"])
def get_messages():
    messages = r.lrange("messages", 0, 9)
    return jsonify(messages)

@app.route("/clear", methods=["POST"])
def clear_messages():
    r.delete("messages")
    return jsonify({"status": "cleared"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
