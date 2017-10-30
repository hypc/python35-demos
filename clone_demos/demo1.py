import unittest

import copy


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def test_1(self):
        """浅拷贝--基础类型"""
        origin = [1, 2, 3, 4]
        backup = copy.copy(origin)
        self.assertEqual(origin, backup)
        self.assertNotEqual(id(origin), id(backup))

    def test_2(self):
        """浅拷贝--基础类型"""
        origin = {'a': 1, 'b': 2}
        backup = copy.copy(origin)
        self.assertEqual(origin, backup)
        self.assertNotEqual(id(origin), id(backup))

    def test_3(self):
        """浅拷贝--list or dict or tuple"""
        origin = [[1], {'a': 1}, (1, 2)]
        backup = copy.copy(origin)
        self.assertEqual(origin, backup)
        self.assertNotEqual(id(origin), id(backup))
        for i in range(len(origin)):
            self.assertEqual(origin[i], backup[i])
            self.assertEqual(id(origin[i]), id(backup[i]))

    def test_4(self):
        """深拷贝"""
        origin = [[1], {'a': 1}, (1, 2)]
        backup = copy.deepcopy(origin)
        self.assertEqual(origin, backup)
        self.assertNotEqual(id(origin), id(backup))
        self.assertEqual(origin[0], backup[0])
        self.assertNotEqual(id(origin[0]), id(backup[0]))


if __name__ == '__main__':
    unittest.main()
