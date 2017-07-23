import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import re

def file2frame(filename):
    fr = open(filename, 'rt', encoding='utf-8')
    data_list = [line.strip() for line in fr.readlines()]
    return DataFrame(data_list)

# 参数初始化
negfile = './data/meidi_jd_neg_cut.txt'
posfile = './data/meidi_jd_pos_cut.txt'
stoplist = './data/stoplist.txt'

# 读入数据
neg = file2frame(negfile)
pos = file2frame(posfile)
stop = file2frame(stoplist)

neg[1] = neg[0].apply(lambda s: re.split('\s+', s))
neg[2] = neg[1].apply(lambda x: [i for i in x if i not in list(stop[0])])
pos[1] = pos[0].apply(lambda s: re.split('\s+', s))
pos[2] = pos[1].apply(lambda x: [i for i in x if i not in list(stop[0])])

from gensim import corpora, models

# 负面主题分析
neg_dict = corpora.Dictionary(neg[2])   # 建立词典
neg_corpus = [neg_dict.doc2bow(i) for i in neg[2]]  # 建立语料库
neg_lda = models.LdaModel(neg_corpus, num_topics = 3, id2word=neg_dict)    # LDA模型训练

for i in range(3):
    neg_lda.print_topic(i)


