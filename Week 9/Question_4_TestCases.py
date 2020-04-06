import unittest
from Week_9.Question_4 import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        arr = [2, 5, 3, 8, 6, 5, 4, 7]
        heapSort(arr)
        n = len(arr)
        for i in range(n):
            print(arr[i], end=" ")
        self.assertEqual(heapSort(arr), None)

    def test_case_2(self):
        global i
        mambo = [1, 5, 9, 6, 10]
        heapSort(mambo)
        n = len(mambo)
        for i in range(n):
            print(mambo[i], end=" ")
        self.assertEqual(heapSort(mambo), None)

    def test_case_3(self):
        case_3 = [-2, -5, -3, -8, -6, -5, -4, -7]
        heapSort(case_3)
        n = len(case_3)
        for i in range(n):
            print(case_3[i], end=" ")
        self.assertEqual(heapSort(case_3), None)

if __name__ == '__main__':
    unittest.main()
