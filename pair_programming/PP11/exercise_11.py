import sqlite3 as sql

db = sql.connect('PP11_db.sqlite')
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
db.close()