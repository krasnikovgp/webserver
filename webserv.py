from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return f"""
    <h1>Мой Сервер</h1>
    <p><a href="{url_for('index')}">Сайт</a></p>
    <p><a href="{url_for('start')}">Старт</a></p>
    <p><a href="{url_for('base')}">База</a></p>
    """


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/day-<num>')
def day(num):
    return render_template(f'day-{num}.html')


@app.route('/photo-<num>')
def photo(num):
    return render_template(f'photo-{num}.html')


@app.route('/start')
def start():
    return render_template('start.html')


@app.route('/base')
def base():
    return render_template('base.html')


if __name__ == '__main__':
    app.run(debug=True)
