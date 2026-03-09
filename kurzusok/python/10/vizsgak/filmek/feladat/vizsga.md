# Python szintfelmérő – 10. évfolyam

**Időtartam:** 90 perc
**Összpontszám:** 40 pont

---

## 1. feladat – Felhasználónév generáló program (8 pont)

Készíts programot, amely bekéri a felhasználó **vezetéknevét**, **keresztnevét** és **kedvenc számát**, majd három ajánlott felhasználónevet állít össze.

### Működés:

1. A program kérje be a vezetéknevet, a keresztnevet és a kedvenc számot.
2. A beírt neveket alakítsa kisbetűsre.
3. Állítson össze három felhasználónevet az alábbi formátumokban:
   - **1. név:** teljes keresztnév + vezetéknév első betűje + kedvenc szám (pl. `annak42`)
   - **2. név:** keresztnév első betűje + `_` + teljes vezetéknév + kedvenc szám (pl. `a_kiss42`)
   - **3. név:** teljes vezetéknév + `.` + teljes keresztnév + kedvenc szám (pl. `kiss.anna42`)
4. Jelenítse meg a három felhasználónevet a képernyőn.

### Technikai elvárások:

- A program függvényekre bontva legyen megírva.
- Az adatbekérés, az összefűzés és a megjelenítés külön függvényben legyen.

---

## 2. feladat – Kártyahúzós tippelős játék (14 pont)

Készíts programot, amely három véletlenszerű kártyát húz (1–13 értékűt), és a játékosnak ki kell találnia a kártyák összegét.

### Működés:

1. A program generáljon három véletlenszerű számot 1 és 13 között, és tárolja listában.
2. A játékos tippelhet, mennyi a három kártya összege.
3. A program értékelje ki a tippet:
   - Ha a tipp kisebb, mint 3 vagy nagyobb, mint 39: **„HIBA: nem lehetséges érték!"**
   - Ha a tipp kisebb, mint az összeg: **„Ennél több"**
   - Ha a tipp nagyobb, mint az összeg: **„Ennél kevesebb"**
   - Ha a tipp megegyezik az összeggel: **„Talált!"**
4. A játék addig folytatódik, amíg a játékos el nem találja az összeget.
5. Tartsa nyilván a tippek számát.
6. A játék végén írja ki a húzott kártyákat, a tippek számát, és köszönje meg a játékot.

### Technikai elvárások:

- A `random` modul használata szükséges.
- A program függvényekre bontva és `while` ciklussal legyen megírva.

---

## 3. feladat – Filmek feldolgozása (18 pont)

Az UTF-8 kódolású `filmek.txt` fájl filmek adatait tartalmazza pontosvesszővel elválasztva:

**cím;kategória;év;hossz_perc;értékelés**

A kategóriák: akció, vígjáték, dráma, horror.

### Feladatok:

1. Olvasd be az állomány tartalmát, és tárold összetett adatszerkezetű listában (lista listája vagy szótárak listája). Az évet és a hosszt alakítsd egész számmá, az értékelést valós számmá (float).
2. Írd ki, hány film található a listában.
3. Írd ki, hogy hány akció, vígjáték, dráma és horror film van.
4. Keresd meg és írd ki a legjobb és a legrosszabb értékelésű film címét és értékelését.
5. Kérd be egy film címét! Ha megtalálható a listában, írd ki az adatait egy `valasztott_film.txt` fájlba pontosvesszővel elválasztva. Ha nem létezik, írd ki: „Nincs ilyen cím a listában".
6. Kérd be egy kategória nevét! Írd ki az adott kategóriába tartozó filmek címét és megjelenési évét.

### Technikai elvárások:

- A segédfüggvényeket külön modulban (`fgv.py`) kell megírni.
- A `fgv.py` modult importálni kell a `feladat3.py`-ban.
- Minden alfeladathoz külön függvény tartozzon.
