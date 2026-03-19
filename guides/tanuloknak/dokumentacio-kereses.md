# Hogyan keress dokumentációt?

A programozás egyik legfontosabb készsége a hatékony keresés. Ez az útmutató megmutatja, hol érdemes keresni — mielőtt kérdést tennél fel.

---

## 1. Olvasd el a hibaüzenetet

A hibaüzenet nem ellenség — az **utolsó sor** tartalmazza a lényeget. Az angol típusnevet (`ValueError`, `TypeError`, `KeyError`) másold ki kereséshez.

Részletes útmutató: [Hibaelhárítás](hibaelharitas.md)

---

## 2. Keress az OpenSchool tudásbázisban

- [Hibaelhárítás](hibaelharitas.md) — leggyakoribb hibák megoldása
- [Szótár](szotar.md) — ha egy fogalmat nem értesz (ORM, fixture, middleware…)
- [Git puskalap](../puskak/git-puskalap.md) — Git parancsok
- [Docker puskalap](../puskak/docker-puskalap.md) — Docker parancsok

VS Code-ban: `Ctrl+Shift+F` — keresés a teljes munkaterületen.

---

## 3. Hivatalos dokumentáció

A hivatalos dokumentáció a legmegbízhatóbb forrás. Tanulj meg benne keresni.

### Python

| Forrás | Link |
|--------|------|
| Python docs (beépített függvények, modulok) | [docs.python.org](https://docs.python.org/3/) |
| Python Tutorial (nyelvi alapok) | [docs.python.org/3/tutorial](https://docs.python.org/3/tutorial/) |
| W3Schools Python (egyszerű példák) | [w3schools.com/python](https://www.w3schools.com/python/) |

### Backend

| Forrás | Link |
|--------|------|
| FastAPI | [fastapi.tiangolo.com](https://fastapi.tiangolo.com/) |
| SQLAlchemy | [docs.sqlalchemy.org](https://docs.sqlalchemy.org/) |
| Pydantic | [docs.pydantic.dev](https://docs.pydantic.dev/) |
| pytest | [docs.pytest.org](https://docs.pytest.org/) |
| HTTP státuszkódok | [developer.mozilla.org/HTTP/Status](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) |

### Git & Docker

| Forrás | Link |
|--------|------|
| Git docs | [git-scm.com/docs](https://git-scm.com/docs) |
| Docker docs | [docs.docker.com](https://docs.docker.com/) |
| Docker Hub | [hub.docker.com](https://hub.docker.com/) |

---

## 4. Keresés a weben

**Angolul keress** — sokkal több és jobb találat.

Bevált minták:
- `python ValueError invalid literal for int` — hibaüzenet + nyelv
- `fastapi dependency injection example` — könyvtár + funkció
- `site:stackoverflow.com python list comprehension` — szűrés egy oldalra

A hibaüzenetből vedd ki a saját fájlneveidet és változóidat, mielőtt beilleszted a keresőbe.

---

## 5. Beépített súgó

```python
# Python interpretben:
>>> help(str.split)
>>> dir([])
```

```bash
# Parancssor:
git help commit
docker compose --help
python3 -m pytest --help
```

VS Code: vidd az egeret egy függvény fölé → megjelenik a dokumentáció. `Ctrl+Click` → ugrás a definícióra.

---

## 6. Ha nem találsz megoldást

Ha 10-15 percig kerestél és nem jutottál előre, kérdezz a Discord `#segítség` csatornán — de mutasd meg, mit próbáltál. Lásd: [Hogyan kérdezz jól?](../mentoroknak/kozossegi-utmutato.md#hogyan-kérdezz-jól)
