import unittest

from PIL import Image


class PillowTest(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_1(self):
        im = Image.open("0ac871ea1292419ba2268498ca8836e3.jpg")
        print(im.format, im.size, im.mode)
        im.show()


if __name__ == '__main__':
    unittest.main()
