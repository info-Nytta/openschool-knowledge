from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Recept API"


def test_create_recept_unauthorized():
    response = client.post("/receptek", json={
        "nev": "Teszt Leves",
        "kategoria": "leves",
        "elkeszitesi_ido": 30,
        "kaloria": 250,
    })
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


def test_create_recept_with_auth():
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
        "/receptek",
        json={"nev": "Auth teszt recept", "kategoria": "leves", "elkeszitesi_ido": 20, "kaloria": 150},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 201


def test_get_receptek():
    response = client.get("/receptek")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_recept_not_found():
    response = client.get("/receptek/9999")
    assert response.status_code == 404


def test_delete_recept_unauthorized():
    response = client.delete("/receptek/1")
    assert response.status_code == 401
