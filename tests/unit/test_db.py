from db import init_db, save_note, get_notes

def test_save_and_get_note():
    init_db()
    save_note("nota de prueba")
    notes = get_notes()
    assert "nota de prueba" in notes
