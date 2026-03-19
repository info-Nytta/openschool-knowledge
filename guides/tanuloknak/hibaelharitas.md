# Hibaelhárítás

A leggyakoribb problémák és megoldásaik. Ha itt nem találod → keresd meg a [dokumentációban](dokumentacio-kereses.md), vagy kérdezz a Discord `#segítség` csatornán.

---

## Általános módszer

1. **Olvasd el a hibaüzenetet** — alulról felfelé, az utolsó sor a legfontosabb
2. **Ellenőrizd a környezetet** — a venv aktív? A Docker fut? Jó mappában vagy?
3. **Keresd meg online** — a hiba típusát (pl. `ValueError`) angolul írd be a keresőbe
4. **Kérdezz Discordon** — de [mutasd meg, mit próbáltál](../mentoroknak/kozossegi-utmutato.md)

---

## Git és GitHub

**`fatal: not a git repository`** — Nem Git repó mappában vagy. `cd`-zz a repó mappájába.

**`failed to push` / `rejected`** — A távoli repó újabb. Futtasd: `git pull --rebase` majd `git push`.

**`Permission denied (publickey)`** — SSH kulcs nincs beállítva. Ellenőrizd: `ssh -T git@github.com`. Ha nem megy, lásd: [Környezet beállítás](kornyezet-beallitas.md).

## GitHub Classroom

**A tesztek nem futnak le** — A fájljaid a **gyökérmappában** legyenek, ne almappában.

**Lokálisan működik, Actions-ben nem** — Ne használj abszolút fájlutat. Az `open()` hívásokhoz add meg: `encoding="utf-8"`.

**„404 Not Found" a Classroom linknél** — Nem vagy bejelentkezve GitHubra.

**„You don't have access"** — Nem vagy tagja a GitHub szervezetnek. Kérd a mentorod.

## Python

**`ModuleNotFoundError`** — A virtuális környezet nincs aktiválva: `source .venv/bin/activate`

**`FileNotFoundError`** — A fájl (`.txt`/`.csv`) nem ugyanabban a mappában van, mint a `.py`. Mozgasd egy helyre, vagy használj relatív útvonalat.

**`UnicodeDecodeError`** — Hiányzik az encoding: `open("fajl.txt", encoding="utf-8")`

**`TypeError: can't concat str to int`** — Típuskonverzió kell: `int()` számokhoz, `str()` szövegekhez.

## Backend (FastAPI)

**`ModuleNotFoundError: No module named 'fastapi'`** — A venv nincs aktiválva.

**`sqlalchemy.exc.OperationalError: connection refused`** — A PostgreSQL konténer nem fut: `docker compose up -d`

**`422 Unprocessable Entity`** — A request body nem felel meg a Pydantic sémának. Ellenőrizd a JSON-t és a mezők típusait.

**`401 Unauthorized`** — Lejárt JWT token. Jelentkezz be újra.

**GitHub Classroom tesztek FAIL, de lokálisan PASS** — A tesztek SQLite-ot használnak. Ellenőrizd a `conftest.py`-t és a `dependency_overrides` beállítást.

**`psycopg2` telepítési hiba** — Linux: `sudo apt install libpq-dev python3-dev`. Windows: használd a `psycopg2-binary` csomagot.

## Docker

**`permission denied` (Linux)** — `sudo usermod -aG docker $USER`, majd jelentkezz ki és be.

**`port is already allocated`** — Valami más foglalja a portot. `docker compose down` vagy változtasd meg a portot.

**A konténer elindul, de azonnal leáll** — Nézd a logokat: `docker compose logs <szolgáltatás>`

**A PostgreSQL konténer nem indul** — Ellenőrizd a `.env` fájlban: `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`.

---

**Kapcsolódó:** [Git puskalap](../puskak/git-puskalap.md) · [Docker puskalap](../puskak/docker-puskalap.md) · [Környezet beállítás](kornyezet-beallitas.md) · [GitHub Classroom útmutató](github-classroom-tanulo-utmutato.md)
