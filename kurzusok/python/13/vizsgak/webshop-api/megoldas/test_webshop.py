from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Webshop API" in response.json()["message"]


def test_create_termek_unauthorized():
    response = client.post("/termekek", json={"nev": "Teszt termek", "ar": 2990, "kategoria": "teszt"})
    assert response.status_code == 401


def test_register():
    response = client.post("/auth/regisztracio", json={
        "felhasznalonev": "tesztelek",
        "jelszo": "titkosjelszo",
    })
    assert response.status_code == 201


def test_login():
    client.post("/auth/regisztracio", json={
        "felhasznalonev": "loginuser",
        "jelszo": "titkosjelszo",
    })
    response = client.post("/auth/login", json={
        "felhasznalonev": "loginuser",
        "jelszo": "titkosjelszo",
    })
    assert response.status_code == 200
    assert "access_token" in response.json()


def test_create_termek_with_auth():
    client.post("/auth/regisztracio", json={
        "felhasznalonev": "authuser",
        "jelszo": "titkosjelszo",
    })
    login = client.post("/auth/login", json={
        "felhasznalonev": "authuser",
        "jelszo": "titkosjelszo",
    })
    token = login.json()["access_token"]
    response = client.post(
        "/termekek",
        json={"nev": "Auth teszt termek", "ar": 2990, "kategoria": "teszt"},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 201


def test_get_termekek():
    response = client.get("/termekek")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_termek_not_found():
    response = client.get("/termekek/9999")
    assert response.status_code == 404


def test_delete_termek_unauthorized():
    response = client.delete("/termekek/1")
    assert response.status_code == 401
