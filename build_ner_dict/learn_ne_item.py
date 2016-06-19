# encoding=utf-8
from __future__ import print_function, unicode_literals

import jieba
import jieba.posseg as pseg
import xlrd
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def load_data(file_path, sheet_name='Sheet1'):
    '''
    :param file_path: 文件路径
    :param sheet_name: 工作簿名称
    :return:
    '''
    curr_dir = os.getcwd()
    f = xlrd.open_workbook(file_path)
    table = f.sheet_by_name(sheet_name)
    nrows = table.nrows
    # ncols = table.ncols
    sentences = []
    for row_idx in range(0, nrows):
        sentences.append(table.row_values(row_idx, start_colx=0, end_colx=1))
    print('Successfully load ' + str(len(sentences)) + ' sentences!')
    return sentences


def grab_ne(corpus, ner_dictionary):
    jieba.load_userdict(ner_dictionary)
    for idx,sentences in enumerate(corpus):
        list=[]
        words = pseg.cut(sentences[0])
        for word, flag in words:
            if 'ne' in flag:
                list.append(word)
        if len(list) == 0:
            list.append(idx+1)
            list.append('领域未知')
        print(list)



def small_test(corpus, ner_dictionary):
    jieba.load_userdict(ner_dictionary)

    for sentences in corpus:
        words = pseg.cut(sentences)
        for word, flag in words:
            print('%s %s' % (word, flag))


def big_test():
    corpus = load_data("01 命名实体学习表格.xlsx")
    grab_ne(corpus, "ner_model.dict")


if __name__ == '__main__':
    jieba.initialize()
    jieba.set_dictionary('/home/gyq-mac/Desktop/NLP毕业实验数据/Nuclear Event Classification and Domain Recognition/01 Named entity recognition/build_ner_dict/dict.txt.small')
    corpus = ["空气干燥机与接管位置与图纸不符"]
    small_test(corpus, "/home/gyq-mac/Desktop/NLP毕业实验数据/Nuclear Event Classification and Domain Recognition/01 Named entity recognition/build_ner_dict/ner_model.dict")
    #big_test()






