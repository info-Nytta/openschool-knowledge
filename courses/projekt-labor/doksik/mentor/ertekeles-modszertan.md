# Értékelési módszertan – Projekt Labor

## Értékelési filozófia

A Projekt Labor értékelése eltér a hagyományos kurzusoktól. Nem heti házi feladatokat és vizsgákat értékelünk, hanem egy **folyamatosan épülő projektet**. Az értékelés négy alapelvre épül:

1. **Mérföldkő-alapú** — Minden modul egy konkrét, mérhető eredménnyel zárul
2. **Automatizált + emberi** — Verifikációs tesztek + mentor kód review együtt
3. **Folyamatos** — Nem egyetlen vizsga, hanem modulonkénti értékelés
4. **Valós munkafolyamat** — Git history, PR-ek, kódminőség — ahogy az iparban is

## Értékelés összetétele

| Komponens | Súly | Leírás |
|---|---|---|
| Verifikációs tesztek | 40% | Automatikus tesztek modulonként |
| Kódminőség | 30% | Kód review eredménye |
| Git munkafolyamat | 15% | Commit history, branch-ek, PR-ek |
| Dokumentáció | 15% | README, kód kommentek, API docs |

### 1. Verifikációs tesztek (40%)

Minden modulhoz tartoznak verifikációs tesztek a `tesztek/` mappában. Ezek objektíven mérik a funkcionális követelmények teljesítését.

**Futtatás:**
```bash
pytest tests/test_modul01_*.py -v
```

**Modulonkénti értékelés:**

| Modul | Teszt fájlok | Fő ellenőrzési pontok |
|---|---|---|
| 01 | `test_modul01_*.py` | Docker Compose, CI pipeline |
| 02 | `test_modul02_*.py` | Autentikáció, szerepkörök |
| 03 | `test_modul03_*.py` | Kurzuskezelés, haladás |
| 04 | `test_modul04_*.py` | Tanúsítvány generálás |
| 05 | `test_modul05_*.py` | Frontend integráció |
| 06 | `test_modul06_*.py` | Deployment konfiguráció |
| 07 | `test_modul07_*.py` | Közösségi munkafolyamatok |

### 2. Kódminőség (30%)

A mentor az alábbi szempontok alapján értékeli a kódot:

**Kód review ellenőrzőlista:**

- [ ] Tiszta, olvasható kódstruktúra
- [ ] Értelmező függvény- és változónevek
- [ ] Nincs felesleges kódduplikáció
- [ ] Hibakezelés megfelelő (try/except, HTTP hibakódok)
- [ ] Biztonsági szempontok betartva (input validáció, SQL injection védelem)
- [ ] Konfigurációs értékek környezeti változókban
- [ ] API végpontok RESTful konvenciót követnek
- [ ] Adatmodell normalizált, kapcsolatok helyesek

### 3. Git munkafolyamat (15%)

A git history tükrözi a tanuló munkafolyamatát és fejlődését.

**Értékelési szempontok:**

- **Commit üzenetek**: Értelmesek, leíróak (nem „fix", „update", „asdf")
- **Commit gyakoriság**: Rendszeres, kis lépésekben haladás
- **Branch használat**: Feature branch-ek modulonként vagy feladatonként
- **PR-ek**: Leíró PR szöveg, önálló review kérés

**Piros zászlók:**
- Egyetlen nagy commit az egész modulra
- Copy-paste nyomai (hirtelen nagy mennyiségű, stílusidegen kód)
- Generált kód review nélküli beillesztése

### 4. Dokumentáció (15%)

- README.md naprakész, tartalmazza a futtatási utasításokat
- API végpontok dokumentálva (Swagger/OpenAPI automatikusan)
- Konfigurációs lépések leírva
- Telepítési útmutató más fejlesztők számára is érthető

## Teljesítményszintek

| Szint | Követelmény |
|---|---|
| **Kiváló** (90-100%) | Minden modul tesztje zöld, kódminőség magas, tiszta git history, teljes dokumentáció |
| **Haladó** (75-89%) | Tesztek többsége zöld, jó kódminőség, rendszeres commitok, alapvető dokumentáció |
| **Megfelelő** (60-74%) | Alap funkciók működnek, elfogadható kódminőség, van git history |
| **Kezdő** (32-59%) | Részleges funkciók, kódminőségi problémák, minimális dokumentáció |
| **Nem teljesített** (0-31%) | Tesztek nem futnak, hiányzó modulok, nincs érdemi munka |

## Modulonkénti értékelés menete

1. **Tanuló jelzi** a modul befejezését (Discord vagy PR)
2. **Mentor futtatja** a verifikációs teszteket
3. **Mentor kód review-t** végez az adott modul kódjára
4. **Visszajelzés** szöveges formában PR kommentként vagy Discord üzenetben
5. **Javítási lehetőség** — a tanuló kijavíthatja a hibákat újraértékelés előtt

## Különleges esetek

### Késői leadás
A moduloknak nincs szigorú határideje, de a mentor rögzíti a haladási tempót. Tartósan elmaradó tanulóval egyéni konzultáció szükséges.

### Együttműködés vs. plágium
A Projekt Laborban az együttműködés támogatott (kód review, pair programming). Azonban minden tanuló a saját repójában dolgozik, és a git history-nak tükröznie kell az egyéni munkát. Ha két repó kódja gyanúsan azonos, a mentor egyéni kérdésekkel ellenőrzi a megértést.

### AI eszközök használata
Az AI eszközök (GitHub Copilot, ChatGPT stb.) használata megengedett, de a tanuló felelős azért, hogy megértse és el tudja magyarázni a kódot. A mentor szúrópróbaszerűen kérdezhet az implementáció részleteiről.

## Kapcsolódó dokumentumok

- [Mentori útmutató](mentori-utmutato.md)
- [Tanterv](../tanterv/tanterv.md)
- [Verifikációs tesztek](../../tesztek/README.md)
