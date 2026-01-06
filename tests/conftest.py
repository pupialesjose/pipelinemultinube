import os
import tempfile
import pytest
import db

@pytest.fixture(autouse=True)
def test_db(monkeypatch):
    db_fd, db_path = tempfile.mkstemp()

    # Forzar uso de DB temporal
    monkeypatch.setattr(db, "DB_PATH", db_path)

    # 🔑 Crear tablas DESPUÉS de cambiar el DB_PATH
    db.init_db()

    yield

    os.close(db_fd)
    os.unlink(db_path)
