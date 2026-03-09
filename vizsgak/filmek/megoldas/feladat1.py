def bekeres():
    vezeteknev = input("Add meg a vezetékneved: ")
    keresztnev = input("Add meg a keresztneved: ")
    kedvenc_szam = input("Add meg a kedvenc számod: ")
    return vezeteknev, keresztnev, kedvenc_szam


def nevek_osszeallitasa(vezeteknev, keresztnev, kedvenc_szam):
    vezeteknev = vezeteknev.lower()
    keresztnev = keresztnev.lower()
    nev1 = keresztnev + vezeteknev[0] + kedvenc_szam
    nev2 = keresztnev[0] + "_" + vezeteknev + kedvenc_szam
    nev3 = vezeteknev + "." + keresztnev + kedvenc_szam
    return nev1, nev2, nev3


def megjelenites(nev1, nev2, nev3):
    print(f"1. felhasználónév: {nev1}")
    print(f"2. felhasználónév: {nev2}")
    print(f"3. felhasználónév: {nev3}")


def main():
    vezeteknev, keresztnev, kedvenc_szam = bekeres()
    nev1, nev2, nev3 = nevek_osszeallitasa(vezeteknev, keresztnev, kedvenc_szam)
    megjelenites(nev1, nev2, nev3)


main()
