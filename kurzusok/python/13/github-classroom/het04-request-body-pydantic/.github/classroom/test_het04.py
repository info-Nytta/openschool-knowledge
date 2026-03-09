"""
Rejtett tesztek a 4. heti házi feladathoz.
Request body, Pydantic modellek, CRUD in-memory.
"""
import sys
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_models_exist():
    import models
    assert hasattr(models, "Termek")
    print("PASS")


def test_get_termekek():
    r = client.get("/termekek")
    assert r.status_code == 200
    assert isinstance(r.json(), list)
    print("PASS")


def test_post_termek():
    r = client.post("/termekek", json={
        "nev": "Laptop",
        "ar": 350000,
        "leiras": "Teszt termék"
    })
    assert r.status_code == 201
    data = r.json()
    assert data["nev"] == "Laptop"
    assert "id" in data
    print("PASS")


def test_post_termek_invalid():
    r = client.post("/termekek", json={
        "nev": "",
        "ar": -100,
        "leiras": "Hibás"
    })
    assert r.status_code == 422
    print("PASS")


def test_get_termek_by_id():
    r = client.post("/termekek", json={
        "nev": "Egér",
        "ar": 5000,
        "leiras": "Teszt"
    })
    termek_id = r.json()["id"]
    r2 = client.get(f"/termekek/{termek_id}")
    assert r2.status_code == 200
    assert r2.json()["nev"] == "Egér"
    print("PASS")


def test_get_termek_not_found():
    r = client.get("/termekek/99999")
    assert r.status_code == 404
    print("PASS")


def test_put_termek():
    r = client.post("/termekek", json={
        "nev": "Monitor",
        "ar": 80000,
        "leiras": "Eredeti"
    })
    termek_id = r.json()["id"]
    r2 = client.put(f"/termekek/{termek_id}", json={"nev": "Módosított"})
    assert r2.status_code == 200
    assert r2.json()["nev"] == "Módosított"
    print("PASS")


def test_delete_termek():
    r = client.post("/termekek", json={
        "nev": "Törlendő",
        "ar": 1000,
        "leiras": "Teszt"
    })
    termek_id = r.json()["id"]
    r2 = client.delete(f"/termekek/{termek_id}")
    assert r2.status_code == 200
    r3 = client.get(f"/termekek/{termek_id}")
    assert r3.status_code == 404
    print("PASS")


def test_put_partial_update():
    r = client.post("/termekek", json={
        "nev": "Partial teszt",
        "ar": 9999,
        "leiras": "Eredeti leírás"
    })
    termek_id = r.json()["id"]
    r2 = client.put(f"/termekek/{termek_id}", json={"nev": "Csak név változott"})
    assert r2.status_code == 200
    data = r2.json()
    assert data["nev"] == "Csak név változott"
    assert data["ar"] == 9999
    print("PASS")


def test_post_rendeles():
    r = client.post("/rendelesek", json={
        "vevo_nev": "Kiss Anna",
        "cim": {"varos": "Budapest", "utca": "Fő utca 1", "irszam": "1001"},
        "tetelek": [{"nev": "Toll", "db": 3, "ar": 500}]
    })
    assert r.status_code in (200, 201)
    print("PASS")


if __name__ == "__main__":
    globals()[sys.argv[1]]()
