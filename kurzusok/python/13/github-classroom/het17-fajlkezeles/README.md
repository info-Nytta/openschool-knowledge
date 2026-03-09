# 17. hét – Fájlkezelés és képfeltöltés

> **Határidő:** a következő óra előtt
> **Beadás:** commitold és pushold a megoldásaidat ebbe a repóba!
> A feladatok nehézség szerint vannak jelölve: ⭐ könnyű | ⭐⭐ közepes | ⭐⭐⭐ nehéz

---

## Feladat

Bővítsd a Termék API-t fájlfeltöltéssel.

### Végpontok:
- `POST /feltoltes` → fájl feltöltés, visszaadja a fájl nevét és méretét ⭐
- `POST /feltoltes/kep` → csak JPEG/PNG, max 5 MB, mentés `uploads/`-ba ⭐⭐
- `POST /termekek/{id}/kep` → kép hozzárendelése termékhez (kep_url mező) ⭐⭐⭐

### Tesztelés:
Írj teszteket a feltöltéshez (`io.BytesIO` használatával).

---

## Dokumentáció

- [FastAPI File Upload](https://fastapi.tiangolo.com/tutorial/request-files/)
- [StaticFiles](https://fastapi.tiangolo.com/tutorial/static-files/)

## Beadás

1. `app/` csomag + `tests/` mappa legyen a repóban
2. Commitolj értelmes üzenetekkel
3. `git push` – ez a beadás!
