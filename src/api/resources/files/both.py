from flask import request, send_file
# from rest_core import (
#     Resource,
# )
from flask.views import MethodView


class Both(MethodView):

    def post(self):
        print(request.files)
        # checking if the file is present or not.
        if 'file' not in request.files:
            return "No file found"
        file = request.files['file']
        # file.save("/home/mikhail/PycharmProjects/Proteus/src/downloads/sound.wav")
        file.save("/code/downloads/sound.wav")
        # return "file successfully saved"
        print('Upload and download')
        path_to_file = '/code/downloads/sound.wav'

        return send_file(path_to_file, attachment_filename='sound.wav', as_attachment=True)
