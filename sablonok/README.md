# Sablonok

Új kurzus létrehozásához használható mappastruktúra-sablon.

## Kurzus sablon

Új kurzus indításakor hozd létre a következő mappastruktúrát a `kurzusok/{nyelv}/{évfolyam}/` alatt:

```
├── doksik/
│   ├── diakok/
│   │   ├── leckek/
│   │   ├── feladatok/
│   │   └── README.md
│   ├── tanar/
│   │   ├── tanari-utmutato.md
│   │   ├── github-classroom-utmutato.md
│   │   ├── ertekeles-modszertan.md
│   │   └── README.md
│   ├── tanterv/
│   │   └── tanterv.md
│   └── README.md
├── vizsgak/
│   └── README.md
├── github-classroom/
│   └── README.md
└── README.md
```

Mintaként használd a meglévő kurzusokat: [Python 10](../kurzusok/python/10/), [Backend 13](../kurzusok/python/13/).

## Használat

1. Hozd létre a mappastruktúrát a `kurzusok/{nyelv}/{évfolyam}/` alatt
2. Töltsd ki a README fájlokat a kurzus adataival
3. Készítsd el a heti leckéket és feladatokat
4. Hozd létre a GitHub Classroom template repókat
