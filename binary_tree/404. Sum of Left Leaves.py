"""
Given the root of a binary tree, return the sum of all left leaves.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode, isLeft=False) -> int:
        if not root: return 0
        if not (root.left or root.right): return root.val * isLeft
        return self.sumOfLeftLeaves(root.left, True) + self.sumOfLeftLeaves(root.right)

root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

s =  Solution()
print(s.sumOfLeftLeaves(root))