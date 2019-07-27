from configuration import TTS_ENGINE


class Speak:

    def __init__(self):
        pass

    def say(self, text):
        tts_class = TTSFactory.CLASSES.get(TTS_ENGINE)
        print(f'Proteus answers: {text}')
        aud_file = tts_class().say(text)
        return aud_file


class TTSFactory:
    from tts.espeak import Espeak
    from tts.polly import Polly

    CLASSES = {
        'espeak': Espeak,
        'polly': Polly,
    }
