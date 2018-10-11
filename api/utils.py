import json

from bson.json_util import dumps


def bson_to_dict(collection):
    return json.loads(dumps(collection))
