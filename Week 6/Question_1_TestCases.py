import unittest
from Question_1 import *

searchValues = LinkedList()
searchValues.push(5)
searchValues.push(12)
searchValues.push(23)
searchValues.push(13)


class MyTestCase(unittest.TestCase):
    # test for equality
    def test_equal(self):
        self.assertEqual(searchValues.searching_value(21), False)

    # test for StringInput
    def test_StringInput(self):
        self.assertEqual(searchValues.searching_value("Mambo"), False)

    # Test for alphanumeric
    def test_Alphanumeric(self):
        self.assertIsNotNone(searchValues.searching_value(1213), False)

    # test for known available number
    def test_number(self):
        self.assertTrue(searchValues.searching_value(12), True)

    def test_push(self):
        self.assertNotEqual(searchValues.push(13), 45)


if __name__ == '__main__':
    unittest.main()
