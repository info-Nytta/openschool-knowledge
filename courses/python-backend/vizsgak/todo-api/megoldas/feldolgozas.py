def beolvasas(fajlnev: str) -> list[dict]:
    todok = []
    with open(fajlnev, "r", encoding="utf-8") as f:
        for sor in f:
            adatok = sor.strip().split(";")
            todo = {
                "cim": adatok[0],
                "leiras": adatok[1],
                "prioritas": int(adatok[2]),
                "hatarido": adatok[3] if adatok[3] else None,
                "kesz": adatok[4] == "True",
            }
            todok.append(todo)
    return todok


def osszes_darab(todok: list[dict]) -> int:
    return len(todok)


def kesz_arany(todok: list[dict]) -> float:
    if not todok:
        return 0.0
    kesz = sum(1 for t in todok if t["kesz"])
    return round(kesz / len(todok) * 100, 1)


def legmagasabb_prioritas(todok: list[dict]) -> list[dict]:
    return [t for t in todok if t["prioritas"] == 5]


def kategoriak_szerint(todok: list[dict]) -> dict:
    szamlalo = {}
    for todo in todok:
        p = todo["prioritas"]
        szamlalo[p] = szamlalo.get(p, 0) + 1
    return szamlalo
