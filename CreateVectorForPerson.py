import fasttext.util as fu
import fasttext
import json
from spellchecker import SpellChecker
import pymorphy2
import csv
import pandas as pd
import string

def vecofdists(vecint):
    coscos = []
    for i in range(len(vecint)):
        idi = pdt['id'].iloc[i]
        cosa = cosine(vecint[i],inpint)
        if np.isnan(cosa):
            continue
        cel = [cosa,idi]
        coscos.append(cel)
    coscos.sort(key=lambda x: x[1])
    ans = [coscos[0],coscos[1],coscos[2]]
    return ans

def get_mean(str): #получение вектора интересов
    word = str.split(' ')
    vw = []
    for i in word:
        vw.append(ft.get_sentence_vector(i))
    ans = np.mean(vw, axis = 0)
    print(ans.shape)
    return ans

def findid_content(pdt,end):
    fu.download_model('ru', if_exists='ignore')
    ft = fasttext.load_model('cc.ru.300.bin')
    vecint = [] #здесь хранятся все вектора интересов (у кого они заполнены)
    for i in pdt[pdt['Пол'].notnull()]['все интересы']:
        vecint.append(get_mean(i))
        inpint = get_mean(end[1])
        vecdist = []
        hip = vecofdists(vecint)
        bofimu = pdt[pdt['id'] == hip[0][1]]['Фильм']+pdt[pdt['id'] == hip[0][1]]['Книга']+pdt[pdt['id'] == hip[0][1]]['Музыка']
        final = []
        final.append([hip[0][1],hip[1][1],hip[2][1]])
        final.append(bofimu)
        return final   

