# Time Complexity
"""
The time Complexity of  for all traversal is O(n)

# Space Complexity:
The auxiliary space to run the algorithm is O(1) while if we consider the size of stack
would be O(n)
"""


class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    # Insert Node
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # Print the Tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

    def InOrderTraversal(self, root):
        In_Order_Traversal = []
        if root:
            In_Order_Traversal = self.InOrderTraversal(root.left)
            In_Order_Traversal.append(root.data)
            In_Order_Traversal = In_Order_Traversal + self.InOrderTraversal(root.right)
        return  In_Order_Traversal

    def PreOrderTraversal(self, root):
        Pre_Order_Tree = []
        if root:
            Pre_Order_Tree.append(root.data)
            Pre_Order_Tree = Pre_Order_Tree + self.PreOrderTraversal(root.left)
            Pre_Order_Tree = Pre_Order_Tree + self.PreOrderTraversal(root.right)
        return Pre_Order_Tree

    # Post-Order Traversal
    def PostOrderTraversal(self, root):
        Post_Order_Traversal = []

        if root:
            Post_Order_Traversal = self.PostOrderTraversal(root.left)
            Post_Order_Traversal = Post_Order_Traversal + self.PostOrderTraversal(root.right)
            Post_Order_Traversal.append(root.data)
        return Post_Order_Traversal


root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.InOrderTraversal(root))
print(root.PreOrderTraversal(root))
print(root.PostOrderTraversal(root))
