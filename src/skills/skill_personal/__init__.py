from skills.core import Skill
from adapt.intent import IntentBuilder


class PersonalSkill(Skill):
    def __init__(self):
        super(PersonalSkill, self).__init__(name="PersonalSkill")

    def initialize(self):
        what_is_your_name_intent = IntentBuilder("WhatIsYourNameIntent"). \
            require("WhatIsYourNameKeyword").build()
        self.register_intent(what_is_your_name_intent, self.handle_what_is_your_name_intent)

        your_creator_intent = IntentBuilder("YourCreatorIntent"). \
            require("YourCreatorKeyword").build()
        self.register_intent(your_creator_intent, self.handle_your_creator_intent)

    def handle_what_is_your_name_intent(self):
        answer_text = self.speak_dialog("what.is.your.name")
        return answer_text

    def handle_your_creator_intent(self):
        answer_text = self.speak_dialog("your.creator")
        return answer_text


def create_skill():
    return PersonalSkill()
