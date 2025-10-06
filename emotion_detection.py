import json
import requests

def emotion_detector(text_to_analyze):
    """
    Analyzes the emotions of the given text using an external sentiment analysis API.

    Args:
        text (str): The text to analyze.

    Returns:
        dict: A dictionary containing the emotiojnn analysis results.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    requestObj =  { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=requestObj, headers=headers)
    response_json = response.json() #json.loads(response.text)
    emotion_response = response_json["emotionPredictions"][0]["emotion"]
    dominant_emotion = max(emotion_response, key=emotion_response.get)
    emotion_response["dominant_emotion"] = dominant_emotion
    return emotion_response
  