# 2. hét – FastAPI bevezetés

> **Határidő:** a következő óra előtt
> **Beadás:** commitold és pushold a megoldásaidat ebbe a repóba!
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

## 2.1 – Hello API ⭐
Készíts FastAPI alkalmazást (`main.py`), amely a `GET /` végponton `{"message": "Helló, világ!"}` választ ad. Készíts `requirements.txt`-t (`fastapi`, `uvicorn`).

## 2.2 – Több végpont ⭐
Adj hozzá `GET /info` és `GET /datum` végpontokat. Az `/info` adja vissza az API nevét és verzióját, a `/datum` az aktuális dátumot.

## 2.3 – Swagger UI ⭐⭐
Add meg az alkalmazás `title`, `description` és `version` paramétereit. Készíts képernyőképet a `/docs` oldalról (`screenshot.png`).

## 2.4 – Lista végpont ⭐⭐
Hozz létre egy in-memory listát 5 gyümölccsel. Készíts `GET /gyumolcsok` végpontot (lista) és `GET /gyumolcsok/{index}` végpontot (egy elem).

## 2.5 – CRUD alap ⭐⭐⭐
Egészítsd ki a `POST /gyumolcsok` (hozzáadás) és `DELETE /gyumolcsok/{index}` (törlés) végpontokkal. Teszteld a Swagger UI-ban.

---

## Dokumentáció

- [FastAPI First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/)
- [FastAPI Path Parameters](https://fastapi.tiangolo.com/tutorial/path-params/)
- [REST API fogalmak](https://restfulapi.net/)

## Beadás

1. `main.py` + `requirements.txt` legyen a repóban
2. Commitolj értelmes üzenetekkel
3. `git push` – ez a beadás!
