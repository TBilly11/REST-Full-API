'''from flask import Flask, request, jsonify
import sqlite3
import sqlite3

conn = sqlite3.connect('autos.sqlite')
cursor = conn.cursor()

# SQL-Befehl, um die Tabelle 'book' zu erstellen
create_table_query = 
CREATE TABLE IF NOT EXISTS auto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    marke TEXT,
    Baujahr INTERGER,
    Preis FLOAT,
    Farbe TEXT,
    Getriebe TEXT    
);


cursor.execute(create_table_query)
conn.commit()
conn.close()

app = Flask(__name__)

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect('autos.sqlite')
        return conn
    except sqlite3.Error as e:
        print(e)
        return conn

@app.route('/autos', methods=["GET", "POST"])
def books():
    conn = db_connection()
    if conn is None:
        return "Database connection error", 500

    cursor = conn.cursor()
    
    if request.method == 'GET':
        cursor.execute("SELECT * FROM auto")
        autos = [
            dict(id=row[0], Marke=row[1], Baujahr=row[2], Preis=row[3],Farbe=row[4],Getriebe=row[5])
            for row in cursor.fetchall()
        ]
        return jsonify(books)

    if request.method == 'POST':
        neu_marque = request.form['Marke']
        neu_baujahr = request.form['Baujahr']
        neu_preis = request.form['Preis']
        neu_farbe=request.form['Farbe']
        neu_getriebe=request.form['Getriebe']
        sql = """INSERT INTO auto(Marke,Baujahr,Preis,Farbe,Getriebe)
               VALUES(?,?,?,?,?)"""
        cursor.execute(sql, (neu_marque, neu_baujahr,neu_preis, neu_farbe,neu_getriebe))
        conn.commit()
        return f'Auto mit der id:{cursor.lastrowid} wurde erfolgreich erstellt', 201
    


@app.route('/auto/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_auto(id):
    conn = db_connection()
    cursor = conn.cursor()
    auto = None
    
    if request.method == 'GET':
        cursor.execute("SELECT * FROM auto WHERE id=?", (id,))
        row = cursor.fetchone()
        if row:
            auto = {
                'id': row[0],
                'Marque': row[1],
                'Baujahr': row[2],
                'Preis': row[3],
                'Farbe': row[4],
                'Getriebe': row[5]
            }
            return jsonify(auto), 200
        else:
            return "Auto wurde nicht gefunden", 404
    
    if request.method == 'PUT':
        sql = """ UPDATE auto
                  SET Marke=?,
                      Baujahr=?,
                      Preis=?,
                      Farbe=?,
                      Getriebe
                  WHERE id=?"""
        Marke = request.form['Marke']
        Baujahr = request.form['Baujahr']
        Preis = request.form['Preis']
        Farbe=request.form['Farbe']
        Getriebe=request.form['Getriebe']
        updated_auto = {
            'id': id,
            'Marke':Marke,
            'Baujahr':Baujahr,
            'Preis':Preis,
            'Farbe':Farbe,
            'Getriebe':Getriebe
        }
        conn.execute(sql, (Marke, Baujahr, Preis, Farbe,Getriebe,id))
        conn.commit()
        return jsonify(updated_auto), 200
    
    
    if request.method == 'DELETE':
        cursor.execute("SELECT * FROM auto WHERE id=?", (id,))
        row = cursor.fetchone()
        if row:
            sql = """DELETE FROM auto WHERE id=?"""
            conn.execute(sql, (id,))
            conn.commit()
            return f"Das Auto mit der id: {id} wurde gelöscht.", 200
        else:
            return f"Das Auto mit der id: {id} wurde nicht gefunden.", 404

if __name__ == '__main__':
    app.run(debug=True)'''

from flask import Flask, request, jsonify
import sqlite3

app_auto = Flask(__name__)

# Verbindung zur Datenbank und Erstellung der Tabelle
conn = sqlite3.connect('autos.sqlite')
cursor = conn.cursor()

create_table_query = '''
CREATE TABLE IF NOT EXISTS auto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Marke TEXT,
    Baujahr INTEGER,
    Preis FLOAT,
    Farbe TEXT,
    Getriebe TEXT    
);
'''

cursor.execute(create_table_query)
conn.commit()
conn.close()

# Datenbankverbindungsfunktion
def db_connection():
    conn = None
    try:
        conn = sqlite3.connect('autos.sqlite')
        return conn
    except sqlite3.Error as e:
        print(e)
        return conn

# Endpunkt für alle Autos
@app_auto.route('/autos', methods=["GET", "POST"])
def autos():
    conn = db_connection()
    if conn is None:
        return "Database connection error", 500

    cursor = conn.cursor()
    
    if request.method == 'GET':
        cursor.execute("SELECT * FROM auto")
        autos = [
            dict(id=row[0], Marke=row[1], Baujahr=row[2], Preis=row[3], Farbe=row[4], Getriebe=row[5])
            for row in cursor.fetchall()
        ]
        return jsonify(autos)

    if request.method == 'POST':
        neu_marke = request.form['Marke']
        neu_baujahr = request.form['Baujahr']
        neu_preis = request.form['Preis']
        neu_farbe = request.form['Farbe']
        neu_getriebe = request.form['Getriebe']
        sql = """INSERT INTO auto(Marke, Baujahr, Preis, Farbe, Getriebe)
               VALUES (?, ?, ?, ?, ?)"""
        cursor.execute(sql, (neu_marke, neu_baujahr, neu_preis, neu_farbe, neu_getriebe))
        conn.commit()
        return f'Auto mit der ID {cursor.lastrowid} wurde erfolgreich erstellt', 201

# Endpunkt für ein einzelnes Auto anhand der ID
@app_auto.route('/auto/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_auto(id):
    conn = db_connection()
    cursor = conn.cursor()
    
    if request.method == 'GET':
        cursor.execute("SELECT * FROM auto WHERE id=?", (id,))
        row = cursor.fetchone()
        if row:
            auto = {
                'id': row[0],
                'Marke': row[1],
                'Baujahr': row[2],
                'Preis': row[3],
                'Farbe': row[4],
                'Getriebe': row[5]
            }
            return jsonify(auto), 200
        else:
            return "Auto wurde nicht gefunden", 404
    
    if request.method == 'PUT':
        cursor.execute("SELECT * FROM auto WHERE id=?", (id,))
        row = cursor.fetchone()
        if row:
            neu_marke = request.form['Marke']
            neu_baujahr = request.form['Baujahr']
            neu_preis = request.form['Preis']
            neu_farbe = request.form['Farbe']
            neu_getriebe = request.form['Getriebe']
            
            sql = """UPDATE auto 
                     SET Marke=?, Baujahr=?, Preis=?, Farbe=?, Getriebe=?
                     WHERE id=?"""
                     
            cursor.execute(sql, (neu_marke, neu_baujahr, neu_preis, neu_farbe, neu_getriebe, id))
            conn.commit()
            
            updated_auto = {
                'id': id,
                'Marke': neu_marke,
                'Baujahr': neu_baujahr,
                'Preis': neu_preis,
                'Farbe': neu_farbe,
                'Getriebe': neu_getriebe
            }
            return jsonify(updated_auto), 200
        else:
            return f"Das Auto mit der ID {id} wurde nicht gefunden.", 404
    if request.method == 'DELETE':
        # (Dein Code für die DELETE-Methode hier einfügen)
        cursor.execute("SELECT * FROM auto WHERE id=?", (id,))
        row = cursor.fetchone()
        if row:
            sql = """DELETE FROM auto WHERE id=?"""
            cursor.execute(sql, (id,))
            conn.commit()
            return f"Das Auto mit der ID {id} wurde gelöscht.", 200
        else:
            return f"Das Auto mit der ID {id} wurde nicht gefunden.", 404


if __name__ == '__main__':
    app_auto.run(debug=True)


