# this module offers funtion to build a unigram and bigram model and 
# another funtion to generate random sentences using existing model. 

import numpy as np

# construct unigram and bigram through corpus string. 
# Return gram list and corresponding probabiliy.

def gram(string):
    # count uni bi tri words
    words = string.split()
    uni_cnt = {}; bi_cnt = {}; tri_cnt = {}
    pre_word = words[0]
    pre_word2 = words[1]
    uni_cnt[pre_word] = 1
    uni_cnt[pre_word2] = 1
    bi_cnt[(pre_word,pre_word2)]=1
    for word in words[2:]:
        uni = word
        bi = (pre_word2,word)
        tri = (pre_word,pre_word2,word)
        
        if uni in uni_cnt: 
            uni_cnt[uni] += 1
        else: uni_cnt[uni] = 1
    
        if bi in bi_cnt:
            bi_cnt[bi] += 1
        else: bi_cnt[bi] = 1
       
        if tri in tri_cnt :
            tri_cnt[tri] += 1           
        else:            
            tri_cnt[tri] =1
        pre_word = pre_word2
        pre_word2 = word
        
    # calculate uni probabiliy
    length = len([word for word in words if word != "</s>"])
    uni_word = uni_cnt.keys() 
    uni_prob = []
    for word in uni_word:
        prob = (float)(uni_cnt[word])/length
        uni_prob.append(prob)
    
    # calculate bi probability
    bi_word = {}
    bi_prob = {}
    for word in bi_cnt:
        pre = word[0]
        w = word[1]
        prob = (float)(bi_cnt[word])/uni_cnt[pre]
        if pre not in bi_word:
            bi_word[pre] = [w]
            bi_prob[pre] = [prob]
        elif type(bi_word[pre])==list and type(bi_prob[pre])==list:
            bi_word[pre].append(w)
            bi_prob[pre].append(prob)
  
   # calculate tri probablity
    tri_word = {}
    tri_prob = {}
    for word in tri_cnt:        
        pre = (word[0], word[1])
        w = word[2]
        prob = (float)(tri_cnt[word])/bi_cnt[(pre)]
        if pre not in tri_word:
            tri_word[pre] = [w]
            tri_prob[pre] = [prob]
        elif type(tri_word[pre])==list and type(tri_prob[pre])==list:
            tri_word[pre].append(w)
            tri_prob[pre].append(prob)
        
    
    return length,uni_word,uni_cnt,uni_prob,bi_word,bi_cnt,bi_prob,tri_word,tri_cnt,tri_prob



# generate one or many random sentences using given model and given incomplete sentence.
# Default is to generate one complete sentence using unigram model.

def sentence_generator(uni_word,uni_prob,bi_word,bi_prob,model='uni',num=2, given_str='</s>'):
    if model=='uni':
        print 'Unigram sentence generator: %i sentences' %num
        for i in xrange(num):
            sentence = '' if given_str=='</s>' else given_str
            word = given_str
            while (word!='</e>'):
                sample = np.array(uni_word)
                prob = np.array(uni_prob)
                word = np.random.choice(sample,p=prob)
                sentence = sentence+' '+word if word!='</e>'else sentence
            print (str)(i+1) + '. ' + sentence.replace('</e>','').replace('</s> ','') + '\n'
    
    elif model=='bi':
        print 'Bigram sentence generator: %i sentences' %num
        for i in xrange(num):
            sentence = '' if given_str=='</s>' else given_str
            word = given_str.split()[-1]
            while (word!='</e>'):
                if word in bi_word:
                    sample = np.array(bi_word[word])
                    prob = np.array(bi_prob[word])
                    word = np.random.choice(sample,p=prob)
                    sentence = sentence + ' ' + word if word!='</e>' else sentence
                else:
                    print 'The word is not in the training set '
                    break
            print (str)(i+1) + '. ' + sentence.replace('</e>','') + '\n'
    else: print 'Warning! Please select uni or bi grams'



