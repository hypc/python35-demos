import unittest
from unittest.case import skip

import pyexcel
from pyexcel_xls.xls import XLSBook


class Test(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    @skip('')
    def test_1(self):
        with open('aa.xlsx', 'rb') as f:
            xlsbook = XLSBook()
            xlsbook.open_content(f.read())
            sheet = xlsbook.read_sheet_by_index(0)
            for key, value in sheet.items():
                print(key, value)
                for _ in value:
                    print(_)

    def test_2(self):
        with open('aa.xlsx', 'rb') as f:
            sheet = pyexcel.get_sheet(file_type='xlsx', file_content=f.read())
            print(sheet)
            print(sheet.array)
            print(sheet.csv)

if __name__ == '__main__':
    unittest.main()
