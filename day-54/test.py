from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/bye')
def bye():
    return 'bye Page'


if __name__ == '__main__':
    app.run(debug=True)