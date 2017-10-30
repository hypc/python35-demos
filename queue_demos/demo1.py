'''
Queue一般用来作为线程通信的一种技术，
在使用时需要注意，get之后数据会从队列中移除，
若要实现一个生产者对应多个不同类型的消费者，可以在生产者这边按类型创建多个队列，
不同的类型队列对应相应的消费者。
'''
from queue import Queue
from threading import Thread
import time
import unittest


class Test(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self._queue = Queue()

    @classmethod
    def _put_msg(cls, q):
        while True:
            q.put(time.time())
            time.sleep(3)

    @classmethod
    def _get_msg(cls, q, n):
        _ = 0
        while True:
            msg = q.get()
            print(n, _, msg)
            _ += 1

    def test_1(self):
        t = Thread(target=self._put_msg, args=[self._queue])
        t.start()
        time.sleep(10)
        t2 = Thread(target=self._get_msg, args=[self._queue, 2])
        t2.start()
        t3 = Thread(target=self._get_msg, args=[self._queue, 3])
        t3.start()

        time.sleep(1000)

if __name__ == '__main__':
    unittest.main()
