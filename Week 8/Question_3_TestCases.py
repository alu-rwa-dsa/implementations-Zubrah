import unittest
from Week_8.Question_3 import *
from Week_8.Question_3 import Max_Height


class MyTestCase(unittest.TestCase):
    def test_equal(self):
        Root = Node(1)
        Root.left = Node(2)
        Root.right = Node(3)
        Root.left.left = Node(4)
        Root.left.right = Node(5)
        self.assertEqual(Max_Height(Root), 3)

    def test_Case_2(self):
        Case_2 = Node(1)
        Case_2.left = Node(2)
        Case_2.right = Node(3)
        Case_2.left.left = Node(4)
        Case_2.left.right = Node(5)
        Case_2.left.left.left = Node(6)
        Case_2.left.left.right = Node(7)
        Case_2.left.right.left = Node(5)
        Case_2.left.right.right = Node(5)
        self.assertEqual(Max_Height(Root), 3)

    def test_Case_3(self):
        Case_2 = Node(1)
        Case_2.left = Node(2)
        Case_2.right = Node(3)
        Case_2.left.left = Node(4)
        Case_2.left.right = Node(5)
        Case_2.right.left = Node(6)
        Case_2.right.right = Node(7)
        Case_2.left.left.left = Node(8)
        Case_2.left.left.right = Node(9)
        Case_2.left.right.left = Node(10)
        Case_2.left.right.right = Node(11)
        Case_2.right.left.left = Node(12)
        Case_2.right.left.right = Node(13)
        Case_2.right.right.left = Node(14)
        Case_2.right.right.right = Node(15)
        self.assertEqual(Max_Height(Case_2), 4)

    def test_Not_equal(self):
        Case_3 = Node(1)
        Case_3.left = Node(2)
        Case_3.right = Node(3)
        Case_3.left.left = Node(4)
        Case_3.left.right = Node(5)
        self.assertNotEqual(Max_Height(Case_3), 8)

    def test_for_Negative(self):
        Case_4 = Node(-10)
        Case_4.left = Node(2)
        Case_4.right = Node(-3)
        Case_4.left.left = Node(-6)
        Case_4.left.right = Node(-7)
        self.assertEqual(Max_Height(Case_4), 3)


if __name__ == '__main__':
    unittest.main()
