from flask import Flask

app = Flask(__name__)


@app.route("/info")
def index():
    return {'info': 'some information'}


if __name__ == '__main__':
    app.run(debug=True) 