import pytest
from fastapi.testclient import TestClient
from main import app


@pytest.fixture
def client():
    return TestClient(app)


# GET /

def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Jegyzet API"


# GET /jegyzetek

def test_jegyzetek_ures(client):
    response = client.get("/jegyzetek")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# POST /jegyzetek

def test_jegyzet_letrehozas(client):
    response = client.post("/jegyzetek", json={
        "cim": "Teszt jegyzet",
        "tartalom": "Ez egy teszt"
    })
    assert response.status_code == 201
    data = response.json()
    assert data["cim"] == "Teszt jegyzet"
    assert data["tartalom"] == "Ez egy teszt"
    assert "id" in data


def test_jegyzet_ures_cim(client):
    response = client.post("/jegyzetek", json={
        "cim": "",
        "tartalom": "Tartalom"
    })
    assert response.status_code == 422


# GET /jegyzetek/{id}

def test_jegyzet_lekeres(client):
    create_resp = client.post("/jegyzetek", json={
        "cim": "Keresett",
        "tartalom": "Tartalom"
    })
    jegyzet_id = create_resp.json()["id"]
    response = client.get(f"/jegyzetek/{jegyzet_id}")
    assert response.status_code == 200
    assert response.json()["cim"] == "Keresett"


def test_jegyzet_nem_letezik(client):
    response = client.get("/jegyzetek/99999")
    assert response.status_code == 404


# DELETE /jegyzetek/{id}

def test_jegyzet_torles(client):
    create_resp = client.post("/jegyzetek", json={
        "cim": "Törlendő",
        "tartalom": "Tartalom"
    })
    jegyzet_id = create_resp.json()["id"]
    response = client.delete(f"/jegyzetek/{jegyzet_id}")
    assert response.status_code == 200

    # Ellenőrzés: már nem létezik
    get_resp = client.get(f"/jegyzetek/{jegyzet_id}")
    assert get_resp.status_code == 404


def test_jegyzet_torles_nem_letezik(client):
    response = client.delete("/jegyzetek/99999")
    assert response.status_code == 404
