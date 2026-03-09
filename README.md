# Kurzusok

Programozás kurzusok középiskolai és felnőttképzési diákok számára, GitHub Classroom integrációval és automatizált értékeléssel.

## Kurzusok

| Kurzus | Évfolyam | Időtartam | Nyelv / Keretrendszer | Vizsga |
|--------|----------|-----------|----------------------|--------|
| [Python alapok](kurzusok/python/10/) | 10. (nappali) | 13 hét, heti 2 óra | Python 3.10+ | 40 pont, 90 perc |
| [Backend FastAPI](kurzusok/python/13/) | 13. (esti / felnőtt) | 25 hét, heti 6 óra | Python + FastAPI | 60 pont, 240 perc |

## Szerkezet

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

## Értékelés

Mindkét kurzus GitHub Classroom-on keresztül működik: a diákok hetente pusholják a megoldásaikat, az automatikus tesztek (pytest / shell) azonnal pontoznak.
