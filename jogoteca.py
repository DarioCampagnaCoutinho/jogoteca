from flask import Flask, render_template

app = Flask(__name__)


@app.route('/inicio')
def ola():
    lista = ['Tetris', 'Super Mário', 'Angry Birds', 'Mortal Kombat', 'Free Fire']
    return render_template('lista.html', titulo='Jogos', jogos=lista)


app.run()