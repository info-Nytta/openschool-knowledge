# Eszközök

Szkriptek és segédeszközök a kurzusok kezeléséhez. Minden eszköz külső függőség nélkül működik (Python stdlib + `gh` CLI).

## Elérhető eszközök

| Eszköz | Fájl | Leírás |
|--------|------|--------|
| GitHub Setup | `github-setup.sh` / `github-setup.ps1` | Template repók automatikus létrehozása egy GitHub Organization alatt |
| Discord Webhook | `discord-webhook.py` | Bejelentések, emlékeztetők és szálnyitók küldése Discord csatornákra |
| Jegy Kalkulátor | `jegy-szamolo.py` | Házi feladatok összesítése és végső jegy kiszámítása |

---

### github-setup.sh / github-setup.ps1

GitHub Organization-ben automatikusan létrehozza a template repókat a helyi mappákból.

**Követelmények:** `gh` CLI (telepítve és bejelentkezve)

**Linux / macOS:**
```bash
chmod +x github-setup.sh
./github-setup.sh <ORGANIZATION> <TEMPLATE_MAPPA>

# Példa: Python 10 template repók létrehozása
./github-setup.sh iskolam-org ../kurzusok/python/10/github-classroom
```

**Windows (PowerShell):**
```powershell
.\github-setup.ps1 -Organization <ORGANIZATION> -TemplateMappa <TEMPLATE_MAPPA>

# Példa: Python 10 template repók létrehozása
.\github-setup.ps1 -Organization iskolam-org -TemplateMappa ..\kurzusok\python\10\github-classroom
```

---

### discord-webhook.py

Discord webhook üzeneteket küld – bejelentések, emlékeztetők, heti szálnyitók.

**Követelmények:** Python 3.7+ (nincs külső csomag)

Környezeti változók beállítása (a szkript `.env` fájlból is olvas):

**Linux / macOS:**
```bash
export DISCORD_WEBHOOK_KOZLEMENYEK="https://discord.com/api/webhooks/..."
export DISCORD_WEBHOOK_PYTHON10="https://discord.com/api/webhooks/..."
export DISCORD_WEBHOOK_BACKEND13="https://discord.com/api/webhooks/..."
```

**Windows (PowerShell):**
```powershell
$env:DISCORD_WEBHOOK_KOZLEMENYEK = "https://discord.com/api/webhooks/..."
$env:DISCORD_WEBHOOK_PYTHON10 = "https://discord.com/api/webhooks/..."
$env:DISCORD_WEBHOOK_BACKEND13 = "https://discord.com/api/webhooks/..."
```

**Windows (cmd):**
```cmd
set DISCORD_WEBHOOK_KOZLEMENYEK=https://discord.com/api/webhooks/...
set DISCORD_WEBHOOK_PYTHON10=https://discord.com/api/webhooks/...
set DISCORD_WEBHOOK_BACKEND13=https://discord.com/api/webhooks/...
```

Használat (mindegyik rendszeren):
```bash
# Bejelentés küldése
python discord-webhook.py bejelentes python10 "Holnap nincs óra"

# Heti szál nyitása
python discord-webhook.py szal python10 3 "Feltételes elágazások"

# Határidő emlékeztető
python discord-webhook.py emlekezteto python10 3 "2025-02-14"
```

---

### jegy-szamolo.py

Végső jegy kiszámítása az összes tanulóra, közvetlenül a GitHub Classroom CSV exportokból.

**Követelmények:** Python 3.7+ (nincs külső csomag)

**Adatok helye:** `adatok/<év>/<kurzus>/` (lásd [adatok/README.md](../adatok/README.md))

```bash
# A projekt gyökérmappájából futtatva:

# Összes tanuló jegye (Python 10, 2026)
python eszkozok/jegy-szamolo.py --kurzus python10 --ev 2026

# Egy tanuló részletes eredménye
python eszkozok/jegy-szamolo.py --kurzus python10 --ev 2026 --tanulo "Kovács Anna"

# Eredmények mentése CSV-be
python eszkozok/jegy-szamolo.py --kurzus python10 --ev 2026 --kimenet adatok/2026/python10/eredmenyek.csv

# Egyéni adatmappa megadása
python eszkozok/jegy-szamolo.py --kurzus python10 --mappa /path/to/adatok
```

**Bemeneti fájlok** (`adatok/2026/python10/` példa):

| Fájl | Formátum | Forrás |
|------|----------|--------|
| `classroom/*.csv` | GitHub Classroom export | Classroom → Download Grades |
| `vizsga.csv` | `tanulo,pont` | Kézi |
| `orai.csv` | `tanulo,jegy` | Kézi |
| `probavizsga.csv` | `tanulo,pont` | Kézi |

**Súlyozás:**

| Komponens | Python 10 | Backend 13 |
|-----------|-----------|------------|
| Házi feladatok | 25% | 20% |
| Órai munka | 15% | 15% |
| Próbavizsga | 10% | 15% |
| Vizsga | 50% | 50% |
