# 5. hét – Response modellek és hibakezelés

> **Határidő:** a következő óra előtt
> **Beadás:** commitold és pushold a megoldásaidat ebbe a repóba!
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

## 5.1 – Response model ⭐
Módosítsd a Termek modellt: adj hozzá `titkos_kod` mezőt. Készíts `TermekResponse` modellt `titkos_kod` nélkül. Használd `response_model`-ként.

## 5.2 – Status kódok ⭐
Állítsd be a helyes status kódokat: POST → 201, DELETE → 200, GET nem létező → 404.

## 5.3 – HTTPException ⭐⭐
Készíts `GET /felhasznalok/{id}` végpontot: 404 ha nem létezik, 403 ha id == 0 (admin). Részletes hibaüzenetekkel.

## 5.4 – Egyedi kivétel ⭐⭐
Hozz létre `NemTalalhatoError` kivételt és regisztrálj hozzá kezelőt. A válasz formátuma: `{"hiba": true, "uzenet": "..."}`.

## 5.5 – Hibakód gyűjtemény ⭐⭐⭐
Készíts API-t ami 5 különböző hibakódot ad vissza (400, 401, 403, 404, 422). Dokumentáld a `responses` paraméterrel.

---

## Dokumentáció

- [Response Model](https://fastapi.tiangolo.com/tutorial/response-model/)
- [HTTPException](https://fastapi.tiangolo.com/tutorial/handling-errors/)
- [Status Codes](https://fastapi.tiangolo.com/tutorial/response-status-code/)

## Beadás

1. `main.py` + `models.py` legyen a repóban
2. Commitolj értelmes üzenetekkel
3. `git push` – ez a beadás!
