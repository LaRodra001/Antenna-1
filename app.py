
from flask import Flask, render_template, request, jsonify
from pathlib import Path

BaseDirectory = Path(__file__).resolve().parent

app = Flask(
    __name__,
    template_folder=str(BaseDirectory / "templates"),
    static_folder=str(BaseDirectory / "static")
)

antenna1Pos = (None, None)

@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/get-coords", methods=["GET"])
def GetDate():
    return jsonify({
        "question": "¿Cual es tu posicion actual?"
    })

@app.route("/answer-coords", methods=["POST"])
def AnswerDate():
    Data = request.get_json()

    x, y = Data.get("pos")
    state = "online" if Data.get("state") else "offline"

    print(f"HTML's position is: {x, y}")
    print(f"HTML is {state}")

    return jsonify({
        "message": [
            f"Actual Position: {x}, {y}.",
            f"State: {state}."
        ]
    })

@app.route("/ask-state", methods=["GET"])
def GetState():
    return jsonify({
        "question": "¿Cual es tu estado?"
    })

@app.route("/answer-state", methods=["POST"])
def AnwerState():
    Data = request.get_json()

    state = "online" if Data.get("state") else "offline"

    print(f"HTML {state}")

    return jsonify({
        "question": "¿Whats your state?"
    })



if __name__ == "__main__":
    app.run(debug=True)
