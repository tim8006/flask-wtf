from flask import Flask, render_template, request, url_for

app = Flask(__name__)

PROFESSIONS = ['инженер-исследователь', 'пилот', 'строитель', 'футболист', 'врач',
               'баскетболист', 'тенниссист', 'полицейский', 'штурман',
               'месси', 'гений', 'инженер жизнеобеспечения', 'метеоролог', 'пилот дронов']


@app.route('/list_prof/<type>')
def list_prof(type: str):
    params = {'type': type, 'professions': PROFESSIONS}
    return render_template('list_prof.html', **params)


if __name__ == '__main__':
    app.run()
