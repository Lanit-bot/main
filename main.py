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
    if not checkJsonData(newData): #проверка корректности введенных данных
        raise TypeError
    answersArray = GetAnswers.GetAnswers(newData) #функция принимает строку и возвращает ее обработанной
    pdt = processing_dataset.processing_dataset() #база данных, полученная из json, обрабатывается и представляется pandas-объектом
    similarIds, similarContent = CreateVectorForPerson.findid_content(
        pdt,answersArray) #здесь скачивается fasttext (или navec), создаются вектора "интересов", находятся расстояния между входным и интересами из базы данных
    return similarIds, similarContent #возвращается список id и контента
