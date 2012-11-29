# Written by Nick Jones for Josh Davis's CS 201 course at Carleton College, November 2010.

from huffmantreenode import HuffmanTreeNode

class HuffmanTree(object):

	def __init__(self, root = None):
		"""Creates a new instance of a Huffman tree. The root is the HuffmanTreeNode at the top of the entire tree. """
		self.root = root
		self.codeWords = {} # of form char => binary string
		
	def parseCodeWords(self, currentNode, currentCode = ''):
		"""Traverses the tree, populating the dictionary with characters and their cooresponding codewords."""
		if currentNode == None: # i.e. parent was a leaf node
			return
		else:
			if currentNode.getValue() != None: # we don't want branch nodes in our dictionary
				self.codeWords[currentNode.getValue()] = currentCode
				
			self.parseCodeWords(currentNode.getLeftChild(), currentCode + '0') # set left to be currentCode + '0'
			self.parseCodeWords(currentNode.getRightChild(), currentCode + '1') # set right to be currentCode + '1'
			
	def getCodeWords(self):
		"""Returns dictionary with character keys and codeword values."""
		return self.codeWords
		
	def setCodeWords(self, dict):
		"""For rebuilding. Program will read in representation of codeWords dictionary, set codeWords equal to it."""
		self.codeWords = dict
		
	def getRoot(self):
		"""Returns root of this HuffmanTree"""
		return self.root
		
	def writeFile(self, doc):
		"""Returns a string in binary form of the inputted string doc, and the ASCII equivalent of the binary string, which will be written to the compressed file. Uses the codeWord dictionary to convert from characters to binary digits"""
		
		binStr = self.convertToBinary(doc)	
		encodedStr = self.getDictRep() # this will add the dictionary to start of compressed file
		i = 0
		while i < len(binStr) - 8: # change binary reps. to characters. Must stop before the end, because string length isn't necessarily divisble by 8. Last chunk will probably not be 8 long.
			temp = chr(int(binStr[i:i+8], 2))
			encodedStr += temp
			i += 8

		lastLength = len(binStr[i:]) # how many left over are there?
		encodedStr += chr(int(binStr[i:], 2)) + str(lastLength) # add the ascii of last few bits, and how many bits that is
		return (encodedStr, binStr)
		
	def getDictRep(self):
		"""Returns a string representation of the codeWords dictionary to be written to compressed file."""
		fullStr = str(len(self.codeWords)) + '\nnjh\n'
		for char in self.codeWords:
			binStr = self.codeWords[char]
			encodedStr = char + str(len(binStr)) + ':'
			i = 0
			while i < len(binStr) - 8: # change binary reps. to characters. Must stop before the end, because string length isn't necessarily divisble by 8. Last chunk will probably not be 8 long.
				temp = chr(int(binStr[i:i+8], 2))
				encodedStr += temp
				i += 8
				
			encodedStr += chr(int(binStr[i:], 2)) # add the ascii of last few bits, and how many bits whole string is
			fullStr += encodedStr
		return fullStr
		
	def convertToBinary(self, originalDoc):
		"""Converts originalDoc to binary string based on HuffmanTree"""
		binStr = ''
		for x in originalDoc:
			binStr += self.codeWords[x]
		return binStr
		
	def decodeFile(self, doc):
		"""Takes in the twice encoded file (i.e. the ascii characters of the orignial binary code). Decodes to binary and eventually to original text. Should only be called once the tree has been rebuilt."""
		binStr = ''
		lastTwoChars = doc[len(doc) - 2:] # Last two characters are important. Last one tells us how many bin. digits the second to last one should have when changed to binary representation.
		adjustedDoc = doc[:len(doc) - 2] 
		for character in adjustedDoc:
			temp = bin(ord(character))[2:] # strip '0b'
			extraSpace = 8 - len(temp) # this number indicates how many zeros should be added at front of temp (so that it is of length 7)
			zeros = '0'*extraSpace
			temp = zeros + temp
			binStr += temp
		lastCharBin = bin(ord(lastTwoChars[0]))[2:] # just like for all the others
		lastCharBin = '0'*(int(lastTwoChars[1]) - len(lastCharBin)) + lastCharBin # lastTwoChars[1] tells how long bin. rep. of lastChar should be.
		binStr += lastCharBin
		
		toReturn = self.binToOriginal(binStr)
		return toReturn
		
	def binToOriginal(self, binStr):
		"""Takes in binary string of digits, converts them to text based on the codeWords dictionary"""
		reverseDir = {}
		for x in self.codeWords:
			reverseDir[self.codeWords[x]] = x
		begIndex = 0
		curIndex = 0
		rebuiltStr = ''
		while curIndex < len(binStr) + 1:
			try:
				rebuiltStr += reverseDir[str(binStr[begIndex:curIndex])] # try looking up current digit string in dict
				begIndex = curIndex # if it worked, move the beginning index to the end of last chunk
			except KeyError:
				curIndex += 1 # move along if current digit string was not found in dictionary
		return rebuiltStr
			