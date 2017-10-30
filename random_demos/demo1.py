import random
import string
import unittest


class RandomTest(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def test_random_str(self):
        letters = string.ascii_letters + string.digits
        print(''.join(random.sample(letters, 10)))

    def test_random_char(self):
        letters = string.ascii_letters + string.digits
        print(random.choice(letters))

if __name__ == '__main__':
    unittest.main()
