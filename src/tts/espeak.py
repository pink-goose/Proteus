from tts import Speak
import subprocess
# from configuration import PATH_TO_SENTENCE_FILE, LANG
from io import BytesIO


class Espeak(Speak):

    def say(self, text):
        # subprocess.call(["espeak", text, "-w", PATH_TO_SENTENCE_FILE])
        buffered_audio = BytesIO()
        print(f'FIRST: {buffered_audio}')
        # subprocess.call(["espeak", self.choose_lang(LANG), text, "-w", buffered_audio])
        print(f'After: {buffered_audio}')
        return buffered_audio

    def choose_lang(self, lang):
        langs = {
            'en-us': '-ven',
            'ru-ru': '-vru'
        }
        return langs.get(lang)
