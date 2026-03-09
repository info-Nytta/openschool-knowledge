def beolvasas(fajlnev):
    konyvek = []
    with open(fajlnev, "r", encoding="utf-8") as f:
        for sor in f:
            adatok = sor.strip().split(";")
            konyv = {
                "cim": adatok[0],
                "nyelv": adatok[1],
                "mufaj": adatok[2],
                "ev": int(adatok[3]),
                "bevetel": int(adatok[4])
            }
            konyvek.append(konyv)
    return konyvek


def darabszam(konyvek):
    return len(konyvek)


def nyelvek_szama(konyvek):
    szamlalo = {}
    for konyv in konyvek:
        nyelv = konyv["nyelv"]
        szamlalo[nyelv] = szamlalo.get(nyelv, 0) + 1
    return szamlalo


def legtobb_legkevesebb_bevetel(konyvek):
    legtobb = konyvek[0]
    legkevesebb = konyvek[0]
    for konyv in konyvek:
        if konyv["bevetel"] > legtobb["bevetel"]:
            legtobb = konyv
        if konyv["bevetel"] < legkevesebb["bevetel"]:
            legkevesebb = konyv
    return legtobb, legkevesebb


def konyv_keresese(konyvek, cim):
    for konyv in konyvek:
        if konyv["cim"] == cim:
            return konyv
    return None


def konyv_fajlba_iras(konyv, fajlnev):
    with open(fajlnev, "w", encoding="utf-8") as f:
        sor = f"{konyv['cim']};{konyv['nyelv']};{konyv['mufaj']};{konyv['ev']};{konyv['bevetel']}"
        f.write(sor)


def mufajhoz_tartozo_konyvek(konyvek, mufaj):
    talalatok = []
    for konyv in konyvek:
        if konyv["mufaj"] == mufaj:
            talalatok.append((konyv["cim"], konyv["ev"]))
    return talalatok
