import sys

def compareFiles(file1, file2):
	"""Prints whether or not two fils are the same"""
	f1 = open(file1, 'r')
	f2 = open(file2, 'r')

	f1Str = f1.read()
	f2Str = f2.read()
	if f1Str == f2Str:
		print 'Same file!'
	else:
		print 'They\'re different...'
		
if __name__ == "__main__":
	file1 = sys.argv[1]
	file2 = sys.argv[2]
	compareFiles(file1, file2)