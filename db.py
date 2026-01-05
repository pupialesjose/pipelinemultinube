import sqlite3

DB_PATH = "notes.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS people (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            edad INTEGER NOT NULL,
            cedula TEXT NOT NULL,
            nota TEXT
        )
    """)
    conn.commit()
    conn.close()

def create_person(data):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        INSERT INTO people (nombre, apellido, edad, cedula, nota)
        VALUES (?, ?, ?, ?, ?)
    """, (
        data["nombre"],
        data["apellido"],
        data["edad"],
        data["cedula"],
        data.get("nota", "")
    ))
    conn.commit()
    conn.close()

def get_people():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        SELECT id, nombre, apellido, edad, cedula, nota
        FROM people
        ORDER BY id DESC
    """)
    rows = c.fetchall()
    conn.close()
    return rows

def update_person(pid, data):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        UPDATE people
        SET nombre=?, apellido=?, edad=?, cedula=?, nota=?
        WHERE id=?
    """, (
        data["nombre"],
        data["apellido"],
        data["edad"],
        data["cedula"],
        data.get("nota", ""),
        pid
    ))
    conn.commit()
    conn.close()

def delete_person(pid):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("DELETE FROM people WHERE id=?", (pid,))
    conn.commit()
    conn.close()
