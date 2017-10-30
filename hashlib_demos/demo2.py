import hashlib
import unittest


class HashlibTest(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def test_file_md5(self):
        hash_data = hashlib.md5()
        data = b''
        with open('demo1.py', 'rb') as f:
            data += f.read()
        hash_data.update(data)
        print(hash_data.hexdigest())

    def test_file_sha256(self):
        hash_data = hashlib.sha256()
        data = b''
        with open('demo1.py', 'rb') as f:
            data += f.read()
        hash_data.update(data)
        print(hash_data.hexdigest())

if __name__ == '__main__':
    unittest.main()
