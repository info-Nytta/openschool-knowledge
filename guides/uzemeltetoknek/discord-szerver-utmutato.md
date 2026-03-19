# Discord szerver kezelése

Egyetlen Discord szerver szolgál minden kurzushoz. Kurzusonként egy kategória biztosítja az elkülönítést.

---

## Szerver létrehozása

Discord → **+** → **Create My Own** → **For a club or community** → adj nevet (pl. `Programozás kurzusok`). Ne tedd bele az évszámot — a szerver évről évre újrahasználható.

## Csatornaszerkezet

```
📋 INFORMÁCIÓ
  #szabályzat
  #közlemények         (csak mentorok írhatnak)
  #hasznos-linkek

🐍 PYTHON ALAPOK
  #python-alapok-általános
  #python-alapok-segítség
  #python-alapok-megoldások

⚡ BACKEND FASTAPI
  #backend-általános
  #backend-segítség
  #backend-megoldások

💬 KÖZÖSSÉG
  #általános
  #off-topic

🎤 HANG
  🔊 konzultáció
  🔊 foglalkozás

🔒 TANÁRI (rejtett)
  #mentori-szoba
  #értékelések
```

Új kurzus = új kategória 2–3 csatornával. A `#segítség` csatornákon **szálakat** használj heti bontásban (pl. *„2026 – 3. hét – Feltételes elágazások"*), így a csatornák száma fix marad.

## Szerepkörök

Szerver beállítások → **Roles** → **Create Role**:

| Szerepkör | Jogok |
|-----------|-------|
| `Mentor` | Adminisztrátor |
| `Python Alapok – 2026` | Üzenetküldés, olvasás, reakciók, fájlcsatolás |
| `Backend FastAPI – 2026` | Üzenetküldés, olvasás, reakciók, fájlcsatolás |

Az évszám a szerepkör nevében segít kezelni, ki az aktív tanuló. Ha nem kell kurzusonkénti elkülönítés, elég egyetlen `Tanuló – 2026` szerepkör.

### Jogosultságok

- **`#közlemények`**: `@everyone` → ❌ Send Messages, `Mentor` → ✅ Send Messages
- **`🔒 TANÁRI`**: `@everyone` → ❌ View Channel, `Mentor` → ✅ View Channel
- **Kurzus elrejtése** (opcionális): kategória → `@everyone` ❌ View, kurzus-szerepkör ✅ View

## Meghívó link

Szerver neve → **Invite People** → **Edit invite link** → Expire: **Never**, Max uses: **No limit**. Oszd meg a tanulókkal, de ne tedd nyilvánossá.

## Webhook-ok

A webhook-ok lehetővé teszik, hogy szkriptek (pl. `discord-webhook.py`) üzeneteket küldjenek.

1. Csatorna → **⚙️** → **Integrations** → **Webhooks** → **New Webhook**
2. Adj nevet, ellenőrizd a csatornát, **Copy Webhook URL**
3. Tárold `.env` fájlban (soha ne commitold):

```bash
# tools/.env
DISCORD_WEBHOOK_KOZLEMENYEK=https://discord.com/api/webhooks/...
DISCORD_WEBHOOK_PYTHON=https://discord.com/api/webhooks/...
DISCORD_WEBHOOK_BACKEND=https://discord.com/api/webhooks/...
```

Teszt: `python tools/discord-webhook.py uzenet --webhook-url $DISCORD_WEBHOOK_PYTHON --uzenet "Teszt"`

Részletek a Discord dokumentációban: [discord.com/developers/docs/resources/webhook](https://discord.com/developers/docs/resources/webhook)

## Botok (opcionális)

- **GitHub bot** — push/PR értesítések: `/github subscribe ORG/REPO` ([telepítés](https://github.com/integrations/discord))
- **Carl-bot** — automatikus szerepkör, ütemezett üzenetek: [carl.gg](https://carl.gg)

## Moderáció

Szerver beállítások → **Safety Setup**:
- Verification Level: **Medium**
- Explicit Media Content Filter: **Scan messages from all members**
- AutoMod: spam szűrés be, max 5 mention/üzenet

## Heti rutin

1. **Hét eleje**: közlemény a `#közlemények`-ben (🐍 vagy ⚡ jelöléssel)
2. **Szál nyitása**: a `#segítség` csatornán az aktuális héthez
3. **Pinelés**: fontos üzenetek pin-elése, kérdéseknél 👀/✅ reakció

## Évváltás

Minden tanév elején:
1. Új éves szerepkörök (pl. `Python Alapok – 2027`)
2. Régi tanulók szerepkörét nem kell elvenni — a szálak évszám prefixe elkülöníti az évfolyamokat
3. Üdvözlő közlemény az új tanévre

## Hibaelhárítás

| Probléma | Megoldás |
|----------|---------|
| Tanuló nem lát csatornát | Ellenőrizd a szerepkörét |
| Nem tud írni `#közlemények`-be | Szándékos — csak mentorok írhatnak |
| Webhook 404/401 hiba | A webhook törölve lett — hozd létre újra |
| Bot nem működik | Ellenőrizd a jogosultságait a szerver beállításokban |
