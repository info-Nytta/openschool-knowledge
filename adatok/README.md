# Adatok mappa

Ez a mappa tartalmazza a tanulók értékelési adatait. **Nem kerül verziókezelésbe** (`.gitignore`-ban van).

## Mappaszerkezet

```
adatok/
  <év>/
    <kurzus>/
      classroom/              ← GitHub Classroom CSV exportok (hetente)
        het01-alapok.csv
        het02-bevitel-szoveg.csv
        ...
      vizsga.csv              ← vizsgapontszámok
      orai.csv                ← órai munka jegyek
      probavizsga.csv         ← próbavizsga pontszámok
      eredmenyek.csv          ← generált kimenet (jegy-szamolo.py)
```

## GitHub Classroom CSV letöltése

1. Nyisd meg a GitHub Classroom dashboardot
2. Válaszd ki az assignment-et
3. Kattints a **Download Grades** gombra
4. Mentsd a CSV-t a `classroom/` mappába az assignment nevével

A Classroom CSV formátuma:
```
assignment_name,assignment_url,starter_code_url,github_username,roster_identifier,student_repository_name,student_repository_url,submission_timestamp,points_awarded,points_available
```

## Kiegészítő CSV fájlok formátuma

### vizsga.csv
```
tanulo,pont
Kovács Anna,35
Nagy Péter,28
```

### orai.csv
```
tanulo,jegy
Kovács Anna,4
Nagy Péter,5
```

### probavizsga.csv
```
tanulo,pont
Kovács Anna,32
Nagy Péter,45
```

A `tanulo` oszlop a tanuló GitHub Classroom `roster_identifier` értékével egyezzen meg.

## Használat

```bash
# A projekt gyökérmappájából:
python eszkozok/jegy-szamolo.py --kurzus python10 --ev 2026

# Egy tanuló jegye:
python eszkozok/jegy-szamolo.py --kurzus python10 --ev 2026 --tanulo "Kovács Anna"

# Eredmények mentése CSV-be:
python eszkozok/jegy-szamolo.py --kurzus python10 --ev 2026 --kimenet adatok/2026/python10/eredmenyek.csv
```
