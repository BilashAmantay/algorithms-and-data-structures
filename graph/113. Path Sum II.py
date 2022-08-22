"""
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

 

Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: []
Example 3:

Input: root = [1,2], targetSum = 0
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root, c: int):
        if not root: return 
        
        res = []; sm = 0
        remainder = targetSum
        
        def dfs(node, path, remainder):
            if not node:
                if remainder == 0:
                    return path
                else:
                    return 

            # path.append(node.val)
            remainder -= node.val


            leftResult = dfs(node.left, path + [node.val], remainder)
            if leftResult and leftResult not in res: res.append(leftResult)

            rightResult = dfs(node.right, path + [node.val], remainder)
            if rightResult and rightResult not in res: res.append(rightResult)            

            
       
        dfs(root, [], remainder)
        return res
            
        
# root = [5,4,8,11,None,13,4,7,2,None,None,5,1]
left =  TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2) ))
right = TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1)))
root = TreeNode(5, left, right)
targetSum = 22

s = Solution()
print(s.pathSum(root,targetSum))