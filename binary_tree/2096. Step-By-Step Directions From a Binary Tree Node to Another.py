class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

lr = TreeNode(2, TreeNode(7), TreeNode(4))
l = TreeNode(5, TreeNode(6), lr)
r = TreeNode(1, TreeNode(0), TreeNode(8))
root = TreeNode(3, l, r)

class Solution:
    def lca(root, startValue, destValue):
        stack = [root]  
        parent = {root: None}
        
        startNode = None
        destValueNode = None

        while startValue not in parent  or destValue not in parent:

            node = stack.pop()

            if node.val == startValue:
                startNode = node
            if node.val == destValue:
                destValueNode = node 

            if node.left:
                stack.append(node.left)
                parent[node.left] = node
            if node.right:
                stack.append(node.right)
                parent[node.right] = node
        
        ansestor = set()
        ans = ''
        while startNode not in ansestor:
            ansestor.add(startNode)
            startNode = parent[startNode]
            ans += 'U'
        
        while destValueNode not in ansestor:
            destValueNode = parent[destValueNode]
        
        return destValueNode

    # def getDirections(self, root: TreeNode, startValue: int, destValue: int) -> str:


