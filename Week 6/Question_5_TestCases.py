import unittest
from Question_5 import *

BinarySearch(list_to_test, 30)


class MyTestCase(unittest.TestCase):
    # test for equality
    def test_equality(self):
        self.assertEqual(BinarySearch(list_to_test, 30), True)

    # Test for an element not present in the array
    def test_not_available(self):
        self.assertIs(BinarySearch(list_to_test, 200), False)

    # test for comparison of results
    def test_not_equal(self):
        self.assertTrue(BinarySearch(list_to_test, 30), True)



if __name__ == '__main__':
    unittest.main()
