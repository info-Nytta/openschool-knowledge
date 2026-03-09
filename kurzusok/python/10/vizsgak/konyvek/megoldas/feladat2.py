import random


def kockadobas():
    dobasok = [random.randint(1, 6) for _ in range(3)]
    return dobasok


def tipp_bekerese():
    tipp = int(input("Tippelj, mennyi a három kocka összege: "))
    return tipp


def tipp_kiertekeles(tipp, osszeg):
    if tipp < 3 or tipp > 18:
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
    dobasok = kockadobas()
    osszeg = sum(dobasok)
    tippek_szama = 0
    talalt = False

    while not talalt:
        tipp = tipp_bekerese()
        tippek_szama += 1
        talalt = tipp_kiertekeles(tipp, osszeg)

    print(f"\nA dobások: {dobasok}")
    print(f"A tippek száma: {tippek_szama}")
    print("Köszönjük a játékot!")


jatek()
