def ar_formatum(ar: int) -> str:
    return f"{ar:,} Ft".replace(",", " ")


def keszleten_van(termek: dict) -> bool:
    return termek["keszlet"] > 0


def szuro_kategoria(termekek: list[dict], kategoria: str) -> list[dict]:
    return [t for t in termekek if t["kategoria"] == kategoria]


def statisztika(termekek: list[dict]) -> dict:
    osszes = len(termekek)
    keszleten = sum(1 for t in termekek if t["keszlet"] > 0)
    arak = [t["ar"] for t in termekek]
    atlag = round(sum(arak) / len(arak), 1) if arak else 0.0
    return {
        "osszes": osszes,
        "keszleten": keszleten,
        "kifogyott": osszes - keszleten,
        "atlag_ar": atlag,
    }
