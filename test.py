import os

from flask import Flask, request, abort, jsonify, send_from_directory, send_file


UPLOAD_DIRECTORY = '/home/mikhail/PycharmProjects/Proteus/src/downloads'

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)


api = Flask(__name__)


@api.route("/files")
def list_files():
    """Endpoint to list files on the server."""
    files = []
    for filename in os.listdir(UPLOAD_DIRECTORY):
        path = os.path.join(UPLOAD_DIRECTORY, filename)
        if os.path.isfile(path):
            files.append(filename)
    return jsonify(files)


@api.route("/files/<path:path>")
def get_file(path):
    """Download a file."""
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)


@api.route("/1", methods=["POST"])
def post_file():
    """Upload a file."""

    filename = 'DAfifth.wav'

    # with open(os.path.join(UPLOAD_DIRECTORY, filename), "wb") as fp:
    #     fp.write(request.data)

    # Return 201 CREATED
    path_to_file = '/home/mikhail/PycharmProjects/Proteus/src/downloads/DAfifth.wav'
    # print(send_from_directory(UPLOAD_DIRECTORY, filename, as_attachment=True))
    return send_from_directory(UPLOAD_DIRECTORY, filename, as_attachment=True)


# upload
@api.route('/upload', methods=['POST'])
def upload_file():
    print(request.files)
    # checking if the file is present or not.
    if 'file' not in request.files:
        return "No file found"
    file = request.files['file']
    file.save("/home/mikhail/PycharmProjects/Proteus/src/downloads/sound.wav")
    return "file successfully saved"


# download
@api.route('/voice', methods=['POST'])
def download_file():
    path_to_file = '/home/mikhail/PycharmProjects/Proteus/src/downloads/111.wav'
    return send_file(path_to_file, attachment_filename='111.wav', as_attachment=True)


if __name__ == "__main__":
    api.run(debug=True, port=8000)
