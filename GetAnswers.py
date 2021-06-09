import csv #БОЛЬШЕ НЕ ЗАПУСКАТЬ ТАБЛИЦА ЕСТЬ В CSV
from spellchecker import SpellChecker
import pymorphy2

def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True
    
    
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

injson = input()
meow = injson.replace('[','').replace('{','').replace(']','').replace('}','').replace('"','').replace('answer','').replace('questionId:','').replace(':',',').replace(',,',',')
end = ['','','','','','']
ans = meow.split(',')
for i in range(len(ans)):
    try:
        if int(ans[i]) > 5:
            end[0] = ans[i]
        else:
            end[int(ans[i])+1] = ans[i+1]
    except ValueError:
        pass
    #print(end)
#в end хранится список сортированный
for i in range(len(end)):
    end[i] = splitters(end[i])
