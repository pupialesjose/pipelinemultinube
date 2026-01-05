import sqlite3

DB_PATH = "notes.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def save_note(content):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        "INSERT INTO notes (content) VALUES (?)",
        (content,)
    )
    conn.commit()
    conn.close()

def update_note(note_id, content):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        "UPDATE notes SET content = ? WHERE id = ?",
        (content, note_id)
    )
    conn.commit()
    conn.close()

def delete_note(note_id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        "DELETE FROM notes WHERE id = ?",
        (note_id,)
    )
    conn.commit()
    conn.close()

def get_notes():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT id, content FROM notes ORDER BY id DESC")
    notes = [{"id": row[0], "content": row[1]} for row in c.fetchall()]
    conn.close()
    return notes
