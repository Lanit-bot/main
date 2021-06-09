import json
from spellchecker import SpellChecker
import pymorphy2
import csv
import pandas as pd
import string


def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True
    
def empty(nn):
    nn = ''.join(e for e in nn if e.isalnum())
    if nn == '':
        return True
    else:
        return False
    
def checking(a):
    mm = pymorphy2.MorphAnalyzer()
    ans = ''
    cra = a.split(' ')
    for i in range(len(cra)):
        if not isEnglish(cra[i]):
            prev = cra[i]
            cra[i] = mm.parse(cra[i])[0].normal_form
            if cra[i] == None:
                cra[i] = prev
        ans+=cra[i]
        if i != len(cra)-1:
            if len(cra[i]) > 0 and cra[i][0].isalnum():
                ans+='_'
    return ans
            
def splitters(anq):
    if anq!='':
        anq1 = ''
        #print(anq)
        meow = anq.split(';')
        for i in range(len(meow)):
            meow[i] = checking(meow[i])
            meow[i] = ''.join(e for e in meow[i] if e.isalnum() or e=="_")
            meow[i] = meow[i].lower()
            anq1+=meow[i]+' '
    return anq1
  
def makes(lis):
    #print(type(lis))
    str = ''
    meow = 0
    for i in lis:
        #print(i)
        str+=i
        if meow!=len(lis)-1 and i != '':
            str+=' '
        meow+=1
    return str

def finds_rep(lis,zn1,zn2):
    for i in lis:
        #print(i,zn1)
        if zn1 in i:
            #print(i)
            lis.remove(i)
            lis.append(zn2)
    return lis
  

with open("questionary-2.json", "r", encoding="utf8") as read_file:
    now = json.load(read_file)

with open("users.csv", mode="r", encoding='latin-1') as gen:  #вставка пола, муж - 0, жен - 1
    csv_reader = csv.reader(gen, delimiter=',')
    line = 0
    muz = ''
    for row in csv_reader:    
        na = row[0]
        se = row[1]
        if line == 0:
            line+=1
            muz = se
        if se == muz:
            se = '0'
        else:
            se = '1'
        try:
            if now[0]['participations'][na] != None:
                try:
                    if type(now[0]['participations'][na]) == list:
                        now[0]['participations'][na].append({'questionId':'5','answer':se})
                    else:
                        jetz = now[0]['participations'][na]
                        now[0]['participations'][na] = [jetz]
                        now[0]['participations'][na].append({'questionId':'5','answer':se})
                except AttributeError:
                    print(na)
            else:
                now[0]['participations'][na] = [{'questionId':'5','answer':se}]
        except KeyError:
            pass
        
with open("dataset.csv", mode="w", encoding='utf-8') as w_file: 
    file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
    file_writer.writerow(["id", "Интересы", "Фильм","Книга", "Музыка","Желаемое хобби","Пол"])
    for key, value in now[0]['participations'].items():
        row = [key]+['']*6
        if value != None:
            for meow in value:
                #print(key, meow)
                idq = meow['questionId']
                anq = meow['answer']
                anq = splitters(anq)
                print(anq)
                row[int(idq)+1] = anq
        file_writer.writerow(row) #до этого момента создается таблица со значениями
        
pdt = pd.read_csv('dataset.csv')
pdt.loc[:, 'все интересы'] = pdt['Интересы'] + ' ' + pdt['Желаемое хобби']
pdt.drop('Интересы', axis=1, inplace=True)
pdt.drop('Желаемое хобби', axis=1, inplace=True)
pdt['все интересы'].fillna(' ', inplace = True)
pdt.loc[:, 'все интересы'] = pdt.loc[:, 'все интересы'].str.split(' ')
fir = ['веосипед','велосипед','it','coding', 'путешествие', 'авто', 'альпин','йог','английский','компьютерный_игра','есть', 'барабан',
      'гитар', 'клавиш', 'фортепиано','компьютер_сборка', "нет_такой",'вино','чтение', 'шить', 'швейный', 'спортилитанец', 
      'танцы','танец','спорт','книг']
sec = ['велосипед','велосипед','программирование','программирование','путешествие','авто','альпинизм','йога','английский','видеоигра','еда','барабаны','гитара','фортепиано','фортепиано','компьютерныйжелезо',
       ' ','вино','книги','шить','шить','танец','танец','танец','спорт','книги']
for i in range (len(pdt['все интересы'])):
    for j in range(26):
        pdt.at[i,'все интересы'] = finds_rep(pdt.at[i,'все интересы'],fir[j],sec[j])
    pdt.at[i,'все интересы'] = makes(pdt.at[i,'все интересы'])
