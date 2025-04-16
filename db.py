import sqlite3

'''conn=sqlite3.connect("books.sqlite")
cursor=conn.cursor()
sql_query="""CREATE TABLE books(
id integer PRIMARY KEY,
author text NOT NULL,
language text NOT NULL,
title text NOT NULL
)"""
cursor.execute(sql_query) '''

conn=sqlite3.connect("autos.sqlite")
cursor=conn.cursor()
sql_query="""CREATE TABLE autos(
id integer PRIMARY KEY,
Marke text NOT NULL,
Baujahr interger NOT NULL,
Preis float NOT NULL,
Farbe text NOT NULL,
Getriebe text NOT NULL,
Geschwindigkeit text NOT NULL
)"""
cursor.execute(sql_query)

# Importiere das sqlite3-Modul, um mit SQLite-Datenbanken zu interagieren
import sqlite3

# Stelle eine Verbindung zur SQLite-Datenbank her (falls nicht vorhanden, wird eine neue erstellt)
conn = sqlite3.connect("autos.sqlite")

# Erstelle einen Cursor, der verwendet wird, um SQL-Abfragen auszuführen
cursor = conn.cursor()

# Definiere eine SQL-Abfrage zum Erstellen einer Tabelle mit dem Namen "autos"
sql_query = """CREATE TABLE autos(
    id INTEGER PRIMARY KEY,  # Eine eindeutige ID, die als Primärschlüssel dient
    Marke TEXT NOT NULL,     # Der Text des Automarkenfelds, darf nicht leer sein
    Baujahr INTEGER NOT NULL, # Das Baujahr als Ganzzahl, darf nicht leer sein
    Preis REAL NOT NULL,      # Der Preis als Fließkommazahl, darf nicht leer sein
    Farbe TEXT NOT NULL,      # Die Farbe des Autos als Text, darf nicht leer sein
    Getriebe TEXT NOT NULL,   # Die Art des Getriebes als Text, darf nicht leer sein
    Geschwindigkeit TEXT NOT NULL  # Die Geschwindigkeit als Text, darf nicht leer sein
)"""

# Führe die erstellte SQL-Abfrage aus, um die Tabelle in der Datenbank zu erstellen
cursor.execute(sql_query)

# Schließe die Verbindung zur Datenbank
conn.close()
