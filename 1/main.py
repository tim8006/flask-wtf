from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    title = "Подготовка к миссии колонизации Марса"
    return render_template('base.html', title=title)

if __name__ == '__main__':
    app.run()