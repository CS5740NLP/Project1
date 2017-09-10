#!/usr/bin/python

# python main.py filename(no need to add path
# must run this file outside SentimentDataset Folder

import sys

global Start_token, End_token
global truncation, conjunction

Start_token = "</s>"
End_token = "</e>"
truncation = ["...", ":", ";", ".", "!", "?", "!?", "?!"]
conjunction = ["--", "-", ',']

def helper(lines):
	sentence = ""
	for i in range(len(lines)):
		if i is not len(lines)-1:
			sentence = sentence + lines[i] + " "
		else:
			sentence = sentence + lines[i]
	print("the end:      ", sentence)

def breakAndinsertToken(line):
	lines = []
	data = []
	is_start = False # whether a start token is inserted
	for j in range(len(line)):
		if j is 0 :
			lines.append(Start_token)
			is_start = True
			lines.append(line[j])

		elif j is len(line)-1:
			lines.append(line[j])
			lines.append(End_token)
			is_start = False
			data.append(' '.join(lines))
			lines = []
		else:
			if is_start and line[j] in truncation: # start token has been added
				lines.append(line[j])
				lines.append(End_token)
				is_start = False
				data.append(' '.join(lines))
				lines = []
				lines.append(Start_token)
				is_start = True
			elif not is_start and line in truncation: # start token has not been added
				lines.append(Start_token)
				lines.append(line[j])
				is_start = True
			else:
				lines.append(line[j])

	for i in data:
		print(i)

def remove_quote(line):
	lines = []
	arr = line.split(' ')

	is_quote_1 = False # for single quote ` '
	is_quote_2 = False # for double quote `` ''

	for j in range(len(arr)):
		# deal with case e.g. she said: ' I 'm coming . '
		# strong punctuation shows before quote 
		if j is len(arr)-1 and arr[j] == "'" and is_quote_1:
			is_quote_1 = False
			break
		elif j is len(arr)-1 and arr[j] == "''" and is_quote_2:
			is_quote_2 = False
			break

		elif not is_quote_1 and (arr[j] == '`' or arr[j] == "'"):
			temp_1 = len(lines)
			value_1 = arr[j]
			is_quote_1 = True
		elif arr[j] == "'" and is_quote_1:
			is_quote_1 = False
		elif not is_quote_2 and (arr[j] == "``" or arr[j] == "''"):
			temp_2 = len(lines)
			value_2 = arr[j]
			is_quote_2 = True
		elif arr[j] == "''" and is_quote_2:
			is_quote_2 = False
		
		else:
			lines.append(arr[j])
	
	if is_quote_1:
		lines.insert(temp_1, value_1)
	if is_quote_2:
		lines.insert(temp_2, value_2)
	
	breakAndinsertToken(lines)

def processing():
	with open('SentimentDataset/Train/%s' % tag, 'r') as f:
		pos_data = f.readlines()
	
	for line in pos_data:
		# print("the original: ", line[:-1]) 
		remove_quote(line[:-1]) # line[:-1] for removing the end '\n' symbol
		# print()

tag = sys.argv[1]
processing()



