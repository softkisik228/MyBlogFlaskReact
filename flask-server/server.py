import statistics
from flask import Flask, request
import sqlite3
import json
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/info')
def index():
    return {'info': 'some information'}


@app.route('/get_posts', methods=['GET'])
def get_posts():
    try:
        con = sqlite3.connect("posts.db")
        cur = con.cursor()
        cur.execute("""SELECT * FROM posts""")
        posts = json.dumps(cur.fetchall(), ensure_ascii=False)
        return posts
    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)
        return None, statistics.HTTP_500_INTERNAL_SERVER_ERROR
    finally:
        print('[INFO] PostgreSQL connection closed')


@app.route('/add_post', methods=['POST'])
def add_post():
    if request.method == 'POST':
        post = request.get_json(force=True)
        try:
            con = sqlite3.connect("posts.db")
            cur = con.cursor()
            cur.execute(
                    f"""INSERT INTO posts(post, nickname, date) VALUES
                    ('{post['post']}', '{post['nickname']}', '{post['date']}    ');""")
            con.commit()
        except Exception as _ex:
            print('[INFO] Error while working with PostgreSQL', _ex)
            return None, statistics.HTTP_500_INTERNAL_SERVER_ERROR
        finally:
            print('[INFO] PostgreSQL connection closed')
    return {'status': '200'}
    
if __name__ == '__main__':
    app.run(debug=True)