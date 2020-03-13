import unittest
from Week_7.Question_3a import *

alist = [30, 20, 90, 70, 2000, 10, 50, 80, 100, 1010]
list_to_sort = [19, 2, 31, 45, 6, 11, 121, 27]
Implementation = bubble_sort(list_to_sort)


class MyTestCase(unittest.TestCase):
    def test_Equality(self):
        self.assertEqual(Implementation, [2, 6, 11, 19, 27, 31, 45, 121])

    def test_negative(self):
        a_list = [30, 20, 90, 70, 2000, 10, 50, 80, 100, 1010]
        test_1 = bubble_sort(a_list)
        self.assertEqual(test_1, [10, 20, 30, 50, 70, 80, 90, 100, 1010, 2000])

    def test_for_negative(self):
        test_2 = bubble_sort([10, -15, 56, 34, 12, -13, -5])
        self.assertEqual(test_2, [-15, -13, -5, 10, 12, 34, 56])

    def test_String_element(self):
        test_3 = bubble_sort(['Mambo', 'Ugali', 'Mwanzo', 'First'])
        self.assertEqual(test_3, ['First', 'Mambo', 'Mwanzo', 'Ugali'])


if __name__ == '__main__':
    unittest.main()
