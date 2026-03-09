def beolvasas(fajlnev: str) -> list[dict]:
    receptek = []
    with open(fajlnev, "r", encoding="utf-8") as f:
        for sor in f:
            adatok = sor.strip().split(";")
            recept = {
                "nev": adatok[0],
                "leiras": adatok[1],
                "kategoria": adatok[2],
                "elkeszitesi_ido": int(adatok[3]),
                "kaloria": int(adatok[4]),
                "kedvenc": adatok[5] == "True",
            }
            receptek.append(recept)
    return receptek


def osszes_darab(receptek: list[dict]) -> int:
    return len(receptek)


def atlag_kaloria(receptek: list[dict]) -> float:
    if not receptek:
        return 0.0
    kalorik = [r["kaloria"] for r in receptek]
    return round(sum(kalorik) / len(kalorik), 1)


def leggyorsabb(receptek: list[dict]) -> dict:
    return min(receptek, key=lambda r: r["elkeszitesi_ido"])


def kategoriak_szerint(receptek: list[dict]) -> dict:
    szamlalo = {}
    for recept in receptek:
        kat = recept["kategoria"]
        szamlalo[kat] = szamlalo.get(kat, 0) + 1
    return szamlalo
