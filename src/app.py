from flask import Flask, render_template, request
import json

import helpers.noRepeatQuestion as helpers
import helpers.scoreCalculate as scoreCalculate

app = Flask(__name__)

@app.route('/')
def homePage():
    return render_template('home/index.html')

@app.route('/game/<int:id>', methods=['GET', 'POST'])
def telajogo(id):
    if request.method == 'GET':
        bd = open('models/bd.json', 'r')
        jsonObj = json.load(bd)

        questionRandom = helpers.noRepeatQuestion()
            
        question = jsonObj[questionRandom]
        
        bd.close()
        return render_template('screenGame/index.html', question = question, questionRandom = questionRandom)
    else:
        bd = open('models/bd.json', 'r')
        jsonObj = json.load(bd)
    
        questionVerify = jsonObj[id]

        formValue = request.form['traducao']
        if questionVerify['traducao'] == formValue:
            newQuestionRandom = helpers.noRepeatQuestion()

            scoreCalculate.uniqueScoreCalculate()
            if newQuestionRandom == 'fim':
                noQuestion = True

                score = scoreCalculate.scoreEndGame()
                scoreCalculate.clearScore()
                helpers.clearQuestion()

                return render_template('endGame/index.html', score = score, noQuestion = noQuestion)
            else:
                newQuestion = jsonObj[newQuestionRandom]

                bd.close()
                return render_template('screenGame/index.html', question = newQuestion, questionRandom = newQuestionRandom)
        else:
            score = scoreCalculate.scoreEndGame()
            scoreCalculate.clearScore()
            helpers.clearQuestion()

            bd.close()
            return render_template('endGame/index.html', score = score)
        
@app.route('/scoreall')
def scoreAllScreen():
    scoreAll = scoreCalculate.scoreAll()

    return render_template('scoreAll/index.html', scoreAll = scoreAll)

@app.route('/endGame')
def endGameScreen():
     score = scoreCalculate.scoreEndGame()
     scoreCalculate.clearScore()
     helpers.clearQuestion()

     return render_template('endGame/index.html', score = score)

if __name__ == '__main__':
    app.run(debug=True)