import uuid
from unittest import TestCase

from base58.base58 import Base58


class Base58Test(TestCase):
    def setUp(self):
        super(Base58Test, self).setUp()

    def test(self):
        a = uuid.uuid1().hex.encode()
        print(a)
        b = Base58.b58encode(a)
        print(b)
        c = Base58.b58decode(b)
        print(c)

    def test2(self):
        a = uuid.uuid1().hex
        print(a)
        b = Base58.b58encode(bytes.fromhex(a))
        print(b)
        c = Base58.b58decode(b)
        print(hex(int.from_bytes(c, 'big'))[2:])    # 前面补0

    def test3(self):
        a = uuid.uuid1().hex
        print(a)
        b = Base58.b58encode_int(int(a, base=16))
        print(b)
        c = Base58.b58decode_int(b)
        print(hex(c)[2:])   # 前面补0
