import psycopg2
from config import host, password, user, db_name

try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )


    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE posts(
            id serial PRIMARY KEY,
            post varchar(500) NOT NULL,
            nickname varchar(15) NOT NULL,
            date varchar(20) NOT NULL
            );"""
        )
        connection.commit()
except Exception as _ex:
    print('[INFO] Error while working with PostgreSQL', _ex)
finally:
    if connection:
        connection.close()
        print('[INFO] PostgreSQL connection closed')