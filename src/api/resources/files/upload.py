from flask import request, send_from_directory
# from rest_core import (
#     Resource,
# )
from flask.views import MethodView


class Upload(MethodView):

    def post(self):
        print(request.files)
        # checking if the file is present or not.
        if 'file' not in request.files:
            return "No file found"
        file = request.files['file']
        file.save("/home/mikhail/PycharmProjects/Proteus/src/downloads/sound.wav")
        return "file successfully saved"
