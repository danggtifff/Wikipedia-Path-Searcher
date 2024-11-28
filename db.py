# Made by Daphne Calin 11/17/2024
# To create the database, put data.csv in a folder data/
# or change the below variable to its location.
in_file_path = 'data/merged.csv'
# Change where the .db file is created
db_file_path = 'data/wikilinks.db'

import csv, click, sqlite3
from flask import current_app, g

insert_rows = '''INSERT INTO wikilinks (name, outlinks) VALUES(?, ?)'''

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()
    
    with current_app.open_resource('data/schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
    load_csv(in_file_path)


@click.command('init-db')
def init_db_command():
    init_db()
    click.echo('Initialized the database.')

def load_csv(file_path):
    db = get_db()
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        print("started up")
        db.executemany(insert_rows, reader)
        db.commit()
        print("finished up")
    f.close()

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)



