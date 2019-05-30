import base64
import uuid
from unittest import TestCase


class Base64Test(TestCase):
    def setUp(self):
        super(Base64Test, self).setUp()

    def test(self):
        a = uuid.uuid1().hex
        print(a)
        b = base64.b64encode(bytes.fromhex(a))
        print(b)
        c = base64.b64decode(b)
        print(hex(int.from_bytes(c, 'big'))[2:])
