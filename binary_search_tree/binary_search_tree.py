from binary_search_tree_node import BinarySearchTreeNode

""" Binary search tree
Let x be a node in a binary search tree. If y is a node in the left subtree of x, then y.key <= x.key.
If y is a node in the right subtree of x, then y.key >= x.key.
"""

class BinarySearchTree:

    # Init gives you an empty tree
    def __init__(self):
        self.root = None
        self.left = None
        self.right = None

    # display is inorder traversal
    def display(self):
        if self.left is None:
            leftStr = ''
        else:
            leftStr = self.left.display()
        middleStr = str(self.root.key) + '\n'
        if self.right is None:
            rightStr = ''
        else:
            rightStr = self.right.display()
        return leftStr + middleStr + rightStr


    """ Pseudocode for recursive insert
    insert(tree, key):
        if tree is empty - add node
        if newkey > key
            insert(right, key)
        else
            insert(left, key )

    """

    def insert(self, key):

        n = BinarySearchTreeNode(key)

        if self.isEmpty():
            print("self is empty")
            self.root = n
            return
        if key > self.root.key:
            if self.right is None:
                t = BinarySearchTree()
                t.root = n
                self.right = t
            else:
                self.right.insert(key)
        else:
            if self.left is None:
                t = BinarySearchTree()
                t.root = n
                self.left = t
            else:
                self.left.insert(key)

    def isEmpty(self):
        if self.root is None:
            return True
