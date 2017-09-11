# Project1 -- Language Modeling and Word Embeddings

Memeber : Chengcheng Ji, Feng Qi, Tianjie Sun

This is project assignment credited by members above. DO NOT violate academic integrity.

# How to run the program
1. put the programs outside the SentimentDataset folder. Make sure there exists a subfolder called `Train` which contains `pos.txt` and `neg.txt` in SentimentDataset directory. Our codes do not handle any Error about non-exist! 
2. Run `python preprocess.py pos` or `python preprocess.py neg` to generate a file of preprocessed data. a file is named as `pos_pre.txt` or `neg_pre.txt` in the same folder which contains our python files.
3. Run `python main.py pos_pre.txt uni 5 '</s>'` to generate 5 random complete sentences using unigram model. Or run `python main.py neg_pre.txt uni 5 '</s>'`. Please make sure the last argument is _quoted_ using single quotation marks, e.g. '</s>' , it won't work otherwise.
You can change uni to bi for bigram, and '</s>' to other words like 'I' to start from an incomplete sentence. 
