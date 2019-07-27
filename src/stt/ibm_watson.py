# pip install --upgrade "ibm-watson>=3.1.1"

from flask import current_app
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
import json
import requests


speech_to_text = SpeechToTextV1(
    iam_apikey='NQISnvBQQeGeN9J44tFcmV6Xbu1SilcImjvkWxuwoAN-',
    url='https://gateway-lon.watsonplatform.net/speech-to-text/api'
)
#
#
# class MyRecognizeCallback(RecognizeCallback):
#
#     def __init__(self):
#         RecognizeCallback.__init__(self)
#
#     def on_data(self, data):
#         results = data['results']
#         text = results[0]['alternatives'][0]['transcript']
#         recognizer = Watson()
#         recognizer.text = text
#         print(f'IBM Watson recognized text: {text}')
#         # aud_file = current_app.skill_inits.intent_determiner(text)
#         # return aud_file
#
#     def on_error(self, error):
#         print('Error received: {}'.format(error))
#
#     def on_inactivity_timeout(self, error):
#         print('Inactivity timeout: {}'.format(error))


class Watson:
    def __init__(self):
        # self.text = None
        pass

    # def recognize1(self, file):
    #     myRecognizeCallback = MyRecognizeCallback()
    #     audio_source = AudioSource(file)
    #     speech_to_text.recognize_using_websocket(
    #         audio=audio_source,
    #         content_type='audio/wav',
    #         recognize_callback=myRecognizeCallback,
    #         model='en-US_BroadbandModel'
    #     )
    #     print(f'HERE!!!!!!!!!!!: {self.text}')

    def recognize(self, speech_file):
        speech_recognition_results = speech_to_text.recognize(
            audio=speech_file,
            content_type='audio/wav'
        ).get_result()

        results = speech_recognition_results['results']
        text = results[0]['alternatives'][0]['transcript']
        print(f'IBM Watson recognized text: {text}')
        return text



