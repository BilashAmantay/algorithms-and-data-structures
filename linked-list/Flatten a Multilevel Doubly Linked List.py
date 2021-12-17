https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1225/

### solution from https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1225/discuss/152725/Python-solution-with-explanation
### This solution beat  87% of the python solution

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        # Initialize the current reference and stack of saved next pointers
        curr, tempStack = head, [];
        while curr:
            if curr.child:
                # If the current node is a parent
                if curr.next:
                    # Save the current node's old next pointer for future reattachment
                    tempStack.append(curr.next);
                # Current <-> Current.child
                #   \-> None
                curr.next, curr.child.prev, curr.child = curr.child, curr, None;
            if not curr.next and len(tempStack):
                # If the current node is a child without a next pointer
                temp = tempStack.pop();
                # Current <-> Temp
                temp.prev, curr.next = curr, temp;
            curr = curr.next;
        return head;

## sample 16ms solution
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        #headprev=head
        def GetChild(parent):
            #print('parent',parent.val)
            #while parent.child:
            if parent.child:
                parent.next=parent.child
                parent.child.prev=parent
                holdchild=parent.child
                parent.child=None
                parent=holdchild#e
            return parent
        
        def ChildFlat(childstart):
            #print('childstart',childstart.val)
            while childstart:
                if childstart.child==None:
                    if childstart.next==None:
                        #print('chd',childstart.val)
                        return childstart
                    else:
                        childstart=childstart.next
                else:
                    if childstart.next:
                        holdnext=childstart.next
                        childstart=GetChild(childstart)
                        childstart=ChildFlat(childstart)
                        holdnext.prev=childstart
                        childstart.next=holdnext
                        childstart=holdnext
                    else:
                        childstart=GetChild(childstart)
                        childstart=ChildFlat(childstart)
            return
        
        ChildFlat(head)
        
        #ans=[]
        #while headprev:
            #print(headprev.val)
            #if headprev.prev:
                #ans.append(headprev.prev.val)
            #headprev=headprev.next
        #print(head) 
        
        return head#prev