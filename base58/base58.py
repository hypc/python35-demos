class Base58Exception(Exception):
    """"""
    pass


class Base58UnknowAlgorithmException(Base58Exception):
    """"""
    pass


class Alphabet(object):
    def __init__(self, alphabet):
        """
        :type alphabet: str
        """
        if len(alphabet) != 58:
            raise Base58UnknowAlgorithmException()

        self.alphabet = scrub_input(alphabet)

    def index(self, v):
        """
        :type v: str | bytes
        :rtype: int
        """
        v = scrub_input(v)
        return self.alphabet.index(v)

    def __getitem__(self, y):
        return self.alphabet[y]

    def __len__(self):
        return len(self.alphabet)


def scrub_input(s):
    """
    :param s:
    :type s: str | bytes
    :return:
    :rtype: bytes
    """
    if isinstance(s, str) and not isinstance(s, bytes):
        s = s.encode('ascii')
    return s


class Base58(object):
    alphabets = (
        ('bitcoin', Alphabet(
            '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz')),
        ('ipfs', Alphabet(
            '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz')),
        ('flickr', Alphabet(
            '123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ')),
        ('ripple', Alphabet(
            'rpshnaf39wBUDNEGHJKLM4PQRST7VWXYZ2bcdeCg65jkm8oFqi1tuvAxyz')),
    )

    @classmethod
    def alphabet(cls, algorithm='bitcoin'):
        for al in cls.alphabets:
            if al[0] == algorithm:
                return al[1]

        raise Base58UnknowAlgorithmException()

    @classmethod
    def b58encode(cls, s, algorithm='bitcoin'):
        """
        base58编码
        :param s: 待编码的字符串
        :type s: str | bytes
        :param algorithm: 算法，值可以是 bitcoin、ipfs、flickr、ripple
        :type algorithm: str
        :return: 编码之后的字节数组
        :rtype: bytes
        """
        s = scrub_input(s)

        alphabet = cls.alphabet(algorithm=algorithm)
        origin_len = len(s)
        s = s.lstrip(b'\0')
        pre_result = alphabet[0:1] * (origin_len - len(s))

        acc = int.from_bytes(s, 'big')
        result = cls.b58encode_int(acc, algorithm=algorithm)

        return pre_result + result

    @classmethod
    def b58encode_int(cls, i, algorithm='bitcoin'):
        """
        将10进制数字转成58进制字节数组
        :type i: int
        :param algorithm: 算法，值可以是 bitcoin、ipfs、flickr、ripple
        :type algorithm: str
        :return: 编码之后的字节数组
        :rtype: bytes
        """
        alphabet = cls.alphabet(algorithm=algorithm)
        if i == 0:
            return alphabet[0:1]
        string = b''
        while i > 0:
            i, idx = divmod(i, 58)
            string = alphabet[idx:idx + 1] + string
        return string

    @classmethod
    def b58decode(cls, s, algorithm='bitcoin'):
        """
        base58反编码
        :param s: 待反编码的字符串
        :type s: str | bytes
        :param algorithm: 算法，值可以是 bitcoin、ipfs、flickr、ripple
        :type algorithm: str
        :return: 反编码之后的字节数组
        :rtype: bytes
        """
        s = s.rstrip()
        s = scrub_input(s)

        alphabet = cls.alphabet(algorithm=algorithm)
        origin_len = len(s)
        s = s.lstrip(alphabet[0:1])
        pre_result = b'\0' * (origin_len - len(s))

        acc = cls.b58decode_int(s)
        result = []
        while acc > 0:
            acc, mod = divmod(acc, 256)
            result.append(mod)

        return pre_result + bytes(reversed(result))

    @classmethod
    def b58decode_int(cls, s, algorithm='bitcoin'):
        """
        将58进制字符串转成10进制数字
        :type s: str | bytes
        :param algorithm: 算法，值可以是 bitcoin、ipfs、flickr、ripple
        :type algorithm: str
        :return: 反编码之后的字节数组
        :rtype: int
        """
        s = s.rstrip()
        s = scrub_input(s)

        alphabet = cls.alphabet(algorithm=algorithm)
        decimal = 0
        for char in s:
            decimal = decimal * 58 + alphabet.index(char)
        return decimal
