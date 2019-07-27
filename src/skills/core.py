from adapt.engine import IntentDeterminationEngine
import os
from tts import Speak
import random
from configuration import LANG
from stt import SpeechRecognizer
from flask import current_app


engine = IntentDeterminationEngine()


class Dialog:
    def __init__(self):
        pass

    def handle_speech_utterance(self, speech_file):
        recognizer = SpeechRecognizer()     # make zaranee? on zhe odin dolzhen byt`
        utterance_text = recognizer.recognize(speech_file)
        answer_file = self.handle_utterance(utterance_text)
        return answer_file

    def handle_utterance(self, utterance_text):
        # TODO: refactor this
        answer_text = current_app.skill_inits.intent_determiner(utterance_text)
        speak = Speak()
        answer_file = speak.say(answer_text)
        return answer_file


class Skill:

    events = {}

    def __init__(self, name=None):
        self.name = name or self.__class__.__name__
        self.root_dir = None
        self.initialize()

    def initialize(self):
        self.root_dir = os.getcwd() + '/skills'

        def register_entities():
            for root, dirs, files in os.walk(self.root_dir):
                for file in files:
                    if file.endswith(".voc"):
                        print(f'Founded ".voc" file: {os.path.join(root, file)}')
                        filename = os.path.join(root, file)
                        keyword_name = os.path.splitext(os.path.basename(filename))[0]
                        linelist = [line.rstrip('\n') for line in open(filename)]
                        for keyword in linelist:
                            print(f'Registering keyword: "{keyword}" : {keyword_name}')
                            engine.register_entity(keyword, keyword_name)

        register_entities()
        print('Skill class Initialized')

        # This is analogue of:
        # test_keyword = [
        #     "test",
        #     "pussy"
        # ]
        #
        # for tk in test_keyword:
        #     engine.register_entity(tk, "TestKeyword")

        for i in SkillList.CLASSES.values():
            i().initialize()
            print(f'{i().name} Initialized')

        print(f'Registered events: {self.events}')

    # def find_resource(self, res_name, res_dirname=None):
    #     path = join(self.root_dir, res_dirname, res_name)
    #     print(path)
        # if exists(path):
        #     print(path)
        #     return path
        # return None

    def register_intent(self, intent_parser, handler):
        engine.register_intent_parser(intent_parser)
        self.add_event(intent_parser.name, handler)

    def add_event(self, name, handler):
        # print(f'Name: {name}, Handler: {handler}')
        self.events[name] = handler
        # 3 times run, WTF??? Check this:
        # print(f'Event added: {self.events}')

    def default_action(self):
        answer_text = self.speak_dialog('dont.understand')
        return answer_text

    def intent_determiner(self, text):
        intent_determined = False

        for intent in engine.determine_intent(text):
            intent_determined = True
            print(f'Intent determined: {intent} ')
            # MAGIC!
            answer_text = self.events.get(intent["intent_type"])()
            # analogue of HelloWorldSkill.handle_thank_you_intent()

        if not intent_determined:
            answer_text = self.default_action()

        return answer_text

    # def speak(self, utterance):
    #     speak = Speak()
    #     speak.say(utterance)

    def speak_dialog(self, key):
        # TODO FIX this fucking shit
        self.root_dir = os.getcwd() + '/skills'
        for root, dirs, files in os.walk(self.root_dir):
            for file in files:
                if file.endswith(key + ".dialog"):
                    filename = os.path.join(root, file)
                    print(f'Founded ".dialog" file: {filename}')
                    upper_dir = os.path.basename(os.path.dirname(filename))
                    print(f'Upper dir: {upper_dir}')
                    if LANG == upper_dir:
                        linelist = [line.rstrip('\n') for line in open(filename)]
                        # self.speak(random.choice(linelist))
                        answer_text = random.choice(linelist)
                        # break
                        return answer_text


class SkillList:
    # Непонятно В классе то несколько интентов
    # Переосмыслить!
    from skills.skill_hello import HelloWorldSkill
    from skills.skill_test import TestSkill
    from skills.skill_personal import PersonalSkill
    from skills.skill_time import TimeSkill

    CLASSES = {
        'HelloWorldIntent': HelloWorldSkill,
        'TestIntent': TestSkill,
        'WhatIsYourNameIntent': PersonalSkill,
        'WhatTimeIsIt': TimeSkill,
    }
