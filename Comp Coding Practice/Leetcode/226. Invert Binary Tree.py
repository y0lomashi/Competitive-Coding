# Invert a binary tree.
# Leetcode: https://leetcode.com/problems/invert-binary-tree/
# Use recursive Depth First Search to invert the tree.

from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)
        print (root.val)
        return root


# ! for testing
tree = Solution()
tree.invertTree(root=TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)),
                              TreeNode(7, TreeNode(6), TreeNode(9))))
