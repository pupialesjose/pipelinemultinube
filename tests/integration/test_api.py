from server import app

def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.data.decode() == "OK"


def test_create_person_endpoint():
    client = app.test_client()

    response = client.post("/", data={
        "nombre": "Laura",
        "apellido": "Martínez",
        "edad": 28,
        "cedula": "5556667778",
        "nota": "Integración"
    })

    assert response.status_code in (200, 302)
