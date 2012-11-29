# Written by Nick Jones for Josh Davis's CS 201 course at Carleton College, November 2010.

from binarytreenode import BinaryTreeNode

class HuffmanTreeNode(BinaryTreeNode):
	"""A subclass of BinaryTreeNode. Acts in exact same manner as BTN except has an extra instance variable, weight, which stores the frequency of the instance variable value. Interior nodes' weight is the sum of all of its children. Nodes DO NOT KNOW THEIR OWN CODE! This is instead dealt with by another class, HuffmanTree, which contains a pointer to the root node and deals with the codewords."""

	def __init__(self, weight=0, value=None):
		"""Initializes a new Huffman tree node with given weight and value (though interior nodes will have value None) """
		BinaryTreeNode.__init__(self,value)
		self.weight = weight
		
	def setWeight(self, newWeight):
		"""Sets this node's weight to newWeight. Useful for interior nodes."""
		self.weight = newWeight
		
	def getWeight(self):
		"""Returns this node's weight """
		return self.weight
		
	def setLeftChild(self, node):
		"""Sets left child to given node, which will presumably be a HTN."""
		BinaryTreeNode.setLeftChild(self, node)
		self.weight += node.getWeight()
	
	def setRightChild(self, node):
		"""Sets right child to given node, which will presumably be a HTN."""
		BinaryTreeNode.setRightChild(self, node)
		self.weight += node.getWeight()
		
	def __str__(self):
		"""Returns a string representation - empty child is []. Easier to rewrite this method than to call it from superclass and alter it then."""
		if self.left == None:
			leftStr = '[]'
		else:
			leftStr = str(self.left)
			
		if self.right == None:
			rightStr = '[]'
		else: 
			rightStr = str(self.right)
			
		if self.value == None:
			valStr = 'None'
		else:
			valStr = str(self.value)
		return '[(' + valStr + ', ' + str(self.weight) + '),' + leftStr + ', ' + rightStr + ']'
		
if __name__ == "__main__":
	n = HuffmanTreeNode(12, 'a')
	m = HuffmanTreeNode(13, 'd')
	parent = HuffmanTreeNode()
	parent.setLeftChild(n)
	parent.setRightChild(m)
	print 'm: ' , m
	print 'n: ' , n
	print 'parent:', parent