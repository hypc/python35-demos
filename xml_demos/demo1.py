import unittest
from xml.etree import ElementTree


xmltext = '''
<?test_xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>
'''


def _change_xml_to_dict(element):
    children = element.getchildren()
    if not children:
        return element.text

    dic = {}
    for c in children:
        dic[c.tag] = _change_xml_to_dict(c)
    return dic


def _change_dic_to_xml(dic, root_node):
    root = ElementTree.Element(root_node)
    for key, value in dic.items():
        et = ElementTree.SubElement(root, key)
        et.text = str(value)
    return ElementTree.tostring(root, 'utf-8')


class XmlTest(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_1(self):
        root = ElementTree.fromstring(xmltext)
        print(_change_xml_to_dict(root))

    def test_2(self):
        dic = {
            'country': {
                'neighbor': None,
                'rank': '68',
                'year': '2011',
                'gdppc': '13600'
            }
        }
        print(_change_dic_to_xml(dic, 'countries'))

if __name__ == '__main__':
    unittest.main()
