# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root: return TreeNode(val)
        node = root
        while node:
            print(node.val)
            if val > node.val:
                print('\tgoing right')
                if node.right:
                    node = node.right
                else:
                    node.right =TreeNode(val)
                    return root
            else:
                print('\tgoing left')
                if node.left:
                    node = node.left
                else:
                    node.left = TreeNode(val)
                    return root
        return root

root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
s = Solution()
r = s.insertIntoBST(root, 5)
print(r.val)
print(r.right.left.val)
