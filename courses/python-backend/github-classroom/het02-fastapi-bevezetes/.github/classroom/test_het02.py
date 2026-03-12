"""
Rejtett tesztek a 2. heti házi feladathoz.
A diák main.py-t ír, ez a szkript ellenőrzi a végpontokat.
"""
import sys
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json()["message"] == "Helló, világ!"
    print("PASS")


def test_info():
    r = client.get("/info")
    assert r.status_code == 200
    data = r.json()
    assert "nev" in data or "name" in data or "api" in data
    print("PASS")


def test_datum():
    r = client.get("/datum")
    assert r.status_code == 200
    print("PASS")


def test_gyumolcsok_lista():
    r = client.get("/gyumolcsok")
    assert r.status_code == 200
    assert isinstance(r.json(), list)
    assert len(r.json()) >= 5
    print("PASS")


def test_gyumolcs_index():
    r = client.get("/gyumolcsok/0")
    assert r.status_code == 200
    print("PASS")


def test_gyumolcs_hozzaadas():
    r = client.post("/gyumolcsok", json={"nev": "mangó"})
    assert r.status_code in (200, 201)
    print("PASS")


def test_gyumolcs_torles():
    r = client.get("/gyumolcsok")
    eredeti = len(r.json())
    r = client.delete("/gyumolcsok/0")
    assert r.status_code == 200
    r2 = client.get("/gyumolcsok")
    assert len(r2.json()) == eredeti - 1
    print("PASS")


if __name__ == "__main__":
    globals()[sys.argv[1]]()
