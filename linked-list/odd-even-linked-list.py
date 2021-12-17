##https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1208/

# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

# The first node is considered odd, and the second node is even, and so on.

# Note that the relative order inside both the even and odd groups should remain as it was in the input.

# You must solve the problem in O(1) extra space complexity and O(n) time complexity.

# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]

# psudo code
# if index is odd, odd.next = odd.next.next till end
# if end, index=2 till end , node.next = node.next.next

from make_linked_list_from_list import makeLinkedList,printall

head = [1,2,3,4,5,6,7,8]
# head = [1,2]
head = makeLinkedList(head)
print('head:'),
printall(head)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class Solution:
#     def oddEvenList(self, head: ListNode) -> ListNode:
#         if head is None:
#             return None
#         if head.next is None:
#             return head

#         odd = ListNode(None)
#         even = ListNode(None)
#         idx=1
#         current = head
#         odd_current = odd
#         even_current = even

#         while current.next:
#             print('current =',current.val, ' idx ',idx)

#             if idx % 2 == 1:
#                 print('idx',idx,current.val)
#                 odd_current.next = current
#                 odd_current = odd_current.next
#             else:
#                 # print('idx even',idx,current.val)
#                 even_current.next = current
                
#                 even_current = even_current.next

#             idx+=1
#             current = current.next

#         if idx%2==1:
#             current.next = even.next
#             odd_current.next = current
#             even_current.next=None
#         else:
#             printall(even)
#             even_current.next=current
#             odd_current.next = even.next
            
#         return odd.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

## Above is my solution, following solution I found from leetcode, simple and clear.
## URL: https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1208/discuss/133345/With-detailed-explanation-or-Python

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        
        odd = head # Both of them point at the first node of the target linked list
        even = head.next # doesn't matter even there's only one node in the linked list (even will become None)
        eHead = even # We have to keep where the even-node list starts
        
        while even and even.next: # won't get in the loop at first if there's only one node in the linked list
            # both even and even.next are necessary condition because even might point to None, which has no attribute 'next'
            # AND, why these two, small discussion by myself as below
            odd.next = odd.next.next
            even.next = even.next.next
            # After these two ops, odd/even still points at its original place
            # Therefore, we move them to the next node repectively
            odd = odd.next
            even = even.next
            
        
        odd.next = eHead # the odd pointer currently points at the last node of the odd-node list
        
        return head # We keep the start of the odd-node list in the first of our code

s = Solution()
res = s.oddEvenList(head)
print()
print('Result')
printall(res)



