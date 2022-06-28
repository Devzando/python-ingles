def uniqueScoreCalculate():
    uniqueScore = open('models/uniqueScore.txt', 'a')

    valueScore = 1

    uniqueScore.write(str(valueScore)+'\n')

    uniqueScore.close()

def scoreEndGame():
    uniqueScore = open('models/uniqueScore.txt', 'r')
    scoreAll = open('models/scoreAll.txt', 'a')
    score = 0

    for i in uniqueScore.readlines():
        for x in i:
            if x != '\n':
                score= score + int(x)

    uniqueScore.close()

    scoreAll.write(str(score) + '\n')
    scoreAll.close()

    return score

    
def clearScore():
    uniqueScore = open('models/uniqueScore.txt', 'w')

    uniqueScore.write('')

    uniqueScore.close()

def scoreAll():
    scoreAllRead = open('models/scoreAll.txt', 'r')

    valueScoreList = []
    valueScoreListFinal = []
    valueScore = ''

    for i in scoreAllRead.readlines():
        for x in i:
            if x != '\n' and x != '':
                valueScore = valueScore + x
            if x == '\n':
                valueScoreList = valueScoreList + [int(valueScore)]
                valueScore = ''
            
    scoreAllRead.close()

    trocou = True
    fim = len(valueScoreList) -1
    while fim > 0 and trocou:
        trocou = False
        for i in range(fim):
            if valueScoreList[i] < valueScoreList[i+1]:
                trocou = True
                temp = valueScoreList[i]
                valueScoreList[i] = valueScoreList[i+1]
                valueScoreList[i+1] = temp
        fim = fim -1

    idx = 1
    for i in valueScoreList:
        if idx <= 5:
            valueScoreListFinal = valueScoreListFinal + [i]
        idx = idx + 1
        

    return valueScoreListFinal
