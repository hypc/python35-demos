import re
from unittest import TestCase


class ReTest(TestCase):
    def setUp(self):
        super(ReTest, self).setUp()

    def test(self):
        regex = re.compile('parkings/(?P<parking_id>\w+)')
        self.assertTrue('parkings/(?P<parking_id>\\w+)', regex.pattern)
        regex2 = re.compile(regex.pattern)
        self.assertTrue('parkings/(?P<parking_id>\\w+)', regex2.pattern)
