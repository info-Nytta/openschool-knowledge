import fgv

konyvek = fgv.beolvasas("konyvek.txt")

# 2. Hány könyv van
print(f"A listában {fgv.darabszam(konyvek)} könyv található.")

# 3. Nyelvek szerinti darabszám
szamlalo = fgv.nyelvek_szama(konyvek)
for nyelv, db in szamlalo.items():
    print(f"{nyelv}: {db} db")

# 4. Legnagyobb és legkisebb bevételű könyv
legtobb, legkevesebb = fgv.legtobb_legkevesebb_bevetel(konyvek)
print(f"Legnagyobb bevétel: {legtobb['cim']} ({legtobb['bevetel']} euró)")
print(f"Legkisebb bevétel: {legkevesebb['cim']} ({legkevesebb['bevetel']} euró)")

# 5. Könyv keresése és fájlba írás
cim = input("Add meg egy könyv címét: ")
konyv = fgv.konyv_keresese(konyvek, cim)
if konyv:
    fgv.konyv_fajlba_iras(konyv, "valasztott_konyv.txt")
    print("A könyv adatai kiírva a valasztott_konyv.txt fájlba.")
else:
    print("Nincs ilyen cím a listában")

# 6. Műfaj szerinti szűrés
mufaj = input("Add meg a műfaj nevét: ")
talalatok = fgv.mufajhoz_tartozo_konyvek(konyvek, mufaj)
for cim, ev in talalatok:
    print(f"{cim} ({ev})")
