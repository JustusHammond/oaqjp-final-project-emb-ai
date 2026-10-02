"""Webapp providing emotion detection"""

import os
from flask import Flask, jsonify, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    """Render the app home page."""
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET", "POST"])
def detect_emotion():
    """Analyze emotion from a string"""
    payload = request.get_json(silent=True)

    if not isinstance(payload, dict):
        payload = {}

    text = (
        payload.get("text")
        or payload.get("textToAnalyze")
        or request.form.get("text")
        or request.form.get("textToAnalyze")
        or request.args.get("text")
        or request.args.get("textToAnalyze")
    )
    if not isinstance(text, str) or not text.strip():
        return jsonify({"error": "Please provide text to analyze."}), 400

    result = emotion_detector(text.strip())

    if result["dominant_emotion"] is None:
        return jsonify({"error": "The emotion service could not analyze the text."}), 400

    return jsonify(result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
