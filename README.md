# Project1 -- Language Modeling and Word Embeddings

Memeber : Chengcheng Ji, Feng Qi, Tianjie Sun

This is project assignment credited by members above. DO NOT violate academic integrity.

# N-gram model
1. put the programs outside the SentimentDataset folder. Make sure there exists a subfolder called `Train` which contains `pos.txt` and `neg.txt` in SentimentDataset directory. Our codes do not handle any Error about non-exist! 
2. Run `python preprocess.py pos` or `python preprocess.py neg` to generate a file of preprocessed data. a file is named as `pos_pre.txt` or `neg_pre.txt` in the same folder which contains our python files.
3. Run `python main.py pos_pre.txt uni 5 '</s>'` to generate 5 random complete sentences using unigram model. Or run `python main.py neg_pre.txt uni 5 '</s>'`. Please make sure the last argument is _quoted_ using single quotation marks, e.g. `'</s>'` , it won't work otherwise.
You can change uni to bi for bigram, and `'</s>'` to other words like `'I'` to start from an incomplete sentence. 

# Word Embedding
Please make run do_glove.py right outside the folder SentimentDataset!
1. db.pkl: pickle file to store pre-trained word embeddings. (Not shown here due to large size of this file)
2. do_glove.py : This file is to preprocess our review set and produce averaged word representation for each review entry.

  - Run Python file directly without any needed parameter. It outputs eight file (5 csv files and 3 text files). 
  
  - All the csv files can be identified their function meaning by the name, such as `Glove_840B_Train_feature.csv` means collections of averaged word representations of each review entry from `pos.txt` and `neg.txt` of Train folder. 
  
  - `Glove_Train_not_here.txt` records all the missing words which are in our review data while not in pretrained word embedding dataset.
   
  - `Train_label.txt` records label for collections of averaged word representations of each review entry from `pos.txt` and `neg.txt` of Train folder. 0 means positive.
  
3. svm_modeling.py : machine learning pruning and modeling.
