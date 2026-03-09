from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Todo API" in response.json()["message"]


def test_create_todo_unauthorized():
    response = client.post("/todos", json={"cim": "Teszt feladat"})
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


def test_create_todo_with_auth():
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
        "/todos",
        json={"cim": "Auth teszt todo"},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 201


def test_get_todos():
    response = client.get("/todos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_todo_not_found():
    response = client.get("/todos/9999")
    assert response.status_code == 404


def test_delete_todo_unauthorized():
    response = client.delete("/todos/1")
    assert response.status_code == 401
