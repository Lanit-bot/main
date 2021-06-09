import json

import GetAnswers
import CreateVectorForPerson
import FindSimilarPerson


def checkJsonData(data: str):
    try:
        json.loads(data)
    except:
        return False
    return True

def main():
    # "132524162":[{"questionId":"1","answer":"\"Хористы; Чернобыль\""},{"questionId":"2","answer":"\"Дюна; Благие знамения\""},{"questionId":"3","answer":"ZHU; Asking Alexandria; Ляпис Трубецкой"},{"questionId":"4","answer":"Игра на муз.инструменте"},{"questionId":"0","answer":"\"Автомобили; Путешествия; Музыка\""}]
    newData = input()  # input json string
    if not checkJsonData(newData):
        raise TypeError
    answersArray = GetAnswers.GetAnswers(newData)
    vectorMatrix = CreateVectorForPerson.CreateVector(answersArray)
    personIds = FindSimilarPerson.GetSimilarPerson(vectorMatrix)
    return personIds


if __name__ == '__main__':
    main()
