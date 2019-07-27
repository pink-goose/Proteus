from flask import request, send_from_directory, send_file
# from rest_core import (
#     Resource,
# )
from flask.views import MethodView


class Download(MethodView):

    def post(self):
        path_to_file = '/home/mikhail/PycharmProjects/Proteus/src/downloads/sound.wav'
        return send_file(path_to_file, attachment_filename='sound.wav', as_attachment=True)
