""" A program that stores and updates a counter using a Python pickle file"""

from os.path import exists
import sys, string
import pickle

def update_counter(file_name, reset=False):
	""" Updates a counter stored in the file 'file_name'

		A new counter will be created and initialized to 1 if none exists or if
		the reset flag is True.

		If the counter already exists and reset is False, the counter's value will
		be incremented.

		file_name: the file that stores the counter to be incremented.  If the file
				   doesn't exist, a counter is created and initialized to 1.
		reset: True if the counter in the file should be rest.
		returns: the new counter value

	>>> update_counter('blah.txt',True)
	1
	>>> update_counter('blah.txt')
	2
	>>> update_counter('blah2.txt',True)
	1
	>>> update_counter('blah.txt')
	3
	>>> update_counter('blah2.txt')
	2
	"""


	if not exists(file_name): 
		#If the file does not exist, one is created.
		file = open(file_name, 'w')
		counter = 1
		pickle.dump(counter, file)
		file.close()

	elif reset:
		#If the file is reset, the counter is changed to 0
		file = open(file_name, 'w')
		counter = 1
		pickle.dump(counter, file)
		file.close()
	else:
		#If file exists and reset = False, the counter is updated +1
		file = open(file_name, 'r+')
		counter = pickle.load(file)
		counter += 1
		file.seek(0,0)
		pickle.dump(counter, file)
		

	print counter






if __name__ == '__main__':
	if len(sys.argv) < 2:
		import doctest
		doctest.testmod()
	else:
		print "new value is " + str(update_counter(sys.argv[1]))

#DocTest Passes!

print update_counter('count.txt', reset=False)