import json

import GetAnswers
import CreateVectorForPerson
import processing_dataset


def checkJsonData(data: str):
    try:
        json.loads(data)
    except BaseException:
        return False
    return True


def action(newData):
    #проверка корректности введенных данных
    if not checkJsonData(newData): 
        raise TypeError
    #функция принимает строку и возвращает ее обработанной
    answersArray = GetAnswers.GetAnswers(newData) 
    #база данных, полученная из json, обрабатывается и представляется pandas-объектом
    pdt = processing_dataset.processing_dataset() 
    #здесь скачивается fasttext (или navec), создаются вектора "интересов", 
    #находятся расстояния между входным и интересами из базы данных
    similarIds, similarContent = CreateVectorForPerson.findid_content(
        pdt,answersArray) 
    return similarIds, similarContent #возвращается список id и контента
