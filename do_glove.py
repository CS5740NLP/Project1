#!/usr/bin/python
import pickle
import csv
import sys

from sklearn import svm
import numpy as np

""" customized preprocessing """
def remove_quote(path, filename):
	with open('SentimentDataset/%s/%s.txt' % (path, filename), 'r') as f:
		reviews = f.readlines()
	content_len = len(reviews)
	content = []
	for line in reviews:
		line = line[:-1]
		lines = []
		arr = line.replace('\/', ' ')
		arr = arr.replace('\*', '').split()
		is_quote_1 = False # for single quote ` '
		is_quote_2 = False # for double quote `` ''
		for j in range(len(arr)):
			if j == '':
				continue
			if j is len(arr)-1 and arr[j] == "'" and is_quote_1:
				is_quote_1 = False
				break
			elif j is len(arr)-1 and arr[j] == "''" and is_quote_2:
				is_quote_2 = False
				break
			elif j is len(arr)-1 and (arr[j] == "'" or arr[j] == "''"):
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
		content.append(' '.join(lines))
		# print "original:", line
		# print "after   :", ' '.join(lines) 
	return content, content_len

""" word embedding for each review set """
def do_embedding(tag, feature):
	wordVec = 'glove_840B'
	ref = {}
	count = 0
	miss = 0
	token = 0
	log = []
	for line in feature:
		l = len(line.split())
		s = []
		for i in line.split():
			if i[0] != '-' and (i != "--" or i != "-") and i.count("-") >= 1:
				log.append("line %d :%s \n" %(count,i))
				for j in i.split("-"):
					if db.has_key(j):
						s.append(db[j])
					else:
						log.append("line %d"%count + " not here:%s\n" %j)
						miss+=1
				token += (i.count("-")+1)
			else:
				if db.has_key(i):
					s.append(db[i])
				else:
					log.append("line %d"%count + " not here:%s\n" %i)
					miss+=1
				token += 1
		if s == []:
			s.append([0.00] * 300)

		ref[count] = [sum(j)/l for j in zip(*s)]
		count += 1


	with open('%s_%s_feature.csv' % (wordVec, tag), 'w') as f:
		wtr = csv.writer(f, delimiter=",")
		for key,val in ref.items():
			wtr.writerow(val)

	""" record miss rate """
	log.append("%s --miss: %d  --rate: %f \n" % (tag, miss, float(miss*1./token*1.)))
	""" record missed word """
	with open('glove_%s_not_here.txt' % tag, 'w') as f:
		for l in log:
			f.write(l)


def get_vector():
	path_list = ["Train", "Dev"]
	for tag in path_list:
		reviews, pos_len = remove_quote(tag, 'pos')
		neg_review, neg_len = remove_quote(tag, 'neg')
		reviews.extend(neg_review)
		label = [0] * pos_len
		label.extend([1 for x in range(neg_len)])
		""" write label csv file """
		with open('%s_label.csv' % tag, 'w' ) as f:
			wtr = csv.writer(f, delimiter=",")
			for i in label:
				wtr.writerow([i])

		do_embedding(tag, reviews)

db = pickle.load(open('db.pkl', 'rb'))['glove_840B']
get_vector()
tst_reviews, tst_len = remove_quote('Test', 'test')
do_embedding('Test', tst_reviews)

