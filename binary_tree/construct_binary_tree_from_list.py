# Python3 program to construct binary
# tree from given array in level
# order fashion Tree Node

# Helper function that allocates a
#new node
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
		root.left = insertLevelOrder(arr, root.left,2 * i + 1, n)

		# insert right child
		root.right = insertLevelOrder(arr, root.right, 2 * i + 2, n)
	return root

# Function to print tree nodes in
# InOrder fashion
def inOrder(root):
	if root != None:
		inOrder(root.left)
		print(root.data,end=" ")
		inOrder(root.right)

# Driver Code
if __name__ == '__main__':
	arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	n = len(arr)
	root = None
	root = insertLevelOrder(arr, root, 0, n)
	inOrder(root)
	
# This code is contributed by PranchalK
