from flask import Flask

app = Flask(__name__)


@app.route('/')
def route():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return '<br>'.join('''Человечество вырастает из детства.

Человечеству мала одна планета.

Мы сделаем обитаемыми безжизненные пока планеты.

И начнем с Марса!

Присоединяйся!'''.split('\n'))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
