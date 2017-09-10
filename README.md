# Project1
# Language Modeling and Word Embeddings

Memeber : Chengcheng Ji, Feng Qi, Tianjie Sun

This is project assignment credited by members above. DO NOT violate academic integrity.


# How to run the program
1. put the programs outside the SentimentDataset folder.
2. Run `python preprocess.py pos.txt > pre_pos.txt` to preprocess the training data
3. Run `python main.py pre_pos.txt uni 5 '</s>'` to generate 5 random complete sentences using unigram model.
You can change uni to bi for bigram, and '</s>' to other words like 'I' to start from an incomplete sentence. 
