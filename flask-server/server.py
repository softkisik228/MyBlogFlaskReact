import statistics
from flask import Flask, request
from flask_cors import CORS
import psycopg2
from config import host, password, user, db_name

app = Flask(__name__)

@app.route('/info')
def index():
    print(2)
    return {'info': 'some information'}


@app.route('/add_post', methods=['POST'])
def add_post():
    if request.method == 'POST':
        post = request.get_json(force=True)
        try:
            connection = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                database=db_name
            )


            with connection.cursor() as cursor:
                cursor.execute(
                    f"""INSERT INTO posts(post, nickname, date) VALUES
                    ('{post['post']}', '{post['nickname']}', '{post['date']}    ');""")

                connection.commit()
        except Exception as _ex:
            print('[INFO] Error while working with PostgreSQL', _ex)
            return None, statistics.HTTP_500_INTERNAL_SERVER_ERROR
        finally:
            if connection:
                connection.close()
                print('[INFO] PostgreSQL connection closed')
    return {'status': '200'}
    
if __name__ == '__main__':
    app.run(debug=True)