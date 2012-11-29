# 2010 September 18 by Joshua R. Davis

class BinaryTreeNode(object):
	"""A binary tree node, and in the recursive sense a nonempty binary tree. Each node in the binary tree has a stored value, a left child, and a right child."""
	
	def __init__(self, value=None):
		"""Initializes a new binary tree node with the given value (default None) and no children."""
		self.value = value
		self.left = None
		self.right = None
	
	def setValue(self, value):
		"""Stores the given object as the node's value."""
		self.value = value
	
	def getValue(self):
		"""Returns the value stored in the node."""
		return self.value
	
	def setLeftChild(self, binaryTreeNode):
		"""Sets the left child to the given BinaryTreeNode."""
		self.left = binaryTreeNode
	
	def getLeftChild(self):
		"""Returns the left child."""
		return self.left
	
	def setRightChild(self, binaryTreeNode):
		"""Sets the right child to the given BinaryTreeNode."""
		self.right = binaryTreeNode
	
	def getRightChild(self):
		"""Returns the right child."""
		return self.right
	
	def getHeight(self):
		"""Returns the height of the tree descending from this node. For example, if the node has no children then returns 0."""
		# Compute the height of the left subtree.
		if self.left == None:
			leftHeight = -1
		else:
			leftHeight = self.left.getHeight()
		# Compute the height of the right subtree.
		if self.right == None:
			rightHeight = -1
		else:
			rightHeight = self.right.getHeight()
		return 1 + max(leftHeight, rightHeight)
	
	def __str__(self):
		"""Returns a string representation, with an empty child represented by []. Assumes that the values stored in the tree themselves respond to __str__."""
		# Get the string for the left child.
		if self.left == None:
			leftString = '[]'
		else:
			leftString = str(self.left)
		# Get the string for the right child.
		if self.right == None:
			rightString = '[]'
		else:
			rightString = str(self.right)
		return '[' + str(self.value) + ', ' + leftString + ', ' + rightString + ']'

if __name__ == "__main__":
	myTree = BinaryTreeNode(17)
	myTree.setLeftChild(BinaryTreeNode('jan'))
	myTree.getLeftChild().setRightChild(BinaryTreeNode('juan'))
	myTree.setRightChild(BinaryTreeNode([3, 4, 5]))
	print "The height is", myTree.getHeight()
	print myTree
