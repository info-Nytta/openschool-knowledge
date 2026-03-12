# 3. hét – Útvonalak és paraméterek

> **Határidő:** a következő óra előtt
> **Beadás:** commitold és pushold a megoldásaidat ebbe a repóba!
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

## 3.1 – Köszöntés ⭐
Készíts végpontot (`main.py`): `GET /koszontes/{nev}` → `{"uzenet": "Helló, {nev}!"}`.

## 3.2 – Számológép ⭐
Készíts végpontot: `GET /szorzas/{a}/{b}` ahol mindkettő `int`. Adja vissza: `{"eredmeny": a * b}`.

## 3.3 – Keresés ⭐⭐
Készíts végpontot: `GET /kereses` amelyik `q` (kötelező str) és `limit` (opcionális int, alapért. 10) query paramétereket fogad.

## 3.4 – Validáció ⭐⭐
Készíts 50 elemű listát. `GET /elemek` végpont `skip` (>=0) és `limit` (1-50) query paraméterekkel, `Query()` validációval.

## 3.5 – Kombinált ⭐⭐⭐
Készíts `GET /termekek/{kategoria}` végpontot, ahol `kategoria` Enum (elektronika, ruha, kosar), és `min_ar`, `max_ar` opcionális query paraméterek.

---

## Dokumentáció

- [Path Parameters](https://fastapi.tiangolo.com/tutorial/path-params/)
- [Query Parameters](https://fastapi.tiangolo.com/tutorial/query-params/)
- [Query Validation](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/)

## Beadás

1. Minden megoldás a `main.py`-ban legyen
2. Commitolj értelmes üzenetekkel
3. `git push` – ez a beadás!
