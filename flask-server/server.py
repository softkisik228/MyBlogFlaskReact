from flask import Flask, request, make_response
import psycopg2
from config import host, password, user, db_name

app = Flask(__name__)


@app.route("/info")
def index():
    return {'info': 'some information'}


@app.route('/add_post', methods=['GET'])
def add_post():
    data = request.args.to_dict()
    print(data)
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
                ('{data['post']}', '{data['nickname']}', '{data['date']}');""")

            connection.commit()
            print('ok')
    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)
    finally:
        if connection:
            connection.close()
            print('[INFO] PostgreSQL connection closed')
    return make_response('OK', status_code=200)
    
if __name__ == '__main__':
    app.run(debug=True)