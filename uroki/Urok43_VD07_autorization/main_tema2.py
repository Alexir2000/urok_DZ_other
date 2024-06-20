from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm # Это базовый класс для создания форм
from wtforms import StringField, SubmitField # Это классы для создания полей внутри формы
from wtforms.validators import DataRequired # Валидатор, нужный для проверки


app = Flask(__name__)

app.config['SECRET_KEY'] = 'your_secret_key'

template1 = "index.html"

# Создаем свой класс формы на основе родительского от Flask с теми полями, которые нам нужны
class NameForm(FlaskForm): # Используем FlaskForm в качестве родительского класса
    # Создаем свое поле или поля. В данном случае одно поле c типом String
    name = StringField('Как Ваше имя?', validators=[DataRequired()])
    # name.error = "Надо заполнить это поле" # можно ли так? поставить свой текст ошибки на валидацию
    submit = SubmitField('Отправить данные')

@app.route('/', methods=['GET', 'POST']) #  С помощью этого маршрута мы сможем и отправлять, и получать информацию
def index():
    form = NameForm() #  Создаём объект формы
    form.name.label = "Как Ваше имя?"
    if form.validate_on_submit(): # Проверка того, прошла ли форма валидацию и вообще отправлена ли она
        name = form.name.data #  Получаем значение из формы, информацию из этого значения. Сохраняем в переменную
        return redirect(url_for('hello', name=name)) # Отправляем пользователя на новую страницу, передаём полученное имя
    return render_template(template1, form=form)

@app.route('/hello/<name>')
def hello(name):
    return f'Привет, {name}!. Вы авторизовались и вошли на сайт!'

if __name__ == '__main__':
    app.run(debug=True)