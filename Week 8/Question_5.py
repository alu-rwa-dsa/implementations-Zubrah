"""
Time Complexity and Space Complexity:
The time Complexity  to traverse to all node and create a new list of the specific order will take O(n) amd the
space complexity will take also O(n) as it creates a new array of elements in a specified order.
"""


# tree.py: tree using lists
import sys


def treeInsert(s, a):
    if not s:  # first time through
        s.append(a)
        s.append([])
        s.append([])
    else:
        while True:
            if a == s[0]:  # found
                return 1
            elif a < s[0]:  # left
                if not s[1]:
                    # not found, insert
                    s[1] = [a, [], []]
                    return 0
                else:
                    s = s[1]  # go left
            elif a > s[0]:  # right
                if not s[2]:
                    # not found, insert
                    s[2] = [a, [], []]
                    return 0
                else:
                    s = s[2]  # go right


def binarySearchTree(m):
    r = []  # build tree from scratch
    for i in range(0, len(m)):
        stat = treeInsert(r, m[i])
    return r


def inorderTraversal(s):
    if s[1]:  # left subtree
        inorderTraversal(s[1])
    sys.stdout.write(str(s[0]) + " ")
    if s[2]:  # right subtree
        inorderTraversal(s[2])


def process(m):
    sys.stdout.write("INPUT DATA:        " + str(m) + '\n')
    r = binarySearchTree(m)
    sys.stdout.write("TREE :    " + str(r) + '\n')
    sys.stdout.write("IN- ORDER TRAVERSAL: ")
    inorderTraversal(r)
    sys.stdout.write("\n\n")




