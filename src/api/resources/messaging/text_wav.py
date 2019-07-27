from flask import request, send_file
from flask.views import MethodView
from skills import Dialog


class TextWav(MethodView):

    def post(self):
        data = request.json
        if 'text' in data:

            dialog = Dialog()
            answer_file = dialog.handle_utterance(data["text"])

            return send_file(answer_file, attachment_filename='sound', as_attachment=True)
