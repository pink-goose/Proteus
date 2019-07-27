from adapt.intent import IntentBuilder
from skills.core import Skill


class TestSkill(Skill):
    def __init__(self):
        super(TestSkill, self).__init__(name="TestSkill")

    def initialize(self):
        test_intent = IntentBuilder("TestIntent"). \
            require("TestKeyword").build()
        self.register_intent(test_intent,
                             self.handle_test_intent)

    def handle_test_intent(self):
        # self.speak_dialog("hello.world")
        print('Тестирую!')
        # self.speak('Это тест! Привет')
        return 'Это тест! Привет'


def create_skill():
    return TestSkill()
