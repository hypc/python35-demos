import unittest
from functools import cmp_to_key
from operator import itemgetter


class Test(unittest.TestCase):

    def test_sort(self):
        a = [
            {'a': 10, 'b': 2, 'c': 1},
            {'a': 9, 'b': 2, 'c': 3},
            {'a': 10, 'b': 1, 'c': 2},
            {'a': 9, 'b': 1, 'c': 4},
        ]

        def _cmp(x, y):
            if x['a'] != y['a']:
                return y['a'] - x['a']
            elif x['b'] != y['b']:
                return x['b'] - y['b']
            else:
                return False

        a.sort(key=cmp_to_key(_cmp))
        print(a)
        a.sort(key=itemgetter('a', 'b'), reverse=True)
        print(a)


if __name__ == '__main__':
    unittest.main()
