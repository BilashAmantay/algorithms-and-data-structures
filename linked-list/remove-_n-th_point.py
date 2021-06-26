##https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1296/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

lst = ListNode(1)
# lst.next = ListNode(2)
# lst.next.next = ListNode(3)
# lst.next.next.next = ListNode(4)
# lst.next.next.next.next = ListNode(5)

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return None

        current = head
        leng = 0
        while current:
            leng+=1
            current = current.next
        
        drp = leng - n -1
        print('drp = ',drp, ' leng',leng)
        
        if drp>leng or drp<0:
            return None
        
        idx=1
        a = head
        b = head.next

        while b:

            print(idx,a.val, b.next.val)

            if idx==drp:
                
                
                a.next = b.next
                break
                
            a = b
            b = b.next
            idx+=1
        current = head
        return current

def printall(a_linked_list):
    idx=0
    current = a_linked_list
    while current.next != None:
        print(current.val)
        current = current.next
        idx+=1
        if idx>40:
            break
    print(current.val)

s = Solution()
a = s.removeNthFromEnd(lst, 1)
printall(a)
print(a)



                