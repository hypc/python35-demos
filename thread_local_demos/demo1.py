"""
线程局部变量

先使用threading.local创建一个全局变量，然后在线程中直接引用，
每个线程引用变量都是不同的，达到线程隔离的目的。

注意：需要警惕的是，在使用线程池的时候，可能会复用线程，这样将无法达到使用线程局部变量的目的。
还有就是，在使用协程的时候，也服务达到变量隔离的目的。
"""
import threading
from multiprocessing.pool import ThreadPool
from unittest import TestCase

import time

global_data = threading.local()


def func():
    if not hasattr(global_data, 'num'):
        global_data.num = 0
    for _ in range(1000000):
        global_data.num += 1
    print(threading.current_thread().getName(), global_data.num)


class ThreadLocalTestCase(TestCase):
    def setUp(self):
        super(ThreadLocalTestCase, self).setUp()

    def test_1(self):
        for _ in range(20):
            thread = threading.Thread(target=func)
            thread.start()
        time.sleep(10)

    def test_2(self):
        pool = ThreadPool(10)
        for _ in range(20):
            pool.apply_async(func)
        pool.close()
        pool.join()
