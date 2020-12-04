import sys, pickle, os, random
import numpy as np

def read_corpus(corpus_path):
    """
    read corpus and return the list of samples
    :param corpus_path:
    :return: data
    """
    data = []
    with open(corpus_path, encoding='utf-8') as fr:
        lines = fr.readlines()
    sent_, tag_ = [], []
    for line in lines:
        if line != '\n':
            char = line.strip().split(' ')[0]
            label = line.strip().split(' ')[-1]
            sent_.append(char)
            tag_.append(label)
        else:
            data.append((sent_, tag_))
            sent_, tag_ = [], []

    return data
    
def main():
   
    vocab_path = "data_path/word2id_test.pkl"
    corpus_path = "data_path/train_data"
    min_count = 10
    
    data = read_corpus(corpus_path)
    word2id = {}
    
    for sent_, tag_ in data:
        for word in sent_:
            print(word)
            if word.isdigit():
                word = '<NUM>'
            if word not in word2id:
                word2id[word] = [len(word2id)+1, 1]
            else:
                word2id[word][1] += 1
     
    new_id = 1
    for word in word2id.keys():
        word2id[word] = new_id
        new_id += 1
    word2id['<UNK>'] = new_id
    word2id['<PAD>'] = 0

    print(len(word2id))
    with open(vocab_path, 'wb') as fw:
        pickle.dump(word2id, fw)

   
   
if __name__ == "__main__":
    main()
