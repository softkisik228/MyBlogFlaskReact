from flask import Flask, request
import psycopg2
from config import host, password, user, db_name

app = Flask(__name__)


@app.route("/info")
def index():
    return {'info': 'some information'}


@app.route('/', methods=['GET', 'POST'])
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

    
if __name__ == '__main__':
    app.run(debug=True) 