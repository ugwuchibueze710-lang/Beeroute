from flask import Flask, render_template, request, jsonify
from core.orchestrator import BeeOrchestrator

app = Flask(__name__)
bee = BeeOrchestrator()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/send", methods=["POST"])
def send():
    user_input = request.json.get("text")

    response = bee.handle(user_input)

    return jsonify({
        "response": response
    })


if __name__ == "__main__":
    print("🌐 BeeRoute UI running...")
    app.run(debug=True)
