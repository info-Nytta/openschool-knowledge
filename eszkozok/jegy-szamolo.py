"""
Jegy kalkulátor – GitHub Classroom eredmények feldolgozása és jegyek kiszámítása.

Két mód:

  Kötegelt mód – az összes tanuló jegyét kiszámítja a Classroom exportokból:
    python eszkozok/jegy-szamolo.py --kurzus python10 --ev 2026

  Egyéni mód – egy tanuló jegye:
    python eszkozok/jegy-szamolo.py --kurzus python10 --ev 2026 --tanulo "Kovács Anna"

  Eredmények mentése:
    python eszkozok/jegy-szamolo.py --kurzus python10 --ev 2026 --kimenet eredmenyek.csv

Az adatok elvárt helye (a projekt gyökérmappájából):
    adatok/<év>/<kurzus>/
        classroom/           ← GitHub Classroom CSV exportok (assignment-enként)
        vizsga.csv           ← tanulo,pont
        orai.csv             ← tanulo,jegy
        probavizsga.csv      ← tanulo,pont
"""

import argparse
import csv
import os
import sys
from pathlib import Path


# --- Jegyhatárok ---

JEGYHATÁROK = {
    "python10": {
        "vizsga": {  # 40 pont max
            5: 36, 4: 28, 3: 20, 2: 12, 1: 0,
        },
        "osszesitett": {  # százalékos
            5: 80, 4: 60, 3: 40, 2: 20, 1: 0,
        },
        "sulyok": {
            "hazi": 0.25,
            "orai": 0.15,
            "probavizsga": 0.10,
            "vizsga": 0.50,
        },
        "vizsga_max": 40,
        "probavizsga_max": 40,
        "min_beadas": 8,
    },
    "backend13": {
        "vizsga": {  # 60 pont max
            5: 54, 4: 43, 3: 31, 2: 19, 1: 0,
        },
        "osszesitett": {  # százalékos
            5: 80, 4: 60, 3: 40, 2: 20, 1: 0,
        },
        "sulyok": {
            "hazi": 0.20,
            "orai": 0.15,
            "probavizsga": 0.15,
            "vizsga": 0.50,
        },
        "vizsga_max": 60,
        "probavizsga_max": 60,
        "min_beadas": 16,
    },
}

# A projekt gyökérmappájának meghatározása (a script eszkozok/ mappában van)
SCRIPT_DIR = Path(__file__).resolve().parent
PROJEKT_GYOKER = SCRIPT_DIR.parent


def pont_to_jegy(pont, hatarok):
    """Pont → jegy konverzió a megadott határok alapján."""
    for jegy in [5, 4, 3, 2]:
        if pont >= hatarok[jegy]:
            return jegy
    return 1


def szazalek_to_jegy(szazalek, hatarok):
    """Százalék → jegy konverzió."""
    for jegy in [5, 4, 3, 2]:
        if szazalek >= hatarok[jegy]:
            return jegy
    return 1


# ---------------------------------------------------------------------------
# Classroom CSV feldolgozás
# ---------------------------------------------------------------------------

def classroom_csv_beolvasas(mappa):
    """Beolvassa az összes Classroom CSV-t a mappából.

    Visszaad egy dict-et: {tanulo_nev: [{het, max_pont, elert_pont}, ...]}
    A hét sorszámát a fájlnévből veszi (hetXX-*.csv), vagy a fájl sorrendjéből.
    """
    tanulok = {}  # tanulo -> [{het, max_pont, elert_pont}]

    csv_fajlok = sorted(Path(mappa).glob("*.csv"))
    if not csv_fajlok:
        print(f"⚠️  Nincs CSV fájl a {mappa} mappában.", file=sys.stderr)
        return tanulok

    for het_index, csv_path in enumerate(csv_fajlok):
        # Hét sorszám a fájlnévből (hetXX-...) vagy az index
        nev = csv_path.stem
        het_szam = het_index
        if nev.startswith("het"):
            try:
                het_szam = int(nev[3:5])
            except ValueError:
                pass

        with open(csv_path, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # GitHub Classroom CSV mezők
                tanulo = row.get("roster_identifier", "").strip()
                if not tanulo:
                    tanulo = row.get("github_username", "").strip()
                if not tanulo:
                    continue

                try:
                    elert = int(row.get("points_awarded", 0) or 0)
                    maximum = int(row.get("points_available", 0) or 0)
                except (ValueError, TypeError):
                    elert, maximum = 0, 0

                if tanulo not in tanulok:
                    tanulok[tanulo] = []
                tanulok[tanulo].append({
                    "het": het_szam,
                    "max_pont": maximum,
                    "elert_pont": elert,
                })

    return tanulok


def kieg_csv_beolvasas(fajl, ertek_oszlop):
    """Kiegészítő CSV beolvasása (vizsga.csv / orai.csv / probavizsga.csv).

    Visszaad: {tanulo_nev: szám}
    """
    eredmeny = {}
    path = Path(fajl)
    if not path.exists():
        return eredmeny

    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            tanulo = row.get("tanulo", "").strip()
            if not tanulo:
                continue
            try:
                ertek = int(row[ertek_oszlop])
            except (ValueError, KeyError):
                continue
            eredmeny[tanulo] = ertek

    return eredmeny


# ---------------------------------------------------------------------------
# Házi feladat statisztika
# ---------------------------------------------------------------------------

def hazi_statisztika(hetek):
    """Heti pontokból összesített statisztika."""
    ossz_max = sum(h["max_pont"] for h in hetek)
    ossz_elert = sum(h["elert_pont"] for h in hetek)
    szazalek = (ossz_elert / ossz_max * 100) if ossz_max > 0 else 0
    beadott = sum(1 for h in hetek if h["elert_pont"] > 0)

    return {
        "hetek": hetek,
        "ossz_max": ossz_max,
        "ossz_elert": ossz_elert,
        "szazalek": round(szazalek, 1),
        "beadott": beadott,
        "osszes_het": len(hetek),
    }


# ---------------------------------------------------------------------------
# Jegy számítás
# ---------------------------------------------------------------------------

def jegy_szamitas_tanulo(kurzus, hazi_hetek, vizsga_pont, orai_jegy=None, probavizsga_pont=None):
    """Végső jegy kiszámítása egy tanulóra."""
    config = JEGYHATÁROK[kurzus]
    sulyok = config["sulyok"]

    hazi = hazi_statisztika(hazi_hetek)
    hazi_jegy = szazalek_to_jegy(hazi["szazalek"], config["osszesitett"])

    vizsga_jegy = pont_to_jegy(vizsga_pont, config["vizsga"]) if vizsga_pont is not None else 1

    if orai_jegy is None:
        orai_jegy = 3

    if probavizsga_pont is not None:
        proba_szazalek = probavizsga_pont / config["probavizsga_max"] * 100
        proba_jegy = szazalek_to_jegy(proba_szazalek, config["osszesitett"])
    else:
        proba_jegy = 3

    sulyozott = (
        hazi_jegy * sulyok["hazi"]
        + orai_jegy * sulyok["orai"]
        + proba_jegy * sulyok["probavizsga"]
        + vizsga_jegy * sulyok["vizsga"]
    )

    vegso_jegy = round(sulyozott)

    figyelmeztetesek = []
    min_beadas = config.get("min_beadas")
    if min_beadas and hazi["beadott"] < min_beadas:
        vegso_jegy = 1
        figyelmeztetesek.append(f"Kevés beadás ({hazi['beadott']}/{min_beadas} minimum)")

    if vizsga_pont is None:
        figyelmeztetesek.append("Nincs vizsgaeredmény")

    return {
        "hazi": hazi,
        "hazi_jegy": hazi_jegy,
        "vizsga_pont": vizsga_pont,
        "vizsga_max": config["vizsga_max"],
        "probavizsga_max": config["probavizsga_max"],
        "vizsga_jegy": vizsga_jegy,
        "orai_jegy": orai_jegy,
        "proba_pont": probavizsga_pont,
        "proba_jegy": proba_jegy,
        "sulyozott": round(sulyozott, 2),
        "vegso_jegy": vegso_jegy,
        "sulyok": sulyok,
        "figyelmeztetesek": figyelmeztetesek,
    }


# ---------------------------------------------------------------------------
# Kötegelt feldolgozás
# ---------------------------------------------------------------------------

def kotegelt_feldolgozas(kurzus, adatok_mappa):
    """Az összes tanuló jegyének kiszámítása a mappában lévő adatokból."""
    mappa = Path(adatok_mappa)
    classroom_mappa = mappa / "classroom"

    if not classroom_mappa.exists():
        print(f"❌ Nem található: {classroom_mappa}", file=sys.stderr)
        sys.exit(1)

    # Classroom CSV-k beolvasása → házi pontok tanulónként
    tanulo_hazik = classroom_csv_beolvasas(classroom_mappa)
    if not tanulo_hazik:
        print("❌ Nincsenek tanulók a Classroom CSV-kben.", file=sys.stderr)
        sys.exit(1)

    # Kiegészítő adatok
    vizsgak = kieg_csv_beolvasas(mappa / "vizsga.csv", "pont")
    oraik = kieg_csv_beolvasas(mappa / "orai.csv", "jegy")
    probak = kieg_csv_beolvasas(mappa / "probavizsga.csv", "pont")

    # Számítás tanulónként
    eredmenyek = {}
    for tanulo in sorted(tanulo_hazik.keys()):
        eredmenyek[tanulo] = jegy_szamitas_tanulo(
            kurzus,
            tanulo_hazik[tanulo],
            vizsgak.get(tanulo),
            oraik.get(tanulo),
            probak.get(tanulo),
        )

    return eredmenyek


# ---------------------------------------------------------------------------
# Kimenet
# ---------------------------------------------------------------------------

def print_tablazat(kurzus, eredmenyek):
    """Összesítő táblázat az összes tanulóról."""
    config = JEGYHATÁROK[kurzus]
    print(f"\n{'=' * 72}")
    print(f"  JEGY ÖSSZESÍTÉS – {kurzus.upper()}")
    print(f"  Tanulók száma: {len(eredmenyek)}")
    print(f"{'=' * 72}\n")

    fejlec = f"  {'Tanuló':<25} {'Házi':>5} {'Órai':>5} {'Próba':>5} {'Vizsga':>6} {'Átlag':>6} {'JEGY':>4}  Megj."
    print(fejlec)
    print(f"  {'─' * 70}")

    for tanulo, e in eredmenyek.items():
        vizsga_str = f"{e['vizsga_pont']}/{e['vizsga_max']}" if e["vizsga_pont"] is not None else "  –"
        megj = ", ".join(e["figyelmeztetesek"]) if e["figyelmeztetesek"] else ""
        print(
            f"  {tanulo:<25} "
            f"{e['hazi_jegy']:>5} "
            f"{e['orai_jegy']:>5} "
            f"{e['proba_jegy']:>5} "
            f"{vizsga_str:>6} "
            f"{e['sulyozott']:>6} "
            f"{e['vegso_jegy']:>4}"
            f"  {megj}"
        )

    print(f"\n  {'─' * 70}")
    jegyek = [e["vegso_jegy"] for e in eredmenyek.values()]
    atlag = sum(jegyek) / len(jegyek) if jegyek else 0
    print(f"  Osztályátlag: {atlag:.2f}")
    for j in [5, 4, 3, 2, 1]:
        db = jegyek.count(j)
        print(f"    {j}-ös: {db} fő ({db/len(jegyek)*100:.0f}%)" if jegyek else "")
    print()


def print_reszletes(tanulo, eredmeny):
    """Egy tanuló részletes eredménye."""
    e = eredmeny
    sulyok = e["sulyok"]
    print(f"\n{'=' * 50}")
    print(f"  {tanulo}")
    print(f"{'=' * 50}\n")

    hazi = e["hazi"]
    print(f"📝 Házi feladatok ({int(sulyok['hazi']*100)}%)")
    print(f"   Beadott: {hazi['beadott']}/{hazi['osszes_het']} hét")
    print(f"   Pontok:  {hazi['ossz_elert']}/{hazi['ossz_max']} ({hazi['szazalek']}%)")
    print(f"   Jegy:    {e['hazi_jegy']}")
    print()
    print(f"🏫 Órai munka ({int(sulyok['orai']*100)}%)")
    print(f"   Jegy:    {e['orai_jegy']}")
    print()
    print(f"📋 Próbavizsga ({int(sulyok['probavizsga']*100)}%)")
    if e["proba_pont"] is not None:
        print(f"   Pontok:  {e['proba_pont']}/{e['probavizsga_max']}")
    print(f"   Jegy:    {e['proba_jegy']}")
    print()
    print(f"🎓 Vizsga ({int(sulyok['vizsga']*100)}%)")
    if e["vizsga_pont"] is not None:
        print(f"   Pontok:  {e['vizsga_pont']}/{e['vizsga_max']}")
    print(f"   Jegy:    {e['vizsga_jegy']}")
    print()
    print(f"{'─' * 50}")
    print(f"   Súlyozott átlag: {e['sulyozott']}")
    print(f"   ★ VÉGSŐ JEGY:    {e['vegso_jegy']}")
    print(f"{'─' * 50}")

    if e["figyelmeztetesek"]:
        for f in e["figyelmeztetesek"]:
            print(f"   ⚠️  {f}")
        print()

    # Heti részletek
    print(f"\n  {'Hét':>3}  {'Elért':>6}  {'Max':>4}  {'%':>6}")
    print(f"  {'───':>3}  {'─────':>6}  {'───':>4}  {'─────':>6}")
    for h in hazi["hetek"]:
        szaz = h["elert_pont"] / h["max_pont"] * 100 if h["max_pont"] > 0 else 0
        print(f"  {h['het']:>3}  {h['elert_pont']:>6}  {h['max_pont']:>4}  {szaz:>5.1f}%")
    print()


def kimenet_csv(eredmenyek, fajl):
    """Eredmények mentése CSV fájlba."""
    with open(fajl, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "tanulo", "hazi_szazalek", "hazi_jegy", "orai_jegy",
            "probavizsga_jegy", "vizsga_pont", "vizsga_jegy",
            "sulyozott_atlag", "vegso_jegy", "megjegyzes",
        ])
        for tanulo, e in eredmenyek.items():
            writer.writerow([
                tanulo,
                e["hazi"]["szazalek"],
                e["hazi_jegy"],
                e["orai_jegy"],
                e["proba_jegy"],
                e["vizsga_pont"] if e["vizsga_pont"] is not None else "",
                e["vizsga_jegy"],
                e["sulyozott"],
                e["vegso_jegy"],
                "; ".join(e["figyelmeztetesek"]),
            ])
    print(f"✅ Eredmények mentve: {fajl}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Jegy kalkulátor – GitHub Classroom eredmények és jegyek",
        epilog="Futtatás a projekt gyökérmappájából: python eszkozok/jegy-szamolo.py --kurzus python10 --ev 2026",
    )
    parser.add_argument("--kurzus", choices=["python10", "backend13"], required=True,
                        help="Kurzus neve")
    parser.add_argument("--ev", type=int, default=2026,
                        help="Tanév (alapértelmezett: 2026)")
    parser.add_argument("--mappa",
                        help="Adatmappa útvonal (alapértelmezett: adatok/<év>/<kurzus>/)")
    parser.add_argument("--tanulo",
                        help="Egy tanuló neve – részletes eredmény")
    parser.add_argument("--kimenet",
                        help="Eredmények mentése CSV fájlba")

    args = parser.parse_args()

    # Adatmappa meghatározása
    if args.mappa:
        adatok_mappa = Path(args.mappa)
    else:
        adatok_mappa = PROJEKT_GYOKER / "adatok" / str(args.ev) / args.kurzus

    if not adatok_mappa.exists():
        print(f"❌ Nem található az adatmappa: {adatok_mappa}", file=sys.stderr)
        print(f"   Hozd létre és helyezd el a Classroom CSV-ket:", file=sys.stderr)
        print(f"   {adatok_mappa}/classroom/", file=sys.stderr)
        sys.exit(1)

    eredmenyek = kotegelt_feldolgozas(args.kurzus, adatok_mappa)

    if args.tanulo:
        if args.tanulo not in eredmenyek:
            print(f"❌ Nem található tanuló: {args.tanulo}", file=sys.stderr)
            print(f"   Elérhető tanulók:", file=sys.stderr)
            for nev in sorted(eredmenyek.keys()):
                print(f"     - {nev}", file=sys.stderr)
            sys.exit(1)
        print_reszletes(args.tanulo, eredmenyek[args.tanulo])
    else:
        print_tablazat(args.kurzus, eredmenyek)

    if args.kimenet:
        kimenet_csv(eredmenyek, args.kimenet)


if __name__ == "__main__":
    main()
