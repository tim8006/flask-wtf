from flask import Flask, render_template

app = Flask(__name__)


@app.route('/training/')
@app.route('/training/<prof>')
def training(prof=None):
    title = "Подготовка к миссии колонизации Марса"
    return render_template('training.html', title=title, prof=prof)


if __name__ == '__main__':
    app.run()
