import sqlite3

conn=sqlite3.connect("autos.sqlite")
cursor=conn.cursor()
sql_query="""CREATE TABLE autos(
id integer PRIMARY KEY,
Marke text NOT NULL,
Baujahr interger NOT NULL,
Preis float NOT NULL,
Farbe text NOT NULL,
Getriebe text NOT NULL
)"""
cursor.execute(sql_query)