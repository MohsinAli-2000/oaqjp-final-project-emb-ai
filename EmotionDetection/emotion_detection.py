import requests
import json

def emotion_detector(text_to_analyze):
    # This is the EXACT URL required by the IBM environment
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, json=myobj, headers=headers)
    
    # Catch any connection errors cleanly instead of crashing
    if response.status_code != 200:
        return {
            'anger': 0, 'disgust': 0, 'fear': 0, 'joy': 0, 'sadness': 0,
            'dominant_emotion': f"Error: Status code {response.status_code}"
        }

    formatted_response = json.loads(response.text)
    
    # The API returns a list, so we MUST select index [0] first
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    output = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': max(emotions, key=emotions.get)
    }
    
    return output
