# Kurzusok

Programozás kurzusok középiskolai és felnőttképzési diákok számára, GitHub Classroom integrációval és automatizált értékeléssel.

**Operációs rendszer:** Windows 10+, Linux, macOS – minden útmutató és eszköz mindhárom platformon működik.

---

## Miért jó ez a projekt?

### A probléma

Egy programozástanár félévente ugyanazokat a feladatokat végzi el kézzel: repók létrehozása, feladatok kiosztása, megoldások ellenőrzése, pontok összesítése, kommunikáció a diákokkal. Ez rengeteg ismétlődő munka, ami elveszi az időt az oktatástól.

### A megoldás

Ez a projekt egy **teljes, újrahasználható oktatási rendszert** ad egyetlen tanár kezébe:

- **Automatikus értékelés** — a diákok pusholnak, a GitHub Actions azonnal pontozza a megoldásokat. A tanár nem kézzel javít, hanem a kódminőséget és a tanulási folyamatot figyeli.
- **Félév 3 parancsból indul** — template repók létrehozása, Discord szálak nyitása, assignment linkek küldése. A félév végén egy szkript kiszámolja a jegyeket.
- **Évről évre újrahasználható** — ugyanaz a szerver, ugyanazok a sablonok, ugyanazok az eszközök. Új tanév = új szerepkörök és szálak, semmi mást nem kell újraépíteni.
- **Két nagyon különböző kurzus, egy rendszer** — 10.-es kezdők és felnőtt backend-fejlesztők is ugyanabban a struktúrában tanulnak, de a saját szintjükön.

### Alapelvek

| Elv | Megvalósítás |
|-----|-------------|
| **Gyakorlat az elmélet előtt** | Max 15 perc elmélet, utána live coding és kézzel írás. A programozás kézműves szakma. |
| **A vizsga nem meglepetés** | Minden házi feladat egy vizsgafeladat-típust gyakoroltat. A félév végére a diák már 10× megcsinálta, amit a vizsgán kérünk. |
| **Az automatikus teszt alap, nem cél** | Az autograding objektív alapot ad, de a tanár a kódminőséget, a git történetet és szükség esetén szóban értékel. |
| **Növekedési szemlélet** | A házi feladat visszajelzés, nem büntetés. A fejlődés számít, nem a hibátlanság. |
| **Nulla külső függőség** | Minden eszköz Python stdlib + `gh` CLI. Nincs npm, nincs pip csomag, nincs fizetős szolgáltatás. |
| **Adatvédelem beépítve** | Tanulói adatok soha nem kerülnek verziókövetésbe (`.gitignore`). Webhook URL-ek `.env` fájlban. |

### Kinek való?

Programozástanároknak, akik:
- GitHub Classroom-ot használnak (vagy szeretnének)
- szeretnék automatizálni az ismétlődő adminisztrációt
- magyar nyelvű, kulturálisan illeszkedő anyagokat keresnek
- egy jól strukturált kiindulópontot akarnak, amit a saját igényeikre szabhatnak

---

## Kurzusok

| Kurzus | Évfolyam | Időtartam | Nyelv / Keretrendszer | Vizsga |
|--------|----------|-----------|----------------------|--------|
| [Python alapok](kurzusok/python/10/) | 10. (nappali) | 13 hét, heti 2 óra | Python 3.10+ | 40 pont, 90 perc |
| [Backend FastAPI](kurzusok/python/13/) | 13. (esti / felnőtt) | 25 hét, heti 6 óra | Python + FastAPI | 60 pont, 240 perc |

## Projekt szerkezet

```
├── kurzusok/                # Kurzus-specifikus tartalom
│   └── python/
│       ├── 10/              #   Python alapok (13 hét)
│       └── 13/              #   Backend FastAPI (25 hét)
├── kozos/                   # Kurzusokon átívelő közös dokumentáció
│   ├── discord-szerver-utmutato.md
│   └── integralt-munkafolyamat.md
├── sablonok/                # Új kurzus létrehozásához sablonok
├── eszkozok/                # Szkriptek, segédeszközök
│   ├── github-setup.sh      #   Template repók létrehozása (bash)
│   ├── github-setup.ps1     #   Template repók létrehozása (PowerShell)
│   ├── discord-webhook.py   #   Discord értesítések küldése
│   └── jegy-szamolo.py      #   Félév végi jegy kiszámítása
└── adatok/                  # Tanulói adatok – .gitignore-olt
    └── {év}/{kurzus}/classroom/
```

### Kurzus mappastruktúra

Minden kurzus azonos mappastruktúrát követ:

```
kurzusok/python/{évfolyam}/
├── doksik/                  # Dokumentáció
│   ├── diakok/              #   Leckék + feladatok
│   ├── tanar/               #   Tanári útmutató, értékelés
│   └── tanterv/             #   Tanterv
├── vizsgak/                 # Vizsgavariánsok (feladatlap, megoldás, értékelés)
└── github-classroom/        # GitHub Classroom template repók
```

## Közös dokumentáció

Kurzusokon átívelő dokumentumok: → [kozos/](kozos/)

- **[Discord szerver útmutató](kozos/discord-szerver-utmutato.md)** — szerver beállítás, csatornák, webhook-ok, moderáció
- **[Integrált munkafolyamat](kozos/integralt-munkafolyamat.md)** — félév eleji beállítástól a jegyek kiszámításáig, lépésről lépésre

## Eszközök

A tanári munkát automatizáló szkriptek: → [eszkozok/](eszkozok/)

| Eszköz | Leírás |
|--------|--------|
| `github-setup.sh` / `.ps1` | Template repók létrehozása egy GitHub Organization alatt |
| `discord-webhook.py` | Bejelentések, emlékeztetők és szálnyitók küldése Discord csatornákra |
| `jegy-szamolo.py` | Házi feladatok összesítése és végső jegy kiszámítása |

## Értékelés

Mindkét kurzus GitHub Classroom-on keresztül működik: a diákok hetente pusholják a megoldásaikat, az automatikus tesztek (pytest / shell) azonnal pontoznak.

| Komponens | Python 10 | Backend 13 |
|-----------|-----------|------------|
| Házi feladatok | 25% | 20% |
| Órai munka | 15% | 15% |
| Próbavizsga | 10% | 15% |
| Vizsga | 50% | 50% |

A félév végi jegyek a `jegy-szamolo.py` szkripttel számíthatók ki a GitHub Classroom CSV exportokból (lásd [integrált munkafolyamat](kozos/integralt-munkafolyamat.md)).
