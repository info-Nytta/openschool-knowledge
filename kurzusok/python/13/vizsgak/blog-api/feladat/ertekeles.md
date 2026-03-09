# Értékelési rubrika – Backend szintfelmérő 13. évfolyam (B variáns: Blog API)

**Összesen: 60 pont**

---

## 1. feladat – Pydantic sémák és utility függvények (10 pont)

### 1.1 Sémák (6 pont)

| Szempont | Pont |
|----------|------|
| `PostCreate` séma – mezők és típusok helyesek | 1 |
| `PostCreate` – validáció (min_length) | 1 |
| `PostRead` séma – id, publikalva, letrehozva mezők | 1 |
| `PostUpdate` séma – opcionális mezők | 1 |
| `FelhasznaloCreate` séma – felhasznalonev, jelszo, validáció | 1 |
| `Token` séma – access_token, token_type | 1 |

### 1.2 Utility függvények (4 pont)

| Szempont | Pont |
|----------|------|
| `szavak_szama()` – helyes számolás | 1 |
| `rovid_kivonat()` – helyes csonkolás és `"..."` | 1 |
| `szuro_cimke()` – helyes szűrés | 1 |
| `statisztika()` – helyes összesítés | 1 |

---

## 2. feladat – SQLAlchemy adatbázis és CRUD API (20 pont)

### 2.1 Adatbázis beállítás (6 pont)

| Szempont | Pont |
|----------|------|
| `database.py` – engine, SessionLocal, Base helyes | 1 |
| `database.py` – `get_db()` dependency (yield + close) | 1 |
| `models.py` – `PostModel` definiálva, mezők helyesek | 2 |
| `models.py` – `FelhasznaloModel` definiálva (unique felhasznalonev) | 1 |
| Táblák automatikus létrehozása (`Base.metadata.create_all`) | 1 |

### 2.2 CRUD végpontok (14 pont)

| Szempont | Pont |
|----------|------|
| `GET /` végpont – helyes válasz | 1 |
| `GET /posts` – listázás SQLAlchemy query-vel | 2 |
| `GET /posts` – query paraméter szűrés (publikalva, cimke) | 2 |
| `GET /posts/{post_id}` – létező poszt visszaadása | 1 |
| `GET /posts/{post_id}` – 404 hiba kezelés | 1 |
| `POST /posts` – létrehozás adatbázisba (201 státusz) | 2 |
| `PUT /posts/{post_id}` – módosítás (exclude_unset) | 1 |
| `DELETE /posts/{post_id}` – törlés + 404 kezelés | 1 |
| `GET /posts/statisztika` – helyes eredmény | 1 |
| `posztok.txt` betöltése induláskor (ha üres a tábla) | 1 |
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
| `beolvasas()` – helyes típuskonverzió (bool) | 1 |
| `osszes_darab()` – helyes darabszám | 1 |
| `publikus_arany()` – helyes százalék, kerekítés | 2 |
| `leghosszabb_poszt()` – helyes keresés | 2 |
| `cimkek_szerint()` – helyes csoportosítás | 2 |

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
| `test_root` + `test_get_posts` – alap végpontok tesztelése | 1 |
| `test_create_post_unauthorized` + `test_delete_unauthorized` – 401 tesztelés | 1 |
| `test_register` + `test_login` – auth végpontok tesztelése | 1 |
| `test_create_post_with_auth` – auth flow tesztelése | 1 |
| TestClient használat, assert-ek helyessége | 1 |
