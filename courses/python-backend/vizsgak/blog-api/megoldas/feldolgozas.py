def beolvasas(fajlnev: str) -> list[dict]:
    posztok = []
    with open(fajlnev, "r", encoding="utf-8") as f:
        for sor in f:
            adatok = sor.strip().split(";")
            poszt = {
                "cim": adatok[0],
                "tartalom": adatok[1],
                "szerzo": adatok[2],
                "cimke": adatok[3] if adatok[3] else None,
                "publikalva": adatok[4] == "True",
            }
            posztok.append(poszt)
    return posztok


def osszes_darab(posztok: list[dict]) -> int:
    return len(posztok)


def publikus_arany(posztok: list[dict]) -> float:
    if not posztok:
        return 0.0
    publikus = sum(1 for p in posztok if p["publikalva"])
    return round(publikus / len(posztok) * 100, 1)


def leghosszabb_poszt(posztok: list[dict]) -> dict:
    return max(posztok, key=lambda p: len(p["tartalom"]))


def cimkek_szerint(posztok: list[dict]) -> dict:
    szamlalo = {}
    for poszt in posztok:
        cimke = poszt.get("cimke", "nincs")
        szamlalo[cimke] = szamlalo.get(cimke, 0) + 1
    return szamlalo
