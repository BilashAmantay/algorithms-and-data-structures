# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Function to insert nodes in level order
def insertLevelOrder(arr, root, i, n):
     
    # Base case for recursion
    if i < n:
        temp = TreeNode(arr[i])
        root = temp
 
        # insert left child
        root.left = insertLevelOrder(arr, root.left,
                                     2 * i + 1, n)
 
        # insert right child
        root.right = insertLevelOrder(arr, root.right,
                                      2 * i + 2, n)
    return root

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        
        q = [root]
        while q:
            pre, q = q, [child for p in q for child in [p.left, p.right] if child]
        return sum(node.val if node else 0 for node in pre)
        

# arr = [1, 2, 3, 4, 5, 6, 6, 6, 6]
arr = [1,2,3,4,5,None,6,7,None,None,None,None,8]
n = len(arr)
root = None
root = insertLevelOrder(arr, root, 0, n)

s = Solution()
print(s.deepestLeavesSum(root))

