from flask import Blueprint
from .rest_core import Api
from .resources.tests import (
    Hello,
)
from .resources.messaging import (
    TextText,
    Voice,
    TextWav,
    WavWav,
)
from .resources.files import (
    Upload,
    Download,
    Both,
)
from .resources.dialoguing import (
    TextAudio,
    SpeechAudio,
)


api_bp = Blueprint('api', __name__)

api = Api(api_bp)

#####################################################################
# tests
api.add_resource(Hello, '/hello')
api.add_resource(TextText, '/message')
api.add_resource(Voice, '/voice')
api.add_resource(Upload, '/upload')
api.add_resource(Download, '/download')
api.add_resource(Both, '/both')
api.add_resource(TextWav, '/textwav')
api.add_resource(WavWav, '/wavwav')
# release
api.add_resource(TextAudio, '/dialogue/text')
api.add_resource(SpeechAudio, '/dialogue/speech')
