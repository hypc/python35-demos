import time
import unittest
from unittest.case import skip

import redis


class Test(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    @skip('')
    def test_pub(self):
        r = redis.StrictRedis()
        p = r.pubsub()
        p.subscribe('my-first-channel', 'my-second-channel')
        while True:
            r.publish('my-first-channel', time.time())
            time.sleep(3)

    def test_sub(self):
        r = redis.StrictRedis()
        p = r.pubsub()
        p.psubscribe('my-first-channel')
        for message in p.listen():
            print(message)


if __name__ == '__main__':
    unittest.main()
