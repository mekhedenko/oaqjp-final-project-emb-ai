from flask import Flask, request, render_template 
import EmotionDetection

app = Flask(__name__)

@app.route("/") 
def home():
    return render_template('index.html') 

@app.route("/emotionDetector", methods = ["GET"])
def emotions():
    query = request.args["textToAnalyze"]
    return EmotionDetection.emotion_detection.emotion_detector(query)
