# Modul 6 — Éles üzem

## Cél

A platform kihelyezése éles környezetbe. A modul végére:

- A platform fut a VPS-en, saját domain-en, HTTPS-sel
- Minden main-re push-olt kód automatikusan kitelepül (CD)
- Van staging és production környezet
- Az adatbázisról rendszeres backup készül

## 6.1 Szerver előkészítés

**VPS követelmények:**
- Linux (Ubuntu 22.04+)
- Docker és Docker Compose telepítve
- SSH hozzáférés kulcs-alapú autentikációval

**Feladat:**
- Telepítsd a Docker-t és Docker Compose-t a VPS-re
- Hozz létre egy deploy felhasználót (ne root-ként futtasd a platformot)
- Állítsd be az SSH kulcs-alapú belépést
- Tűzfal beállítás: csak 80, 443, és SSH port legyen nyitva

## 6.2 Domain és SSL

**Cloudflare beállítás:**
1. Domain hozzáadása a Cloudflare-hez
2. DNS rekord: `devschool.hu` → VPS IP (A rekord)
3. SSL mód: Full (strict)
4. Cloudflare automatikusan kezeli az SSL tanúsítványt

**Staging domain:**
- `staging.devschool.hu` → ugyanaz a VPS, külön Docker Compose konfig

**Feladat:**
- Állítsd be a DNS rekordokat
- Cloudflare SSL: Full (strict)
- Teszteld: `https://devschool.hu` elérhető (egyelőre akár egy statikus oldallal)

## 6.3 nginx konfiguráció

```nginx
# nginx/nginx.conf
server {
    listen 80;
    server_name devschool.hu;

    # API → FastAPI backend
    location /api/ {
        proxy_pass http://backend:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # Tanúsítvány verifikáció → FastAPI
    location /verify/ {
        proxy_pass http://backend:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    # Minden más → Astro frontend (statikus fájlok)
    location / {
        root /usr/share/nginx/html;
        try_files $uri $uri/ /index.html;
    }
}
```

**Feladat:**
- Írd meg az nginx konfigurációt
- Az API hívások (`/api/*`) a backend-re proxy-zódjanak
- A statikus fájlokat az Astro build mappából szolgálja ki
- Teszteld helyben: `docker compose up` → minden elérhető

## 6.4 Production Docker Compose

```yaml
# docker-compose.prod.yml
services:
  backend:
    build: ./backend
    restart: always
    env_file: .env.prod
    depends_on:
      - db

  db:
    image: postgres:16
    restart: always
    environment:
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
      POSTGRES_DB: ${DB_NAME}
    volumes:
      - pgdata:/var/lib/postgresql/data

  nginx:
    image: nginx:alpine
    restart: always
    ports:
      - "80:80"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf
      - frontend_build:/usr/share/nginx/html
    depends_on:
      - backend
      - frontend

  frontend:
    build: ./frontend
    volumes:
      - frontend_build:/app/dist

volumes:
  pgdata:
  frontend_build:
```

**Különbségek a dev konfighoz képest:**
- `restart: always` — a container-ek automatikusan újraindulnak
- Nincs port mapping a backend-en (csak nginx-en keresztül érhető el)
- Nincs volume mount fejlesztői fájlokhoz
- `.env.prod` a production környezeti változókkal

**Feladat:**
- Írd meg a `docker-compose.prod.yml` fájlt
- Hozd létre a `.env.prod` fájlt (ne commitold, legyen a `.gitignore`-ban)
- Teszteld: `docker compose -f docker-compose.prod.yml up --build`

## 6.5 GitHub Actions CD

```yaml
# .github/workflows/cd.yml
name: CD

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - name: Deploy to VPS
        uses: appleboy/ssh-action@v1
        with:
          host: ${{ secrets.VPS_HOST }}
          username: ${{ secrets.VPS_USER }}
          key: ${{ secrets.VPS_SSH_KEY }}
          script: |
            cd /opt/devschool
            git pull origin main
            docker compose -f docker-compose.prod.yml pull
            docker compose -f docker-compose.prod.yml up --build -d
            docker compose -f docker-compose.prod.yml exec backend alembic upgrade head
```

**GitHub Secrets beállítása:**
- `VPS_HOST`: a szerver IP címe
- `VPS_USER`: a deploy felhasználó neve
- `VPS_SSH_KEY`: a privát SSH kulcs

**Feladat:**
- Hozd létre a CD workflow-t
- Állítsd be a GitHub Secrets-et a repóban
- Teszteld: push to main → a szerveren frissül a platform

## 6.6 Staging vs Production

| Környezet | Domain | Branch | Cél |
|-----------|--------|--------|-----|
| Staging | `staging.devschool.hu` | `develop` | Tesztelés éles-szerű környezetben |
| Production | `devschool.hu` | `main` | Éles, felhasználók által használt |

**Feladat:**
- A CD workflow-t bővítsd: `develop` branch → staging, `main` branch → production
- Külön `.env.staging` és `.env.prod` fájlok
- A staging adatbázis legyen független a production-tól

## 6.7 Monitoring és logok

**Alap monitoring:**
- Health check endpoint: `GET /api/health` → a CD script hívja deploy után
- Docker health check a `docker-compose.prod.yml`-ben:
  ```yaml
  backend:
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
  ```

**Logok:**
- Docker logok: `docker compose logs -f backend`
- Strukturált logolás: `uvicorn` access log + Python `logging` modul
- Log rotáció: Docker `json-file` driver max-size beállítással

**Feladat:**
- Adj hozzá health check-et a Docker konfigurációhoz
- Állíts be log rotációt
- A deploy script ellenőrizze a health check-et deploy után

## 6.8 Backup

**PostgreSQL backup:**

```bash
#!/bin/bash
# scripts/backup.sh
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/opt/devschool/backups"
mkdir -p "$BACKUP_DIR"

docker compose -f /opt/devschool/docker-compose.prod.yml exec -T db \
  pg_dump -U "$DB_USER" "$DB_NAME" | gzip > "$BACKUP_DIR/db_$TIMESTAMP.sql.gz"

# Régi backupok törlése (30 napnál régebbi)
find "$BACKUP_DIR" -name "*.sql.gz" -mtime +30 -delete
```

**Cron job (napi backup):**
```
0 3 * * * /opt/devschool/scripts/backup.sh
```

**Feladat:**
- Írd meg a backup scriptet
- Állítsd be a cron job-ot a szerveren
- Teszteld: futtasd manuálisan, ellenőrizd, hogy a backup fájl visszaállítható

## Háttéranyag

Ezeket nem kell elejétől végig elolvasni — használd referenciaként, amikor az adott témánál tartasz.

| Téma | Link | Miért hasznos |
|------|------|---------------|
| nginx reverse proxy | [nginx.org/en/docs/beginners_guide.html](https://nginx.org/en/docs/beginners_guide.html) | nginx konfiguráció, proxy_pass, SSL |
| Cloudflare SSL | [developers.cloudflare.com/ssl](https://developers.cloudflare.com/ssl/) | Domain + SSL beállítás, Full (strict) mód |
| Docker Compose production | [docs.docker.com/compose/production](https://docs.docker.com/compose/production/) | Éles környezet best practice-ek |
| GitHub Actions SSH deploy | [github.com/appleboy/ssh-action](https://github.com/appleboy/ssh-action) | SSH-n keresztüli automatikus deploy |
| PostgreSQL backup | [www.postgresql.org/docs/current/backup-dump.html](https://www.postgresql.org/docs/current/backup-dump.html) | pg_dump, automatikus backup stratégiák |
| Linux tűzfal (ufw) | [help.ubuntu.com/community/UFW](https://help.ubuntu.com/community/UFW) | Szerver portok védelme |
| Docker logging | [docs.docker.com/engine/logging](https://docs.docker.com/engine/logging/) | Container logok kezelése és rotálása |

## Verifikációs tesztek

A modul végén futtasd a verifikációs teszteket:

```bash
cd devschool-platform
pytest tesztek/modul-06/ -v
```

**Mit ellenőriznek a tesztek:**

| Tesztfájl | Ellenőrzések |
|-----------|---------------|
| `test_prod.py` | `docker-compose.prod.yml` létezik és van restart policy; nginx konfig létezik; CD workflow létezik; `.env.prod` a `.gitignore`-ban van; backup script létezik; a DB port nincs kívülre nyitva a prod compose-ban |

> **Megjegyzés:** Az éles deploy működését a tesztek nem tudják autómatikusan ellenőrizni (VPS hozzáférés kell hozzá). A konfigurációs fájlok meglétét és helyes felépítését viszont igen.

## Ellenőrzőlista

- [ ] A platform fut a VPS-en: `https://devschool.hu` elérhető
- [ ] HTTPS működik (Cloudflare SSL)
- [ ] Push to main → automatikus deploy (GitHub Actions CD)
- [ ] Staging környezet külön domain-en fut
- [ ] Health check endpoint elérhető
- [ ] PostgreSQL backup cron job fut naponta
- [ ] Logok elérhetők és rotálódnak
- [ ] `.env.prod` nincs a Git repóban
- [ ] `pytest tesztek/modul-06/ -v` → minden zöld (verifikációs tesztek)
