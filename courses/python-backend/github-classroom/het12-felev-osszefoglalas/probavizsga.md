# Próbavizsga – Könyv API (60 pont, 120 perc)

Ez a próbavizsga az első félév anyagát (1–11. hét) fedi le. A valódi vizsga (24. hét) 240 perc és 5 feladatból áll — a próbavizsga az első 3 feladattípust (API, DB, Auth) gyakoroltatja.

- **Időtartam:** 120 perc
- **Összpontszám:** 60 pont
- **Eszközök:** Saját gép, VS Code, dokumentáció (internet)
- **Megoldásodat a `probavizsga/` mappába tedd!**

---

## 1. feladat – Alap végpontok (15 pont)

Készíts egy FastAPI alkalmazást könyv-nyilvántartásra:
- `GET /` – üdvözlő üzenet (3 pont)
- `GET /konyvek` – összes könyv listázása (4 pont)
- `GET /konyvek/{id}` – egy könyv lekérése, 404 ha nem létezik (4 pont)
- `POST /konyvek` – új könyv hozzáadása (4 pont)

---

## 2. feladat – Adatbázis integráció (20 pont)

- SQLAlchemy modell: Konyv (id, cim, szerzo, ev, ar) (5 pont)
- Pydantic sémák (Create, Update, Response) (5 pont)
- CRUD műveletek (crud.py) (5 pont)
- Alembic migráció (5 pont)

---

## 3. feladat – Auth és védett végpontok (25 pont)

- Felhasznalo modell és regisztráció (5 pont)
- JWT login (5 pont)
- `POST /konyvek` csak bejelentkezett felhasználóknak (5 pont)
- `PUT /konyvek/{id}` és `DELETE /konyvek/{id}` védett (5 pont)
- Helyes hibakódok (401, 403, 404) (5 pont)

---

## Beadás

1. A megoldásodat a `probavizsga/` mappába tedd
2. Commitolj és pushold
3. Mérj időt – a cél a 120 perc!
