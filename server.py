from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

# Initialize the Flask application instance
app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_analyzer():
    """
    Retrieves text parameters from the web client, analyzes emotions via 
    the backend package, and returns a formatted summary response string.
    """
    # Retrieve the text query parameter passed from the front-end JS script
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Send the extracted text payload into our package function
    response = emotion_detector(text_to_analyze)
    
    # Construct the precise client response layout requested by the customer
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )
    
    return formatted_response

@app.route("/")
def render_index_page():
    """
    Renders the default landing user-interface dashboard template.
    """
    return render_template('index.html')

if __name__ == "__main__":
    # Host the application on localhost port 5000 as requested
    app.run(host="0.0.0.0", port=5000)
