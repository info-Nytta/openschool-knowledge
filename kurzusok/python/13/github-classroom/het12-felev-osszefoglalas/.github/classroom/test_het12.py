"""
Rejtett tesztek a 12. heti házi feladathoz (félév összefoglalás).
Gyors Leltár API teszt – in-memory, DB nélkül.
"""
import sys
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root():
    r = client.get("/")
    assert r.status_code == 200
    print("PASS")


def test_get_eszkozok():
    r = client.get("/eszkozok")
    assert r.status_code == 200
    assert isinstance(r.json(), list)
    print("PASS")


def test_post_eszkoz():
    r = client.post("/eszkozok", json={
        "nev": "Laptop",
        "kategoria": "elektronika",
        "ertek": 350000
    })
    assert r.status_code in (200, 201)
    data = r.json()
    assert data["nev"] == "Laptop"
    print("PASS")


def test_post_eszkoz_invalid():
    r = client.post("/eszkozok", json={
        "nev": "",
        "kategoria": "elektronika",
        "ertek": -100
    })
    assert r.status_code == 422
    print("PASS")


if __name__ == "__main__":
    globals()[sys.argv[1]]()
