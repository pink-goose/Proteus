from adapt.intent import IntentBuilder
from skills.core import Skill


class HelloWorldSkill(Skill):
    def __init__(self):
        super(HelloWorldSkill, self).__init__(name="HelloWorldSkill")

    def initialize(self):
        thank_you_intent = IntentBuilder("ThankYouIntent"). \
            require("ThankYouKeyword").build()
        self.register_intent(thank_you_intent, self.handle_thank_you_intent)

        how_are_you_intent = IntentBuilder("HowAreYouIntent"). \
            require("HowAreYouKeyword").build()
        self.register_intent(how_are_you_intent,
                             self.handle_how_are_you_intent)

        hello_world_intent = IntentBuilder("HelloWorldIntent"). \
            require("HelloWorldKeyword").build()
        self.register_intent(hello_world_intent,
                             self.handle_hello_world_intent)

    def handle_thank_you_intent(self):
        answer_text = self.speak_dialog("welcome")
        return answer_text

    def handle_how_are_you_intent(self):
        answer_text = self.speak_dialog("how.are.you")
        return answer_text

    def handle_hello_world_intent(self):
        answer_text = self.speak_dialog("hello.world")
        return answer_text

    def stop(self):
        pass


def create_skill():
    return HelloWorldSkill()
