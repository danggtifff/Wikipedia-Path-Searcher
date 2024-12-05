# Made by Daphne Calin 11/17/2024
# To create the database, put data.csv in a folder data/
# or change the below variable to its location.
wikilinks_path = 'data/merged.csv'
id_to_title_path = 'data/id_to_title.csv'
# Change where the .db file is created
db_file_path = 'data/wikilinks.db'

import csv, click, sqlite3, json
from flask import current_app, g
from functools import lru_cache

insert_wikilinks_rows = '''INSERT INTO wikilinks (name, outlinks) VALUES(?, ?)'''
insert_title_rows = '''INSERT INTO id_title (id, name) VALUES (?, ?)'''

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
    load_csv(wikilinks_path, insert_wikilinks_rows)
    load_csv(id_to_title_path, insert_title_rows)


@click.command('init-db')
def init_db_command():
    init_db()
    click.echo('Initialized the database.')

def load_csv(file_path, operation):
    db = get_db()
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        print("Start reading csv")
        db.executemany(operation, reader)
        db.commit()
        print("Finished reading csv")
    f.close()

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

# Load neighbors on demand with caching for repeated access
@lru_cache(maxsize=100000)  # Cache up to 100,000 nodes
def fetch_neighbors(name):
    conn = get_db()
    cursor = conn.cursor()
    query = "SELECT outlinks FROM wikilinks WHERE name = ?"
    cursor.execute(query, (name,))
    row = cursor.fetchone()

    try:
        return json.loads(row[0]) if row else []
    except json.JSONDecodeError as e:
        print(f"JSON decoding failed: {e}")
        return []
    
def check_name(id):
    conn = get_db()
    #print("haiiii :3")   
    cursor = conn.cursor()
    query = "SELECT name FROM id_title WHERE id = ?"
    cursor.execute(query, (id,))
    row = cursor.fetchone()
    #print("row:", row)
    if row:
        return row[0] # returns the name

def check_id(name):
    conn = get_db() 
    #print("haiiii :3")    
    cursor = conn.cursor()
    query = "SELECT id FROM id_title WHERE name = ?"
    cursor.execute(query, (name,))
    row = cursor.fetchone()
    if row:
        return row[0] # returns the name

def get_a_few_neighbors(name):
    conn = get_db() 
    cursor = conn.cursor()

    # Query to get the id for the node name
    id_query = "SELECT id FROM id_title WHERE name = ?"
    # Query to get the outlinks for the node by id
    wk_query = "SELECT outlinks FROM wikilinks WHERE name = ?"

    # Get the id for the node name
    cursor.execute(id_query, (name,)) 
    row = cursor.fetchone()

    if not row:
        return None  # Return None if no such node exists

    # Get the outlinks (neighbors) using the node's id
    cursor.execute(wk_query, (name,))
    row = cursor.fetchone()

    if row and row[0]:
        neighbors = json.loads(row[0])  
        return neighbors[:3] 
    else:
        return []  # Return an empty list if no neighbors are found
