def beolvasas(fajlnev: str) -> list[dict]:
    termekek = []
    with open(fajlnev, "r", encoding="utf-8") as f:
        for sor in f:
            adatok = sor.strip().split(";")
            termek = {
                "nev": adatok[0],
                "leiras": adatok[1],
                "ar": int(adatok[2]),
                "kategoria": adatok[3],
                "keszlet": int(adatok[4]),
                "aktiv": adatok[5] == "True",
            }
            termekek.append(termek)
    return termekek


def osszes_darab(termekek: list[dict]) -> int:
    return len(termekek)


def atlag_ar(termekek: list[dict]) -> float:
    if not termekek:
        return 0.0
    arak = [t["ar"] for t in termekek]
    return round(sum(arak) / len(arak), 1)


def legdragabb(termekek: list[dict]) -> dict:
    return max(termekek, key=lambda t: t["ar"])


def kategoriak_szerint(termekek: list[dict]) -> dict:
    szamlalo = {}
    for termek in termekek:
        kat = termek["kategoria"]
        szamlalo[kat] = szamlalo.get(kat, 0) + 1
    return szamlalo
