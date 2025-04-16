from flask import Flask, request, jsonify,render_template
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
    Getriebe TEXT,
    Geschwindigkeit TEXT    
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
            dict(id=row[0], Marke=row[1], Baujahr=row[2], Preis=row[3], Farbe=row[4], Getriebe=row[5], Geschwindigkeit=row[6])
            for row in cursor.fetchall()
        ]
        return jsonify(autos)

    if request.method == 'POST':
        neu_marke = request.form['Marke']
        neu_baujahr = request.form['Baujahr']
        neu_preis = request.form['Preis']
        neu_farbe = request.form['Farbe']
        neu_getriebe = request.form['Getriebe']
        neu_geschwindigkeit = request.form['Geschwindigkeit']
        sql = """INSERT INTO auto(Marke, Baujahr, Preis, Farbe, Getriebe,Geschwindigkeit)
               VALUES (?, ?, ?, ?, ?,?)"""
        cursor.execute(sql, (neu_marke, neu_baujahr, neu_preis, neu_farbe, neu_getriebe, neu_geschwindigkeit))
        conn.commit()
        return f'Auto mit der ID {cursor.lastrowid} wurde erfolgreich hinzugefügt', 201

    # Dies wird erreicht, wenn weder GET noch POST aufgerufen wurden
    return render_template('index.html', autos=autos)

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
                'Getriebe': row[5],
                'Geschwindigkeit':row[6]
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
            neu_geschwindigkeit=request.form['Geschwindigkeit']
            
            sql = """UPDATE auto 
                     SET Marke=?, Baujahr=?, Preis=?, Farbe=?, Getriebe=?,Geschwindigkeit=?
                     WHERE id=?"""
                     
            cursor.execute(sql, (neu_marke, neu_baujahr, neu_preis, neu_farbe, neu_getriebe,neu_geschwindigkeit, id))
            conn.commit()
            
            updated_auto = {
                'id': id,
                'Marke': neu_marke,
                'Baujahr': neu_baujahr,
                'Preis': neu_preis,
                'Farbe': neu_farbe,
                'Getriebe': neu_getriebe,
                'Geschwindigkeit':neu_geschwindigkeit
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


