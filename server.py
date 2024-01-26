from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import analyze_emotions

app = Flask('Emotion Detector')

@app.route('/emotionDetector')
def emotion_detector_function():
    test_to_analyze = request.args.get('textToAnalyze')

    # Manejo de entrada en blanco
    if not test_to_analyze:
        return "Error: Text input is blank. Please provide valid text."

    response = analyze_emotions(test_to_analyze)

    # Manejo de status_code 400
    if response.get('dominant_emotion') is None:
        return "Invalid text! Please try again."

    response_text = f"For the given statement, the system response is 'anger': \
                    {response.get('anger')}, 'disgust': {response.get('disgust')}, \
                    'fear': {response.get('fear')}, 'joy': {response.get('joy')}, \
                    'sadness': {response.get('sadness')}. The dominant emotion is \
                    {response.get('dominant_emotion')}."
    
    return response_text

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)