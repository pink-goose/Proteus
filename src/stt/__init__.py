from configuration import STT_ENGINE


class SpeechRecognizer:

    def __init__(self):
        pass

    # def send_to_recognizer(self, audio_file):
    #     stt_class = STTFactory.CLASSES.get(STT_ENGINE)
    #     recognizer = stt_class()
    #     recognizer.recognize(audio_file)
    #     # return text
    #     print(recognizer.text)

    def recognize(self, speech_file):
        stt_class = STTFactory.CLASSES.get(STT_ENGINE)
        recognizer = stt_class()
        recognized_text = recognizer.recognize(speech_file)
        # print(f'Recognized text: {recognized_text}')
        return recognized_text


class STTFactory:
    from stt.ibm_watson import Watson

    CLASSES = {
        'ibm_watson': Watson,
    }
