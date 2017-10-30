'''
线程间通信Event
'''
from threading import Thread, Event
import time
import unittest


class Test(unittest.TestCase):

    def test_1(self):

        def _(event):
            while True:
                print(time.time())
                event.wait()

        event = Event()
        t = Thread(target=_, args=[event])
        t.start()

        for _ in range(10):
            time.sleep(2)
            event.set()
            event.clear()

        time.sleep(1000)


if __name__ == '__main__':
    unittest.main()
