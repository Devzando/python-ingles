import random
import json

def noRepeatQuestion():
    valoresBd = open('models/valoresBd.txt', 'r')
    valoresBdAdd = open('models/valoresBd.txt', 'a')

    bd = open('models/bd.json', 'r')
    jsonObj = json.load(bd)


    listNums = []

    questionRandom = random.randint(0, len(jsonObj) - 1)

    for i in valoresBd.readlines():
        for x in i:
            if x != '\n':
                listNums = listNums + [int(x)]
    
    if len(listNums) < len(jsonObj):
        while questionRandom in listNums:
            questionRandom = random.randint(0, len(jsonObj) - 1)
    else:
        return 'fim'

    valoresBdAdd.write(str(questionRandom)+'\n')

    bd.close()
    valoresBd.close()
    valoresBdAdd.close()

    return questionRandom

def clearQuestion():
    questionFile = open('models/valoresBd.txt', 'w')

    questionFile.write('')

    questionFile.close()