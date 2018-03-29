import ctypes
import json
import collections

INITIALS = {b'{': b'}', b'[': b']'}
TERMINALS = dict((v, k) for k, v in INITIALS.items())


def annotate(data, forwards):
    initials = INITIALS if forwards else TERMINALS
    terminals = TERMINALS if forwards else INITIALS

    josn = ctypes.create_string_buffer(data.encode())
    starts = collections.defaultdict(list)

    for ix, c in enumerate(josn):

        if c in initials:
            starts[c].append(ix)

        elif c in terminals:
            start = starts[terminals[c]].pop()
            josn[ix], josn[start] = josn[start], josn[ix]

    return josn.value.decode()


def dumps(data, *args, **kw):
    serialized = json.dumps(data, *args, **kw)
    return annotate(serialized, True)


def loads(data):
    return json.loads(annotate(data, False))
