from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def detect_emotion():
    textToAnalyse = request.args.get('textToAnalyze')
    emotion_detection_response = emotion_detector(textToAnalyse)
    
    response = "For the given statement, the system response is "

    response += f"'anger': {emotion_detection_response['anger']}, "
    response += f"'disgust': {emotion_detection_response['disgust']}, "
    response += f"'fear': {emotion_detection_response['fear']}, "
    response += f"'joy': {emotion_detection_response['joy']} and "
    response += f"'sadness': {emotion_detection_response['sadness']}. "
    response += f"The dominant emotion is <b>{emotion_detection_response['dominant_emotion']}. "
    
    return response

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)