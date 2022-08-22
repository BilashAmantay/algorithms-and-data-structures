"""
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
Example 2:

Input: root = [1]
Output: ["1"]

"""
from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = Node(1,Node(2,None,Node(5)), Node(3, Node(5,Node(6))))

# dfs + stack
class Solution:
    def binaryTreePaths1(self, root):
        """
        Runtime: 24 ms, faster than 98.58% of Python3 online submissions for Binary Tree Paths.
        """
        if not root:
            return []
        res, stack = [], [(root, "")]
        while stack:
            node, ls = stack.pop()
            if not node.left and not node.right:
                res.append(ls+str(node.val))
            if node.right:
                stack.append((node.right, ls+str(node.val)+"->"))
            if node.left:
                stack.append((node.left, ls+str(node.val)+"->"))
        return res

    def binaryTreePaths2(self, root):
        if not root:
            return []
        res, queue = [], deque([(root, "")])
        while queue:
            node, ls = queue.popleft()
            if not node.left and not node.right:
                res.append(ls+str(node.val))
            if node.left:
                queue.append((node.left, ls+str(node.val)+"->"))
            if node.right:
                queue.append((node.right, ls+str(node.val)+"->"))
        return res

s = Solution()

print(s.binaryTreePaths1(root))