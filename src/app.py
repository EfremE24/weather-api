from flask import Flask, request, jsonify,render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app = Flask(__name__)

def classify_temperature(temp: float) -> str:
    """Return a human-readable message based on the temperature."""
    if temp < 0:
        return "It's freezing-stay warm!"
    elif temp < 50:
        return "It's cold-wear a jacket!"
    elif temp < 75:
        return "It's nice and beautiful outside!"
    elif temp < 90:
        return "It's hot, but not too hot! Put some sunscreen on!"
    elif temp <= 100:
        return "It's hot-stay hydrated!"
    else:
        return "It's dangerously hot-don't spend much time out"


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/weather", methods=["GET"])
def weather():
    """
    Example:
      /weather?temp=45
    Returns:
      { "temperature": 45, "message": "It's cold—wear a jacket!" }
    """
    temp_str = request.args.get("temp")

    if temp_str is None:
        return jsonify({"error": "Missing required query parameter 'temp'."}), 400

    try:
        temp = float(temp_str)
    except ValueError:
        return jsonify({"error": "Invalid temperature. Provide a number."}), 400

    message = classify_temperature(temp)

    return jsonify({
        "temperature": temp,
        "message": message
    }), 200


if __name__ == "__main__":
    # 0.0.0.0 so it works inside Docker, port 8080 so it's easy to map
    app.run(host="0.0.0.0", port=8080)

