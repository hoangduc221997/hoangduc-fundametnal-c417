import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds163738.mlab.com:63738/muadong

host = "ds163738.mlab.com"
port = 63738
db_name = "muadong"
user_name = "admin"
password = "admin"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
