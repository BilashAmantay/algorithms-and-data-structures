# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next     # skip duplicated node
            cur = cur.next     # not duplicate of current node, move to next node
        return head

head = ListNode(1)
a = ListNode(2)
b = ListNode(2)
c = ListNode(2)
d = ListNode(2)
e = ListNode(2)
f = ListNode(4)

head.next = a
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

p = head
while p and p.next:
    print(p, hex(id(p)))
    p = p.next


s = Solution()
res = s.deleteDuplicates(head)
while res and res.next:
    print(res.val)
    res = res.next