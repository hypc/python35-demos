import json
import unittest
import uuid


class MyClass(object):

    def __init__(self, name, value):
        self.uid = uuid.uuid1()
        self.name = name
        self.value = value

    def info(self):
        return {
            'uid': self.uid,
            'name': self.name,
            'value': self.value,
        }


class MyJSONEncoder(json.JSONEncoder):

    def default(self, o):
        if isinstance(o, uuid.UUID):
            return o.hex
        elif isinstance(o, MyClass):
            return o.info()
        return super(MyJSONEncoder, self).default(o)


class TestCase(unittest.TestCase):

    def test_1(self):
        uid = uuid.uuid1()
        json_str = json.dumps(uid, cls=MyJSONEncoder)
        print(json_str)

    def test_2(self):
        d = {
            'uid': uuid.uuid1(),
            'name': 'A',
            'boolean': True,
            'none': None,
            'num': 123,
            'aa': MyClass(1, 2),
        }
        json_str = json.dumps(d, cls=MyJSONEncoder)
        print(json_str)
