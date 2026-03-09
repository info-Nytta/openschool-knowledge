# 10. hét – Authentikáció és JWT

> **Határidő:** a következő óra előtt
> **Beadás:** commitold és pushold a megoldásaidat ebbe a repóba!
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

## 10.1 – Jelszó hash ⭐
Készíts `auth.py`-t `hash_jelszo()` és `jelszo_ellenorzes()` függvényekkel (passlib + bcrypt). Teszteld a `main.py`-ból.

## 10.2 – Regisztráció ⭐⭐
Készíts `Felhasznalo` modellt (id, nev, email, jelszo_hash). `POST /auth/regisztracio` végpont: hash-eli a jelszót, elmenti az adatbázisba. Dupla email → 400.

## 10.3 – JWT Login ⭐⭐
Egészítsd ki `auth.py`-t JWT token generálással. `POST /auth/login` végpont: email + jelszó → access_token.

## 10.4 – Védett végpont ⭐⭐
Készíts `get_current_user` dependency-t (token dekódolás). `GET /auth/profil` → visszaadja a bejelentkezett user adatait. Token nélkül 401.

## 10.5 – Jogosultság ⭐⭐⭐
A `POST /konyvek` és `DELETE /konyvek/{id}` végpontok csak bejelentkezett felhasználóknak legyenek elérhetők. Teszteld a Swagger UI 🔒 gombbal.

---

## Dokumentáció

- [FastAPI Security](https://fastapi.tiangolo.com/tutorial/security/)
- [python-jose](https://github.com/mpdavis/python-jose)
- [passlib](https://passlib.readthedocs.io/)

## Beadás

1. `auth.py`, `dependencies.py` legyen a repóban
2. Commitolj értelmes üzenetekkel
3. `git push` – ez a beadás!
