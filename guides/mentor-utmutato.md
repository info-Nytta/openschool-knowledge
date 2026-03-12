# Mentor útmutató

Ez az útmutató a mentorok számára készült — azoknak, akik segítik a tanulókat a kurzusok során, kód-átnézést végeznek, és visszajelzést adnak.

---

## Ki lehet mentor?

A mentori szerepkör az OpenSchool közösségen belül a tapasztaltabb tagok számára elérhető:

1. **Legalább egy kurzus sikeres elvégzése** (tanúsítvánnyal)
2. **Aktív közösségi részvétel** — segítőkészség a Discord csatornákon
3. **A mentor útmutató elolvasása** (ez a dokumentum)

> A mentori szerep nem kötelezettség, hanem lehetőség. Ha úgy érzed, hogy tudsz és szeretnél segíteni, jelentkezz a közösségi csatornán.

---

## A mentor szerepe

| Feladat | Leírás |
|---------|--------|
| Segítségnyújtás | Válaszolj a tanulók kérdéseire a Discord csatornákon |
| Kód-átnézés | Nézd át a beadott feladatokat, adj visszajelzést |
| Iránymutatás | Segíts megtalálni a helyes irányt, de ne oldd meg helyettük |
| Motiválás | Bátorítsd a tanulókat, különösen nehezebb heteknél |
| Hibakeresés segítése | Mutasd meg a hibakeresés módszereit, ne csak a megoldást |

---

## Hogyan segíts jól?

### Fő elv: Segíts gondolkodni, ne gondolkodj helyette

```
❌ Rossz: "Írd ezt: for i in range(len(lista)):..."
✅ Jó:   "Milyen ciklussal tudnál végigmenni egy listán? Mi a különbség a for és a while között?"

❌ Rossz: "A hiba az, hogy a 3. sorban print helyett input kell."
✅ Jó:   "Olvasd el a hibaüzenetet — melyik sorra mutat? Mit jelent az 'unexpected EOF'?"
```

### A segítés lépései

1. **Értsd meg a problémát** — kérdezz vissza: „Mit szeretnél, hogy csináljon a kód? Mi történik helyette?"
2. **Irányítsd a figyelmet** — „Nézd meg a hibaüzenet sorszámát" / „Mi az `x` értéke ezen a ponton?"
3. **Adj tippet, ne megoldást** — „Próbáld ki az `int()` függvényt" / „Gondolj a `while` feltételére"
4. **Ha elakad, mutass egy példát** — más kontextusban, ne a pontos megoldást
5. **Ha nagyon elakad, magyarázd el** — de kérd meg, hogy ismételje meg saját szavaival

### Segítés kérés struktúrája (amit elvárj a tanulótól)

Kérd meg a tanulókat, hogy a kérdéseikben adják meg:

```
1. Melyik hét / feladat / fájl?
2. Mit próbáltam?
3. Mi történt (hibaüzenet vagy váratlan eredmény)?
4. Mit vártam volna?
```

---

## Kód-átnézés (Code Review)

A kód-átnézés a tanulási folyamat egyik legfontosabb eleme. A cél: **segíteni a tanulót jobb kódot írni**, nem csak értékelni.

### Alapelvek

- **Pozitív visszajelzéssel kezdj** — „Jól van, a függvényre bontás szép, látszik a logika"
- **Kérdésként fogalmazz** — „Mi lenne, ha a felhasználó negatív számot adna meg?" (nem: „Kezeld a negatív számokat!")
- **Egy dolgot emelsz ki** — ne írd felül 10 megjegyzéssel. Fókuszálj a legfontosabb fejlődési pontra.
- **Adj kontextust** — magyarázd meg, *miért* jobb az egyik megoldás (olvashatóság, karbantarthatóság)
- **Dicsérj, ha fejlődés van** — „A múlt héthez képest sokkal szebben bontottad függvényekre!"

### Python Alapok — Ellenőrzőlista

```
□ Működik-e hiba nélkül?
□ Az input/output megfelel a feladat leírásnak?
□ Függvényekre bontotta-e a kódot?
□ Nincsenek globális változók?
□ A változónevek értelmesek-e? (nem a, b, x, y)
□ Van-e felesleges kód (kikommentezett sorok, debug printek)?
□ A Git története értelmes-e? (több commit, leíró üzenetek)
```

### Backend FastAPI — Ellenőrzőlista

```
□ A Pydantic sémák elkülönülnek (Create/Read)?
□ Az SQLAlchemy modellek helyesek (oszloptípusok, kapcsolatok)?
□ A CRUD réteg paraméteres (session átadva, nincs globális)?
□ Az endpointok a helyes HTTP metódust és státuszkódot használják?
□ Van HTTPException hibakezelés?
□ Vannak tesztek (pozitív ÉS negatív)?
□ A jelszavak hash-elve vannak (bcrypt)?
□ A .env nincs commitolva?
□ A Git történet logikus (5+ commit, értelmes üzenetek)?
□ Nincs felesleges, kikommentezett kód?
```

### Visszajelzés formátuma

GitHub-on (Pull Request vagy commit megjegyzés):

```markdown
## 🔍 Kód-átnézés — 3. hét

### ✅ Ami jó
- Szép, olvasható kódstruktúra
- A `while` ciklus logikusan van felépítve

### 💡 Fejlesztési javaslat
- A `szam_ellenorzes()` függvény túl sokat csinál — érdemes lenne szétbontani
  egy input kérő és egy validáló részre. Miért? Mert így könnyebb tesztelni.

### 📝 Megjegyzés
- Jó haladás a múlt héthez képest!
```

---

## Git történet elemzése

A Git történet sokat elárul a tanuló munkamódszeréről:

| Amit nézz | Mi a jó? | Mi a gyanús? |
|-----------|----------|--------------|
| Commit szám | 3+ commit per feladat | 1 commit az egész feladatra |
| Commit üzenetek | „2. feladat: input kezelés kész" | „asdf" / „." / „done" |
| Időzítés | Több napon át dolgozott | Minden az utolsó percben |
| Szerző | Konzisztens felhasználónév | Váltakozó szerzők |

Ha gyanús mintát látsz, ne vádolj — kérdezz:
> „Látom, hogy egy commitban jött az egész feladat. Előfordult, hogy nem commitoltál közben, vagy szükséged van-e segítségre a Git munkafolyamatban?"

---

## Szóbeli visszakérdezés

Ha a kód-átnézés során kérdés merül fel, informális szóbeli visszakérdezéssel tisztázhatod:

### Python Alapok — példa kérdések

- „Miért használtál itt `while`-t `for` helyett?"
- „Mi történik, ha a felhasználó nem számot ad meg?"
- „Hogyan működik a te `szamol()` függvényed?"

### Backend FastAPI — példa kérdések

- „Mi a különbség a Pydantic séma és az SQLAlchemy modell között?"
- „Miért kell `dependency_overrides` a tesztekhez?"
- „Hogy működik a JWT token a te API-dban?"

### Hogyan reagálj

| Válasz minősége | Reakció |
|----------------|---------|
| Magabiztosan elmagyarázza | Minden rendben |
| Részben érti, bizonytalan | Segíts megérteni — ez tanulási alkalom |
| Nem tudja elmagyarázni a saját kódját | Beszéljétek meg, honnan másolta, és segíts megérteni |

---

## Discord mentori jelenlét

### Hol segíts?

| Csatorna | Mikor válaszolj |
|----------|-----------------|
| `#python-alapok-segítség` | Ha valaki elakadt a Python feladatokkal |
| `#backend-segítség` | Backend kurzus kérdések |
| `#általános` | Általános programozási kérdések |

### Hogyan válaszolj?

- **Használj szálakat (threads)** — ne a fő csatornába írd a hosszú magyarázatot
- **Kódot code blockban** — ` ```python ... ``` `
- **Reagálj emojival** ha láttad de nem tudsz most válaszolni — a tanuló tudja, hogy nem lett figyelmen kívül hagyva
- **Ha nem tudod a választ** — ne tippelj. Mondd, hogy utánanézel, vagy jelezd, hogy más mentor segíthet

### Válaszidő

- Nincs kötelező válaszidő — a mentorálás önkéntes
- Ha rendszeresen elérhető vagy, jelezd a profilodon (pl. „Általában este 18-21 között elérhető")

---

## Tippek

- **Légy türelmes** — ami neked egyszerű, annak a tanulónak az első alkalom
- **Emlékezz, te is tanuló voltál** — a saját tapasztalataid a legjobb tanítóeszköz
- **Kérdezz, mielőtt válaszolsz** — gyakran nem az a kérdés, amit elsőre feltesznek
- **Ne írd át a kódját** — ha muszáj kódot mutatnod, írd más kontextusban
- **Jelezz, ha kiégsz** — tarts szünetet, a közösség megérti

---

**Kapcsolódó útmutatók:**
- [Közösségi útmutató](kozossegi-utmutato.md)
- [GitHub Classroom — Diák útmutató](github-classroom-diak-utmutato.md)
- [Kezdő útmutató](kezdo-utmutato.md)
