# Definition for a binary tree node.
from sympy import Q


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2,None,TreeNode(6))), TreeNode(5))
subRoot = TreeNode(4, TreeNode(1), TreeNode(2))

## add new sub tree
newSubRoot = TreeNode(4, TreeNode(1), TreeNode(2))
root.left.right.right.left = newSubRoot

root = TreeNode(4, TreeNode(5))
subRoot = TreeNode(4, None, TreeNode(5))

class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not root or not subRoot: return False


        def identical(node1, node2):
            if not node1 and not node2: return True
            if node1 and not node2: return False
            if not node1 and node2: return False

            q1 = [node1]; q2 = [node2]

            while q1 or q2:
                if len(q1) != len(q2): return False
                cur1, cur2 = q1.pop(), q2.pop()
                if cur1.val != cur2.val:
                    return False
                # if cur1.right: q1.append(cur1.right)
                # if cur2.right: q2.append(cur2.right)
                # if cur1.left: q1.append(cur1.left)
                # if cur2.left: q2.append(cur2.left)
                return identical(cur1.left, cur2.left) and identical(cur1.right, cur2.right)
            return True
        
        q1 , q2 = [root], [subRoot]
        cur2 = subRoot
        while q1:
            cur1 = q1.pop()
            if cur1.val == cur2.val:
                node1, node2 = cur1, cur2
                if identical(node1, node2):
                    return True
            if cur1.right: q1.append(cur1.right)
            if cur1.left:  q1.append(cur1.left)
        return False
s = Solution()
print(s.isSubtree(root, subRoot))
            


        