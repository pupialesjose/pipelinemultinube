import os
import tempfile
import pytest

@pytest.fixture(autouse=True)
def test_db(monkeypatch):
    db_fd, db_path = tempfile.mkstemp()
    monkeypatch.setattr("db.DB_PATH", db_path)
    yield
    os.close(db_fd)
    os.unlink(db_path)
