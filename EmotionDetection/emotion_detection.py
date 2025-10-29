import requests
import json

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(URL, json=obj, headers = Headers)

    #parse the json response from api
    #format_response = json.loads(response.text)

    if response.status_code == 200:
        # Convert JSON response text to a Python dictionary
        response_dict = json.loads(response.text)

        # Extract emotion scores
        emotions = response_dict["emotionPredictions"][0]["emotion"]
        anger_score = emotions["anger"]
        disgust_score = emotions["disgust"]
        fear_score = emotions["fear"]
        joy_score = emotions["joy"]
        sadness_score = emotions["sadness"]

        # Find dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)

        # Return your formatted dictionary
        return {
            "anger": anger_score,
            "disgust": disgust_score,
            "fear": fear_score,
            "joy": joy_score,
            "sadness": sadness_score,
            "dominant_emotion": dominant_emotion
        }

    elif response.status_code == 500:
        # Handle server errors
        return {"error": "Internal Server Error - the text may be invalid or too short."}

    else:
        # Handle any other status codes
        return {"error": f"Unexpected status code: {response.status_code}"}

    #return format_response
