# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root):
        ret = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                ret.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return ret

d = TreeNode(3)
c = TreeNode(2,d,None)
# null = TreeNode()
root = TreeNode(1, None, c)

s = Solution()
r = s.preorderTraversal(root)
print(r)



### Anoterh solution 
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    ## Recursive solution
    ## Preorder: Root -> Left -> Right
    ## Time complexity: O(N)
    ## Space complexity: O(N)
    def preorderTraversal(self, root: TreeNode):
        res = []
        if not root: return res
        res.append(root.val)
        res = res + self.preorderTraversal(root.left);
        res = res + self.preorderTraversal(root.right);
        return res

s = Solution()
print(s.preorderTraversal(root))