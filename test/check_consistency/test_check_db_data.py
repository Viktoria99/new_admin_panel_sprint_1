import sqlite3
import psycopg2
from psycopg2.extras import DictCursor
from sqlite_to_postgres.tables import *
from sqlite_to_postgres.settings import *


def get_counters(table_size: int, batch: int):

    batch_count = round(table_size / batch)
    match table_size, batch:
        case table_size, batch if table_size < batch:
            batch_count = 1

        case table_size, batch if table_size > batch and table_size % batch > 0:
            batch_count += 1

    return batch_count


if __name__ == '__main__':
    get_counters(10, 100)


def test_check_data_film():
    with sqlite3.connect(path_sqllite) as sqlite_conn, psycopg2.connect(
        **dsl, cursor_factory=DictCursor
    ) as pg_conn:

        postgres_cursor = pg_conn.cursor()
        postgres_cursor.arraysize = batch_100

        sqlite_conn.row_factory = sqlite3.Row
        sqlLite_curs = sqlite_conn.cursor()
        sqlLite_curs.arraysize = batch_100

        sqlLite_curs.execute(
            'select count(*) as count from film_work order by id;'
        )
        row_count = sqlLite_curs.fetchone()
        batch_count = get_counters(row_count['count'], batch_100)

        postgres_cursor.execute('select * from film_work order by id;')
        sqlLite_curs.execute('select * from film_work order by id;')

        for w in range(batch_count):
            data_sqlLite = sqlLite_curs.fetchmany()
            data_postgres = postgres_cursor.fetchmany()
            films_lite = [Film(**item_sl) for item_sl in data_sqlLite]
            film_postgres = [Film(**film_ps) for film_ps in data_postgres]
            for i in range(len(film_postgres)):
                assert film_postgres[i] == films_lite[i]


if __name__ == '__main__':
    test_check_data_film()


def test_check_data_genre():
    with (
        sqlite3.connect(path_sqllite) as sqlite_conn,
        psycopg2.connect(**dsl, cursor_factory=DictCursor) as pg_conn,
    ):

        postgres_cursor = pg_conn.cursor()
        postgres_cursor.arraysize = batch_100

        sqlite_conn.row_factory = sqlite3.Row
        sqlLite_curs = sqlite_conn.cursor()
        sqlLite_curs.arraysize = batch_100

        sqlLite_curs.execute(
            'select count(*) as count from genre order by id;'
        )
        row_count = sqlLite_curs.fetchone()
        batch_count = get_counters(row_count['count'], batch_100)

        postgres_cursor.execute('select * from genre order by id;')
        sqlLite_curs.execute('select * from genre order by id;')

        for w in range(batch_count):

            data_sqlLite = sqlLite_curs.fetchmany()
            data_postgres = postgres_cursor.fetchmany()

            films_lite = [Genre(**item_sl) for item_sl in data_sqlLite]
            film_postgres = [Genre(**item_ps) for item_ps in data_postgres]

            for i in range(len(film_postgres)):
                assert film_postgres[i] == films_lite[i]


if __name__ == '__main__':
    test_check_data_genre()


def test_check_data_person():
    with sqlite3.connect(path_sqllite) as sqlite_conn, psycopg2.connect(
        **dsl, cursor_factory=DictCursor
    ) as pg_conn:

        postgres_cursor = pg_conn.cursor()
        postgres_cursor.arraysize = batch_1000

        sqlite_conn.row_factory = sqlite3.Row
        sqlLite_curs = sqlite_conn.cursor()
        sqlLite_curs.arraysize = batch_1000

        sqlLite_curs.execute(
            'select count(*) as count from person order by id;'
        )
        row_count = sqlLite_curs.fetchone()
        batch_count = get_counters(row_count['count'], batch_1000)

        postgres_cursor.execute('select * from person order by id;')
        sqlLite_curs.execute('select * from person order by id;')

        for w in range(batch_count):

            data_sqlLite = sqlLite_curs.fetchmany()
            data_postgres = postgres_cursor.fetchmany()

            films_lite = [Person(**item_sl) for item_sl in data_sqlLite]
            film_postgres = [Person(**item_ps) for item_ps in data_postgres]

            for i in range(len(film_postgres)):
                assert film_postgres[i] == films_lite[i]


if __name__ == '__main__':
    test_check_data_person()


def test_check_data_person_film():
    with sqlite3.connect(path_sqllite) as sqlite_conn, psycopg2.connect(
        **dsl, cursor_factory=DictCursor
    ) as pg_conn:

        postgres_cursor = pg_conn.cursor()
        postgres_cursor.arraysize = batch_1000

        sqlite_conn.row_factory = sqlite3.Row
        sqlLite_curs = sqlite_conn.cursor()
        sqlLite_curs.arraysize = batch_1000

        sqlLite_curs.execute(
            'select count(*) as count from person_film_work order by id;'
        )
        row_count = sqlLite_curs.fetchone()
        batch_count = get_counters(row_count['count'], batch_1000)

        postgres_cursor.execute('select * from person_film_work order by id;')
        sqlLite_curs.execute('select * from person_film_work order by id;')

        for w in range(batch_count):

            data_sqlLite = sqlLite_curs.fetchmany()
            data_postgres = postgres_cursor.fetchmany()

            films_lite = [PersonFilm(**item_sl) for item_sl in data_sqlLite]
            film_postgres = [
                PersonFilm(**item_ps) for item_ps in data_postgres
            ]

            for i in range(len(film_postgres)):
                assert film_postgres[i] == films_lite[i]


if __name__ == '__main__':
    test_check_data_person_film()


def test_check_data_genre_film():
    with sqlite3.connect(path_sqllite) as sqlite_conn, psycopg2.connect(
        **dsl, cursor_factory=DictCursor
    ) as pg_conn:

        postgres_cursor = pg_conn.cursor()
        postgres_cursor.arraysize = batch_1000

        sqlite_conn.row_factory = sqlite3.Row
        sqlLite_curs = sqlite_conn.cursor()
        sqlLite_curs.arraysize = batch_1000

        sqlLite_curs.execute(
            'select count(*) as count from genre_film_work order by id;'
        )
        row_count = sqlLite_curs.fetchone()
        batch_count = get_counters(row_count['count'], batch_1000)

        postgres_cursor.execute('select * from genre_film_work order by id;')
        sqlLite_curs.execute('select * from genre_film_work order by id;')

        for w in range(batch_count):

            data_sqlLite = sqlLite_curs.fetchmany()
            data_postgres = postgres_cursor.fetchmany()

            films_lite = [GenreFilm(**item_sl) for item_sl in data_sqlLite]
            film_postgres = [GenreFilm(**item_ps) for item_ps in data_postgres]

            for i in range(len(film_postgres)):
                assert film_postgres[i] == films_lite[i]


if __name__ == '__main__':
    test_check_data_genre_film()
