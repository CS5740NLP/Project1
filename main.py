#!/usr/bin/python

# python main.py filename(no need to add path)
# must run this file outside SentimentDataset Folder

import sys

global Start_token, End_token
global truncation, abbreviation

Start_token = "</s>"
End_token = "</e>"
truncation = ["...", ":", ";", "--", "-", ".", "!", "?", ","]
abbreviation = ["'s", "n't", "'ve", "'ll", "'d", "'m", "'re"]


def helper(lines):
	sentence = ""
	for i in range(len(lines)):
		if i is not len(lines)-1:
			sentence = sentence + lines[i] + " "
		else:
			sentence = sentence + lines[i]# enter token?
	print("the end:      ", sentence)

def breakAndinsertToken(line):
	lines = []
	data = []
	is_start = False # whether a start token is inserted
	for j in range(len(line)):
		if j is 0 :
			lines.append(Start_token)
			is_start = True
			if line[j] in truncation:
				continue
			else:
				lines.append(line[j])
		elif j is len(line)-1:
			if line[j] not in truncation:
				lines.append(line[j])
			lines.append(End_token)
				
			data.append(' '.join(lines))
			lines = []
		else:
			if is_start and line[j] in truncation:
				lines.append(End_token)
				data.append(' '.join(lines))
				lines = []
				is_start = False
			
			if j is not len(line)-1 and line[j] in truncation:
				lines.append(Start_token)
				is_start = True
				continue
			
			lines.append(line[j])
	for i in data:
		print(i)


def preprocessing(line):
	lines = []
	arr = line.split(' ')

	is_quote_1 = False # for single quote ` '
	is_quote_2 = False # for double quote `` ''

	for j in range(len(arr)):
		if j > 0 and arr[j] in abbreviation: # if current chars is an abbreviation
			lines[-1] = lines[-1] + arr[j]
		
		elif arr[j] == '`':
			is_quote_1 = True
		elif arr[j] == "'" and is_quote_1:
			is_quote_1 = False
		# special case e.g " Assayas ' "
		# issue!
		elif j is not len(arr)-1 and arr[j] == "'" and (not is_quote_1 or not is_quote_2) and len(lines) is not 0: 
			lines[-1] = lines[-1] + arr[j]
		
		elif arr[j] == '``':
			is_quote_2 = True
		elif arr[j] == "''" and is_quote_2:
			is_quote_2 = False

		elif j is len(arr)-1 and (arr[j] == "'" or arr[j] == "''"):
			break
		else:
			lines.append(arr[j])
	breakAndinsertToken(lines)

def processing():
	with open('SentimentDataset/Train/%s' % tag, 'r') as f:
		pos_data = f.readlines()
	for line in pos_data:
		print("the original: ", line[:-1]) 
		preprocessing(line[:-1]) # line[:-1] for removing the end '\n' symbol
		print()

	
tag = sys.argv[1]
processing()



