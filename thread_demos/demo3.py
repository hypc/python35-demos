"""
对于IO密集型的业务，普通顺序执行效率最差，而ThreadPool与ProcessPool差别不大

建议：当遇到IO密集型的业务时，推荐使用多线程而不是多进程
"""
from datetime import datetime
from multiprocessing.pool import ThreadPool
from multiprocessing import Pool as ProcessPool

import requests


def fun(*args):
    requests.get('https://www.baidu.com')


def main1(p=10):
    for _ in range(p):
        fun(32)


def main2(p=10):
    pool = ThreadPool(p)
    pool.map(fun, (None,) * p)
    pool.close()
    pool.join()


def main3(p=10):
    pool = ProcessPool(p)
    pool.map(fun, (None,) * p)
    pool.close()
    pool.join()


if __name__ == '__main__':
    _num = 10

    start_time = datetime.now()
    main1(_num)
    end_time = datetime.now()
    print((end_time - start_time).total_seconds())

    start_time = datetime.now()
    main2(_num)
    end_time = datetime.now()
    print((end_time - start_time).total_seconds())

    start_time = datetime.now()
    main3(_num)
    end_time = datetime.now()
    print((end_time - start_time).total_seconds())
