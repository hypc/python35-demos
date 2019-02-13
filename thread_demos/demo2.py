"""
对于计算密集型的业务，普通顺序执行与ThreadPool区别不大，ProcessPool效率最好

建议：遇到计算密集型的业务时，可使用多进程
"""
from datetime import datetime
from multiprocessing.pool import ThreadPool
from multiprocessing import Pool as ProcessPool


def fib(n):
    if n in (0, 1):
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def main1(p=10):
    for _ in range(p):
        fib(32)


def main2(p=10):
    pool = ThreadPool(p)
    pool.map(fib, (32,) * p)
    pool.close()
    pool.join()


def main3(p=10):
    pool = ProcessPool(p)
    pool.map(fib, (32,) * p)
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
