def beolvasas(fajlnev):
    filmek = []
    with open(fajlnev, "r", encoding="utf-8") as f:
        for sor in f:
            adatok = sor.strip().split(";")
            film = {
                "cim": adatok[0],
                "kategoria": adatok[1],
                "ev": int(adatok[2]),
                "hossz": int(adatok[3]),
                "ertekeles": float(adatok[4])
            }
            filmek.append(film)
    return filmek


def darabszam(filmek):
    return len(filmek)


def kategoriak_szama(filmek):
    szamlalo = {}
    for film in filmek:
        kat = film["kategoria"]
        szamlalo[kat] = szamlalo.get(kat, 0) + 1
    return szamlalo


def legjobb_legrosszabb(filmek):
    legjobb = filmek[0]
    legrosszabb = filmek[0]
    for film in filmek:
        if film["ertekeles"] > legjobb["ertekeles"]:
            legjobb = film
        if film["ertekeles"] < legrosszabb["ertekeles"]:
            legrosszabb = film
    return legjobb, legrosszabb


def film_keresese(filmek, cim):
    for film in filmek:
        if film["cim"] == cim:
            return film
    return None


def film_fajlba_iras(film, fajlnev):
    with open(fajlnev, "w", encoding="utf-8") as f:
        sor = f"{film['cim']};{film['kategoria']};{film['ev']};{film['hossz']};{film['ertekeles']}"
        f.write(sor)


def kategoriahoz_tartozo_filmek(filmek, kategoria):
    talalatok = []
    for film in filmek:
        if film["kategoria"] == kategoria:
            talalatok.append((film["cim"], film["ev"]))
    return talalatok
