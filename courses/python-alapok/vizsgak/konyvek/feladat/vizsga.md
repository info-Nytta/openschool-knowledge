# Python Alapok szintfelmérő

**Időtartam:** 90 perc
**Összpontszám:** 40 pont

---

## 1. feladat – Emailgeneráló program (8 pont)

Készítsen emailgeneráló programot, amely az alábbiak szerint működik!

### Működés:

1. Billentyűzetről kérje be a felhasználó vezeték- és keresztnevét, valamint a születési évét!
2. A bekért adatokból állítson össze három ajánlott email címet `mail.com` végződéssel, és jelenítse meg a képernyőn a minta szerint:
   - **1. cím:** teljes keresztnév és a vezetéknév első betűje csupa kisbetűvel
   - **2. cím:** keresztnév első betűje és a teljes vezetéknév csupa kisbetűvel, végén a születési évszám
   - **3. cím:** teljes keresztnév és teljes vezetéknév csupa kisbetűvel, ponttal elválasztva

### Technikai elvárások:

- A program függvényekre bontva legyen megírva.
- Az adatbekérés, az összefűzés és a megjelenítés külön függvényben legyen.

---

## 2. feladat – Kockadobós tippelős játék (14 pont)

Készítsen tippelő játékprogramot, ahol a program kockadobásainak összegét kell a felhasználónak megtippelnie!

### Működés:

1. A program generáljon három kockadobást, amit egy listában tároljon el!
2. A program ezután kérje be a felhasználó tippjét arra vonatkozóan, hogy mennyi lehet a kockák összesített pontszáma?
3. A program értékelje ki a választ:
   - Ha a tipp 3-nál kisebb, vagy 18-nál nagyobb: **„HIBA: nem lehetséges érték!"**
   - Ha a tipp a kockák összesített pontszámával megegyezik: **„Talált!"**
   - Ha a tipp kisebb: **„Ennél több"**
   - Ha a tipp nagyobb: **„Ennél kevesebb"**
4. A játék addig folytatódjon, amíg a felhasználó el nem találja a helyes pontszámot!
5. Tartsa nyilván a tippek számát.
6. A játék végén a program írja ki a dobásokat és azt, hogy hányadik tippelésre sikerült eltalálni a megfelelő pontszámot, majd köszönje meg a játékot!

### Technikai elvárások:

- A `random` modul használata szükséges.
- A program függvényekre bontva és `while` ciklussal legyen megírva.

---

## 3. feladat – Könyvek feldolgozása (18 pont)

Az UTF-8 kódolású `konyvek.txt` állomány néhány könyv adatának listáját tartalmazza. Az állomány sorai azonos szerkezetűek, az adattagok pontosvesszővel tagoltak. Az állomány egy sora például:

**A vándor árnyéka;német;fantasy;2005;1250000**

Az adattagok jelentése rendre a következők: könyv címe, eredeti megjelenési nyelve, műfaja, megjelenési éve, eladásából származó bevétel (euró).

### Feladatok:

1. Olvassa be az állomány tartalmát, és tárolja le a megfelelő összetett adatszerkezetű listában! Ha nem tudja a fájlt beolvasni, használhatja a `konyvek.py` modult.
2. Írja ki, hogy hány könyv található a listában!
3. Írja ki, hogy hány angol, német és francia nyelven íródott könyv található a listában!
4. Írja ki a legnagyobb és a legkisebb bevételt hozó könyv címét és bevételét!
5. Kérje be a felhasználótól egy könyv címét! Ha van ilyen cím a listában, akkor annak az összes adatát írja ki egy fájlba (`valasztott_konyv.txt`), és erről tájékoztassa a felhasználót! Ha nincs a listában ilyen címen könyv, akkor a „Nincs ilyen cím a listában" szöveget jelenítse meg!
6. Kérje be a felhasználótól egy műfaj nevét! A képernyőre írja ki az összes könyvcímet és kiadásának évét, amely a megadott műfajhoz tartozik!

### Technikai elvárások:

- A segédfüggvényeket külön modulban (`fgv.py`) kell megírni.
- A `fgv.py` modult importálni kell a főprogramban.
- Minden alfeladathoz külön függvény tartozzon.
