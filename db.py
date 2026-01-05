import sqlite3

DB_PATH = "notes.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            age INTEGER NOT NULL,
            cedula TEXT NOT NULL,
            content TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def save_note(first_name, last_name, age, cedula, content):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        "INSERT INTO notes (first_name, last_name, age, cedula, content) VALUES (?, ?, ?, ?, ?)",
        (first_name, last_name, age, cedula, content)
    )
    conn.commit()
    conn.close()

def get_notes():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT first_name, last_name, age, cedula, content FROM notes ORDER BY id DESC")
    notes = c.fetchall()  # lista de tuplas
    conn.close()
    return notes
