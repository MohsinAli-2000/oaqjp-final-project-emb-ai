import requests
import json

def emotion_detector(text_to_analyze):
    # Define the URL for the Emotion Predict function
    url = 'https://skills.network'
    
    # Define the headers required by the API
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Format the input JSON payload
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Send a POST request to the API
    response = requests.post(url, json=myobj, headers=headers)
    
    # Convert the response text into a dictionary
    formatted_response = json.loads(response.text)
    
    # Extract the emotion predictions sub-dictionary
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Extract individual scores
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # Logic to find the dominant emotion (highest score)
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Format the required output dictionary
    output = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
    
    return output
