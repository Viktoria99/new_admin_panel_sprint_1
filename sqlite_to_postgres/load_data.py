import contextlib
import sqlite3
from dataclasses import fields

import psycopg2
from psycopg2.extras import DictCursor

from integration import ServiceLoad
from settings import batch_size, db_path, dsl
from tables import getTablesClass


def load_from_sqlite(db_path: str):
    with contextlib.closing(
        sqlite3.connect(db_path)
    ) as sqlite_conn, contextlib.closing(
        psycopg2.connect(**dsl, cursor_factory=DictCursor)
    ) as pg_conn:
        sqlite_conn.row_factory = sqlite3.Row
        dict_tables = getTablesClass()
        keys = dict_tables.keys()
        for item in keys:
            load = ServiceLoad()
            load.sql_count = 'select count(*) as count from %s;' % item
            load.sql_load = 'select * from %s;' % item
            column_names = [field.name for field in fields(dict_tables[item])]
            column_names_str = ','.join(column_names)
            load.sql_insert = (
                f'insert into {item}' f' ({column_names_str}) values %s '
            )
            load.load_sqllite(
                sqlite_conn, pg_conn, batch_size, dict_tables[item]
            )


if __name__ == '__main__':
    load_from_sqlite(db_path)
