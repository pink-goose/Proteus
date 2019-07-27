from flask import request, send_file
from flask.views import MethodView
# from configuration import PATH_TO_SENTENCE_FILE
# from stt import SpeechRecognizer
# from skills import Core
from skills import Dialog


class WavWav(MethodView):

    def post(self):
        speech_file = request.files['file']

        dialog = Dialog()
        answer_file = dialog.handle_speech_utterance(speech_file)

        return send_file(answer_file, attachment_filename='sound.wav', as_attachment=True)
