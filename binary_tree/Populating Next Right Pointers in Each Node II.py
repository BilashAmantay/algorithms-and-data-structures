class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        tail = dummy = Node(0)
        while root:
            tail.next = root.left
            if tail.next:
                tail = tail.next
            tail.next = root.right
            if tail.next:
                tail = tail.next
            root = root.next
            if not root:
                tail = dummy
                root = dummy.next
l = Node(2, Node(4), Node(5))
r = Node(3, None, Node(7))
root = Node(1, l, r)

s = Solution()
r = s.connect(root)
print(root.next)
print(root.left.next.val)
print(root.left.left.next.val)
print(root.left.left.next.next.val)
