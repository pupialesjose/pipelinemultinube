from server import app

def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.data.decode() == "OK"

def test_create_note():
    client = app.test_client()
    response = client.post("/", data={"note": "integración"})
    assert response.status_code in (200, 302)
