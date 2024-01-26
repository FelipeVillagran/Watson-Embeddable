from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def analyze_emotions(text_to_analyze):
    api_key = "INSERTAR_API_KEY_SERVICIO_IBM"
    url = "https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/instances/39e3a091-d296-4a3d-bfbd-bb73a4138323"

    authenticator = IAMAuthenticator(api_key)
    nlu = NaturalLanguageUnderstandingV1(
        version="2021-08-01",
        authenticator=authenticator
    )

    nlu.set_service_url(url)

    try:
        response = nlu.analyze(
            text=text_to_analyze,
            features={"emotion": {}}
        ).get_result()

        emotions = {
            'anger': response['emotion']['document']['emotion']['anger'],
            'disgust': response['emotion']['document']['emotion']['disgust'],
            'fear': response['emotion']['document']['emotion']['fear'],
            'joy': response['emotion']['document']['emotion']['joy'],
            'sadness': response['emotion']['document']['emotion']['sadness'],
            'dominant_emotion': max(
                response['emotion']['document']['emotion'],
                key=response['emotion']['document']['emotion'].get
            )
        }

        return emotions

    except Exception as e:
        return f"Error: {e}"

# Ejemplo de uso:
#text_to_analyze = "I love this new technology"
#emotions_result = analyze_emotions(text_to_analyze)
#print(emotions_result)

