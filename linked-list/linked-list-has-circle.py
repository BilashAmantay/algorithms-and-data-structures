class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next=next


class MyLinkedList:

    def __init__(self,next=None):
        self.Head = Node(None)
        """
        Initialize your data structure here.
        """
        
    def get(self, index: int):

        index_count = 0
        return_this = -1
        
        if self.Head != None:

            current = self.Head
            while True:

                if index == index_count:

                    return_this = current.val
                    return current.val

                index_count +=1

                if current.next == None:
                    break
                
                current = current.next
        return return_this
                
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        

    def addAtHead(self, val: int):

        if self.Head.val == None:
            self.Head.val = val
            return

        old_Head = self.Head

        # newNode = Node(val, old_Head)
        # newNode.next = old_Head

        self.Head = Node(val, old_Head)
        # self.Head.next = old_Head
        
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        

    def addAtTail(self, val: int):

        if self.Head.val == None:
            self.Head.val = val
            return
        
        newNode = Node(val)
        current = self.Head
        while True:

            if current.next == None:

                current.next = newNode
                break



            current = current.next
        
        """
        Append a node of value val to the last element of the linked list.
        """

    def ShowAll(self):

        values = []    
        current = self.Head

        
        count = 0

        while True:

            count +=1
            

            values.append(current.val)
            current = current.next
            if current == None:
                break

        return values

    
    
    def addAtIndex(self, index: int, val: int):
        loop_index = 0
        newNode = Node(val)

        if index == 0 and self.Head.val != None:

            self.addAtHead(val)
            return
        
        if self.Head.val != None:
            current = self.Head
            # while current.next != None:
            while True:

                if loop_index!=index-1:
                    current = current.next
                    loop_index+=1
                else:
                    #Node before index Node
                    beforeCurrent = current
                    current = current.next

                    #Storing the address of next node in new node
                    newNode.next = current

                    beforeCurrent.next = newNode
                    break

                
                if current == None:
                    break


        elif self.Head.val == None and index == 0:
            self.Head = newNode


        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        

    def deleteAtIndex(self, index: int):
        
        # print("Before Delete")
        # print(self.ShowAll())

        current = self.Head
        count_index = 0

        if index == 0:
            self.Head = self.Head.next
            return 


        while True:

            if count_index != index-1:
                current = current.next
                count_index+=1
                                
            elif current.next == None:
                # print("Here")
                break

            else:
                beforeCurrent = current
                deleteCurrent = beforeCurrent.next
                current = deleteCurrent.next
                beforeCurrent.next = current
                break
        # print("Afer Del")
        # print(self.ShowAll())