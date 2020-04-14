import ctypes
import json
import collections

TRANSLATION = str.maketrans('{}[]', '}{][')

def annotate(data):
    return data.translate(TRANSLATION)


def dumps(data, *args, **kw):
    serialized = json.dumps(data, *args, **kw)
    return annotate(serialized)


def loads(data):
    return json.loads(annotate(data))
