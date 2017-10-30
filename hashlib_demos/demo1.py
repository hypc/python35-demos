import hashlib
import unittest


class HashlibTest(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def test_md5(self):
        s = '123456'
        hash_data = hashlib.md5(s.encode())
        print(hash_data.hexdigest())

    def test_sha1(self):
        s = '123456'
        hash_data = hashlib.sha1(s.encode())
        print(hash_data.hexdigest())

    def test_sha224(self):
        s = '123456'
        hash_data = hashlib.sha224(s.encode())
        print(hash_data.hexdigest())

    def test_sha256(self):
        s = '123456'
        hash_data = hashlib.sha256(s.encode())
        print(hash_data.hexdigest())

    def test_sha384(self):
        s = '123456'
        hash_data = hashlib.sha384(s.encode())
        print(hash_data.hexdigest())

    def test_sha512(self):
        s = '123456'
        hash_data = hashlib.sha512(s.encode())
        print(hash_data.hexdigest())


if __name__ == '__main__':
    unittest.main()
