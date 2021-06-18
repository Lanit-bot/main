from navec import Navec
import json
import spellchecker
import pymorphy2
import csv
import pandas as pd
import string
import numpy as np
from scipy.spatial.distance import cosine


def vecofdists(vecint, pdt, inpint):
    coscos = []
    for i in range(len(vecint)):
        idi = pdt['id'].iloc[i]
        cosa = cosine(vecint[i], inpint)
        if np.isnan(cosa):
            continue
        cel = [cosa, idi]
        coscos.append(cel)
        #print(cosa)
    coscos.sort(key=lambda x: x[0])
    return coscos


def get_sentence_vector(unline,nana):
    ws = unline.split('_')
    vw = []
    for i in ws:
        try:
            vw.append(nana[i])
        except KeyError:
            vw.append(nana['<unk>'])
    ans = np.mean(vw, axis=0)
    return ans

def get_mean(str, nana):  # получение вектора интересов
    word = str.split(' ')
    vw = []
    for i in word:
        vw.append(get_sentence_vector(i,nana))
    ans = np.mean(vw, axis=0)
    #print(ans.shape)
    return ans

def findint(hip,pdt,inte):
    i = 0
    while i < len(hip) and pd.isna(pdt[pdt['id'] == hip[i][1]][inte].iloc[0]):
        i+=1
    #print(pdt[pdt['id'] == hip[i][1]][inte])
    return pdt[pdt['id'] == hip[i][1]][inte].iloc[0]

def findid_content(pdt, end, nana):
#    path = 'navec_hudlit_v1_12B_500K_300d_100q.tar'
#    nana = Navec.load(path)
    vecint = []  # здесь хранятся все вектора интересов (у кого они заполнены)
    for i in pdt[pdt['Пол'].notnull()]['все интересы']:
        vecint.append(get_mean(i,nana))
    inpint = get_mean(end,nana)
    hip = vecofdists(vecint, pdt, inpint)
    movie = findint(hip, pdt, 'Фильм')
    book = findint(hip, pdt, 'Книга')
    music = findint(hip, pdt, 'Музыка')
    bofimu = movie+ " - "+ book+ " - "+music
    final = []
    final.append([hip[0][1], hip[1][1], hip[2][1]])
    final.append(bofimu)
    return final
