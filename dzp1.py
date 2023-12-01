niz = []
while 1:
    print(
        "Meni:\n1. stvaranje matrice zadatih dimenzija uz inicijalizaciju nepodrazumevanim vrednostima\n2. postavljanje podrazumevane vrednosti\n"
        "3. dohvatanje zadatog elementa, uz proveru validnosti opsega\n4. postavljanje vrednosti zadatom elementu, uz proveru validnosti opsega\n"
        "5. dohvatanje broja nepodrazumevanih elemenata\n6. ispis matrice (uključujući i elemente podrazumevane vrednosti)\n"
        "7. računanje ostvarene uštede memorijskog prostora\n8. brisanje matrice\n0. prekid programa")
    s = int(input("Odaberite opciju iz menija "))
    if s == 1:
        m = int(input("Unesite dimenzije matrice "))
        duzina = int((m * (m + 1)) / 2)
        print("Unesite nepodrazumevane vrednosti matrice")
        for i in range(duzina):
            niz.append(int(input()))
        print("Matrica je uneta")
    elif s == 2:
        print("Nema podrazumevane vrednosti")
    elif s == 3:
        try:
            print("Unesite poziciju trazenog elementa ")
            i = int(input())
            j = int(input())
            if i > m or j > m or i < 1 or j < 1:
                print("Nevalidan opseg")
                continue
            if i + j > m + 1:
                p = m + 1 - j
                j = m + 1 - i
                i = p
            pomeraj = int((j-1)*m - ((j-1)*(j-2))/2 + i-1)
            print("Trazeni element je", niz[pomeraj])
        except NameError:
            print("Matrica ne postoji!")
    elif s == 4:
        try:
            print("Unesite poziciju trazenog elementa ")
            i = int(input())
            j = int(input())
            if i > m or j > m or i < 1 or j < 1:
                print("Nevalidan opseg")
                continue
            vrednost = int(input("Unesite vrednost elementa "))
            if i + j > m + 1:
                p = m + 1 - j
                j = m + 1 - i
                i = p
            pomeraj = int((j-1)*m - ((j-1)*(j-2))/2 + i-1)
            niz[pomeraj] = vrednost
            print("Vrednost je promenjena")
        except NameError:
            print("Matrica ne postoji!")
    elif s == 5:
        print("Broj nepodrazumevanih clanova je", len(niz))
    elif s == 6:
        try:
            for i in range(1, m+1):
                for j in range(1, m+1):
                    if i + j > m + 1:
                        p = m + 1 - j
                        j1 = m + 1 - i
                        i1 = p
                        pomeraj = int((j1-1)*m - ((j1-1)*(j1-2))/2 + i1-1)
                        print(niz[pomeraj], end=' ')
                    else:
                        pomeraj = int((j-1)*m - ((j-1)*(j-2))/2 + i-1)
                        print(niz[pomeraj], end = ' ')
                print("")
        except NameError:
            print("Matrica ne postoji!")
    elif s == 7:
        try:
            usteda = (m*m - duzina) / (m*m) * 100
            print("Ostvarene uštede memorijskog prostora je", usteda, "%")
        except NameError:
            print("Matrica ne postoji!")
    elif s == 8:
        try:
            del niz[0:duzina]
            del m
            del duzina
            print("Matrica je obrisana")
        except NameError:
            print("Matrica ne postoji!")
    elif s == 0:
        print("Kraj")
        break
    else:
        print("Izabrana nepostojeca stavka, pokusaj opet")