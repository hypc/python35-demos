import unittest
from unittest.case import skip

from Crypto.PublicKey import RSA

from rsa_demos.rsa import RSAUtils


class TestRSAUtils(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        key = RSA.generate(2048)
        self.public_key = key.publickey().exportKey()
        self.private_key = key.exportKey()
        print(self.public_key)
        print(self.private_key)

    @skip('')
    def test_sign(self):
        message = b'1234'
        sign = RSAUtils.sign(message, self.private_key)
        print(sign)

    @skip('')
    def test_verify(self):
        message = b'1234'
        sign = RSAUtils.sign(message, self.private_key)
        verify = RSAUtils.verify(message, sign, self.public_key)
        print(verify)

    @skip('')
    def test_encrypt(self):
        message = b'1234'
        ciphertext = RSAUtils.encrypt(message, self.public_key)
        print(ciphertext)

    def test_decrypt(self):
        message = b'1234'
        ciphertext = RSAUtils.encrypt(message, self.public_key)
        message2 = RSAUtils.decrypt(ciphertext, self.private_key)
        print(message2)

if __name__ == '__main__':
    unittest.main()
