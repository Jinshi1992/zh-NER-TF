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

    with open('train_data_format.txt', 'w') as fp:
        for char, label in data:
            fp.write('\n'.join(["%s %s" % (char, label)]) + "\n")
    
    
if __name__ == "__main__":
    main()
