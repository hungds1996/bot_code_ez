# mongodb://<dbuser>:<dbpassword>@ds137826.mlab.com:37826/ezgame

import mongoengine

host = "ds137826.mlab.com"
port = 37826
db_name = "ezgame"
user_name = "admin"
password = "admin"


def mlab_connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
