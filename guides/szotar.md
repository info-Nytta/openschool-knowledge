# Szótár — Technikai fogalmak

Ez a szótár a kurzusok során használt legfontosabb technikai fogalmakat gyűjti össze, magyar magyarázattal.

---

## Python

| Fogalom | Magyarázat |
|---------|------------|
| **Változó (variable)** | Adat tárolására szolgáló elnevezett hely. Pl. `nev = "Anna"` |
| **Adattípus (data type)** | Az adat kategóriája: `int` (egész szám), `float` (tizedes), `str` (szöveg), `bool` (igaz/hamis) |
| **Függvény (function)** | Újrafelhasználható kódblokk, amit `def` kulcsszóval hozunk létre |
| **Paraméter (parameter)** | A függvény bemeneti értéke: `def koszont(nev):` — itt `nev` a paraméter |
| **Visszatérési érték (return)** | A függvény kimenete: `return eredmeny` |
| **Lista (list)** | Rendezett, módosítható gyűjtemény: `[1, 2, 3]` |
| **Szótár (dictionary)** | Kulcs-érték párok gyűjteménye: `{"nev": "Anna", "kor": 25}` |
| **Ciklus (loop)** | Ismétlődő kódblokk: `for` (ismert darabszám) vagy `while` (feltétel alapján) |
| **Feltételes elágazás (if/elif/else)** | A program döntést hoz egy feltétel alapján |
| **Modul (module)** | Újrafelhasználható Python fájl, amit `import`-tal használunk |
| **List comprehension** | Tömör listaépítés: `[x*2 for x in lista if x > 0]` |
| **Fájlkezelés (file I/O)** | Fájlok olvasása/írása: `open("fajl.txt", encoding="utf-8")` |
| **Kivételkezelés (try/except)** | Hibák kezelése a program leállása nélkül |
| **pip** | Python csomagkezelő — csomagok telepítése: `pip install csomagnev` |
| **venv (virtual environment)** | Elszigetelt Python környezet, hogy a projektek ne zavarják egymást |
| **requirements.txt** | A projekt függőségeinek listája: `pip install -r requirements.txt` |

---

## Git és GitHub

| Fogalom | Magyarázat |
|---------|------------|
| **Repository (repó)** | Verziókezelt projekt mappa, ami tartalmazza a kód teljes történetét |
| **Commit** | Változások mentése pillanatképként, üzenettel: `git commit -m "leírás"` |
| **Push** | Commitok feltöltése a távoli szerverre: `git push` |
| **Pull** | Változások letöltése a távoli szerverről: `git pull` |
| **Clone** | Repó másolása a saját gépre: `git clone <URL>` |
| **Branch (ág)** | Független fejlesztési vonal: `git checkout -b uj-funkció` |
| **Merge** | Két ág egyesítése |
| **Fork** | A repó független másolata a saját GitHub fiókon |
| **Pull Request (PR)** | Változások beolvasztásának kérelme — kód-átnézéssel |
| **Remote (origin)** | A távoli szerver, ahova a kód fel van töltve (általában GitHub) |
| **`.gitignore`** | Fájlok listája, amiket a Git figyelmen kívül hagy (pl. `venv/`, `.env`) |
| **Git log** | A commitok történetének megtekintése: `git log --oneline` |
| **GitHub Actions** | Automatizált munkafolyamatok GitHub-on (tesztek, deploy) |

---

## Web és API

| Fogalom | Magyarázat |55
|---------|------------|
| **API** | Application Programming Interface — programok közötti kommunikáció |
| **Endpoint** | Egy konkrét URL cím az API-ban (pl. `/users`, `/items/5`) |
| **HTTP metódus** | A kérés típusa: `GET` (lekérés), `POST` (létrehozás), `PUT` (frissítés), `DELETE` (törlés) |
| **Request (kérés)** | A kliens kérése a szerver felé |
| **Response (válasz)** | A szerver válasza a kliensnek |
| **Status code (státuszkód)** | Eredmény jelző: `200` (OK), `201` (létrehozva), `404` (nem található), `422` (érvénytelen), `500` (szerverhiba) |
| **JSON** | Adatformátum: `{"kulcs": "érték"}` — az API-k standard nyelve |
| **REST** | API tervezési stílus — erőforrás-alapú URL-ek + HTTP metódusok |
| **CRUD** | Négy alapművelet: Create, Read, Update, Delete |
| **Path paraméter** | URL-be ágyazott változó: `/users/{id}` |
| **Query paraméter** | URL-hez fűzött szűrő: `/users?limit=10&skip=5` |
| **Request body** | A kéréssel küldött adat (JSON formátumban, POST/PUT kéréseknél) |
| **Middleware** | Köztes réteg, ami a kérést/választ módosítja mielőtt a végponthoz érne |
| **CORS** | Cross-Origin Resource Sharing — más domainről érkező kérések engedélyezése |
| **Swagger UI** | Interaktív API dokumentáció (`/docs` URL alatt) |

---

## FastAPI

| Fogalom | Magyarázat |
|---------|------------|
| **FastAPI** | Modern Python web keretrendszer API-k építésére |
| **Uvicorn** | ASGI szerver, ami futtatja a FastAPI alkalmazást: `uvicorn main:app --reload` |
| **Dekorátor** | Végpont jelölő: `@app.get("/users")`, `@app.post("/items")` |
| **Pydantic** | Adatvalidáló könyvtár — sémák (schemas) definiálására |
| **Schema (séma)** | Pydantic modell, ami leírja az adat struktúráját és típusait |
| **Dependency Injection** | Függőségek automatikus átadása a végpontoknak (pl. adatbázis kapcsolat) |
| **Router** | Kapcsolódó végpontok csoportosítása — `APIRouter()` |
| **Response model** | A válasz elvárt struktúrájának megadása a végponton |
| **HTTPException** | Hiba válasz küldése: `raise HTTPException(status_code=404, detail="Nem található")` |
| **`--reload`** | Fejlesztési mód — a szerver automatikusan újraindul fájlmódosításnál |

---

## Adatbázis

| Fogalom | Magyarázat |
|---------|------------|
| **SQL** | Structured Query Language — adatbázis lekérdező nyelv |
| **PostgreSQL** | Nyílt forráskódú relációs adatbázis-kezelő |
| **SQLite** | Fájl-alapú, könnyű adatbázis (teszteléshez ideális) |
| **ORM** | Object-Relational Mapping — Python objektumok és adatbázis táblák közötti leképezés |
| **SQLAlchemy** | Python ORM könyvtár |
| **Model (modell)** | Python osztály, ami egy adatbázis táblát reprezentál |
| **Session** | SQLAlchemy kapcsolat az adatbázishoz — ezen keresztül futnak a lekérdezések |
| **Engine** | SQLAlchemy adatbázis-kapcsolat kezelő |
| **Alembic** | Adatbázis migrációs eszköz — a séma változások verziókezelése |
| **Migráció** | Adatbázis szerkezet módosítása strukturált módon |
| **Foreign Key (idegen kulcs)** | Hivatkozás egy másik tábla sorára — kapcsolatok létrehozására |
| **Relationship** | SQLAlchemy kapcsolat modellek között (egy-a-többhöz, több-a-többhöz) |

---

## Autentikáció és biztonság

| Fogalom | Magyarázat |
|---------|------------|
| **Autentikáció** | Felhasználó személyazonosságának ellenőrzése (ki vagy?) |
| **Autorizáció** | Jogosultság ellenőrzése (mit tehetsz?) |
| **JWT (JSON Web Token)** | Biztonságos token formátum — bejelentkezés után kapod, és minden kéréshez csatolod |
| **Access token** | Rövid élettartamú hitelesítő token |
| **Hash** | Egyirányú titkosítás — a jelszót hash-eli, visszafejteni nem lehet |
| **bcrypt** | Jelszó hash-elő algoritmus |
| **Bearer token** | A token küldési módja: `Authorization: Bearer <token>` |
| **OAuth** | Külső szolgáltatáson keresztüli bejelentkezés (pl. GitHub OAuth) |
| **`.env` fájl** | Környezeti változók fájl — titkos adatok (jelszavak, kulcsok) tárolása |

---

## Docker

| Fogalom | Magyarázat |
|---------|------------|
| **Konténer (container)** | Elszigetelt futtatási környezet — könnyű virtuális gép |
| **Image (kép)** | Sablon a konténer létrehozásához — tartalmazza a kódot és a függőségeket |
| **Dockerfile** | Szöveges fájl, ami leírja, hogyan kell az image-et felépíteni |
| **Docker Compose** | Több konténer együttes kezelése egyetlen paranccsal |
| **`docker-compose.yml`** | Szolgáltatások konfigurációs fájlja |
| **Service (szolgáltatás)** | Egy konténer a Docker Compose-ban (pl. `web`, `db`) |
| **Port mapping** | Konténer port összekötése a hoszt porttal: `8000:8000` |
| **Volume (kötet)** | Tartós adattárolás — a konténer törlése után is megmarad |
| **Network (hálózat)** | Konténerek közötti kommunikáció |
| **`depends_on`** | Szolgáltatás indítási sorrend (pl. az app várja az adatbázist) |
| **Registry** | Image-ek tárháza (pl. Docker Hub) |

---

## Tesztelés

| Fogalom | Magyarázat |
|---------|------------|
| **pytest** | Python tesztelési keretrendszer |
| **Test case (teszteset)** | Egyetlen teszt, ami egy konkrét viselkedést ellenőriz |
| **Assert** | Állítás — ha hamis, a teszt elbukik: `assert eredmeny == 42` |
| **Fixture** | Előkészített tesztadat vagy erőforrás (`@pytest.fixture`) |
| **Mock** | Hamis objektum teszteléshez — a valódi függőségek helyettesítése |
| **Konftest (`conftest.py`)** | Megosztott fixture-ök fájlja — pytest automatikusan betölti |
| **Coverage** | A tesztek által lefedett kód aránya (százalékban) |
| **Pozitív teszt** | Ellenőrzi, hogy a helyes bemenet helyes eredményt ad |
| **Negatív teszt** | Ellenőrzi, hogy a hibás bemenet megfelelő hibaüzenetet ad |
| **Autograding** | Automatikus értékelés GitHub Classroom-ban — GitHub Actions futtatja |

---

## CI/CD és üzemeltetés

| Fogalom | Magyarázat |
|---------|------------|
| **CI (Continuous Integration)** | Minden push után automatikusan futnak a tesztek |
| **CD (Continuous Deployment)** | Sikeres tesztek után automatikus telepítés |
| **Pipeline** | Automatizált lépések sorozata: build → teszt → deploy |
| **VPS** | Virtual Private Server — felhő szerver az alkalmazás futtatásához |
| **nginx** | Webszerver és reverse proxy |
| **Reverse proxy** | Az nginx továbbítja a kéréseket az alkalmazásnak |
| **SSL/TLS** | Titkosított kapcsolat (HTTPS) |
| **Deploy** | Az alkalmazás élesbe helyezése |
| **Monitoring** | Az alkalmazás állapotának és teljesítményének figyelése |

---

**Kapcsolódó útmutatók:**
- [Kezdő útmutató](kezdo-utmutato.md)
- [Környezet beállítás](kornyezet-beallitas.md)
- [Git puskalap](git-puskalap.md)
- [Docker puskalap](docker-puskalap.md)
