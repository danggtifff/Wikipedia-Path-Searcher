# Made by Daphne Calin 11/17/2024
# To create the database, put data.csv in a folder data/
# or change the below variable to its location.
in_file_path = 'data/data.csv'
# Change where the .db file is created
out_file_path = 'data/wikilinks.db'

import csv, sqlite3

create_table = '''CREATE TABLE IF NOT EXISTS wikilinks (
    name TEXT PRIMARY_KEY,
    outlinks TEXT
    );'''

insert_rows = '''INSERT INTO wikilinks (name, outlinks) VALUES(?, ?)'''

if __name__ == "__main__":
    print("Creating the wikibase SQLite3 database from", in_file_path)
    # connect to database
    connection = sqlite3.connect(out_file_path)

    # create cursor object to execute queries
    cursor = connection.cursor()

    cursor.execute(create_table)

    # open the csv file and read its contents into memory   
    file = open(in_file_path, 'r', encoding="UTF-8")
    contents = csv.reader(file)


    cursor.executemany(insert_rows, contents)

    connection.commit()

    connection.close()

    print("Database created successfully!")




    
