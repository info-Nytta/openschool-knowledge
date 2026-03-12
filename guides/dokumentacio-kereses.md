# Hogyan keress dokumentációt?

Ez az útmutató megtanítja, hogyan találj válaszokat önállóan — mielőtt kérdést tennél fel. A programozás egyik legfontosabb készsége a **hatékony keresés**.

---

## Tartalomjegyzék

- [1. Olvasd el a hibaüzenetet](#1-olvasd-el-a-hibaüzenetet)
- [2. Keress az OpenSchool tudásbázisban](#2-keress-az-openschool-tudásbázisban)
- [3. Hivatalos dokumentáció használata](#3-hivatalos-dokumentáció-használata)
- [4. Hatékony keresés a weben](#4-hatékony-keresés-a-weben)
- [5. Stack Overflow és fórumok](#5-stack-overflow-és-fórumok)
- [6. Beépített súgó használata](#6-beépített-súgó-használata)
- [7. Ha továbbra sem találsz megoldást](#7-ha-továbbra-sem-találsz-megoldást)

---

## 1. Olvasd el a hibaüzenetet

A hibaüzenet nem ellenség — **a leghasznosabb információforrás**. Mielőtt bármit keresel, olvasd el figyelmesen.

### Hogyan értelmezz egy hibaüzenetet?

```
Traceback (most recent call last):
  File "feladat3.py", line 12, in <module>
    eredmeny = szamol(szoveg)
  File "feladat3.py", line 5, in szamol
    return int(szoveg)
ValueError: invalid literal for int() with base 10: 'alma'
```

| Rész | Mit jelent |
|------|-----------|
| `File "feladat3.py", line 12` | Melyik fájl, melyik sor |
| `in szamol` | Melyik függvényben történt |
| `ValueError` | A hiba típusa — **ezt keresd!** |
| `invalid literal for int()...` | A konkrét ok — a `'alma'` szöveget próbáltad számmá alakítani |

### Tipp

- **Alulról felfelé** olvasd a hibaüzenetet — az utolsó sor a legfontosabb
- A hiba típusát (`ValueError`, `TypeError`, `KeyError`, stb.) másold ki kereséshez
- Ha a hibaüzenet angol, ne fordítsd le — angolul keress rá

---

## 2. Keress az OpenSchool tudásbázisban

### Hibaelhárítás

A leggyakoribb hibákra már van megoldásunk: [Hibaelhárítás és GYIK](hibaelharitas.md)

### Szótár

Ha egy fogalmat nem értesz (pl. „dependency injection", „ORM", „fixture"), nézd meg a [Szótárban](szotar.md).

### Puskalapok

Gyors parancskereső:
- [Git puskalap](git-puskalap.md) — Git parancsok
- [Docker puskalap](docker-puskalap.md) — Docker parancsok

### Keresés a repóban (VS Code)

A tudásbázis teljes szövegében kereshetsz:
- `Ctrl+Shift+F` — keresés a teljes munkaterületen
- Írd be a hibaüzenet kulcsszavát (pl. `FileNotFoundError`, `conftest`)

### Keresés a repóban (GitHub)

A [github.com/ghemrich/openschool-knowledge](https://github.com/ghemrich/openschool-knowledge) oldalon:
- Nyomd meg a `.` billentyűt → megnyílik a webes szerkesztő, ahol `Ctrl+Shift+F`-fel kereshetsz
- Vagy használd a GitHub keresőt: a repó oldalán írd be a keresőmezőbe a kulcsszót

---

## 3. Hivatalos dokumentáció használata

A hivatalos dokumentáció a **legmegbízhatóbb forrás**. Tanulj meg benne keresni.

### Python

| Forrás | Mire jó | Link |
|--------|---------|------|
| Python docs | Beépített függvények, típusok, modulok | [docs.python.org](https://docs.python.org/3/) |
| Python Tutorial | Nyelvi alapok, ha valamit újra meg akarsz érteni | [docs.python.org/3/tutorial](https://docs.python.org/3/tutorial/) |
| W3Schools Python | Egyszerű példák, gyors referencia | [w3schools.com/python](https://www.w3schools.com/python/) |

**Tipp:** Ha egy beépített függvényt keresel (pl. `split`, `enumerate`, `zip`), keress rá: `python docs split`

### FastAPI / Backend

| Forrás | Mire jó | Link |
|--------|---------|------|
| FastAPI docs | Végpontok, Pydantic, dependency injection | [fastapi.tiangolo.com](https://fastapi.tiangolo.com/) |
| SQLAlchemy docs | ORM, modellek, query-k | [docs.sqlalchemy.org](https://docs.sqlalchemy.org/) |
| Pydantic docs | Sémák, validáció, típusok | [docs.pydantic.dev](https://docs.pydantic.dev/) |
| pytest docs | Tesztelés, fixture-ök, parametrizálás | [docs.pytest.org](https://docs.pytest.org/) |
| HTTP státuszkódok | 200, 404, 422, 401 jelentése | [developer.mozilla.org/HTTP/Status](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) |

**Tipp:** A FastAPI dokumentáció kiváló — minden fejezetben van futtatható példakód.

### Git

| Forrás | Mire jó | Link |
|--------|---------|------|
| Git docs | Parancsok részletes leírása | [git-scm.com/docs](https://git-scm.com/docs) |
| W3Schools Git | Egyszerű, lépésről lépésre | [w3schools.com/git](https://www.w3schools.com/git/) |

### Docker

| Forrás | Mire jó | Link |
|--------|---------|------|
| Docker docs | Dockerfile, Compose, parancsok | [docs.docker.com](https://docs.docker.com/) |
| Docker Hub | Elérhető image-ek (postgres, python, stb.) | [hub.docker.com](https://hub.docker.com/) |

---

## 4. Hatékony keresés a weben

### Keresési stratégiák

| Stratégia | Példa | Miért jó |
|-----------|-------|----------|
| Hibaüzenet + nyelv | `python ValueError invalid literal for int` | Pontos találat a hibára |
| Fogalom + „how to" | `python how to read csv file` | Gyakorlati útmutatók |
| Könyvtár + funkció | `fastapi dependency injection example` | Konkrét példakód |
| „site:" szűrő | `site:stackoverflow.com python list comprehension` | Csak egy oldalon keres |

### Amit csinálj

- **Angolul keress** — sokkal több eredmény, jobb minőségű válaszok
- **Másold be a hibaüzenet lényegét** — de vedd ki a saját fájlneveidet, változóidat
- **Szűkíts**, ha túl sok találat van — add hozzá a Python/FastAPI verziószámot
- **Nézd meg a dátumot** — 5+ éves válaszok elavultak lehetnek

### Amit ne csinálj

- Ne keress magyarul technikai kérdésekre — kevés és gyenge eredmény
- Ne másold be az egész hibaüzenetet fájlútvonalakkal együtt
- Ne az első találatot fogadd el vakon — olvass el 2-3 választ

---

## 5. Stack Overflow és fórumok

### Stack Overflow olvasása

A [stackoverflow.com](https://stackoverflow.com) a programozók kérdés-válasz oldala. Így használd hatékonyan:

1. **Nézd a szavazatokat** — a legtöbb szavazatot kapott válasz általában a legjobb
2. **Nézd a zöld pipát ✅** — ez a kérdező által elfogadott válasz (de nem mindig a legjobb)
3. **Nézd a dátumot** — régi válaszok elavultak lehetnek
4. **Olvasd el a kommenteket** — gyakran ott van a lényeges kiegészítés
5. **Nézd a kérdést is** — ha hasonlít a te problémádra, a válasz is releváns lesz

### Hasznos fórumok és közösségek

| Forrás | Nyelv | Mire jó |
|--------|-------|---------|
| [Stack Overflow](https://stackoverflow.com) | EN | Konkrét technikai kérdések |
| [Reddit r/learnpython](https://www.reddit.com/r/learnpython/) | EN | Kezdő Python kérdések |
| [FastAPI GitHub Discussions](https://github.com/fastapi/fastapi/discussions) | EN | FastAPI-specifikus kérdések |
| [Real Python](https://realpython.com/) | EN | Részletes Python tutorialok |

---

## 6. Beépített súgó használata

### Python interaktív súgó

```python
# Terminálban indítsd el a Python interpretert:
python3

# Kérdezz rá bármire:
>>> help(str.split)
>>> help(list)
>>> help(print)

# Nézd meg egy objektum metódusait:
>>> dir(str)
>>> dir([])
```

### Parancssor súgó

```bash
# Git parancsok súgója
git help commit
git commit --help

# Docker súgó
docker --help
docker compose --help

# Python modulok
python3 -m pytest --help
python3 -m pip --help
```

### VS Code beépített segítség

- **Hover:** vidd az egeret egy függvény fölé → megjelenik a dokumentáció
- **Ctrl+Click:** ugrás a definícióra
- **Ctrl+Space:** kódkiegészítés javaslatokkal
- **F1 → „Python: Select Interpreter":** ha rossz Python verzió van kiválasztva

---

## 7. Ha továbbra sem találsz megoldást

Ha 10-15 percig kerestél és nem jutottál előre, kérdezz — de **mutasd meg, mit próbáltál**:

1. Írd le a problémát
2. Másold be a hibaüzenetet
3. Írd le, hol kerestél (pl. „Megnéztem a hibaelhárítás útmutatót, és kerestem Stack Overflow-n")
4. Mutasd meg a kódot kódblokkban

Részletes útmutató a jó kérdésfeltevéshez: [Hogyan kérdezz jól?](kozossegi-utmutato.md#hogyan-kérdezz-jól)

---

## Összefoglaló: a keresés sorrendje

```
1. Olvasd el a hibaüzenetet (utolsó sor!)
2. Keress az OpenSchool tudásbázisban (hibaelhárítás, szótár)
3. Nézd meg a hivatalos dokumentációt
4. Keress a weben angolul (hibaüzenet + nyelv/könyvtár)
5. Nézd át a Stack Overflow válaszokat
6. Ha nem találtál → kérdezz a Discord csatornán
```

> **Az önálló problémamegoldás a programozás egyik legfontosabb készsége.** Minden keresés, minden hibaüzenet-olvasás gyakorlat — idővel egyre gyorsabban fogsz rátalálni a megoldásra.
