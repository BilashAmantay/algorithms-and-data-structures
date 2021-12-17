### Leet code; https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/537/
### solution: https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/537/discuss/36360/Short-Python-recursive-solution-O(n)

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    # 1:27
    def hasPathSum(self, root, sum):
        if not root:
            return False

        if not root.left and not root.right and root.val == sum:
            return True
        
        sum -= root.val

        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)


t = TreeNode(3)
l1 = TreeNode(9)
r1 = TreeNode(20)

r2_l = TreeNode(15)
r2_r = TreeNode(7)

t.left=l1
t.right=r1

r1.left = r2_l
r1.right = r2_r

s=Solution()
print(s.hasPathSum(t,38))
