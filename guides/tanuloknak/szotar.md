# Szótár

A kurzusok során előforduló fogalmak, amik elsőre nem egyértelműek. Ha valami alapvetőbb kell (pl. mi az a változó, lista, ciklus), azt a heti leckék elmagyarázzák.

---

## Python

| Fogalom | Röviden |
|---------|---------|
| **venv** | Elszigetelt Python környezet, hogy a projektek ne zavarják egymást |
| **pip** | Python csomagkezelő: `pip install csomagnev` |
| **requirements.txt** | A projekt függőségei: `pip install -r requirements.txt` |
| **List comprehension** | Tömör listaépítés: `[x*2 for x in lista if x > 0]` |

## Git / GitHub

| Fogalom | Röviden |
|---------|---------|
| **Repository (repó)** | Verziókezelt projektmappa a teljes előzménnyel |
| **Commit** | Pillanatkép a kódról, üzenettel: `git commit -m "leírás"` |
| **Branch (ág)** | Független fejlesztési vonal |
| **Fork** | A repó másolata a saját GitHub fiókodon |
| **Pull Request (PR)** | Változások beolvasztásának kérelme + kód-átnézés |
| **`.gitignore`** | Fájlok, amiket a Git figyelmen kívül hagy (pl. `venv/`, `.env`) |
| **GitHub Actions** | Automatikus tesztek és deploy GitHub-on |

## Web / API

| Fogalom | Röviden |
|---------|---------|
| **API** | Programok közötti kommunikáció (Application Programming Interface) |
| **Endpoint** | Egy URL az API-ban (pl. `/users`, `/items/5`) |
| **REST** | API stílus: erőforrás-alapú URL-ek + HTTP metódusok |
| **CRUD** | Create, Read, Update, Delete — a négy alapművelet |
| **JSON** | Adatformátum: `{"kulcs": "érték"}` |
| **Middleware** | Köztes réteg, ami a kérést/választ módosítja a végpont előtt |
| **CORS** | Más domainről érkező kérések engedélyezése |
| **Swagger UI** | Interaktív API dokumentáció (`/docs`) |

## FastAPI

| Fogalom | Röviden |
|---------|---------|
| **Pydantic** | Adatvalidálás — sémák definiálása típusokkal |
| **Dependency Injection** | Függőségek automatikus átadása végpontoknak (pl. DB session) |
| **Router** | Kapcsolódó végpontok csoportosítása: `APIRouter()` |
| **HTTPException** | Hiba küldése: `raise HTTPException(status_code=404, detail="...")` |

## Adatbázis

| Fogalom | Röviden |
|---------|---------|
| **ORM** | Python objektumok ↔ adatbázis táblák leképezés |
| **SQLAlchemy** | Python ORM könyvtár |
| **Alembic** | Adatbázis séma verziókezelés (migrációk) |
| **Foreign Key** | Hivatkozás másik táblára — kapcsolatok létrehozása |

## Auth

| Fogalom | Röviden |
|---------|---------|
| **JWT** | JSON Web Token — bejelentkezés utáni hitelesítő token |
| **OAuth** | Külső szolgáltatáson keresztüli bejelentkezés (pl. GitHub) |
| **Hash** | Egyirányú titkosítás — jelszó hash-elése, visszafejthetetlen |
| **Bearer token** | Token küldése: `Authorization: Bearer <token>` |

## Docker

| Fogalom | Röviden |
|---------|---------|
| **Konténer** | Elszigetelt futtatási környezet — könnyű virtuális gép |
| **Image** | Sablon a konténerhez — kód + függőségek |
| **Docker Compose** | Több konténer együttes kezelése: `docker compose up` |
| **Volume** | Tartós adattárolás — megmarad a konténer törlésekor is |

## Tesztelés

| Fogalom | Röviden |
|---------|---------|
| **Fixture** | Előkészített tesztadat: `@pytest.fixture` |
| **Mock** | Hamis objektum — a valódi függőségek helyettesítése tesztben |
| **Coverage** | Tesztek által lefedett kód aránya (%) |
| **Autograding** | Automatikus értékelés GitHub Classroom-ban |

## CI/CD

| Fogalom | Röviden |
|---------|---------|
| **CI** | Continuous Integration — minden push után automatikus tesztek |
| **CD** | Continuous Deployment — sikeres tesztek után automatikus deploy |
| **Pipeline** | Automatikus lépések: build → teszt → deploy |
| **VPS** | Felhő szerver az alkalmazás futtatásához |
| **Reverse proxy** | Az nginx továbbítja a kéréseket az alkalmazásnak |

---

**Kapcsolódó:** [Kezdő útmutató](kezdo-utmutato.md) · [Git puskalap](../puskak/git-puskalap.md) · [Docker puskalap](../puskak/docker-puskalap.md)
