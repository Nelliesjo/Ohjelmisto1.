'''
Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus,
Liian pieni arvaus tai Oikein. Huomaa, että tietokone ei saa vaihtaa
lukuaan arvauskertojen välissä.
'''

import random

arvottuluku = random.randint(1,10)

print(arvottuluku)

arvaus=int(input("Mikä luku 1-10 väliltä?"))
while arvaus != arvottuluku:
    if arvaus < arvottuluku:
        print("Liian pieni luku.")
    if arvaus > arvottuluku:
        print("Liian suuri luku.")
    arvaus=int(input("Mikä luku 1-10 väliltä?"))

print("Onneksi olkoon!")


#int=kokonaisluku
#float= desimaaliluku