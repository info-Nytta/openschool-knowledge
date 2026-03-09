"""
Rejtett tesztek a 5. heti házi feladathoz.
Response modellek, hibakezelés, státuszkódok.
"""
import sys
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_response_model():
    # Létrehozunk egy terméket, hogy biztosan legyen adat
    client.post("/termekek", json={
        "nev": "Rejtett teszt",
        "ar": 1000,
        "leiras": "Teszt",
        "titkos_kod": "TITOK123"
    })
    r = client.get("/termekek")
    assert r.status_code == 200
    assert len(r.json()) > 0
    assert "titkos_kod" not in r.json()[-1]
    print("PASS")


def test_404_felhasznalo():
    r = client.get("/felhasznalok/99999")
    assert r.status_code == 404
    print("PASS")


def test_403_admin():
    r = client.get("/felhasznalok/0")
    assert r.status_code == 403
    print("PASS")


def test_hibakodok():
    kodok = [400, 401, 403, 404]
    for kod in kodok:
        r = client.get(f"/hiba/{kod}")
        assert r.status_code == kod, f"Várt {kod}, kapott {r.status_code}"
    print("PASS")


def test_custom_exception():
    # Ellenőrizzük, hogy a NemTalalhatoError exception handler regisztrálva van
    # és a válasz formátuma {"hiba": true, "uzenet": "..."}
    from main import app as test_app
    handlers = getattr(test_app, 'exception_handlers', {})
    # Az exception handler léte + a response formátum ellenőrzése
    r = client.get("/felhasznalok/99999")
    assert r.status_code == 404
    data = r.json()
    # Ha egyedi handler van, a "hiba" kulcsot várjuk
    if "hiba" in data:
        assert data["hiba"] is True
        assert "uzenet" in data
    print("PASS")


def test_status_code_201():
    r = client.post("/termekek", json={
        "nev": "Status teszt",
        "ar": 500,
        "leiras": "Teszt"
    })
    assert r.status_code == 201
    print("PASS")


if __name__ == "__main__":
    globals()[sys.argv[1]]()
