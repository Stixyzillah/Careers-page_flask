from flask import Flask, render_template

app = Flask(__name__)
JOBS = [{
    'id': 1,
    'title': 'Data Engineer',
    'location': 'Lilongwe, Malawi',
    'salary': '$. 200,000',
}, {
    'id': 2,
    'title': 'Data Analyst',
    'location': 'Blantyre, Scotland',
    'salary': '$. 100,000',
}, {
    'id': 3,
    'title': 'Data scientist',
    'location': 'Remote',
}, {
    'id': 4,
    'title': 'Backend engineer',
    'location': 'Remote',
    'salary': '$. 200,000',
}]


@app.route('/')
def hello_world():
    return render_template('home.html', jobs=JOBS)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
