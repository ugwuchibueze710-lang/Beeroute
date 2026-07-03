from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
    data = request.json
    text = data.get("text", "")

    return jsonify({
        "response": f"You said: {text}"
    })
