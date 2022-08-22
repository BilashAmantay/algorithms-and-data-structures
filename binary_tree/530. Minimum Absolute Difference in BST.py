"""
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

 

Example 1:


Input: root = [4,2,6,1,3]
Output: 1
Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1
"""
class Node:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root ) -> int:
        def fn(node, lo, hi):
            if not node: 
                return hi - lo
            left = fn(node.left, lo, node.val)
            right = fn(node.right, node.val, hi)
            return min(left, right)

        return fn(root, float('-inf'), float('inf'))


root = Node(1)
a = Node(0)
b = Node(48)
root.left = a
root.right = b
b.left = Node(12)
b.right = Node(49)

s = Solution()
print(s.getMinimumDifference(root))
