"""
Tesztek a Termék API-hoz.
A diák feladata a conftest.py elkészítése (SQLite mock DB).
"""


def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Termék API"


def test_termek_lista_ures(client):
    response = client.get("/termekek")
    assert response.status_code == 200
    assert response.json() == []


def test_termek_letrehozas(client):
    response = client.post("/termekek", json={
        "nev": "Laptop",
        "ar": 350000,
        "leiras": "Jó laptop"
    })
    assert response.status_code == 201
    data = response.json()
    assert data["nev"] == "Laptop"
    assert data["ar"] == 350000
    assert "id" in data


def test_termek_letrehozas_leiras_nelkul(client):
    response = client.post("/termekek", json={
        "nev": "Egér",
        "ar": 5000
    })
    assert response.status_code == 201
    assert response.json()["nev"] == "Egér"


def test_termek_lekeres(client):
    create_resp = client.post("/termekek", json={
        "nev": "Telefon",
        "ar": 150000
    })
    termek_id = create_resp.json()["id"]

    response = client.get(f"/termekek/{termek_id}")
    assert response.status_code == 200
    assert response.json()["nev"] == "Telefon"


def test_termek_nem_letezik(client):
    response = client.get("/termekek/9999")
    assert response.status_code == 404


def test_termek_torles(client):
    create_resp = client.post("/termekek", json={
        "nev": "Törlendő",
        "ar": 100
    })
    termek_id = create_resp.json()["id"]

    response = client.delete(f"/termekek/{termek_id}")
    assert response.status_code == 200

    get_resp = client.get(f"/termekek/{termek_id}")
    assert get_resp.status_code == 404


def test_termek_torles_nem_letezik(client):
    response = client.delete("/termekek/9999")
    assert response.status_code == 404


def test_tobb_termek(client):
    for i in range(3):
        client.post("/termekek", json={
            "nev": f"Termek {i}",
            "ar": 1000 * (i + 1)
        })
    response = client.get("/termekek")
    assert len(response.json()) == 3


def test_izolacio(client):
    """Az előző teszt adatai nem maradnak meg."""
    response = client.get("/termekek")
    assert response.json() == []
