import unittest
from Week_9.Question_1 import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        test_1 = [90, 15, 10, 7, 12, 2, 7, 3]
        self.assertEqual(isHeap(test_1), True)

    def test_case_2(self):
        test_2 = [9, 5, 0, 1, 2, 20, 17, 30]
        self.assertEqual(isHeap(test_2), False)

    def test_case_3(self):
        test_3 = [-90, -15, -10, -7, -12, -2, -7, -3]
        self.assertEqual(isHeap(test_3), False)

    def test_case_4(self):
        tets_4 = [9, -15, 10, 7, 12, 2, 7, 3]
        self.assertEqual(isHeap(tets_4), False)

    def test_case_5(self):
        test_5 = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(isHeap(test_5), False)


if __name__ == '__main__':
    unittest.main()
