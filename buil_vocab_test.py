import sys, pickle, os, random
import numpy as np

def read_corpus(corpus_path):
    """
    read corpus and return the list of samples
    :param corpus_path:
    :return: data
    """
    data = [];words = [];labels = []
    with open(corpus_path, encoding='utf-8') as fr:
        lines = fr.readlines()

    for line in lines:
        word = line.strip().split(' ')[0]
        label = line.strip().split(' ')[-1]
        # here we dont do "DOCSTART" check
        if len(line.strip())==0 and words[-1] == '.':
            l = ' '.join([label for label in labels if len(label) > 0])
            w = ' '.join([word for word in words if len(word) > 0])
            data.append((l,w))
            words=[]
            labels = []
        words.append(word)
        labels.append(label)
    fr.close()
    return data

def main():
   
    vocab_path = "data_path/word2id_test.pkl"
    corpus_path = "data_path/train_data"
    min_count = 10
    
    data = read_corpus(corpus_path)
    word2id = {}
    for l, w in data:
        for word in w:
        print(w)
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
