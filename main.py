from flask import Flask, url_for, request

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


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
<html lang="en">

    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
        <title>Пример формы</title>
    </head>

    <body>
        <h1>Анкета претендента<br><span>на участие в миссии</span></h1>
        <div class="container">
            <form class="astro-form" method="post">
                <input type="surname" class="form-control" id="text" aria-describedby="emailHelp"
                    placeholder="Введите фамилию" name="surname">
                <input type="name" class="form-control" id="text" placeholder="Введите имя" name="name">
                <br>
                <input type="email" class="form-control" id="email" placeholder="Введите адрес почты" name="email">
                <div class="form-group">
                    <label for="educationSelect">Какое у вас образование?</label>
                    <select class="form-control" id="educationSelect" name="education">
                        <option>Начальное</option>
                        <option>Среднее</option>
                        <option>Высшее</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="form-check">Какие у Вас есть профессии?</label>
                    <div class="form-check">
                        <input class="form-check-input" type="checkbox" name="sex" id="1" value="1">
                        <label class="form-check-label" for="1">
                            Инженер-исследователь
                        </label>
                    </div>
                    <div class="form-check">
                        <input class="form-check-input" type="checkbox" name="sex" id="2" value="2">
                        <label class="form-check-label" for="2">
                            Инженер-строситель
                        </label>
                    </div>
                    <div class="form-check">
                        <input class="form-check-input" type="checkbox" name="sex" id="3" value="3">
                        <label class="form-check-label" for="3">
                            Пилот
                        </label>
                    </div>
                    <div class="form-check">
                        <input class="form-check-input" type="checkbox" name="sex" id="4" value="4">
                        <label class="form-check-label" for="4">
                            Метеоролог
                        </label>
                    </div>
                    <div class="form-check">
                        <input class="form-check-input" type="checkbox" name="sex" id="5" value="5">
                        <label class="form-check-label" for="5">
                            Инженер по жизнеобеспечению
                        </label>
                    </div>
                    <div class="form-check">
                        <input class="form-check-input" type="checkbox" name="sex" id="6" value="6">
                        <label class="form-check-label" for="6">
                            Инженер по радиационной защите
                        </label>
                    </div>
                    <div class="form-check">
                        <input class="form-check-input" type="checkbox" name="sex" id="7" value="7">
                        <label class="form-check-label" for="7">
                            Врач
                        </label>
                    </div>
                    <div class="form-check">
                        <input class="form-check-input" type="checkbox" name="sex" id="8" value="8">
                        <label class="form-check-label" for="8">
                            Экзобиолог
                        </label>
                    </div>
                </div>
                <div class="form-group">
                    <label for="form-check">Укажите пол</label>
                    <div class="form-check">
                        <input class="form-check-input" type="radio" name="prof" id="male" value="male" checked>
                        <label class="form-check-label" for="male">
                            Мужской
                        </label>
                    </div>
                    <div class="form-check">
                        <input class="form-check-input" type="radio" name="prof" id="female" value="female">
                        <label class="form-check-label" for="female">
                            Женский
                        </label>
                    </div>
                </div>
                <div class="form-group">
                    <label for="reason">Почему вы хотите принять участие в миссии?</label>
                    <textarea class="form-control" id="reason" rows="3" name="reason"></textarea>
                </div>
                <div class="form-group">
                    <label for="photo">Приложите фотографию</label>
                    <input type="file" class="form-control-file" id="photo" name="file">
                </div>
                <div class="form-group form-check">
                    <input type="checkbox" class="form-check-input" id="readyToStay" name="readyToStay">
                    <label class="form-check-label" for="readyToStay">Готов остаться на Марсе?</label>
                </div>
                <button type="submit" class="btn btn-primary">Отправить</button>
            </form>
        </div>
    </body>

</html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['education'])
        print(request.form['prof'])
        print(request.form['sex'])
        print(request.form['reason'])
        print(request.form['file'])
        print(request.form['readyToStay'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
