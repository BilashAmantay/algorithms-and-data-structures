# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        depth = 0
        levels = [root] if root else []
        while levels:
            depth += 1
            queue = []
            for leaf in levels:
                if leaf.left:
                    queue.append(leaf.left)
                if leaf.right:
                    queue.append(leaf.right)
            levels = queue
            
        return depth


class RecursiveSolution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


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
print(s.maxDepth(t))

## Recursive solution
rs = RecursiveSolution()
print(rs.maxDepth(t))



##################### other testing
t = TreeNode(1)
l1 = TreeNode(2)
r1 = TreeNode(3)

l2_l = TreeNode(4)
r2_r = TreeNode(5)

t.left=l1
t.right=r1

l1.left = l2_l
r1.right = r2_r

s = Solution()
print('test 2')
print(s.maxDepth(t))