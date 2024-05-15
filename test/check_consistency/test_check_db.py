import sqlite3
import psycopg2
import contextlib
from psycopg2.extras import DictCursor
from sqlite_to_postgres.settings import *


def test_count_film_rows():
    with contextlib.closing(
        sqlite3.connect(path_sqllite)
    ) as sqlite_conn, contextlib.closing(
        psycopg2.connect(**dsl, cursor_factory=DictCursor)
    ) as pg_conn:
        postgres_cursor = pg_conn.cursor()
        sqlLite_curs = sqlite_conn.cursor()

        postgres_cursor.execute('select count(*) from film_work;')
        sqlLite_curs.execute('select count(*) from film_work;')
        postgres_film = postgres_cursor.fetchone()
        sqlLite_film = sqlLite_curs.fetchone()
        assert postgres_film[0] == sqlLite_film[0]


if __name__ == '__main__':
    test_count_film_rows()


def test_count_genre_rows():
    with contextlib.closing(
        sqlite3.connect(path_sqllite)
    ) as sqlite_conn, contextlib.closing(
        psycopg2.connect(**dsl, cursor_factory=DictCursor)
    ) as pg_conn:
        postgres_cursor = pg_conn.cursor()
        sqlLite_curs = sqlite_conn.cursor()

        postgres_cursor.execute('select count(*) from genre;')
        sqlLite_curs.execute('select count(*) from genre;')
        postgres_row = postgres_cursor.fetchone()
        sqlLite_row = sqlLite_curs.fetchone()
        assert postgres_row[0] == sqlLite_row[0]


if __name__ == '__main__':
    test_count_genre_rows()


def test_count_person_rows():
    with contextlib.closing(
        sqlite3.connect(path_sqllite)
    ) as sqlite_conn, contextlib.closing(
        psycopg2.connect(**dsl, cursor_factory=DictCursor)
    ) as pg_conn:
        postgres_cursor = pg_conn.cursor()
        sqlLite_curs = sqlite_conn.cursor()

        postgres_cursor.execute('select count(*) from person;')
        sqlLite_curs.execute('select count(*) from person;')
        postgres_row = postgres_cursor.fetchone()
        sqlLite_row = sqlLite_curs.fetchone()
        assert postgres_row[0] == sqlLite_row[0]


if __name__ == '__main__':
    test_count_person_rows()


def test_count_person_film_rows():
    with contextlib.closing(
        sqlite3.connect(path_sqllite)
    ) as sqlite_conn, contextlib.closing(
        psycopg2.connect(**dsl, cursor_factory=DictCursor)
    ) as pg_conn:
        postgres_cursor = pg_conn.cursor()
        sqlLite_curs = sqlite_conn.cursor()

        postgres_cursor.execute('select count(*) from person_film_work;')
        sqlLite_curs.execute('select count(*) from person_film_work;')
        postgres_row = postgres_cursor.fetchone()
        sqlLite_row = sqlLite_curs.fetchone()
        assert postgres_row[0] == sqlLite_row[0]


if __name__ == '__main__':
    test_count_person_film_rows()


def test_count_genre_film_rows():
    with contextlib.closing(
        sqlite3.connect(path_sqllite)
    ) as sqlite_conn, contextlib.closing(
        psycopg2.connect(**dsl, cursor_factory=DictCursor)
    ) as pg_conn:
        postgres_cursor = pg_conn.cursor()
        sqlLite_curs = sqlite_conn.cursor()

        postgres_cursor.execute('select count(*) from genre_film_work;')
        sqlLite_curs.execute('select count(*) from genre_film_work;')
        postgres_row = postgres_cursor.fetchone()
        sqlLite_row = sqlLite_curs.fetchone()
        assert postgres_row[0] == sqlLite_row[0]


if __name__ == '__main__':
    test_count_genre_film_rows()
