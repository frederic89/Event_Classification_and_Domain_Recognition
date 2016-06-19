# coding: utf-8
__author__ = 'gyq-mac'


import sys

reload(sys)
sys.setdefaultencoding("utf-8")

# import os

from tgrocery import Grocery

import xlrd


file_path = 'ner_model.xlsx'
project_name = 'ner_predict'


def grab_data(file_path):
    sentences = []
    f = xlrd.open_workbook(file_path)
    table = f.sheet_by_name('Sheet1')
    nrows = table.nrows  # 读取行数
    for rownum in range(0, nrows):
        row = table.row_values(rownum)
        row[0].strip().split()
        row[1].strip().split()
        sentences.append((row[0], row[1]))
    return sentences

def predict_corpus(input_file,output_csv):
    import csv
    csvfile = file(output_csv, 'wb')
    writer = csv.writer(csvfile)
    corpus = []
    f = xlrd.open_workbook(input_file)
    table = f.sheet_by_name('Sheet1')
    nrows = table.nrows  # 读取行数
    for rownum in range(0, nrows):
        row = table.row_values(rownum)
        row[2].strip()
        corpus.append(row[2])
    corpus_grocery = Grocery(project_name)
    corpus_grocery.load()
    output = []
    for sentence in corpus:
        predict = corpus_grocery.predict(sentence)
        output.append((sentence,predict))
    writer.writerows(output)
    print('Done!')
    csvfile.close()


grocery = Grocery(project_name)  # 项目名称
train_src = grab_data(file_path)
grocery.train(train_src)
grocery.save()
predict_corpus('NER_test.xlsx','ner_output.csv')
