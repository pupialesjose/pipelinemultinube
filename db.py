import sqlite3

DB_PATH = "notes.db"

def get_conn():
    return sqlite3.connect(DB_PATH, check_same_thread=False)

def init_db():
    conn = get_conn()
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            age INTEGER,
            cedula TEXT,
            content TEXT
        )
    """)
    conn.commit()
    conn.close()

def create_note(data):
    conn = get_conn()
    c = conn.cursor()
    c.execute("""
        INSERT INTO notes (first_name, last_name, age, cedula, content)
        VALUES (?, ?, ?, ?, ?)
    """, (
        data["first_name"],
        data["last_name"],
        data["age"],
        data["cedula"],
        data["content"]
    ))
    conn.commit()
    note_id = c.lastrowid
    conn.close()
    return note_id

def get_notes():
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT * FROM notes ORDER BY id DESC")
    notes = c.fetchall()
    conn.close()
    return notes

def update_note(note_id, data):
    conn = get_conn()
    c = conn.cursor()
    c.execute("""
        UPDATE notes
        SET first_name=?, last_name=?, age=?, cedula=?, content=?
        WHERE id=?
    """, (
        data["first_name"],
        data["last_name"],
        data["age"],
        data["cedula"],
        data["content"],
        note_id
    ))
    conn.commit()
    conn.close()

def delete_note(note_id):
    conn = get_conn()
    c = conn.cursor()
    c.execute("DELETE FROM notes WHERE id=?", (note_id,))
    conn.commit()
    conn.close()

