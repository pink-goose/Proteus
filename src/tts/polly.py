from tts import Speak
import boto3
# from configuration import PATH_TO_SENTENCE_FILE
from io import BytesIO


class Polly(Speak):

    def say(self, text):
        polly_client = boto3.Session(
            aws_access_key_id='AKIAJA3RK2QJ4S7PUD4Q',
            aws_secret_access_key='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',
            region_name='us-west-2').client('polly')

        response = polly_client.synthesize_speech(VoiceId='Joanna',
                                                  OutputFormat='mp3',
                                                  Text=text)

        # file = open(PATH_TO_SENTENCE_FILE, 'wb')
        # file.write(response['AudioStream'].read())
        # file.close()

        audio_buf = BytesIO(response['AudioStream'].read())
        return audio_buf
