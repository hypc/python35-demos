import unittest
from unittest.case import skip


def index_of(seq, value, key=None):
    if not key:
        try:
            return seq.index(value)
        except:
            return -1

    for index in range(len(seq)):
        if seq[index][key] == value:
            return index
    return -1


class Test(unittest.TestCase):

    def test_1(self):
        a = [1, 2, 3, 4]
        print(index_of(a, 1))
        print(index_of(a, 5))

    @skip('')
    def test_2(self):
        a = [{'id': 1}, {'id': 2}]
        print(index_of(a, 2, 'id'))


if __name__ == '__main__':
    unittest.main()
