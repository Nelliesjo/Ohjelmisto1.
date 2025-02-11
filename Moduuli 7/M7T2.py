nimet = set()
nimi = input("Anna nimi: ")

while nimi != "":
    if nimi in nimet:
        nimet.add(nimi)
        print("Aiemmin syötetty nimi")
    else:
        nimet.add(nimi)
        print("Uusi nimi")
    nimi = input("Anna nimi: ")

for n in nimet:
    print(n)