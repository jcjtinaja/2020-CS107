import sqlite3 as sql
import pandas as pd

db = sql.connect(':memory:')

# Load existing db to memory
# src = sql.connect('PP11_db.sqlite')
# src.backup(db)

c = db.cursor()
c.execute('DROP TABLE IF EXISTS candidates')
c.execute(''' CREATE TABLE candidates (
              id INTEGER PRIMARY KEY NOT NULL,
              first_name TEXT,
              last_name TEXT,
              middle_init TEXT,
              party TEXT NOT NULL) ''')

db.commit()

with open('candidates.txt') as f:
    next(f)
    candidates = f.readlines()

for line in candidates:
    int_id, first_name, last_name, middle_init, party = line.strip().split('|')
    vals = (int(int_id), first_name, last_name, middle_init, party)
    c.execute('INSERT INTO candidates'
                '(id, first_name, last_name, middle_init, party)'
                'VALUES (?, ?, ?, ?, ?)', vals)

db.commit()

df = pd.read_sql_query('SELECT * FROM candidates', db)
print(df.to_string())

db.close()