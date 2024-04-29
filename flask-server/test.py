import psycopg2
import sqlite3
from config import host, password, user, db_name

try:
    # connection = psycopg2.connect(
    #     host=host,
    #     user=user,
    #     password=password,
    #     database=db_name
    # )


    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """CREATE TABLE posts(
    #         id serial PRIMARY KEY,
    #         post varchar(500) NOT NULL,
    #         nickname varchar(15) NOT NULL,
    #         date varchar(20) NOT NULL
    #         );"""
    #     )
    #     connection.commit()
    con = sqlite3.connect("posts.db")
    cur = con.cursor()
    cur.execute("""CREATE TABLE posts(
            id integer primary key,
            post varchar(500) NOT NULL,
            nickname varchar(15) NOT NULL,
            date varchar(20) NOT NULL
            );""")
    con.commit()
except Exception as _ex:
    print('[INFO] Error while working with PostgreSQL', _ex)
finally:
    print('[INFO] PostgreSQL connection closed')