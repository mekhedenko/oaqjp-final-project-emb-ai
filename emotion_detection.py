import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, headers=headers, json=input_json)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()
        return "error"

if __name__ == "__main__":
    # Test the function with the provided text
    test_text = "I love this new technology."
    print(emotion_detector(test_text))
