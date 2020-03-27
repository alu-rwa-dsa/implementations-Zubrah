import unittest
from Week_8.Question_1 import *


# tree = fromData2Tree(data2)
# print(tree)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        data_1 = [[10, 11, 12], [1, 2, 3], [0, 4, 5], [0, 0, 6]]
        self.assertNotEqual(fromData2Tree(data_1), "[10 (L:[11 (L:[12] | R:[3]] | R:[2 (L:[3] | R:[5]]] ")

    def test_Case_2(self):
        data_2 = [[1, 2, 3], [0, 4, 5], [0, 0, 6]]
        self.assertIsNot(fromData2Tree(data_2), "[1 (L:[2 (L:[3] | R:[5]] | R:[4 (L:[5] | R:[6]]]")

    def test_Case_3(self):
        data_3 = [[10, 20, 30], [-10, 40, -5], [-9, -10, -11]]
        self.assertNotEqual(fromData2Tree(data_3), "[10 (L:[20 (L:[30] | R:[-5]] | R:[40 (L:[-5] | R:[-11]]]")


if __name__ == '__main__':
    unittest.main()
