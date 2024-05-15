from pathlib import Path

db_path = 'db.sqlite'
batch_size = 100
dsl = {
    'dbname': 'movies_database',
    'user': 'habrpguser',
    'password': 'pgpwd4habr',
    'host': 'localhost',
    'port': 5432,
    'options': '-c search_path=content',
}

batch_100 = 100
batch_1000 = 1000

test_path = 'sqlite_to_postgres/db.sqlite'
path_sqllite = Path(__file__).resolve().parent.parent / test_path
