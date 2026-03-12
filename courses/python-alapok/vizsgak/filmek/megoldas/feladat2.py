import random


def kartyak_huzasa():
    kartyak = [random.randint(1, 13) for _ in range(3)]
    return kartyak


def tipp_bekerese():
    tipp = int(input("Tippelj, mennyi a három kártya összege: "))
    return tipp


def tipp_kiertekeles(tipp, osszeg):
    if tipp < 3 or tipp > 39:
        print("HIBA: nem lehetséges érték!")
        return False
    elif tipp < osszeg:
        print("Ennél több")
        return False
    elif tipp > osszeg:
        print("Ennél kevesebb")
        return False
    else:
        print("Talált!")
        return True


def jatek():
    kartyak = kartyak_huzasa()
    osszeg = sum(kartyak)
    tippek_szama = 0
    talalt = False

    while not talalt:
        tipp = tipp_bekerese()
        tippek_szama += 1
        talalt = tipp_kiertekeles(tipp, osszeg)

    print(f"\nA húzott kártyák: {kartyak}")
    print(f"A tippek száma: {tippek_szama}")
    print("Köszönjük a játékot!")


jatek()
