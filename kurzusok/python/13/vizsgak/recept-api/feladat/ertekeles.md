# Értékelési rubrika – Backend szintfelmérő 13. évfolyam (D variáns: Recept API)

**Összesen: 60 pont**

---

## 1. feladat – Pydantic sémák és utility függvények (10 pont)

### 1.1 Sémák (6 pont)

| Szempont | Pont |
|----------|------|
| `ReceptCreate` séma – mezők és típusok helyesek | 1 |
| `ReceptCreate` – validáció (min_length, ge) | 1 |
| `ReceptRead` séma – id, kedvenc, letrehozva mezők | 1 |
| `ReceptUpdate` séma – opcionális mezők | 1 |
| `FelhasznaloCreate` séma – felhasznalonev, jelszo, validáció | 1 |
| `Token` séma – access_token, token_type | 1 |

### 1.2 Utility függvények (4 pont)

| Szempont | Pont |
|----------|------|
| `ido_formatum()` – helyes formázás (óra + perc) | 1 |
| `kaloria_kategoria()` – helyes kategorizálás | 1 |
| `szuro_kategoria()` – helyes szűrés | 1 |
| `statisztika()` – helyes összesítés | 1 |

---

## 2. feladat – SQLAlchemy adatbázis és CRUD API (20 pont)

### 2.1 Adatbázis beállítás (6 pont)

| Szempont | Pont |
|----------|------|
| `database.py` – engine, SessionLocal, Base helyes | 1 |
| `database.py` – `get_db()` dependency (yield + close) | 1 |
| `models.py` – `ReceptModel` definiálva, mezők helyesek | 2 |
| `models.py` – `FelhasznaloModel` definiálva (unique felhasznalonev) | 1 |
| Táblák automatikus létrehozása (`Base.metadata.create_all`) | 1 |

### 2.2 CRUD végpontok (14 pont)

| Szempont | Pont |
|----------|------|
| `GET /` végpont – helyes válasz | 1 |
| `GET /receptek` – listázás SQLAlchemy query-vel | 2 |
| `GET /receptek` – query paraméter szűrés (kategoria, max_ido) | 2 |
| `GET /receptek/{recept_id}` – létező recept visszaadása | 1 |
| `GET /receptek/{recept_id}` – 404 hiba kezelés | 1 |
| `POST /receptek` – létrehozás adatbázisba (201 státusz) | 2 |
| `PUT /receptek/{recept_id}` – módosítás (exclude_unset) | 1 |
| `DELETE /receptek/{recept_id}` – törlés + 404 kezelés | 1 |
| `GET /receptek/statisztika` – helyes eredmény | 1 |
| `receptek.txt` betöltése induláskor (ha üres a tábla) | 1 |
| Kódminőség (Depends(get_db), struktúra) | 1 |

---

## 3. feladat – Authentikáció (10 pont)

| Szempont | Pont |
|----------|------|
| `POST /auth/regisztracio` – felhasználó létrehozása DB-ben | 2 |
| Jelszó hash-elése (passlib + bcrypt) | 2 |
| Foglalt felhasználónév kezelése (400) | 1 |
| `POST /auth/login` – helyes adatok → JWT token | 2 |
| Hibás adatok → 401 | 1 |
| `get_current_user` dependency – token dekódolás | 1 |
| Védett végpontok használják a dependency-t (POST, DELETE) | 1 |

---

## 4. feladat – Adatfeldolgozás (10 pont)

| Szempont | Pont |
|----------|------|
| `beolvasas()` – fájl megnyitása, sorok feldolgozása | 2 |
| `beolvasas()` – helyes típuskonverzió (int, bool) | 1 |
| `osszes_darab()` – helyes darabszám | 1 |
| `atlag_kaloria()` – helyes átlag, kerekítés | 2 |
| `leggyorsabb()` – helyes keresés | 2 |
| `kategoriak_szerint()` – helyes csoportosítás | 2 |

---

## 5. feladat – Docker és tesztelés (10 pont)

### 5.1 Docker (5 pont)

| Szempont | Pont |
|----------|------|
| `Dockerfile` – helyes base image (python:3.11-slim) | 1 |
| `Dockerfile` – WORKDIR, COPY, RUN pip install | 2 |
| `Dockerfile` – CMD uvicorn, port 8000 | 1 |
| `requirements.txt` – összes szükséges csomag | 1 |

### 5.2 Tesztelés (5 pont)

| Szempont | Pont |
|----------|------|
| `test_root` + `test_get_receptek` – alap végpontok tesztelése | 1 |
| `test_create_recept_unauthorized` + `test_delete_unauthorized` – 401 tesztelés | 1 |
| `test_register` + `test_login` – auth végpontok tesztelése | 1 |
| `test_create_recept_with_auth` – auth flow tesztelése | 1 |
| TestClient használat, assert-ek helyessége | 1 |
