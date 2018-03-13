import unittest
from unittest.case import skip

from Crypto.PublicKey import RSA

from rsa_demos.rsa import RSAUtils


class TestRSAUtils(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        key = RSA.generate(2048)
        self.private_key, self.public_key = RSAUtils.generate_keys()

    def test_generate(self):
        private_key, public_key = RSAUtils.generate_keys()
        self.assertIsInstance(private_key, str)
        self.assertIsInstance(public_key, str)

    def test_sign(self):
        message = b'1234'
        sign = RSAUtils.sign(message, self.private_key)
        self.assertIsInstance(sign, str)

    def test_sign_2(self):
        message = '1234'
        sign = RSAUtils.sign(message, self.private_key)
        self.assertIsInstance(sign, str)

    def test_verify(self):
        message = b'1234'
        sign = RSAUtils.sign(message, self.private_key)
        verify = RSAUtils.verify(message, sign, self.public_key)
        self.assertIsInstance(verify, bool)
        self.assertTrue(verify)
        verify = RSAUtils.verify(message.decode(), sign.encode(), self.public_key)
        self.assertIsInstance(verify, bool)
        self.assertTrue(verify)

    def test_encrypt(self):
        message = b'1234'
        ciphertext = RSAUtils.encrypt(message, self.public_key)
        self.assertIsInstance(ciphertext, str)
        ciphertext = RSAUtils.encrypt(message.decode(), self.public_key)
        self.assertIsInstance(ciphertext, str)

    def test_decrypt(self):
        message = b'1234'
        ciphertext = RSAUtils.encrypt(message, self.public_key)
        message2 = RSAUtils.decrypt(ciphertext, self.private_key)
        self.assertIsInstance(message2, str)
        message2 = RSAUtils.decrypt(ciphertext.encode(), self.private_key)
        self.assertIsInstance(message2, str)
