import importlib
import unittest
from time import sleep


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

    def test2(self):
        for _ in range(10):
            module_spec = importlib.util.find_spec('import_demos.configs')
            module = importlib.util.module_from_spec(module_spec)
            module_spec.loader.exec_module(module)
            print(module.CONFIG_1)
            sleep(5)


if __name__ == '__main__':
    unittest.main()
