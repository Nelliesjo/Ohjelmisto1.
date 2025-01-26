import math

luku = str(input("Ensimmäinen luku, tyhjä lopettaa:"))

pienin = math.inf
suurin = -math.inf

while luku!= "":
    luku = float(luku)
    print(f"Luku: {luku} ")
    if luku < pienin:
        pienin = luku
    if luku > suurin:
        suurin = luku

    luku = str(input("Seuraava luku, tyhjä lopettaa:"))

print(f"suurin luku: {suurin} & pienin luku: {pienin}")
