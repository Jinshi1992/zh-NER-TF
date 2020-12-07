import sys, pickle, os, random
import numpy as np

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
            sent_.append(char)
            tag_.append(label)
        else:
            data.append((sent_, tag_))
            sent_, tag_ = [], []
    #print(data)        
    
    with open("train_data_format.txt","w") as f:
        f.write(data)
    
if __name__ == "__main__":
    main()
