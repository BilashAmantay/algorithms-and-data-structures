#https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1215/

# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a = headA
        b = headB

        lena = 0
        lenb = 0

        while a:
            a = a.next
            lena+=1

        while b:
            b = b.next
            lenb+=1

        a = headA
        b = headB

        if lena > lenb:
            for i in range(lena - lenb):
                a = a.next
        
        if lenb > lena:
            for i in range(lenb - lena):
                b = b.next

        while a and b:
            if a==b:
                return a
            else:
                a = a.next
                b = b.next
        return None

## above solution test result
# Runtime: 176 ms
# Memory Usage: 29.5 MB

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a = headA
        b = headB

        lena = 0
        lenb = 0

        while a:
            a = a.next
            lena+=1

        while b:
            b = b.next
            lenb+=1

        a = headA
        b = headB

        if lena > lenb:
            for i in range(lena - lenb):
                a = a.next
        else:
            for i in range(lenb - lena):
                b = b.next

        while a and b:
            if a==b:
                return a
            else:
                a = a.next
                b = b.next
        return None


## above solution run time
    # Runtime: 164 ms
    # Memory Usage: 29.4 MB