## https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/536/
"""
Input: root = [1,2,2,3,4,4,3]
Output: true

Input: root = [1,2,2,null,3,null,3]
Output: fal
"""
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True
        else:
            return self.isMirror(root.left, root.right)

                                                                                                                                                                                                                                                                                                                             



t = TreeNode(1)
l1 = TreeNode(2)
r1 = TreeNode(2)

l2_l = TreeNode(3)
l2_r = TreeNode(4)

r2_l = TreeNode(4)
r2_r = TreeNode(3)


t.left=l1
t.right=r1

l1.left = l2_l
l1.right = l2_r

r1.left = r2_l
r1.right = r2_r

s = Solution()
print(s.isSymmetric(t))