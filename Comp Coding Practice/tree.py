# create object
class Node:
    """Create a node."""
    # initialize object
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # print tree
    def printTree(self):
        """Print the tree."""
        print(self.data)


root = Node(10)
root.printTree()
