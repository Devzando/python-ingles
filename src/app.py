from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homePage():
    return render_template('home/index.html')
@app.route('/jogo')
def telajogo():
    return render_template('ScreenGame/index.html')

if __name__ == '__main__':
    app.run()