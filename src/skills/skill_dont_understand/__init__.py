from adapt.intent import IntentBuilder
from skills.core import Skill


class DontUnderstandSkill(Skill):
    def __init__(self):
        super(DontUnderstandSkill, self).__init__(name="DontUnderstandSkill")

    def initialize(self):
        pass

    def stop(self):
        pass


def create_skill():
    return DontUnderstandSkill()
