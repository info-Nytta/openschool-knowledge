def bekerés():
    vezeteknev = input("Add meg a vezetékneved: ")
    keresztnev = input("Add meg a keresztneved: ")
    szuletesi_ev = input("Add meg a születési éved: ")
    return vezeteknev, keresztnev, szuletesi_ev


def emailek_osszeallitasa(vezeteknev, keresztnev, szuletesi_ev):
    vezeteknev = vezeteknev.lower()
    keresztnev = keresztnev.lower()
    email1 = keresztnev + vezeteknev[0] + "@mail.com"
    email2 = keresztnev[0] + vezeteknev + szuletesi_ev + "@mail.com"
    email3 = keresztnev + "." + vezeteknev + "@mail.com"
    return email1, email2, email3


def megjelenites(email1, email2, email3):
    print(f"1. email cím: {email1}")
    print(f"2. email cím: {email2}")
    print(f"3. email cím: {email3}")


def main():
    vezeteknev, keresztnev, szuletesi_ev = bekerés()
    email1, email2, email3 = emailek_osszeallitasa(vezeteknev, keresztnev, szuletesi_ev)
    megjelenites(email1, email2, email3)


main()
