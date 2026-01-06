import importlib
import server

def test_aws_detected(monkeypatch):
    monkeypatch.setenv("AZURE_OTHER_HOST", "1.1.1.1")
    monkeypatch.delenv("AWS_OTHER_HOST", raising=False)

    importlib.reload(server)

    assert server.get_current_cloud() == "AWS"


def test_azure_detected(monkeypatch):
    monkeypatch.setenv("AWS_OTHER_HOST", "1.1.1.1")
    monkeypatch.delenv("AZURE_OTHER_HOST", raising=False)

    importlib.reload(server)

    assert server.get_current_cloud() == "Azure"
