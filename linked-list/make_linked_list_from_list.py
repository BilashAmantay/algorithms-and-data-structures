#https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1215/

# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

listA = [4,1,8,4,5]
listB = [5,6,1,8,4,5]
skipA = 2
skipB = 3
intersectVal = 8

def makeLinkedList(pylist):

    a = ListNode(pylist[0])
    this = a
    for i in range(1,len(pylist)):
        # print(pylist[i])
        this.next = ListNode(pylist[i])
        this = this.next
    return a


alist = makeLinkedList(listA)
blist = makeLinkedList(listB)

print(alist.next.next.next.val)
print(blist.next.next.next.val)

def makeCircle(notcircled_list):
    output = ListNode(notcircled_list.val)

    output_current = output
    current = notcircled_list

    while current.next!=None:
        current = current.next
        output_current.next = current
        output_current = output_current.next
    output_current.next = output
  
    return output

circled_a = makeCircle(alist)
circled_b = makeCircle(blist)
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

print('circled list ')
printall(circled_a)
printall(circled_b)

