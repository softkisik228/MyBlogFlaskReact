from flask import Flask, request

app = Flask(__name__)


@app.route("/info")
def index():
    return {'info': 'some information'}


@app.route('/', methods=['GET', 'POST'])
def add_post():
    data = request.data
    print(data)
    
if __name__ == '__main__':
    app.run(debug=True) 