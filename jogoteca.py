from flask import Flask, render_template

app = Flask(__name__)


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


@app.route('/inicio')
def ola():
    jogo1 = Jogo('Super Mário', 'Ação', 'Super Nitendo')
    jogo2 = Jogo('Pokemon Go', 'Ação', 'Android')
    lista = [jogo1, jogo2]
    return render_template('lista.html', titulo='Jogos', jogos=lista)


app.run()