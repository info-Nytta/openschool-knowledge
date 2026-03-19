# Tanterv – Backend fejlesztés FastAPI-val

## Kurzus áttekintés

| Jellemző | Érték |
|----------|-------|
| Szint | Haladó (Python előismeret szükséges) |
| Időtartam | 25 hét (6 hónap) |
| Nyelv | Python 3.10+ |
| Keretrendszer | FastAPI |
| Adatbázis | PostgreSQL (Docker) |
| Tesztelés | pytest + TestClient |
| Vizsga | 60 pont, 240 perc |
| Beadás | GitHub Classroom (automatikus pytest értékelés) |

## Célkitűzés

A kurzus végére a tanuló képes önállóan:
- REST API-t tervezni és implementálni FastAPI-val
- PostgreSQL adatbázist kezelni Docker környezetben
- SQLAlchemy ORM-mel dolgozni, migrációkat futtatni (Alembic)
- JWT alapú authentikációt megvalósítani
- Automatizált API teszteket írni pytest-tel
- Docker Compose-zal több szolgáltatást összehangolni
- CI/CD pipeline-t beállítani GitHub Actions-szel

## Szükséges előismeretek

A Python Alapok kurzus ismeretanyaga:
- Változók, típusok, vezérlési szerkezetek
- Függvények, listák, szótárak
- Fájlkezelés (olvasás/írás)
- Git alapok (commit, push, pull)

## Szükséges eszközök

| Eszköz | Verzió | Megjegyzés |
|--------|--------|------------|
| Python | 3.10+ | `python3 --version` (Windows: `python --version`) |
| Git | 2.x+ | `git --version` |
| VS Code | legújabb | Python + REST Client kiegészítők |
| Docker | 20.x+ | `docker --version` |
| Docker Compose | 2.x+ | `docker compose version` |
| Operációs rendszer | Windows 10+ / Linux / macOS | Windowson Docker Desktop szükséges |

## Heti bontás

---

### 0. hét – Git, GitHub, parancssor alapok
> 3 × 2 lecke = 6 lecke

**1–2. lecke: Parancssor alapok**
- Terminál megnyitása, navigáció (`cd`, `ls`/`dir`, `pwd`, `mkdir`)
- Fájlműveletek (`cp`/`copy`, `mv`/`move`, `rm`/`del`, `cat`/`type`)
- Linux jogosultságok (`chmod`, `chown`) – Windows: a Git Bash vagy WSL2 által elérhetőek

**3–4. lecke: Git ismétlés és haladó funkciók**
- `git init`, `add`, `commit`, `push`, `pull`
- `.gitignore` fájl
- Branch-ek (`git branch`, `git checkout`, `git merge`)
- Konfliktuskezelés

**5–6. lecke: GitHub Classroom munkafolyamat**
- Meghívó link elfogadása
- Klónozás, munka, push
- Automatikus tesztek értelmezése
- Gyakorlás: bemutatkozó repo létrehozása

---

### 1. hét – Python ismétlés, virtuális környezet
> 3 × 2 lecke = 6 lecke

**7–8. lecke: Python ismétlés**
- Változók, típusok, vezérlési szerkezetek
- Függvények, listák, szótárak
- Fájlkezelés gyorsismétlés

**9–10. lecke: Virtuális környezetek**
- Mi a `venv` és miért fontos?
- `python3 -m venv venv` → `source venv/bin/activate` (Windows: `python -m venv venv` → `venv\Scripts\activate`)
- `pip install`, `pip freeze > requirements.txt`
- `pip install -r requirements.txt`
- `.gitignore` beállítása (`venv/`, `__pycache__/`)

**11–12. lecke: Projektstruktúra és csomagkezelés**
- Python csomagok és modulok
- `__init__.py` szerepe
- Mappastruktúra kialakítása backend projekthez
- Gyakorlás: saját csomag készítése

---

### 2. hét – FastAPI bevezetés
> 3 × 2 lecke = 6 lecke

**13–14. lecke: Mi az a REST API?**
- HTTP protokoll: kérés → válasz
- HTTP metódusok: GET, POST, PUT, DELETE
- Státuszkódok: 200, 201, 404, 422, 500
- JSON formátum

**15–16. lecke: Első FastAPI alkalmazás**
- `pip install fastapi uvicorn`
- `main.py` → `app = FastAPI()`
- Első GET végpont: `/`
- Futtatás: `uvicorn main:app --reload`
- Swagger UI: `http://127.0.0.1:8000/docs`

**17–18. lecke: Több végpont, visszatérési értékek**
- Több GET végpont
- JSON válaszok (dict)
- Lista visszaadása
- Gyakorlás: egyszerű „Hello API" alkalmazás

---

### 3. hét – Útvonalak és paraméterek
> 3 × 2 lecke = 6 lecke

**19–20. lecke: Path paraméterek**
- `@app.get("/items/{item_id}")`
- Típusmegkötés: `item_id: int`
- Több path paraméter
- Enum típusú paraméterek

**21–22. lecke: Query paraméterek**
- `?skip=0&limit=10`
- Opcionális paraméterek: `Optional[str] = None`
- Több query paraméter kombinálása
- Validáció: `Query(min_length=3, max_length=50)`

**23–24. lecke: Path + Query kombinálása**
- Összetett végpontok
- Gyakorlás: egyszerű terméklistázó API

---

### 4. hét – Request body és Pydantic
> 3 × 2 lecke = 6 lecke

**25–26. lecke: Pydantic modellek**
- `BaseModel` öröklés
- Mezők típusmegadása
- Alapértelmezett értékek
- Validáció: `Field(min_length=1, ge=0)`

**27–28. lecke: POST végpont request body-val**
- `@app.post("/items/")`
- Pydantic modell mint paraméter
- Automatikus validáció
- Swagger UI-ban tesztelés

**29–30. lecke: PUT, DELETE végpontok**
- Elem módosítása: `@app.put("/items/{item_id}")`
- Elem törlése: `@app.delete("/items/{item_id}")`
- Gyakorlás: teljes CRUD API memóriában (lista/szótár)

---

### 5. hét – Response modellek és hibakezelés
> 3 × 2 lecke = 6 lecke

**31–32. lecke: Response modellek**
- `response_model` paraméter
- Különböző create/read/update sémák
- `response_model_exclude_unset=True`

**33–34. lecke: Státuszkódok és hibakezelés**
- `status_code=201` (created)
- `HTTPException(status_code=404, detail="...")`
- Egyedi hibaválaszok
- `@app.exception_handler()`

**35–36. lecke: Validációs hibák**
- Pydantic validációs hibaüzenetek
- `RequestValidationError` kezelése
- Gyakorlás: robusztus termékkezelő API hibakezeléssel

---

### 6. hét – Dependency Injection és projektstruktúra
> 3 × 2 lecke = 6 lecke

**37–38. lecke: Dependency Injection**
- `Depends()` függvény
- Közös logika kiemelése (pl. pagination)
- Függőségek láncolása

**39–40. lecke: Projekt struktúra kialakítása**
- `app/` → `main.py`, `models.py`, `schemas.py`, `routers/`, `dependencies.py`
- APIRouter használata
- Include router: `app.include_router()`

**41–42. lecke: Konfigurációkezelés**
- Környezeti változók: `os.environ`
- `python-dotenv` és `.env` fájl
- Pydantic `BaseSettings` osztály
- `.env.example` készítése
- Gyakorlás: strukturált API projekt készítése

---

### 7. hét – Docker és PostgreSQL
> 3 × 2 lecke = 6 lecke

**43–44. lecke: Docker alapok**
- Mi az a konténer? Mi a Docker?
- `Dockerfile` készítése Python alkalmazáshoz
- `docker build`, `docker run`
- Port mapping: `-p 8000:8000`

**45–46. lecke: PostgreSQL Dockerben**
- `docker run postgres:16`
- Környezeti változók: `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`
- `psql` csatlakozás
- Alapszintű SQL: `CREATE TABLE`, `INSERT`, `SELECT`

**47–48. lecke: Docker Compose bevezetés**
- `docker-compose.yml` (app + db)
- `docker compose up -d`
- Szolgáltatások összekötése
- Volumes: adatmegőrzés
- Gyakorlás: FastAPI + PostgreSQL docker compose

---

### 8. hét – SQLAlchemy ORM
> 3 × 2 lecke = 6 lecke

**49–50. lecke: SQLAlchemy bevezetés**
- ORM fogalma
- `pip install sqlalchemy psycopg2-binary`
- Engine és Session létrehozása
- `DATABASE_URL` összeállítása

**51–52. lecke: Modellek definiálása**
- `declarative_base()`
- Oszloptípusok: `Column`, `Integer`, `String`, `Float`, `Boolean`, `DateTime`
- Elsődleges kulcs, nullable
- `__tablename__`

**53–54. lecke: Alembic migrációk**
- `pip install alembic`
- `alembic init alembic`
- `alembic revision --autogenerate -m "..."`
- `alembic upgrade head`
- Gyakorlás: felhasználó tábla létrehozása

---

### 9. hét – CRUD műveletek adatbázissal
> 3 × 2 lecke = 6 lecke

**55–56. lecke: Adatbázis session kezelés**
- `get_db()` dependency
- `SessionLocal()` és `yield`
- Session lezárás (finally)

**57–58. lecke: CRUD függvények**
- `crud.py` modul
- `create_item()`, `get_item()`, `get_items()`
- `update_item()`, `delete_item()`
- SQLAlchemy lekérdezések: `query()`, `filter()`, `first()`, `all()`

**59–60. lecke: CRUD összekötése végpontokkal**
- Router → CRUD → DB
- Pydantic schema ↔ SQLAlchemy modell konverzió
- Gyakorlás: teljes CRUD API adatbázissal

---

### 10. hét – Authentikáció és JWT
> 3 × 2 lecke = 6 lecke

**61–62. lecke: Authentikáció alapok**
- Mi az authentikáció és autorizáció?
- Jelszó hash-elés: `passlib` + `bcrypt`
- Felhasználó regisztráció végpont

**63–64. lecke: JWT tokenek**
- Mi a JWT? (header, payload, signature)
- `pip install python-jose[cryptography]`
- Token generálás és validálás
- Login végpont: email + jelszó → token

**65–66. lecke: Védett végpontok**
- `OAuth2PasswordBearer`
- `get_current_user()` dependency
- Token ellenőrzés
- Gyakorlás: regisztráció, login, védett profil végpont

---

### 11. hét – Middleware, CORS, biztonság
> 3 × 2 lecke = 6 lecke

**67–68. lecke: Middleware**
- Mi a middleware?
- Request/response logging
- Végrehajtási idő mérése
- Egyedi middleware írása

**69–70. lecke: CORS beállítás**
- Mi az a CORS?
- `CORSMiddleware` hozzáadása
- `allow_origins`, `allow_methods`, `allow_headers`

**71–72. lecke: Biztonsági bevált gyakorlatok**
- Környezeti változók titkok tárolására
- Rate limiting alapok
- Input szanitizálás
- Gyakorlás: middleware-ek hozzáadása az API-hoz

---

### 12. hét – Félév összefoglalás, próbavizsga
> 3 × 2 lecke = 6 lecke

**73–74. lecke: Összefoglalás 1–11. hét**
- Fogalmak átismétlése
- Kódpéldák átnézése
- Kérdések megbeszélése

**75–76. lecke: Próbavizsga**
- Vizsgakörülmények között
- 60 pont, 120 perc
- GitHub Classroom beadás
- Automatikus pytest értékelés

**77–78. lecke: Próbavizsga megbeszélése**
- Tipikus hibák
- Pontozás áttekintése
- Javítási javaslatok

---

### 13. hét – Tesztelés alapok, pytest
> 3 × 2 lecke = 6 lecke

**79–80. lecke: Miért tesztelünk?**
- Manuális vs. automatikus tesztelés
- Tesztelési szintek: unit, integrációs, E2E
- `pip install pytest`
- Első teszt: `test_` prefix, `assert`

**81–82. lecke: pytest haladó funkciók**
- Fixture-ök: `@pytest.fixture`
- Parametrizálás: `@pytest.mark.parametrize`
- Setup és teardown

**83–84. lecke: Tesztelési minták**
- Arrange-Act-Assert (AAA) minta
- Pozitív és negatív tesztek
- Edge case-ek
- Gyakorlás: egyszerű Python függvények tesztelése

---

### 14. hét – FastAPI tesztelés TestClient-tel
> 3 × 2 lecke = 6 lecke

**85–86. lecke: TestClient bevezetés**
- `from fastapi.testclient import TestClient`
- `pip install httpx`
- GET végpont tesztelése
- Státuszkód és JSON body ellenőrzése

**87–88. lecke: POST, PUT, DELETE tesztelése**
- `client.post("/items/", json={...})`
- `client.put(...)`, `client.delete(...)`
- Hibaválaszok tesztelése (404, 422)

**89–90. lecke: Végpont tesztelés gyakorlat**
- Teljes CRUD tesztcsomag írása
- Tesztek futtatása: `pytest -v`
- Gyakorlás: végpontonként 3-5 teszt

---

### 15. hét – Adatbázis mockolás tesztekhez
> 3 × 2 lecke = 6 lecke

**91–92. lecke: Miért mockolunk?**
- Tesztek függetlensége
- GitHub Classroom: nincs valódi DB
- SQLite in-memory teszt adatbázis

**93–94. lecke: Dependency override**
- `app.dependency_overrides[get_db]`
- SQLite in-memory engine tesztekhez
- Teszt adatbázis séma létrehozása
- Fixture: `test_db` session

**95–96. lecke: Teljes tesztcsomag mock DB-vel**
- conftest.py felépítése
- Teszt adatok beszúrása fixture-ökkel
- CRUD tesztek mock DB-vel
- Gyakorlás: teljes API tesztelése mock adatbázissal

---

### 16. hét – Haladó tesztelés
> 3 × 2 lecke = 6 lecke

**97–98. lecke: Authentikáció tesztelése**
- Teszt felhasználó létrehozása
- Token generálás tesztben
- Védett végpontok tesztelése
- `Authorization: Bearer <token>` header

**99–100. lecke: Tesztelési szervezés**
- `tests/` mappa struktúra
- `conftest.py` fixture-ök megosztása
- Tesztek kategorizálása: `pytest.mark`
- Coverage mérés: `pytest --cov`

**101–102. lecke: Tesztelési bevált gyakorlatok**
- DRY tesztek
- Teszt izoláció
- Gyors tesztek
- Gyakorlás: tesztek refaktorálása, coverage javítása

---

### 17. hét – Fájlkezelés és feltöltés
> 3 × 2 lecke = 6 lecke

**103–104. lecke: Fájl feltöltés**
- `UploadFile` típus
- `@app.post("/upload/")`
- Fájl mentése szerverre
- Típusellenőrzés (csak képek, stb.)

**105–106. lecke: Statikus fájlok kiszolgálása**
- `StaticFiles` mount
- Fájl letöltés végpont
- Kép URL generálás

**107–108. lecke: Adat import/export**
- CSV olvasás és feldolgozás
- JSON export végpont
- Gyakorlás: CSV feltöltés és feldolgozás API

---

### 18. hét – Background Tasks és WebSocket
> 3 × 2 lecke = 6 lecke

**109–110. lecke: BackgroundTasks**
- `BackgroundTasks` paraméter
- Email küldés szimuláció háttérben
- Naplózás háttérben
- Hosszú futású feladatok

**111–112. lecke: WebSocket alapok**
- Mi a WebSocket?
- `@app.websocket("/ws")`
- Egyszerű echo szerver
- Kliens oldali kapcsolódás

**113–114. lecke: Értesítések**
- Broadcast üzenetek
- Gyakorlás: egyszerű chat alkalmazás

---

### 19. hét – Docker Compose haladó
> 3 × 2 lecke = 6 lecke

**115–116. lecke: Többszolgáltatásos alkalmazás**
- FastAPI + PostgreSQL + Adminer
- `docker-compose.yml` bővítése
- Szolgáltatások közötti hálózat

**117–118. lecke: Environment management**
- `.env` fájlok Docker Compose-zal
- Különböző környezetek (dev, test, prod)
- Health check beállítása
- Wait-for-it: adatbázis elérhetőség

**119–120. lecke: Optimalizált Docker image**
- Multi-stage build
- `.dockerignore`
- Méret optimalizálás
- Gyakorlás: production-ready Docker setup

---

### 20. hét – CI/CD és GitHub Actions
> 3 × 2 lecke = 6 lecke

**121–122. lecke: CI/CD fogalmak**
- Mi az a CI/CD?
- Pipeline felépítése
- GitHub Actions alapok
- `.github/workflows/` mappa

**123–124. lecke: Teszt pipeline**
- Workflow fájl: `ci.yml`
- Python setup, dependency install
- pytest futtatás
- Szolgáltatás konténerek (PostgreSQL)

**125–126. lecke: Linting és formázás**
- `ruff` vagy `flake8`
- `black` kódformázó
- Pre-commit hook-ok
- Gyakorlás: teljes CI pipeline

---

### 21. hét – Projekt tervezés
> 3 × 2 lecke = 6 lecke

**127–128. lecke: API tervezés**
- Követelmények felmérése
- Végpontok tervezése
- Adatmodell tervezés
- OpenAPI specifikáció

**129–130. lecke: Projekt váz elkészítése**
- Repository létrehozása
- Mappastruktúra kialakítása
- Adatbázis schema és migrációk
- Alap végpontok elkészítése

**131–132. lecke: Tesztek és CI tervezése**
- Teszt stratégia
- conftest.py és fixture-ök előkészítése
- GitHub Actions workflow
- Gyakorlás: projekt váz elkészítése

---

### 22. hét – Projekt fejlesztés
> 3 × 2 lecke = 6 lecke

**133–134. lecke: CRUD és üzleti logika**
- Végpontok implementálása
- Üzleti logika
- Hibakezelés

**135–136. lecke: Authentikáció beépítése**
- Felhasználókezelés
- JWT integráció
- Védett végpontok

**137–138. lecke: Tesztek írása**
- CRUD tesztek
- Auth tesztek
- Edge case-ek

---

### 23. hét – Projekt fejlesztés II
> 3 × 2 lecke = 6 lecke

**139–140. lecke: Docker és deployment**
- Dockerfile véglegesítése
- docker-compose.yml
- Dokumentáció

**141–142. lecke: README és API dokumentáció**
- README.md: telepítés, futtatás, végpontok
- OpenAPI/Swagger dokumentáció ellenőrzése
- Kód review

**143–144. lecke: Projekt bemutató**
- Projekt prezentáció
- Kérdések és válaszok
- Visszajelzés

---

### 24. hét – Vizsga
> 3 × 2 lecke = 6 lecke

**Vizsgaidőpont: 240 perc, 60 pont**

**1. feladat (10 pont) – Pydantic sémák és utility függvények**
- Pydantic sémák (Create, Read, Update + auth sémák)
- Validációs segédfüggvények (utils.py)

**2. feladat (20 pont) – SQLAlchemy adatbázis és CRUD API**
- SQLAlchemy modellek, SQLite adatbázis (database.py, models.py)
- CRUD végpontok (GET all, GET by id, POST, PUT, DELETE)
- Query paraméterek, hibakezelés, adatfájl betöltése

**3. feladat (10 pont) – JWT autentikáció**
- Felhasználó modell, regisztráció, login
- JWT token generálás és védett végpontok

**4. feladat (10 pont) – Adatfeldolgozás**
- feldolgozas.py: 5 függvény az adatok elemzésére
- Fájlból olvasás és statisztikák

**5. feladat (10 pont) – Docker és tesztelés**
- Dockerfile (python:3.12-slim, uvicorn, port 8000)
- requirements.txt
- pytest tesztek (min. 8 teszt, TestClient)

## Értékelés

| Összetevő | Súly |
|-----------|------|
| Heti házi feladatok | 20% |
| Órai munka | 15% |
| Próbavizsga (12. hét) | 15% |
| Szintfelmérő vizsga (24. hét) | 50% |

## Szinthatárok (vizsga: 60 pont)

| Pont | Szint |
|------|-------|
| 54–60 | Kiváló |
| 43–53 | Haladó |
| 31–42 | Megfelelő |
| 19–30 | Kezdő |
| 0–18 | Nem teljesített |
