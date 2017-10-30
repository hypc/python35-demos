# encoding: utf-8
import base64

from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5 as Cipher
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5 as Signature


class RSAUtils(object):

    @classmethod
    def sign(cls, message, private_key):
        h = SHA.new(message)
        signer = Signature.new(RSA.importKey(private_key))
        return base64.b64encode(signer.sign(h)).decode()

    @classmethod
    def verify(cls, message, sign, public_key):
        sign = base64.b64decode(sign)
        h = SHA.new(message)
        verifier = Signature.new(RSA.importKey(public_key))
        return verifier.verify(h, sign)

    @classmethod
    def encrypt(cls, message, public_key):
        cipher = Cipher.new(RSA.importKey(public_key))
        return base64.b64encode(cipher.encrypt(message)).decode()

    @classmethod
    def decrypt(cls, ciphertext, private_key):
        ciphertext = base64.b64decode(ciphertext)
        sentinel = Random.new().read(SHA.digest_size)
        cipher = Cipher.new(RSA.importKey(private_key))
        return cipher.decrypt(ciphertext, sentinel).decode()
