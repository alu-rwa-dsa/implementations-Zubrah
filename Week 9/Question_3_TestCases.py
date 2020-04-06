import unittest
from Week_9.Question_3 import *

Implementation = BinaryHeap()
Implementation.insert(6)
Implementation.insert(7)
Implementation.insert(12)
Implementation.insert(10)
Implementation.insert(4)
Implementation.insert(5)
# print(Implementation.get_max())
# print(Implementation.extract_max())
# print(Implementation.size())
# print(Implementation.max_heapify(2))
# print(Implementation.get_min())
# print(Implementation.extract_min())



class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(Implementation.insert(3), None)

    def test_case_2(self):
        self.assertEqual(Implementation.insert(-6), None)

    def test_case_3(self):
        self.assertEqual(Implementation.size(), 8)

    def test_case_4(self):
        self.assertEqual(Implementation.get_max(), 12)

    def test_case_5(self):
        self.assertEqual(Implementation.extract_max(), 12)

    def test_case_6(self):
        Case_6 = BinaryHeap()
        Case_6.insert(-6)
        Case_6.insert(-7)
        Case_6.insert(2)
        Case_6.insert(100)
        self.assertEqual(Case_6.get_max(), 100)
        self.assertEqual(Case_6.extract_max(), 100)
        self.assertEqual(Case_6.size(), 3)
        self.assertEqual(Case_6.max_heapify(4), None)


if __name__ == '__main__':
    unittest.main()
