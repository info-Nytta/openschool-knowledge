def ido_formatum(perc: int) -> str:
    if perc < 60:
        return f"{perc} perc"
    orak = perc // 60
    maradek = perc % 60
    if maradek == 0:
        return f"{orak} óra"
    return f"{orak} óra {maradek} perc"


def kaloria_kategoria(kaloria: int) -> str:
    if kaloria <= 200:
        return "könnyű"
    elif kaloria <= 500:
        return "közepes"
    else:
        return "kalóriadús"


def szuro_kategoria(receptek: list[dict], kategoria: str) -> list[dict]:
    return [r for r in receptek if r["kategoria"] == kategoria]


def statisztika(receptek: list[dict]) -> dict:
    osszes = len(receptek)
    kedvenc = sum(1 for r in receptek if r["kedvenc"])
    atlag_ido = round(sum(r["elkeszitesi_ido"] for r in receptek) / osszes, 1) if osszes else 0.0
    atlag_kal = round(sum(r["kaloria"] for r in receptek) / osszes, 1) if osszes else 0.0
    return {
        "osszes": osszes,
        "kedvenc": kedvenc,
        "atlag_ido": atlag_ido,
        "atlag_kaloria": atlag_kal,
    }
