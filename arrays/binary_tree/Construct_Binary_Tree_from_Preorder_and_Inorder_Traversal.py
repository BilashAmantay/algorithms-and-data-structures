## Construct Binary Tree from Preorder and Inorder Traversal
## https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/943/discuss/34579/Python-short-recursive-solution.
## https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/943/

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root


preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
s = Solution()
res = s.buildTree(preorder, inorder)
print(res)

print()


preorder = [3,9,21,8,20,15,7]
inorder = [21,9,8,3,15,20,7]
s = Solution()
res = s.buildTree(preorder, inorder)
print(res)