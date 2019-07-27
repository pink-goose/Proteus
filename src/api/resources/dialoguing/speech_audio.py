from flask import request, send_file
from flask.views import MethodView
from skills import Dialog


class SpeechAudio(MethodView):

    def post(self):
        speech_file = request.files['file']

        dialog = Dialog()
        answer_file = dialog.handle_speech_utterance(speech_file)

        return send_file(answer_file, attachment_filename='some_name', as_attachment=True)
