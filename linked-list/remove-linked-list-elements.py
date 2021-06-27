# # https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1207/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

a = ListNode(1)
a.next=ListNode(2)
a.next.next=ListNode(6)
a.next.next.next=ListNode(3)
a.next.next.next.next=ListNode(4)
a.next.next.next.next.next=ListNode(5)
a.next.next.next.next.next.next=ListNode(6)

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        dummy_head = ListNode(-1)
        dummy_head.next = head
        
        current_node = dummy_head
        while current_node.next != None:
            if current_node.next.val == val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
                
        return dummy_head.next


s = Solution()
r = s.removeElements(a,6)

while r:
    print(r,r.val)
    r=r.next
