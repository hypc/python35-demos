from unittest import TestCase

import base64


class Base64Test(TestCase):
    def setUp(self):
        super(Base64Test, self).setUp()

    def test(self):
        src = '&'.join([
            'MERFLAG=1',
            'MERCHANTID=105000000000000',
            'POSID=000000000',
            'TERMNO1=',
            'TERMNO2=',
            'BRANCHID=110000000',
            'ORDERID=105000000000000123456',
            'QRCODE=CCB9991234567',
            'AMOUNT=0.01',
            'TXCODE=PAY100',
        ])
        bs1 = src.encode('utf-16-be')
        bs2 = b'\xFE\xFF' + bs1
        [print(_, end=' ') for _ in bs1]
        print('\n')
        [print(_, end=' ') for _ in bs2]
        print('\n')
        bs1s = base64.b64encode(bs1).decode()
        print(bs1s)
        self.assertEqual(base64.b64decode(bs1s.encode()), bs1)
        print('\n')
        bs2s = base64.b64encode(bs2).decode()
        print(bs2s)
        self.assertEqual(base64.b64decode(bs2s.encode()), bs2)
