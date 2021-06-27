# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

a = ListNode(1)
a.next=ListNode(2)
a.next.next=ListNode(3)
a.next.next.next=ListNode(4)
a.next.next.next.next=ListNode(5)
class Solution:
    def reverseList(self, head):
        node = None
        iter=0
        while head:
            iter+=1
            print('iter:' ,iter)
            if head: print(head.val)
            tmp = head.next
            head.next = node
            node = head
            head = tmp

        return node


# tmp = a
# while tmp:
#     print(tmp,tmp.val)
#     tmp=tmp.next
# tmp=a

s = Solution()
r = s.reverseList(a)

while r:
    print(r,r.val)
    r=r.next
