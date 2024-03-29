
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root.left is None and root.right is None:
            return root.val
        start = str(root.val)
        return self.dfs(root.left, start) + self.dfs(root.right, start)

    def dfs(self, node, run):
        if node is None:
            return 0
        add = run + str(node.val)
        if node.left is None and node.right is None:
            return int(add)
        return self.dfs(node.left, add) + self.dfs(node.right, add)


# ! for testing
root = TreeNode(4)
root.left = TreeNode(9)
root.right = TreeNode(0)
root.left.left = TreeNode(5)
root.left.right = TreeNode(1)
print(Solution().sumNumbers(root))
