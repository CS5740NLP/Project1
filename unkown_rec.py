import numpy as np
import sys
import math
import os
global Unkown_token

Unkown_token = "</unk>"

# Build a dictionary for train pos and neg txt file

f1 = open("pos_pre.txt", 'r')
f2 = open("neg_pre.txt", 'r')

print ('reading preprocessed trainning data...')
trn_Pos_Dict = list()
trn_Neg_Dict = list()

for line in f1:
    words = line.split(' ')
    for word in words:
            if word not in trn_Pos_Dict:
                if word == "</s>":
                    continue
                elif word == "</e>":
                    continue
                else:
                    trn_Pos_Dict.append(word)
trn_Pos_Dict.sort()
f1.close()

for line in f2:
    words = line.split(' ')
    for word in words:
        if word not in trn_Neg_Dict:
            trn_Neg_Dict.append(word)
trn_Neg_Dict.sort()
f2.close()

print('all words from trainning dataset has been archived!')
# Label all unkown words in dev data

f3 = open("pos_dev_pre.txt", 'r')
f4 = open("neg_dev_pre.txt", 'r')

# where to store all words appeared in validaiton dataset
dev_Pos_Dict = list()
dev_Neg_Dict = list()
# where to store all new words appeared in validation dataset
new_words_Pos = list()
new_words_Neg = list()

unk_Pos = 0
unk_Neg = 0

for line in f3:
    words = line.split(' ')
    for word in words:
        if word in trn_Pos_Dict and word not in dev_Pos_Dict:
            dev_Pos_Dict.append(word)
        else:
            if word == "</s>" or word == "</e>":
                continue
            elif word not in dev_Pos_Dict:
                dev_Pos_Dict.append(word + Unkown_token)
                new_words_Pos.append(word)
                unk_Pos += 1
dev_Pos_Dict.sort()
new_words_Pos.sort()
f3.close()

for line in f4:
    words = line.split(' ')
    for word in words:
        if word in trn_Neg_Dict and word not in dev_Neg_Dict:
            dev_Neg_Dict.append(word)
        else:
            if word == "</s>" or word == "</e>":
                continue
            elif word not in dev_Neg_Dict:
                dev_Neg_Dict.append(word + Unkown_token)
                new_words_Neg.append(word)
                unk_Neg += 1
dev_Neg_Dict.sort()
new_words_Neg.sort()
f4.close()
print('all unkown words from valided data set have been collected and archived')

Pos_UnkProb = unk_Pos/len(dev_Pos_Dict)
Neg_UnkProb = unk_Neg/len(dev_Neg_Dict)

def label_unk_words(line, dic = 1):
    line2 = []
    if dic == 1:
        words = line.split(' ')
        for word in words:
            if word in new_words_Pos:
                word = word + Unkown_token
            line2.append(word)   
    else:
        words = line.split(' ')
        for word in words:
            if word in new_words_Neg:
                word = word + Unkown_token
            line2.append(word)
    return ' '.join(line2)

context1 = list()
context2 = list()
with open("pos_dev_pre.txt", 'r') as f1:
    for line in f1.readlines():
        labeled = label_unk_words(line[:-1], 1)
        context1.append(labeled)

with open("pos_dev_unklb.txt",'w') as f2:
    for line in context1:
        f2.writelines(line + "\n")

with open("neg_dev_pre.txt", 'r') as f3:
    for line in f3.readlines():
        labeled = label_unk_words(line[:-1], 0)
        context2.append(labeled)

with open("neg_dev_unklb.txt", 'w') as f4:
    for line in context2:
        f4.writelines(line + "\n")