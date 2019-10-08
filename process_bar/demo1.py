from datetime import datetime
from time import sleep


class ProcessBar(object):
    fmt = '\r\033[32m{percent:.2%}\033[0m' \
          ' (\033[32m{cur}\033[0m of \033[31m{total}\033[0m)' \
          ' Time: \033[34m{time}\033[0m' \
          ', Elapsed time: \033[33m{elapsed}\033[0m'

    def __init__(self, total, cur=0):
        self._begin_time = None
        self._total = total
        self._cur = cur

    def print(self, cur):
        if self._begin_time is None:
            self._begin_time = datetime.now()
        dt = datetime.now()
        print(self.fmt.format(**{
            'percent': cur / self._total,
            'cur': cur,
            'total': self._total,
            'elapsed': dt - self._begin_time,
            'time': dt,
        }), end='')

    def begin(self):
        self._begin_time = datetime.now()
        self.print(self._cur)

    def end(self):
        self.print(self._total)
        print()


if __name__ == '__main__':
    p = ProcessBar(123)
    p.begin()
    for i in range(123):
        sleep(0.1)  # process ...
        p.print(i + 1)
    p.end()
