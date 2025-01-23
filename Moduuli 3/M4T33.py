import math

luku_str = input("Ensimmäinen luku, tyhjä lopettaa:")

pienin = math.inf
suurin = -math.inf

while luku_str != "":
    luku = float(luku_str)
    print(f"Luku: {luku} ")
    if luku < pienin:
        pienin = luku
    if luku > suurin:
        suurin = luku

    luku_str = (input("Seuraava luku, tyhjä lopettaa:"))




print(f"{suurin}, {pienin}")
