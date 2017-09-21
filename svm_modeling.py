#!/usr/bin/python
import numpy as np
from sklearn import svm
trn_label  = np.genfromtxt('Train_label.csv',delimiter=',')
dev_label  = np.genfromtxt('Dev_label.csv',delimiter=',')

trn_feature  = np.genfromtxt('glove_840B_Train_feature.csv',delimiter=',')
dev_feature  = np.genfromtxt('glove_840B_Dev_feature.csv',delimiter=',')
""" pruning parameter """
C = [0.75, 0.76, 0.77, 0.78, 0.79, 0.8, 0.81, 0.82, 0.83, 0.84, 0.85, 0.86, 0.87, 0.88, 0.89,0.9]
for c in C:
	clf = svm.SVC(C = c, kernel ="linear", random_state = None)
	clf.fit(trn_feature, trn_label)  
	trn_accu = clf.score(trn_feature,trn_label)
	tst_accu = clf.score(dev_feature,dev_label)
	print ("%f" % c, trn_accu, tst_accu)

""" train model """
test_feature  = np.genfromtxt('glove_840B_Test_feature.csv',delimiter=',')
clf = svm.SVC(C = 0.84, kernel = 'linear', random_state = None)
clf.fit(trn_feature, trn_label)  
trn_accu = clf.score(trn_feature,trn_label)
t = clf.predict(test_feature)

""" write csv """
import csv
header = ["ID", "Prediction"]
data = []
count = 1
for l in t:
	data.append([count, int(l)])
	count += 1

with open("submission.csv", 'w') as f:
	g = csv.writer(f, delimiter=",")
	g.writerow(header)
	for i in data:
		g.writerow(i)
