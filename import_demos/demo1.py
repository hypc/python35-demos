import importlib
import unittest


class Test(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def test1(self):
        s = 'import_demos.configs.CONFIG_1'
        module, name = s.rsplit('.', 1)
        config_1 = getattr(importlib.import_module(module), name)
        print(config_1)

        s = 'import_demos.configs'
        module, name = s.rsplit('.', 1)
        configs = getattr(importlib.import_module(module), name)
        print(configs)
        print(configs.CONFIG_1)


if __name__ == '__main__':
    unittest.main()
