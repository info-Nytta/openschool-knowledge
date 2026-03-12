import fgv

filmek = fgv.beolvasas("filmek.txt")

# 2. Hány film van
print(f"A listában {fgv.darabszam(filmek)} film található.")

# 3. Kategóriák szerinti darabszám
szamlalo = fgv.kategoriak_szama(filmek)
for kat, db in szamlalo.items():
    print(f"{kat}: {db} db")

# 4. Legjobb és legrosszabb értékelésű film
legjobb, legrosszabb = fgv.legjobb_legrosszabb(filmek)
print(f"Legjobb értékelésű: {legjobb['cim']} ({legjobb['ertekeles']})")
print(f"Legrosszabb értékelésű: {legrosszabb['cim']} ({legrosszabb['ertekeles']})")

# 5. Film keresése és fájlba írás
cim = input("Add meg egy film címét: ")
film = fgv.film_keresese(filmek, cim)
if film:
    fgv.film_fajlba_iras(film, "valasztott_film.txt")
    print("A film adatai kiírva a valasztott_film.txt fájlba.")
else:
    print("Nincs ilyen cím a listában")

# 6. Kategória szerinti szűrés
kategoria = input("Add meg a kategória nevét: ")
talalatok = fgv.kategoriahoz_tartozo_filmek(filmek, kategoria)
for cim, ev in talalatok:
    print(f"{cim} ({ev})")
