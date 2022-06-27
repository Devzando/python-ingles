import random

def noRepeatQuestion():
    valoresBd = open('models/valoresBd.txt', 'r')
    valoresBdAdd = open('models/valoresBd.txt', 'a')

    listNums = []

    questionRandom = random.randint(0, 5)

    for i in valoresBd.readlines():
        for x in i:
            if x != '\n':
                listNums = listNums + [int(x)]
    
    if len(listNums) != 6:
        while questionRandom in listNums:
            questionRandom = random.randint(0, 5)
    else:
        return 'fim'

    valoresBdAdd.write(str(questionRandom)+'\n')

    valoresBd.close()
    valoresBdAdd.close()

    return questionRandom

def clearQuestion():
    questionFile = open('models/valoresBd.txt', 'w')

    questionFile.write('')

    questionFile.close()