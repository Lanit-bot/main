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
    # "132524162":[{"questionId":"1","answer":"\"Хористы; Чернобыль\""},{"questionId":"2","answer":"\"Дюна; Благие знамения\""},{"questionId":"3","answer":"ZHU; Asking Alexandria; Ляпис Трубецкой"},{"questionId":"4","answer":"Игра на муз.инструменте"},{"questionId":"0","answer":"\"Автомобили; Путешествия; Музыка\""}]
    if not checkJsonData(newData):
        raise TypeError
    answersArray = GetAnswers.GetAnswers(newData)
    pdt = processing_dataset.processing_dataset()
    similarIds, similarContent = CreateVectorForPerson.findid_content(
        pdt,answersArray)
    return similarIds, similarContent
