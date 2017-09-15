#!/usr/bin/python

from preForB import *
from n_gram import *
def getCount(data):
	""" 
	Get the number of word tokens 
	"""
	count = 0
	for line in data:
		count += (len(line.split(' '))-1)
	return count

def perplexity(file_name):
	with open("SentimentDataset/Dev/%s.txt" % file_name, 'r') as f:
		data = f.readlines()
	content = remove_quote(data)
	uni_word,uni_prob,bi_word,bi_prob = gram(' '.join(content))
	num_tokens = getCount(data)
	
	import math
	
	total = 0.0
	"""
	unigram perplexity
	"""
	for i in uni_prob:
		total += math.log(i)
	uni_pp = math.exp(-total/num_tokens)
	print(uni_pp)
	"""
	bigram perplexity
	"""
	total = 0.0
	for value in bi_prob.itervalues():
		for i in value:
			total += i
	bi_pp = math.exp(-total/num_tokens)
	print(bi_pp)

import sys
perplexity(sys.argv[1])