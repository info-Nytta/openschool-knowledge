def szavak_szama(tartalom: str) -> int:
    return len(tartalom.split())


def rovid_kivonat(tartalom: str, max_hossz: int = 100) -> str:
    if len(tartalom) <= max_hossz:
        return tartalom
    return tartalom[:max_hossz] + "..."


def szuro_cimke(posztok: list[dict], cimke: str) -> list[dict]:
    return [p for p in posztok if p.get("cimke") == cimke]


def statisztika(posztok: list[dict]) -> dict:
    osszes = len(posztok)
    publikus = sum(1 for p in posztok if p["publikalva"])
    return {"osszes": osszes, "publikus": publikus, "piszkozat": osszes - publikus}
