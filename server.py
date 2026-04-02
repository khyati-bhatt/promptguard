from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data:
        return jsonify({"error": "no json"})

    msg = data.get("message", "")

    if "ignore previous instructions" in msg.lower():
        return jsonify({"response": "SYSTEM PROMPT: secret config"})

    return jsonify({"response": f"You said: {msg}"})

app.run(port=5000)