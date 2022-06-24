from flask import Flask, render_template, request
import json

import helpers.noRepeatQuestion as helpers

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

            newQuestion = jsonObj[newQuestionRandom]

            bd.close()
            return render_template('screenGame/index.html', question = newQuestion, questionRandom = newQuestionRandom)
        else:
            bd.close()
            return 'teste'
        

if __name__ == '__main__':
    app.run(debug=True)