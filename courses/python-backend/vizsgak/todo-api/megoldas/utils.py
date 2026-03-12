from datetime import date


def prioritas_szoveg(prioritas: int) -> str:
    nevek = {1: "alacsony", 2: "normál", 3: "közepes", 4: "magas", 5: "sürgős"}
    return nevek.get(prioritas, "ismeretlen")


def hatarido_lejart(hatarido: str) -> bool:
    datum = date.fromisoformat(hatarido)
    return datum < date.today()


def szuro_prioritas(todok: list[dict], min_prioritas: int) -> list[dict]:
    return [t for t in todok if t["prioritas"] >= min_prioritas]


def statisztika(todok: list[dict]) -> dict:
    osszes = len(todok)
    kesz = sum(1 for t in todok if t["kesz"])
    return {"osszes": osszes, "kesz": kesz, "hatra_van": osszes - kesz}
