from make_linked_list_from_list import ListNode, makeLinkedList,printall

head = [1,2,2,1]
# head = [1,2,3,2,1]
head = [1,2,3,4,1]
head = makeLinkedList(head)
print('head:'),
printall(head)

class Solution:
    def isPalindrome(self, head):
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev
s = Solution()
print(s.isPalindrome(head))
