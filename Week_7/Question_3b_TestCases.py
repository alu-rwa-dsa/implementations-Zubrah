import unittest
from Week_7.Question_3b import *

unsorted_list = [64, 34, 25, 12, 22, 11, 90]


class MyTestCase(unittest.TestCase):
    def test_Equality(self):
        self.assertEqual(merge_sort(unsorted_list), [11, 12, 22, 25, 34, 64, 90])

    def test_not_empty(self):
        self.assertIsNotNone(merge_sort(unsorted_list), [11, 12, 22, 25, 34, 64, 90])

    def test_not_Equal(self):
        list_to_test = [11, 90, 45, 34, 89, 23]
        self.assertNotEqual(merge_sort(list_to_test), [11, 12, 22, 25, 34, 64, 90])

    def test_for_negative_values(self):
        test = [-12, 45, 67, 13, -34, 567]
        self.assertEqual(merge_sort(test), [-34, -12, 13, 45, 67, 567])


if __name__ == '__main__':
    unittest.main()
