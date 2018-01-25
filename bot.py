from mongoengine import *


class Steam_guard_code(Document):
    bot_id = StringField()
    bot_pass = StringField()
    code = ListField(StringField())
