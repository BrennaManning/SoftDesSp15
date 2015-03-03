""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case."""

	word_list = []

	punct = set(string.punctuation)
	

	fp = open(file_name)
	for line in fp:
		for word in line.split():
			# Process into Pig Latin
			word=(word.lower())

			word = ''.join(ch for ch in word if ch not in punct)

			word_list.append(word)
	return word_list
	
	pass

def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""
	
	
	counter = {}
	for i in word_list: counter[i] = counter.get(i, 0) + 1
	return sorted([ (freq,word) for word, freq in counter.items() ], reverse=True)[:n]
	
	pass

print get_top_n_words(get_word_list('alice.txt'),100)

#print get_word_list('alice.txt')