import sqlite3 as sl

con = sl.connect('my_book.db')

with con:
    con.execute(""" CREATE TABLE USER (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
         Имя TEXT, Фамилия TEXT, Номер телефона TEXT, Описание TEXT);""")

sql = 'INSERT INTO USER (id, Имя, Фамилия, Номер телефона, Описание) values(?, ?, ?, ?, ?)'
data = [(1, 'Антон', 'Федонин', '8-910-154-34-26', 'Мой телефон')]
with con:
    con.executemany(sql, data)
