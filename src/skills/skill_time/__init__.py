from adapt.intent import IntentBuilder
from skills.core import Skill
import datetime


class TimeSkill(Skill):
    def __init__(self):
        super(TimeSkill, self).__init__(name="TimeSkill")

    def initialize(self):
        what_time_is_it_intent = IntentBuilder("WhatTimeIsItIntent"). \
            require("WhatTimeIsItKeyword").build()
        self.register_intent(what_time_is_it_intent, self.handle_what_time_is_it_intent)

    def get_current_time(self):
        current_datetime = datetime.datetime.now()
        time = current_datetime.strftime("%H:%M")
        return time

    def handle_what_time_is_it_intent(self):
        answer_text = self.get_current_time()
        return answer_text


def create_skill():
    return TimeSkill()
