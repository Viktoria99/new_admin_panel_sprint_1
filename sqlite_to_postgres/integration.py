import sqlite3
from dataclasses import astuple

import psycopg2
from psycopg2 import errors
from psycopg2.extensions import connection
from psycopg2.extras import execute_values

from logger import logger_load
from tables import Model


class ServiceLoad:
    def __init__(self):
        self.sql_count = None
        self.sql_load = None
        self.sql_insert = None

    def load_sqllite(
        self,
        sqlLite_conn: sqlite3.Connection,
        ps_conn: connection,
        batch_size: int,
        db_class: Model,
    ):
        postgres_cursor = ps_conn.cursor()
        sqlLite_curs = sqlLite_conn.cursor()
        sqlLite_curs.arraysize = batch_size

        try:
            sqlLite_curs.execute(self.sql_count)
            result = sqlLite_curs.fetchone()
            raise Exception()
            batch_count = round(result['count'] / batch_size)
            if result['count'] < batch_size:
                batch_count = 1
            if ((result['count'] / batch_size) - batch_count) > 0:
                batch_count += 1

            sqlLite_curs.execute(self.sql_load)

            for i in range(batch_count):
                data = sqlLite_curs.fetchmany()
                films = [astuple(db_class(**item)) for item in data]
                psycopg2.extras.register_uuid()
                execute_values(postgres_cursor, self.sql_insert, films)

        except (errors.DataError, errors.IntegrityError) as err:
            logger_load.error(
                'Postgres-{pgcode}: {pgerror}'.format(
                    pgcode=err.pgcode, pgerror=err.pgerror
                )
            )
            raise
        except errors.Error as err:
            logger_load.error(
                'Postgres-{pgcode}: {pgerror}'.format(
                    pgcode=err.pgcode, pgerror=err.pgerror
                )
            )
            raise
        except sqlite3.Error as err:
            logger_load.error(
                'SqlLite-{code}: {name}'.format(
                    code=err.sqlite_errorcode, name=err.sqlite_errorname
                )
            )
            raise
