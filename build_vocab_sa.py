import sys, pickle, os, random
import numpy as np

def read_corpus(corpus_path):
    """
    read corpus and return the list of samples
    :param corpus_path:
    :return: data
    """
    data = []
    
    f = open(corpus_path, 'r')
    lines = []
    for line in f:
      lines.append(line)

    for i, line in enumerate(lines):
      if i == 0:
            continue
      split_line=line.strip().split('+++$+++')
      sent = split_line[1]
      words = sent.strip().split(' ') #把一个sentence的word都打散
      data.append(words) # 将当前句子的数组添加到data里面
    
    return data
    
def main():
   
    vocab_path = "data_path/word2id_sa_en.pkl"
    
    test_sa_path = "data_path/pkl_test"
    #train_path = "data_path/train_data"
    #test_path = "data_path/test_data"
    #dev_path = "data_path/dev_data"
    
    min_count = 3
    
    data_sa_test = read_corpus(test_sa_path)
    #data_train = read_corpus(train_path)
    #data_dev = read_corpus(dev_path)
    #data_test = read_corpus(test_path)
    
    #data = data_train + data_test
    data = data_sa_test
    word2id = {}
    
    for words in data:
        for word in words:
            if word.isdigit():
                word = '<NUM>'
            if word not in word2id:
                word2id[word] = [len(word2id)+1, 1]
            else:
                word2id[word][1] += 1
                
    low_freq_words = []
    for word, [word_id, word_freq] in word2id.items():
        if word_freq < min_count and word != '<NUM>' and word != '<ENG>':
            low_freq_words.append(word)
    for word in low_freq_words:
        del word2id[word]

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
