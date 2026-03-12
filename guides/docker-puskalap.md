# Docker puskalap

A leggyakrabban használt Docker és Docker Compose parancsok, a Backend FastAPI kurzushoz.

---

## Alapvető Docker parancsok

```bash
# Docker verzió ellenőrzése
docker --version
docker compose version

# Futó konténerek listázása
docker ps

# Minden konténer (leállítottak is)
docker ps -a

# Image-ek listázása
docker images
```

---

## Docker Compose — Napi használat

```bash
# Szolgáltatások indítása (háttérben)
docker compose up -d

# Szolgáltatások leállítása
docker compose down

# Szolgáltatások újraindítása
docker compose restart

# Logok megtekintése
docker compose logs

# Egy szolgáltatás logjai (élőben)
docker compose logs -f web

# Szolgáltatások állapota
docker compose ps
```

---

## Konténer kezelés

```bash
# Belépés egy futó konténerbe
docker compose exec web bash

# Parancs futtatása konténerben
docker compose exec web python -c "print('Helló')"

# Konténer leállítása
docker compose stop web

# Konténer törlése
docker compose rm web

# Minden leállítása és törlése (volume-ok nélkül)
docker compose down

# Mindent törlés (volume-okkal együtt!)
docker compose down -v
```

---

## Image kezelés

```bash
# Image újraépítése
docker compose build

# Image újraépítése cache nélkül
docker compose build --no-cache

# Használaton kívüli image-ek törlése
docker image prune

# Minden nem használt erőforrás törlése
docker system prune
```

---

## `docker-compose.yml` — Alap felépítés

```yaml
services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/mydb
    depends_on:
      - db
    volumes:
      - .:/app

  db:
    image: postgres:16
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
      - POSTGRES_DB=mydb
    ports:
      - "5432:5432"
    volumes:
      - db_data:/var/lib/postgresql/data

volumes:
  db_data:
```

### Magyarázat

| Kulcs | Jelentés |
|-------|----------|
| `build: .` | A Dockerfile-ból építi az image-et |
| `image: postgres:16` | Kész image használata a Docker Hub-ról |
| `ports: "8000:8000"` | Hoszt port : Konténer port |
| `environment` | Környezeti változók a konténerben |
| `depends_on` | Indítási sorrend (a `db` indul előbb) |
| `volumes` | Fájlok megosztása hoszt és konténer között |
| `db_data:` | Elnevezett volume — az adatok megmaradnak a konténer törlésekor is |

---

## Dockerfile — Alap felépítés

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Magyarázat

| Utasítás | Jelentés |
|----------|----------|
| `FROM` | Alap image kiválasztása |
| `WORKDIR` | Munkakönyvtár beállítása a konténerben |
| `COPY` | Fájlok másolása a konténerbe |
| `RUN` | Parancs futtatása az image építésekor |
| `CMD` | A konténer indulásakor futó parancs |

---

## PostgreSQL konténer

```bash
# PostgreSQL konténer indítása
docker compose up -d db

# Csatlakozás a PostgreSQL-hez konténerből
docker compose exec db psql -U user -d mydb

# Alembic migrációk futtatása
docker compose exec web alembic upgrade head

# Új migráció generálása
docker compose exec web alembic revision --autogenerate -m "leírás"
```

---

## Port kezelés

```bash
# Ki használja a 8000-es portot?
lsof -i :8000        # macOS / Linux
netstat -ano | findstr :8000   # Windows

# Leállítás, ha a port foglalt
docker compose down
```

---

## Gyakori hibák és megoldásaik

| Hiba | Megoldás |
|------|----------|
| `docker: command not found` | Docker nincs telepítve. Lásd: [Környezet beállítás](kornyezet-beallitas.md) |
| `permission denied` (Linux) | `sudo usermod -aG docker $USER` → kijelentkezés → bejelentkezés |
| `permission denied` (Windows) | Docker Desktop fut? Rendszergazdaként indítsd. |
| `port is already allocated` | `docker compose down`, vagy másik portot használj |
| `connection refused` a DB-hez | Az adatbázis konténer nem fut: `docker compose up -d db` |
| A konténer azonnal leáll | `docker compose logs <szolgáltatás>` — nézd meg a hibaüzenetet |
| `no space left on device` | `docker system prune` — nem használt erőforrások törlése |
| `.env` nem töltődik be | Ellenőrizd: a fájl neve `.env` (nem `env.txt`). Docker Compose automatikusan betölti. |

---

## Hasznos tippek

- **Fejlesztés közben** használj volume mount-ot (`.:/app`), hogy ne kelljen újraépíteni az image-et minden fájlváltoztatásnál
- **Teszteléshez** használj SQLite in-memory adatbázist, nem kell Docker
- **Éles környezetben** ne használj `volumes: .:/app` — építsd be a kódot az image-be
- **Logok** mindig az első hely, ahova nézz, ha valami nem működik

---

**Kapcsolódó útmutatók:**
- [Környezet beállítás](kornyezet-beallitas.md)
- [Git puskalap](git-puskalap.md)
- [Hibaelhárítás](hibaelharitas.md)
- [Szótár](szotar.md)
