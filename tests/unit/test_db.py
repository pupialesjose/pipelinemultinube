from db import init_db, create_person, get_people, update_person, delete_person

def test_create_and_get_person():
    init_db()

    person = {
        "nombre": "Juan",
        "apellido": "Pérez",
        "edad": 30,
        "cedula": "1234567890",
        "nota": "Test unitario"
    }

    create_person(person)
    people = get_people()

    assert len(people) == 1
    assert people[0][1] == "Juan"
    assert people[0][2] == "Pérez"


def test_update_person():
    init_db()

    person = {
        "nombre": "Ana",
        "apellido": "García",
        "edad": 25,
        "cedula": "0987654321",
        "nota": "Inicial"
    }

    create_person(person)
    people = get_people()
    pid = people[0][0]

    updated = {
        "nombre": "Ana María",
        "apellido": "García",
        "edad": 26,
        "cedula": "0987654321",
        "nota": "Actualizada"
    }

    update_person(pid, updated)
    people = get_people()

    assert people[0][1] == "Ana María"
    assert people[0][3] == 26


def test_delete_person():
    init_db()

    person = {
        "nombre": "Carlos",
        "apellido": "Lopez",
        "edad": 40,
        "cedula": "1112223334",
        "nota": ""
    }

    create_person(person)
    people = get_people()
    pid = people[0][0]

    delete_person(pid)
    people = get_people()

    assert len(people) == 0
