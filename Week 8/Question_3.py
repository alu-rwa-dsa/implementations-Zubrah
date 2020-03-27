"""
The time Complexity to run the algorithm is O(n) as it moves through all the nodes and count the
levels associated with them
The Space complexity will be O(1) as it doesn't add anything the overall memory.
"""


# define a binary tree node
class Node:
    # Constructor for data
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# define a Maximum Height func
def Max_Height(node):
    if node is None:
        return 0
    else:
        Left_Height = Max_Height(node.left)
        Right_Height = Max_Height(node.right)
        # compare the right and left nodes and add on either side 
        if Left_Height > Right_Height:
            return Left_Height + 1
        else:
            return Right_Height + 1


Root = Node(1)
Root.left = Node(2)
Root.right = Node(3)
Root.left.left = Node(4)
Root.left.right = Node(5)

print(Max_Height(Root))
