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
    scoreEnd = ''

    if score < 10:
        scoreEnd = '0'+str(score)
        print('teste')
        scoreAll.write(str(score) + '\n')
        scoreAll.close()
        return scoreEnd

    scoreAll.write(str(score) + '\n')
    scoreAll.close()

    return score

    
def clearScore():
    uniqueScore = open('models/uniqueScore.txt', 'w')

    uniqueScore.write('')

    uniqueScore.close()

def scoreAll():
    scoreAllRead = open('models/scoreAll.txt', 'r')

    valueScore = []

    for i in scoreAllRead.readlines():
        for x in i:
            if x != '\n':
                valueScore = valueScore + [int(x)]

    scoreAllRead.close()

    scoreAllWrite = open('models/scoreAll.txt', 'w')

    trocou = True
    fim = len(valueScore) -1
    while fim > 0 and trocou:
        trocou = False
        for i in range(fim):
            if valueScore[i] < valueScore[i+1]:
                trocou = True
                temp = valueScore[i]
                valueScore[i] = valueScore[i+1]
                valueScore[i+1] = temp
        fim = fim -1
        
    scoreAllWrite.write('')
    scoreAllWrite.close()

    scoreAllAdd = open('models/scoreAll.txt', 'a')

    for i in range(len(valueScore)):
        scoreAllAdd.write(str(valueScore[i]) + '\n')
    scoreAllAdd.close()

    return valueScore
