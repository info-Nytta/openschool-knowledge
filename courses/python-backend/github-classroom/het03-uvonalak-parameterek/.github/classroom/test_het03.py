"""
Rejtett tesztek a 3. heti házi feladathoz.
Path paraméterek, query paraméterek, Enum.
"""
import sys
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_koszontes():
    r = client.get("/koszontes/Anna")
    assert r.status_code == 200
    assert "Anna" in r.json()["uzenet"]
    print("PASS")


def test_szorzas():
    r = client.get("/szorzas/3/7")
    assert r.status_code == 200
    assert r.json()["eredmeny"] == 21
    print("PASS")


def test_kereses_query():
    r = client.get("/kereses?q=teszt&limit=5")
    assert r.status_code == 200
    print("PASS")


def test_elemek_skip_limit():
    r = client.get("/elemek?skip=0&limit=5")
    assert r.status_code == 200
    assert isinstance(r.json(), list)
    assert len(r.json()) == 5
    print("PASS")


def test_elemek_limit_validation():
    r = client.get("/elemek?limit=200")
    assert r.status_code == 422
    print("PASS")


def test_termekek_kategoria():
    r = client.get("/termekek/elektronika")
    assert r.status_code == 200
    print("PASS")


def test_termekek_invalid_kategoria():
    r = client.get("/termekek/nem_letezo")
    assert r.status_code == 422
    print("PASS")


def test_termekek_ar_szures():
    r = client.get("/termekek/elektronika?min_ar=1000&max_ar=50000")
    assert r.status_code == 200
    print("PASS")


if __name__ == "__main__":
    globals()[sys.argv[1]]()
