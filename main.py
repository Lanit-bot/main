import json

import GetAnswers
import CreateVectorForPerson
import processing_dataset



def action(newData, nana, pdt):
    #функция принимает строку и возвращает ее обработанной
    answersArray = GetAnswers.GetAnswers(newData) 
    #база данных, полученная из json, обрабатывается и представляется pandas-объектом
    #pdt = processing_dataset.processing_dataset() 
    #здесь скачивается fasttext (или navec), создаются вектора "интересов", 
    #находятся расстояния между входным и интересами из базы данных
    similarIds, similarContent = CreateVectorForPerson.findid_content(
        pdt,answersArray, nana) 
    return similarIds, similarContent #возвращается список id и контента
