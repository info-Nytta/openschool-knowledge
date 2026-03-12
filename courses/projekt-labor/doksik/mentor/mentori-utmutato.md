# Mentori útmutató – Projekt Labor

## Áttekintés

A Projekt Labor kurzus egyetlen nagy projektet épít végig: az **OpenSchool platformot**. A tanulók 7 modulon keresztül jutnak el a lokális fejlesztéstől a production deploymentig. A mentor szerepe itt nem heti előadások tartása, hanem **projektvezetői mentorálás**: mérföldkövek ellenőrzése, kód review, és technikai akadályok elhárítása.

### Előfeltételek

A tanulóknak a **Backend FastAPI** kurzust kell elvégezniük a Projekt Labor előtt. A mentor ellenőrizze, hogy minden tanuló rendelkezik az alábbi alapismeretekkel:

- FastAPI alkalmazásfejlesztés
- Docker és PostgreSQL használat
- Pytest tesztelés
- Git és GitHub munkafolyamatok

## A mentor szerepe

| Hagyományos kurzus | Projekt Labor |
|---|---|
| Heti előadás + házi feladat | Modulonkénti mérföldkövek |
| Autograding minden héten | Verifikációs tesztek + kód review |
| Tananyag átadása | Technikai mentorálás, blocker-ek feloldása |
| Egyéni munka | Közösségi projekt, PR-ek, code review |

## Modulonkénti mentorálási terv

### Modul 01 – Projekt indítás

**Cél:** Docker Compose alapú fejlesztői környezet + CI pipeline

**Mentor feladatok:**
- Ellenőrizni, hogy a repo fork/clone megfelelően megtörtént
- Segíteni a Docker Compose konfigurációban, ha elakadnak
- Bemutatni a GitHub Actions CI pipeline működését
- Verifikációs tesztek futtatásának ellenőrzése (`pytest tests/test_modul01_*.py`)

**Tipikus problémák:**
- Docker Desktop nem fut / nincs telepítve
- Port ütközések (`5432`, `8000`)
- `.env` fájl hiányzik vagy rosszul van kitöltve

**Mérföldkő:** `docker compose up` elindul, CI pipeline zöld

---

### Modul 02 – Felhasználókezelés

**Cél:** OAuth2 + JWT autentikáció, szerepkörök

**Mentor feladatok:**
- JWT token flow áttekintése a tanulóval
- Szerepkör-alapú hozzáférés-vezérlés konzultáció
- Biztonsági szempontok kiemelése (token lejárat, jelszó hashelés)
- Kód review az autentikációs végpontokra

**Tipikus problémák:**
- Token lejárat kezelése nem tiszta
- Jelszó hashelés kihagyása
- CORS beállítások hiányoznak
- Middleware sorrend hibás

**Mérföldkő:** Regisztráció, bejelentkezés, role-based access működik, tesztek zöldek

---

### Modul 03 – Kurzusok és haladás

**Cél:** Kurzuskezelés, GitHub API integráció, haladáskövetés

**Mentor feladatok:**
- GitHub API rate limiting megértése
- Adatmodell review (kurzus → modul → haladás kapcsolatok)
- Webhook vs polling megbeszélése

**Tipikus problémák:**
- GitHub API token jogosultságok
- Rate limiting kezelésének hiánya
- N+1 query probléma az ORM-ben

**Mérföldkő:** Kurzuslista, beiratkozás, haladás mentése működik

---

### Modul 04 – Tanúsítványrendszer

**Cél:** PDF generálás, letöltés, ellenőrzés

**Mentor feladatok:**
- PDF könyvtár választás segítése (pl. ReportLab, WeasyPrint)
- Fájltárolás megbeszélése (helyi vs objektum-tár)
- Tanúsítvány érvényesítési flow áttekintése

**Tipikus problémák:**
- PDF könyvtár telepítési problémák Docker-ben
- Betűkészlet problémák (ékezetes karakterek)
- Fájlméret kezelése

**Mérföldkő:** Tanúsítvány generálás és letöltés működik

---

### Modul 05 – Frontend

**Cél:** Astro frontend, API integráció

**Mentor feladatok:**
- Astro projekt struktúra áttekintése
- API hívások és állapotkezelés konzultáció
- Reszponzív design ellenőrzése

**Tipikus problémák:**
- CORS hibák frontend–backend között
- Környezeti változók frontend vs backend oldalon
- Build hibák Astro-ban

**Mérföldkő:** Frontend megjeleníti a kurzusokat, bejelentkezés működik

---

### Modul 06 – Production deployment

**Cél:** VPS telepítés, SSL, CD pipeline

**Mentor feladatok:**
- VPS beállítás segítése (vagy lokális szimuláció)
- nginx reverse proxy konfiguráció áttekintése
- SSL tanúsítvány (Let's Encrypt) beállítás
- CD pipeline kód review

**Tipikus problémák:**
- SSH kulcs beállítás
- Tűzfal szabályok
- DNS propagáció várási idő
- Docker Compose production vs development különbségek

**Mérföldkő:** Az alkalmazás elérhető HTTPS-en, CD pipeline automatikusan deployol

---

### Modul 07 – Open source és közösség

**Cél:** CONTRIBUTING.md, governance, közösségi munkafolyamatok

**Mentor feladatok:**
- CONTRIBUTING.md és PR template review
- Issue management workflow megbeszélése
- Kód review kultúra és etika
- Nyílt forráskódú licencelés áttekintése

**Tipikus problémák:**
- PR leírás nem informatív
- Code review felületes
- Commit üzenetek nem követnek konvenciót

**Mérföldkő:** A projekt nyílt forráskódú közösségi munkafolyamatokkal működik

---

## Mentorálási munkafolyamat

### Modulkezdés előtt
- Olvassa el az adott modul dokumentációját (`doksik/modulok/`)
- Futtassa a verifikációs teszteket a saját gépen
- Készítse elő a gyakori kérdésekre a válaszokat

### Modul közben
- Heti 1-2 konzultáció (egyéni vagy csoportos)
- Pull request review-k 48 órán belül
- Discord csatornán elérhető kérdésekre

### Modul lezárásakor
- Verifikációs tesztek futtatása a tanuló repóján
- Kód review az adott modul kódjára
- Mérföldkő teljesítésének rögzítése

## Verifikációs tesztek

A tanulók munkáját a `tesztek/` mappában lévő verifikációs tesztek ellenőrzik automatikusan. Ezek **nem a tanulók által írt tesztek**, hanem a kurzus által biztosított ellenőrző tesztek.

```bash
# Összes modul tesztelése
pytest tests/ -v

# Egy adott modul tesztelése
pytest tests/test_modul01_*.py -v
```

A mentor a verifikációs tesztek mellett **kód review-t** is végez — a tesztek a funkcionális követelményeket ellenőrzik, de a kódminőséget emberi szemmel kell értékelni.

## Kapcsolódó dokumentumok

- [Tanterv](../tanterv/tanterv.md)
- [Értékelési módszertan](ertekeles-modszertan.md)
- [Integrált munkafolyamat](../../../guides/integralt-munkafolyamat.md)
