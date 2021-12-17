# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ten=0
        sm = ListNode(0,None)
        smp = sm
    
        if not l1:
            return l2
        if not l2:
            return l1

        lp1 = l1
        lp2 = l2
        a = lp1.val
        b = lp2.val
        
        while True:
            tmp = a + b + ten
            if tmp >=10:
                tmp = tmp % 10
                ten=1
            else:
                ten=0
            smp.next=ListNode(tmp,None)
            smp = smp.next
            
            if lp1.next or lp2.next:
                if lp1.next:
                    lp1 = lp1.next
                    a = lp1.val
                    
                else:
                    a=0

                if lp2.next:
                    lp2 = lp2.next
                    b=lp2.val
                else:
                    b = 0
            else:
                if ten==1:
                    smp.next = ListNode(1,None)
                return sm.next
# [2,4,3]
l1 = ListNode(2,ListNode(4,ListNode(3,None)))            

[5,6,6,1,1,1]
l2 = ListNode(5,ListNode(6,ListNode(4,None)))

s = Solution()
r = s.addTwoNumbers(l1,l2)

### Very good solution by oldcodingfarmer
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = cur = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry%10)
            cur = cur.next
            carry //= 10
        return dummy.next
            
s = Solution()
r = s.addTwoNumbers(l1,l2)
            
            
            
            
            
        