"""Module to detect emotion using Watson NLP library."""

import requests


def emotion_detector(text_to_analyze):
    """Detect the emotion of a given text string."""
    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {"raw_document": {"text": text_to_analyze}}
    empty_result = {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None,
    }

    response = requests.post(
        url=url,
        headers=headers,
        json=payload,
        timeout=7,
    )

    if response.status_code == 400:
        return empty_result

    response.raise_for_status()

    data = response.json()
    emotions = data["emotionPredictions"][0]["emotion"]
    dominant_emotion = max(emotions, key=emotions.get)

    return {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": dominant_emotion,
    }
