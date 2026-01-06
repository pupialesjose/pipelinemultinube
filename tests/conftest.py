import os
import sys
import tempfile
import pytest

# Añadir la raíz del proyecto al PYTHONPATH
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

@pytest.fixture(autouse=True)
def test_db(monkeypatch):
    db_fd, db_path = tempfile.mkstemp()
    monkeypatch.setattr("db.DB_PATH", db_path)
    yield
    os.close(db_fd)
    os.unlink(db_path)
