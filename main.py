from flask import Flask, url_for

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


@app.route('/image_mars')
def image_mars():
    ans = '<title>Привет, Марс!</title>' +\
        '<h1>Жди нас, Марс!</h1>' +\
        f'<img src={url_for("static", filename="images/MARS.png")} alt="здесь должна была быть картинка, но не нашлась">'
    return ans


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
