# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> list:
        if not root:
            return []
        ans, level = [], [root]
        while level:
            ans.append([node.val for node in level])
            temp = []
            for node in level:
                temp.extend([node.left, node.right])
            level = [leaf for leaf in temp if leaf]
        return ans


"""
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
"""

t = TreeNode(3)
l1 = TreeNode(9)
r1 = TreeNode(20)

r2_l = TreeNode(15)
r2_r = TreeNode(7)

t.left=l1
t.right=r1

r1.left = r2_l
r1.right = r2_r

s = Solution()
print(s.levelOrder(t))