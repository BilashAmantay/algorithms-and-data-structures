"""
Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer must have Node.val == 0.

Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.

A full binary tree is a binary tree where each node has exactly 0 or 2 children.

 

Example 1:


Input: n = 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
Example 2:

Input: n = 3
Output: [[0,0,0]]
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def allPossibleFBT(self, N, memos={1: [TreeNode(0)]}):
        if N % 2 ==0: return None
        if N not in memos: 
            ret = []
            for i in range(1, N-1, 2):
                leftTrees  = self.allPossibleFBT(i)
                rightTrees = self.allPossibleFBT(N - i - 1)
                for left in leftTrees:
                    for right in rightTrees:
                        root = TreeNode(0, left, right)
                        ret += [root]
            memos[N] = ret
        return memos[N]
memos = {}
s = Solution()
result = s.allPossibleFBT(7, memos)
if result: print(len(result))
print(result)