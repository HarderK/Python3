import pandas as pd
from pandas import DataFrame, Series
import jieba

inputfile1 = './data/meidi_jd_neg.txt'
inputfile2 = './data/meidi_jd_pos.txt'
outputfile1 = './data/meidi_jd_neg_cut.txt'
outputfile2 = './data/meidi_jd_pos_cut.txt'

def file2frame(filename):
    fr = open(filename, 'rt', encoding='utf-8')
    data_list = [line.strip() for line in fr.readlines()]
    return DataFrame(data_list)

data1 = file2frame(inputfile1)
data2 = file2frame(inputfile2)

mycut = lambda s: ' '.join(jieba.cut(s))

data1 = data1[0].apply(mycut)
data2 = data2[0].apply(mycut)

data1.to_csv(outputfile1, index=False, header=False, encoding='utf-8')
data2.to_csv(outputfile2, index=False, header=False, encoding='utf-8')