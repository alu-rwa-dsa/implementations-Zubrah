import unittest
from Week_7.Question_1 import *

testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]


class MyTestCases(unittest.TestCase):
    def test_equality(self):
        self.assertEqual(Search(testlist, 3), False)

    def test_not_available(self):
        self.assertEqual(Search(testlist, -1), False)

    def test_for_notNone(self):
        self.assertIsNotNone(Search(testlist, -1), False)

    def test_for_negative(self):
        self.assertEqual(Search(testlist, -10), False)


if __name__ == '__main__':
    unittest.main()
