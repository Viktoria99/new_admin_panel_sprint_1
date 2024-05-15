import os
from pathlib import Path

db_path = 'db.sqlite'
batch_size = 100
dsl = {
    'dbname': os.environ.get('dbname', 'movies_database'),
    'user': os.environ.get('user', 'habrpguser'),
    'password': os.environ.get('password', 'pgpwd4habr'),
    'host': os.environ.get('host', 'localhost'),
    'port': os.environ.get('port', 5432),
    'options': os.environ.get('options', '-c search_path=content'),
}

batch_100 = 100
batch_1000 = 1000

test_path = 'sqlite_to_postgres/db.sqlite'
path_sqllite = Path(__file__).resolve().parent.parent / test_path
