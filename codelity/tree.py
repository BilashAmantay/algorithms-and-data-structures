# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
# Function to insert nodes in level order
def insertLevelOrder(arr, root, i, n):
    
    # Base case for recursion
    if i < n:
        temp = newNode(arr[i])
        root = temp

        # insert left child
        root.left = insertLevelOrder(arr, root.left,
                                    2 * i + 1, n)

        # insert right child
        root.right = insertLevelOrder(arr, root.right,
                                    2 * i + 2, n)
    return root 
# Function to print tree nodes in
# InOrder fashion
def inOrder(root):
    if root != None:
        inOrder(root.left)
        print(root.data,end=" ")
        inOrder(root.right)

def maxCity(root):
    

def solution(T):
    # write your code in Python 3.6
    n = len(T)
    root = None
    root = insertLevelOrder(T, root, 0, n)
    inOrder(root)



T = [0,9,0,2,6,8,0,8,3,0]

print(solution(T))