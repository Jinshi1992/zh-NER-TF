import sys, pickle, os, random
import numpy as np

self.max_iter = None

def read_corpus(self, corpus_path):
    """
    read corpus and return the list of samples
    :param corpus_path:
    :return: data
    """
    niter = 0
    with open(self.filename) as f:
        words, tags = [], []
        lines = []
        for line in f:
            line = line.strip()
            if (len(line) == 0 or line.startswith("-DOCSTART-")):
                if len(words) != 0:
                    niter += 1
                    if self.max_iter is not None and niter > self.max_iter:
                        break
                    yield words, tags
                    words, tags = [], []
            else:
                ls = line.split(' ')
                word, tag = ls[0],ls[1]
                word = self.processing_word(word)
                tag = self.processing_tag(tag)
                lines.append((tag,word))
                words += [word]
                tags += [tag]
        return lines
    
def main():
   
    vocab_path = "data_path/word2id_test.pkl"
    corpus_path = "data_path/train_data"
    min_count = 10
    
    data = read_corpus(corpus_path)
    word2id = {}
    for l, w in data:
        for word in w:
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
