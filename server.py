"""Server for emotion detection application."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detect_route():
    """
    This function receives text from the frontend via GET,
    runs the emotion detector on it, and returns a formatted response.
    """

    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze or text_to_analyze.strip() == "":
        return "Invalid input! Please enter some text to analyze."

    response = emotion_detector(text_to_analyze)
    
    if not response or response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    result_str = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    return result_str

@app.route("/")
def home():
    """Render the home page."""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
