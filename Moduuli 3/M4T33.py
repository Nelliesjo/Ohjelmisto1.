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


print(f"suurin luku: {suurin}, pienin luku: {pienin}")


#etsii aina pienimmän luvun uudestaan vertailemalla eka pienin=luku

import math

luku = str(input("Ensimmäinen luku, tyhjä lopettaa:"))

pienin = math.inf
suurin = -math.inf

while luku!= "":
    luku = float(luku)
    #floatin sijalle int nii ei desimaaliluku, kaikki "str" voi ottaa pois
    print(f"Luku: {luku} ")
    if luku < pienin:
        pienin = luku
    if luku > suurin:
        suurin = luku

    luku = str(input("Seuraava luku, tyhjä lopettaa:"))

print(f"suurin luku: {suurin}, pienin luku: {pienin}")


#int=kokonaisluku
#float= desimaaliluku



luku = 1
#yhteensä tai pienempi kuin 30, ei listaa siitä pidemnmälle.
while luku <= 30:
    #onko luku jaollinen kolmella?
    if luku % 3 == 0:
        print(luku)
    luku = luku + 1  # # luku += 1 :sama asia kuin: luku = luku+1

print("done")