# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head):
        dummy = pre = ListNode(0)
        pre.next = head

        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                pre.next = head
            else:
                head = head.next
                pre = pre.next
        return dummy.next
                

head = [1,2,3,3,3,3,4,4,5]
node = ListNode(head[0])
nodes = []
for h in head:
    nodes.append(ListNode(h))
for i in range(len(nodes)-1):
    nodes[i].next = nodes[i+1]

head = nodes[0]
# while head and head.next:
#     print(head.val, end=' ')
#     head = head.next 
# print(head.val)
s = Solution()
r = s.deleteDuplicates(head)
while r and r.next:
    print(r.val, end=' ')
    r = r.next 
print(r.val)

print(r)
print()
