import logging
from logging.handlers import SysLogHandler
import unittest


class Test(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.format = '[%(asctime)s] [%(process)d] [%(levelname)s] [%(name)s] %(message)s'
        self.datefmt = '%Y-%m-%d %H:%M:%S %z'

    def test1(self):
        logging.basicConfig(level='DEBUG',
                            format=self.format,
                            datefmt=self.datefmt,
                            handlers=[SysLogHandler()])
        logger = logging.getLogger()
        logger.debug('this is debug level')
        logger.info('this is info level')
        logger.warn('this is warn level')
        logger.error('this is error level')


if __name__ == '__main__':
    unittest.main()
