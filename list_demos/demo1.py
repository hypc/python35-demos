from operator import itemgetter
import unittest
from unittest.case import skip


class Test(unittest.TestCase):

    @skip('')
    def test_sort(self):
        a = [1, 4, 5, 7, 2, 567, 23, 45, 22, 678, 234]
        a.sort()
        print(a)  # [1, 2, 4, 5, 7, 22, 23, 45, 234, 567, 678]

        b = [1, 4, 5, 7, 2, 567, 23, 45, 22, 678, 234]
        b.sort(reverse=True)
        print(b)  # [678, 567, 234, 45, 23, 22, 7, 5, 4, 2, 1]

        c = [{'id': 1}, {'id': 23}, {'id': 2}]
        c.sort(key=itemgetter('id'), reverse=False)
        print(c)  # [{'id': 1}, {'id': 2}, {'id': 23}]

        d = []
        d.sort(key=itemgetter('id'), reverse=False)
        print(d)  # []


if __name__ == '__main__':
    unittest.main()
