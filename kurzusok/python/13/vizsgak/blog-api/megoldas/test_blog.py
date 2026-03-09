from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Blog API" in response.json()["message"]


def test_create_post_unauthorized():
    response = client.post("/posts", json={
        "cim": "Teszt poszt cime",
        "tartalom": "Ez egy teszt poszt tartalma, ami eleg hosszu.",
        "szerzo": "Teszt Szerzo",
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


def test_create_post_with_auth():
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
        "/posts",
        json={
            "cim": "Auth teszt poszt",
            "tartalom": "Ez egy auth teszthez keszult poszt tartalma.",
            "szerzo": "Auth User",
        },
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 201


def test_get_posts():
    response = client.get("/posts")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_post_not_found():
    response = client.get("/posts/9999")
    assert response.status_code == 404


def test_delete_post_unauthorized():
    response = client.delete("/posts/1")
    assert response.status_code == 401
