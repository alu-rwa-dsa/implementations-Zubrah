import unittest
from Week_8.Question_4 import *


class MyTestCase(unittest.TestCase):
    def test_Case_1(self):
        root = Node(27)
        root.insert(14)
        root.insert(35)
        root.insert(10)
        root.insert(19)
        root.insert(31)
        root.insert(42)
        self.assertEqual(root.PreOrderTraversal(root), [27, 14, 10, 19, 35, 31, 42])

    def test_Case_2(self):
        Case_2 = Node(27)
        Case_2.insert(14)
        Case_2.insert(35)
        Case_2.insert(10)
        Case_2.insert(19)
        Case_2.insert(31)
        Case_2.insert(42)
        self.assertEqual(root.InOrderTraversal(Case_2), [10, 14, 19, 27, 31, 35, 42])
        self.assertEqual(root.PostOrderTraversal(Case_2), [10, 19, 14, 31, 42, 35, 27])

    def test_Case_3(self):
        Case_3 = Node(-12)
        Case_3.insert(-20)
        Case_3.insert(-56)
        Case_3.insert(-10)
        Case_3.insert(12)
        Case_3.insert(-13)
        self.assertEqual(root.InOrderTraversal(Case_3), [-56, -20, -13, -12, -10, 12])
        self.assertEqual(root.PostOrderTraversal(Case_3), [-56, -13, -20, 12, -10, -12])
        self.assertEqual(root.PreOrderTraversal(Case_3), [-12, -20, -56, -13, -10, 12])

    def test_Case_4(self):
        Case_4 = Node(-12)
        Case_4.insert(-20)
        Case_4.insert(-56)
        Case_4.insert(-10)
        Case_4.insert(12)
        Case_4.insert(-13)
        self.assertNotEqual(root.InOrderTraversal(Case_4), [-56, -20, -13, -12, -10, 13])
        self.assertNotEqual(root.PostOrderTraversal(Case_4), [-56, -13, -20, 12, -10, -18])
        self.assertNotEqual(root.PreOrderTraversal(Case_4), [-12, -20, -56, -13, -10, 17])


if __name__ == '__main__':
    unittest.main()
