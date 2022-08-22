"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false
 

Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q: return True
        if p is None or q is None: return False
        if p is None and q is None: return True
        
        queueP = [p]
        queueQ = [q]
        
        while queueP and queueQ:
            currentP = queueP.pop()
            currentQ = queueQ.pop()
            
            if currentP.val != currentQ.val:
                return False
            
            if currentP.left: queueP.append(currentP.left)
            if currentP.right: queueP.append(currentP.right)
            
            if currentQ.left: queueQ.append(currentQ.left)
            if currentQ.right: queueQ.append(currentQ.right)            
            
        return True
        
p = TreeNode(1)
p.left = TreeNode(2,None,None)
p.right = TreeNode(3,None,None)

q = TreeNode(1)
q.left = TreeNode(2,None,None)
q.right = TreeNode(3,None,None)

s = Solution()
print(s.isSameTree(p,q))