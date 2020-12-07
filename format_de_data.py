import sys, pickle, os, random
import numpy as np
import csv

def main():
    """
    read corpus and return the list of samples
    :param corpus_path:
    :return: data
    """
    
    corpus_path = "data_path/train_data"
    
    data = []
    with open(corpus_path, encoding='utf-8') as fr:
        lines = fr.readlines()
    sent_, tag_ = [], []
    for line in lines:
        if line != '\n':
            char = line.strip().split(' ')[0]
            label = line.strip().split(' ')[-1]
            data.append((char, label))
        else:
            data.append(line)

    with open('data_path/train_data_format.txt', 'w') as fp:
        for i in data:
            if i != '\n':
                fp.write('\n'.join('{} {}'.format(i[0], i[1])))
            else:
                fp.write('\n')
        fp.close()
    
    
if __name__ == "__main__":
    main()
