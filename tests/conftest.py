import os
import sys
import tempfile
import pytest

# 🔑 AÑADIR RAÍZ DEL PROYECTO AL PYTHONPATH
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)

import db  # ahora sí funciona

@pytest.fixture(autouse=True)
def test_db(monkeypatch):
    db_fd, db_path = tempfile.mkstemp()

    # Forzar DB temporal
    monkeypatch.setattr(db, "DB_PATH", db_path)

    # Crear tablas en la DB temporal
    db.init_db()

    yield

    os.close(db_fd)
    os.unlink(db_path)
