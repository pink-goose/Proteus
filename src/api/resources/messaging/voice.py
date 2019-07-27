import os
# from flask_restful import reqparse
# import werkzeug
# import wave
# import np
from flask import request, send_from_directory
from flask import send_file
from werkzeug.utils import secure_filename
# from .rest_core import (
#     Resource,
# )
from flask.views import MethodView


UPLOAD_FOLDER = '/home/mikhail/PycharmProjects/Proteus/src/downloads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'mp3', 'wav'])


class Voice(MethodView):

    def post(self):
        file = request.files['file']
        # filePath = "./somedir/" + secure_filename(file.filename)
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        print(file.filename)
        # return 'downloading'
        path_to_file = '/home/mikhail/PycharmProjects/Proteus/src/downloads/DAfifth.wav'
        return send_file(path_to_file, attachment_filename='DAfifth.wav', as_attachment=True)
        # return send_file(
        #     path_to_file,
        #     mimetype="audio/wav",
        #     as_attachment=True,
        #     attachment_filename="test.wav")

    def allowed_file(self, filename):
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
