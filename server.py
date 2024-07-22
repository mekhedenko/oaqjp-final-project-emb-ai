"""server.py."""
from flask import Flask, request, render_template
import EmotionDetection

app = Flask(__name__)

@app.route("/")
def home():
    """home"""
    return render_template('index.html')

@app.route("/emotionDetector", methods = ["GET"])
def emotions():
    """emotions"""
    query = request.args["textToAnalyze"]
    response = EmotionDetection.emotion_detection.emotion_detector(query)

    if response["dominant_emotion"] == "None":
        return "Invalid text! Please try again!"

    return response
