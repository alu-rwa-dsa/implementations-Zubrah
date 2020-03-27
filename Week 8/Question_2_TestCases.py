import unittest
from Week_8.Question_2 import BinaryTreeClasses


class TestMyTestCases(unittest.TestCase):
    def setUp(self):
        self.BinaryTree = BinaryTreeClasses()

    def test_insert(self):
        self.assertEqual([], self.BinaryTree.inorder())
        self.assertEqual(True, self.BinaryTree.insert(5))
        self.assertEqual(False, self.BinaryTree.insert(5))
        self.assertEqual([5], self.BinaryTree.inorder())
        self.assertEqual(True, self.BinaryTree.insert(4))
        self.assertEqual([4, 5], self.BinaryTree.inorder())
        self.assertEqual(True, self.BinaryTree.insert(7))
        self.assertEqual([4, 5, 7], self.BinaryTree.inorder())

    def test_find(self):
        self.assertEqual(False, self.BinaryTree.find(5))
        self.BinaryTree.insert(5)
        self.assertEqual(True, self.BinaryTree.find(5))
        self.assertEqual(False, self.BinaryTree.find(12))
        self.BinaryTree.insert(12)
        self.assertEqual(True, self.BinaryTree.find(5))
        self.assertEqual(True, self.BinaryTree.find(12))
        self.BinaryTree.remove(12)
        self.assertEqual(True, self.BinaryTree.find(5))
        self.assertEqual(False, self.BinaryTree.find(12))
        self.BinaryTree.remove(5)
        self.assertEqual(False, self.BinaryTree.find(5))

    def test_remove_1(self):
        # Empty tree
        self.assertEqual(False, self.BinaryTree.remove(5))

    def test_remove_2_1(self):
        # Value in root
        #  Leaf node
        self.BinaryTree.insert(5)
        self.assertEqual(True, self.BinaryTree.remove(5))
        self.assertEqual([], self.BinaryTree.inorder())

    def test_remove_2_2(self):
        #  Left child only
        self.BinaryTree.insert(5)
        self.BinaryTree.insert(4)
        self.BinaryTree.insert(3)
        self.assertEqual(5, self.BinaryTree.root.data)
        self.assertEqual([3, 4, 5], self.BinaryTree.inorder())
        self.assertEqual(True, self.BinaryTree.remove(5))
        self.assertEqual([3, 4], self.BinaryTree.inorder())
        self.assertEqual(4, self.BinaryTree.root.data)

    def test_remove_2_3(self):
        # Right child only
        self.BinaryTree.insert(5)
        self.BinaryTree.insert(7)
        self.BinaryTree.insert(6)
        self.assertEqual(5, self.BinaryTree.root.data)
        self.assertEqual([5, 6, 7], self.BinaryTree.inorder())
        self.assertEqual(True, self.BinaryTree.remove(5))
        self.assertEqual([6, 7], self.BinaryTree.inorder())
        self.assertEqual(7, self.BinaryTree.root.data)

    def test_remove_2_4(self):
        #  Both children
        self.BinaryTree.insert(5)
        self.BinaryTree.insert(4)
        self.BinaryTree.insert(8)
        self.BinaryTree.insert(7)
        self.BinaryTree.insert(6)
        self.assertEqual(5, self.BinaryTree.root.data)
        self.assertEqual([4, 5, 6, 7, 8], self.BinaryTree.inorder())
        self.assertEqual(True, self.BinaryTree.remove(5))
        self.assertEqual([4, 6, 7, 8], self.BinaryTree.inorder())
        self.assertEqual(6, self.BinaryTree.root.data)

    def test_remove_3(self):
        # Value not in tree
        self.BinaryTree.insert(5)
        self.BinaryTree.insert(4)
        self.BinaryTree.insert(8)
        self.BinaryTree.insert(7)
        self.BinaryTree.insert(6)
        self.assertEqual(False, self.BinaryTree.remove(100))

    def test_remove_4(self):
        # Node is leaf
        self.BinaryTree.insert(5)
        self.BinaryTree.insert(4)
        self.assertEqual(True, self.BinaryTree.remove(4))
        self.assertEqual([5], self.BinaryTree.inorder())

    def test_remove_5(self):
        # Node has left child only
        self.BinaryTree.insert(5)
        self.BinaryTree.insert(4)
        self.BinaryTree.insert(8)
        self.BinaryTree.insert(7)
        self.BinaryTree.insert(6)
        self.assertEqual(True, self.BinaryTree.remove(8))
        self.assertEqual([4, 5, 6, 7], self.BinaryTree.inorder())
        self.assertEqual(7, self.BinaryTree.root.right.data)

    def test_remove_6(self):
        # Node has right child only
        self.BinaryTree.insert(5)
        self.BinaryTree.insert(3)
        self.BinaryTree.insert(4)
        self.assertEqual(True, self.BinaryTree.remove(3))
        self.assertEqual([4, 5], self.BinaryTree.inorder())
        self.assertEqual(4, self.BinaryTree.root.left.data)

    def test_remove_7(self):
        # Node has left and right child
        self.BinaryTree.insert(5)
        self.BinaryTree.insert(3)
        self.BinaryTree.insert(4)
        self.BinaryTree.insert(1)
        self.assertEqual(True, self.BinaryTree.remove(3))
        self.assertEqual([1, 4, 5], self.BinaryTree.inorder())
        self.assertEqual(4, self.BinaryTree.root.left.data)

    def test_preorder(self):
        self.BinaryTree.insert(5)
        self.BinaryTree.insert(4)
        self.BinaryTree.insert(8)
        self.BinaryTree.insert(7)
        self.BinaryTree.insert(6)
        self.BinaryTree.insert(9)
        self.assertEqual([5, 4, 8, 7, 6, 9], self.BinaryTree.preorder())

    def test_postorder(self):
        self.BinaryTree.insert(5)
        self.BinaryTree.insert(4)
        self.BinaryTree.insert(8)
        self.BinaryTree.insert(7)
        self.BinaryTree.insert(6)
        self.BinaryTree.insert(9)
        self.assertEqual([4, 6, 7, 9, 8, 5], self.BinaryTree.postorder())

    def test_inorder(self):
        self.BinaryTree.insert(5)
        self.BinaryTree.insert(4)
        self.BinaryTree.insert(8)
        self.BinaryTree.insert(7)
        self.BinaryTree.insert(6)
        self.BinaryTree.insert(9)
        self.assertEqual([4, 5, 6, 7, 8, 9], self.BinaryTree.inorder())
