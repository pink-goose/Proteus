from adapt.intent import IntentBuilder
from skills.core import Skill


class WikipediaSkill(Skill):
    def __init__(self):
        super(WikipediaSkill, self).__init__(name="WikipediaSkill")


def create_skill():
    return WikipediaSkill()