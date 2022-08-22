"""
Given the root of a binary tree, return the sum of values of nodes with an even-valued grandparent. If there are no nodes with an even-valued grandparent, return 0.

A grandparent of a node is the parent of its parent if it exists.

Example 1:

Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.
Example 2:

Input: root = [1]
Output: 0
 
"""

# Definition for a binary tree node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# l = Node(7, Node(2, Node(9)), Node(7, Node(1), Node(4)))
# r = Node(8, Node(1), Node(3, None, Node(5)))
# root = Node(6, l, r)

root = Node(6,Node(2,Node(4)),None)

class Solution:
    def sumEvenGrandparent(self, root: Node) -> int:
        if not root: return 
        # if not root.left or not root.right: return 0
        
        evenGrandParent = False
        res = 0
        
        # if root.val % 2 ==0:
        #     evenFather = True
        # else:
        evenFather = False
            
        q = [[root, evenFather, evenGrandParent]]
            
        while q:
            cur, evenFather, evenGrandParent = q.pop()
            
            res += cur.val * evenGrandParent
            
            if cur.val % 2 ==0:
                even = True
            else:
                even = False
            
            evenGrandParent = evenFather
            if cur.left:  q.append([cur.left,  even,  evenGrandParent])
            if cur.right: q.append([cur.right, even,  evenGrandParent])
        
        return res
s = Solution()
print(s.sumEvenGrandparent(root))          
                
        