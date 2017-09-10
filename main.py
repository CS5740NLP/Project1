# main function to preprocess the train data and build models to generate sentences.

import sys
from n_gram import *

if __name__ ==  '__main__':

    txt = sys.argv[1]
    # read the file
    with open('%s' % txt,'r') as file:
         file_str = file.read()
    file_str = file_str.replace('\n',' ')

    # construct model
    uni_word,uni_prob,bi_word,bi_prob= gram(file_str)
    model = sys.argv[2]
    num = (int)(sys.argv[3])
    given_sentence = sys.argv[4]

    # generate random sentences
    sentence_generator(uni_word,uni_prob,bi_word,bi_prob,model,num,given_sentence)