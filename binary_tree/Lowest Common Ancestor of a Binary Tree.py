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

    def preorderParent(self, root, parent, level):
        if root:
            if parent:
                self.parents[root] = self.parents[parent].copy()
                self.parents[root].append((root,level))

            if root.left: self.preorderParent(root.left, root, level+1)
            if root.right: self.preorderParent(root.right, root, level+1)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.parents = {root: [(root, 0)]}
        level=0
        self.preorderParent(root, root, level)

        # for node in [root, root.left.right, root.right.left, root.left.left]:
        #     print(node.val, node in self.parents, [x.val for x in self.parents[node]])

        mx = float('-inf')
        common_ancestors = []
        lca = None
        for v in self.parents[p]:
            if v in self.parents[q]:
                if v[1] > mx:
                    mx = v[1]
                    lca = v[0]
                common_ancestors.append(v)
        print(common_ancestors)
        return lca

## ------------------------------ optimum solution from leetcode

class Solution:
    
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # Stack for tree traversal
        stack = [root]

        # Dictionary for parent pointers
        parent = {root: None}

        # Iterate until we find both the nodes p and q
        while p not in parent or q not in parent:

            node = stack.pop()

            # While traversing the tree, keep saving the parent pointers.
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        # Ancestors set() for node p.
        ancestors = set()

        # Process all ancestors for node p using parent pointers.
        while p:
            ancestors.add(p)
            p = parent[p]

        # The first ancestor of q which appears in
        # p's ancestor set() is their lowest common ancestor.
        while q not in ancestors:
            q = parent[q]
        return q

s = Solution()
# print(s.lowestCommonAncestor(root, root.left.right, root.left.right.left))
lca =s.lowestCommonAncestor(root, root.left, root.right)
print(lca.val)



