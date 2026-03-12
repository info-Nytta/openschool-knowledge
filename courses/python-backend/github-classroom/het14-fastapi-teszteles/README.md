# 14. hét – FastAPI tesztelés

> **Határidő:** a következő óra előtt
> **Beadás:** commitold és pushold a megoldásaidat ebbe a repóba!
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

## Feladat

Készíts egy **Jegyzet API**-t a `main.py` fájlban, amely in-memory listát használ:

### Modell (`Jegyzet`):
- `cim` (str, min 1 karakter)
- `tartalom` (str, min 1 karakter)

### Végpontok:

- `GET /` → `{"message": "Jegyzet API"}` ⭐
- `GET /jegyzetek` → az összes jegyzet listája ⭐
- `POST /jegyzetek` → új jegyzet létrehozása (201), id-t a szerver generálja ⭐⭐
- `GET /jegyzetek/{id}` → egy jegyzet lekérése, 404 ha nem létezik ⭐⭐
- `DELETE /jegyzetek/{id}` → jegyzet törlése, 404 ha nem létezik ⭐⭐⭐

Az automatikus tesztelés rejtett tesztekkel ellenőrzi a végpontjaidat.

---

## Automatikus tesztelés

A push után rejtett tesztek futnak (GitHub Classroom Autograding). Helyi teszteléshez használd a TestClient-et:
```bash
pip install fastapi uvicorn httpx pytest
python3 -c "from fastapi.testclient import TestClient; from main import app; c = TestClient(app); print(c.get('/').json())"
```

## Dokumentáció

- [FastAPI Testing](https://fastapi.tiangolo.com/tutorial/testing/)
- [TestClient](https://www.starlette.io/testclient/)

## Beadás

1. `main.py` legyen a repó gyökerében
2. A push után a rejtett tesztek automatikusan futnak
3. Commitolj értelmes üzenetekkel
4. `git push` – ez a beadás!
