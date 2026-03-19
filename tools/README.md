# Eszközök (Tools)

Automatizálási szkriptek a kurzusok adminisztrálásához.

## Szkriptek

| Szkript | Leírás |
|---|---|
| `github-setup.sh` | GitHub Classroom template repók létrehozása (Linux/macOS) |
| `github-setup.ps1` | GitHub Classroom template repók létrehozása (Windows) |
| `discord-webhook.py` | Discord webhook üzenetküldő — bejelentések |

## GitHub Setup

Template repókat hoz létre egy GitHub Organization alatt a `github-classroom/` mappa almappáiból.

**Előfeltételek:**
- [GitHub CLI (gh)](https://cli.github.com) telepítve és bejelentkezve
- Az Organization már létezik a GitHubon

**Használat:**

```bash
# Linux/macOS
./github-setup.sh <ORGANIZATION> <TEMPLATE_MAPPA>
./github-setup.sh openschool-python-2026 ../../courses/python-alapok/github-classroom

# Windows (PowerShell)
.\github-setup.ps1 <ORGANIZATION> <TEMPLATE_MAPPA>
.\github-setup.ps1 openschool-python-2026 ..\..\courses\python-alapok\github-classroom
```

## Discord Webhook

Heti bejelentések és szabad üzenetek küldése Discord csatornákra.

**Előfeltételek:**
- Webhook URL-ek környezeti változókban (vagy `.env` fájl):
  - `DISCORD_WEBHOOK_KOZLEMENYEK` → #közlemények csatorna
  - `DISCORD_WEBHOOK_PYTHON` → #python-alapok-segítség csatorna
  - `DISCORD_WEBHOOK_BACKEND` → #backend-segítség csatorna

**Használat:**

```bash
# Bejelentés küldése
python discord-webhook.py bejelentes --kurzus python --het 3 --tema "Feltételes elágazások"

# Szabad üzenet
python discord-webhook.py uzenet --webhook-url URL --uzenet "Szabad szöveg"
```

## Kapcsolódó dokumentumok

- [Discord szerver útmutató](../guides/uzemeltetoknek/discord-szerver-utmutato.md) — szerver beállítás, webhook-ok
- [Integrált munkafolyamat](../guides/uzemeltetoknek/integralt-munkafolyamat.md) — félév eleji beállítástól a félév végéig
