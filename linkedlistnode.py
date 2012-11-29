# Written by Josh Davis, edited by Nick Jones 9/16/10

class LinkedListNode(object):
	"""A basic linked list node class, for use in implementing other more interesting classes."""
	
	def __init__(self, data):
		"""Initializes a new node with the given data and no next node."""
		self.data = data
		self.next = None
	
	def setData(self, data):
		"""Sets the node's data, which is set for the first time in __init__()."""
		self.data = data
	
	def getData(self):
		"""Returns the data currently stored in the node."""
		return self.data
	
	def setNext(self, next):
		"""Sets the next node, which is None by default."""
		self.next = next
	
	def getNext(self):
		"""Returns the next node, or None."""
		return self.next
	
	def __str__(self):
		"""Returns data as string"""
		return self.data

if __name__ == "__main__":
	node = LinkedListNode('hello')
	node2 = LinkedListNode('bye')
	node3 = LinkedListNode('later')
	node.setNext(node2)
	node2.setNext(node3)
	
	temp = node
	while temp != None:
		print str(temp)
		temp = temp.getNext()