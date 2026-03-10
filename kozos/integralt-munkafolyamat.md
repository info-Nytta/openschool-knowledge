# Integrált munkafolyamat útmutató

A tanári munkafolyamat három eszközre épül: **GitHub Classroom** (feladatok kiadása és automatikus értékelés), **Discord** (kommunikáció és értesítések), és a **jegy kalkulátor** (félév végi összesítés). Ez a dokumentum leírja, hogyan kapcsolódnak össze.

---

## 1. Félév indításkor (egyszeri beállítás)

### 1.1 GitHub Classroom előkészítése

**Linux / macOS:**
```bash
# Template repók létrehozása az Organizationben
cd eszkozok/
./github-setup.sh iskolam-org ../kurzusok/python/10/github-classroom
```

**Windows (PowerShell):**
```powershell
# Template repók létrehozása az Organizationben
cd eszkozok/
.\github-setup.ps1 -Organization iskolam-org -TemplateMappa ..\kurzusok\python\10\github-classroom
```

```bash
# Classroom-ban: Create Assignment → válaszd a template repót → engedélyezd az autograding-et
```

Minden hétre létrejön egy template repó (pl. `het01-alapok`, `het02-bevitel-szoveg`), amelyet a GitHub Classroom assignment-hez kapcsolhatsz.

### 1.2 Discord szerver

Ha még nincs szerver, kövesd a [Discord szerver útmutatót](discord-szerver-utmutato.md).

Ha már van szerver, csak az éves karbantartást kell elvégezni (lásd útmutató 8. fejezet):
- Új éves szerepkörök létrehozása (`Python 10 – 2026`)
- Régi szálak archiválása

### 1.3 Webhook-ok beállítása

A szkriptek webhook-okon keresztül küldenek üzeneteket a Discord csatornákra. A részletes beállítási útmutatót (létrehozás, .env fájl, tesztelés) lásd:
**[Discord szerver útmutató – 5.3 Webhook-ok](discord-szerver-utmutato.md#53-webhook-ok-beállítása-automatizáláshoz)**

Röviden: 3 webhook kell (`#közlemények`, `#python10-segítség`, `#backend13-segítség`), az URL-eket a `eszkozok/.env` fájlban tárold:

```bash
# eszkozok/.env
DISCORD_WEBHOOK_KOZLEMENYEK=https://discord.com/api/webhooks/...
DISCORD_WEBHOOK_PYTHON10=https://discord.com/api/webhooks/...
DISCORD_WEBHOOK_BACKEND13=https://discord.com/api/webhooks/...
```

---

## 2. Heti rutin

### 2.1 Óra előtt – szál nyitása és bejelentés

```bash
cd eszkozok/

# Heti szál nyitása a kurzus csatornáján
python discord-webhook.py szal python10 3 "Feltételes elágazások"

# Bejelentés (opcionális)
python discord-webhook.py bejelentes python10 "Ma az if/elif/else szerkezeteket nézzük meg."
```

### 2.2 Házi feladat kiadása

1. GitHub Classroom-ban: **Create Assignment** → válaszd a heti template-et
2. Az invite linket küldd el Discord-on:

```bash
python discord-webhook.py uzenet python10 "📎 Házi feladat: https://classroom.github.com/a/XXXXXX"
```

### 2.3 Határidő emlékeztető

```bash
# Határidő előtt 1-2 nappal
python discord-webhook.py emlekezteto python10 3 "2025-02-14"
```

### 2.4 Eredmények letöltése

GitHub Classroom → **Download Grades** → CSV fájl.

Az autograding automatikusan értékeli a beadásokat:
- **Python 10:** shell-alapú tesztek (`test -f megoldas.py && python megoldas.py < bemenet.txt | diff - vart_kimenet.txt`)
- **Backend 13:** pytest tesztek (`pytest test_*.py`)

---

## 3. Félév végén – jegyek kiszámítása

### 3.1 Classroom CSV-k összegyűjtése

A félév során a GitHub Classroom CSV exportokat az `adatok/` mappába kell menteni:

```
adatok/2026/python10/
  classroom/              ← GitHub Classroom → Download Grades
    het01-alapok.csv
    het02-bevitel-szoveg.csv
    het03-feltetelek.csv
    ...
```

Minden assignment-nél: Classroom dashboard → assignment → **Download Grades** → mentsd a `classroom/` mappába.

### 3.2 Vizsga és egyéb pontok rögzítése

Hozz létre kiegészítő CSV fájlokat az `adatok/2026/python10/` mappában:

```bash
# vizsga.csv
tanulo,pont
Kovács Anna,35
Nagy Péter,38

# orai.csv
tanulo,jegy
Kovács Anna,4
Nagy Péter,5

# probavizsga.csv (ha volt)
tanulo,pont
Kovács Anna,32
Nagy Péter,38
```

A `tanulo` oszlop a GitHub Classroom `roster_identifier` értékével egyezzen.

### 3.3 Jegyek kiszámítása

```bash
# A projekt gyökérmappájából:

# Összes tanuló – összesítő táblázat
python eszkozok/jegy-szamolo.py --kurzus python10 --ev 2026

# Egy tanuló – részletes bontás
python eszkozok/jegy-szamolo.py --kurzus python10 --ev 2026 --tanulo "Kovács Anna"

# Eredmények mentése CSV-be (importálható táblázatkezelőbe)
python eszkozok/jegy-szamolo.py --kurzus python10 --ev 2026 \
    --kimenet adatok/2026/python10/eredmenyek.csv
```

### 3.4 Eredmény közlése

```bash
python eszkozok/discord-webhook.py bejelentes python10 "A félév végi jegyek elkészültek. Egyéni eredményekért írjatok privát üzenetet!"
```

---

## 4. Eszközök összefoglalása

| Mikor | Eszköz | Parancs |
|-------|--------|---------|
| Félév eleje | `github-setup.sh` / `.ps1` | Template repók létrehozása |
| Heti | `discord-webhook.py szal` | Heti szál nyitása |
| Heti | `discord-webhook.py bejelentes` | Bejelentés küldése |
| Házi kiadásakor | `discord-webhook.py uzenet` | Invite link megosztása |
| Határidő előtt | `discord-webhook.py emlekezteto` | Emlékeztető küldése |
| Heti (opcionális) | Classroom CSV mentése | `adatok/<év>/<kurzus>/classroom/` mappába |
| Félév vége | `jegy-szamolo.py` | Összes tanuló jegyének kiszámítása |

---

## 5. Mappaszerkezet hivatkozások

```
adatok/                         ← tanulói adatok (.gitignore-olt)
    2026/
      python10/
        classroom/              ← GitHub Classroom CSV exportok
        vizsga.csv              ← vizsgapontszámok
        orai.csv                ← órai jegyek
        probavizsga.csv         ← próbavizsga pontszámok
        eredmenyek.csv          ← generált kimenet
      backend13/
        classroom/
        ...
eszkozok/                       ← szkriptek
    github-setup.sh
    discord-webhook.py
    jegy-szamolo.py
kozos/                          ← közös dokumentáció
    discord-szerver-utmutato.md ← szerver beállítás
    integralt-munkafolyamat.md  ← ez a fájl
kurzusok/python/10/             ← Python 10 kurzusanyag
kurzusok/python/13/             ← Backend 13 kurzusanyag
sablonok/                       ← sablonok (assignment, értékelés)
```
