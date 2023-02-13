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


@app.route('/<path>/promotion_image')
def promotion_image(path):
    ans = f'''<!DOCTYPE html>
<html lang="ru">

    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
        <title>Колонизация</title>
    </head>

    <body>
        <h1>Жди нас, Марс!</h1>
        <img src="{url_for('static', filename='images/MARS.png')}" alt="здесь должна была быть картинка, но не нашлась">
        <div class="alert alert-primary" role="alert">
            Человечество вырастает из детства.
        </div>
        <div class="alert alert-secondary" role="alert">
            Человечеству мала одна планета.
        </div>
        <div class="alert alert-success" role="alert">
            Мы сделаем обитаемыми безжизненные пока планеты.
        </div>
        <div class="alert alert-danger" role="alert">
            И начнем с Марса!
        </div>
        <div class="alert alert-warning" role="alert">
            Присоединяйся!
        </div>
    </body>

</html>'''
    return ans


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
