import random

arvottuluku = random.randint(1,10)

arvaus=int(input("Mikä luku 1-10 väliltä?"))
while arvaus != arvottuluku:
    if arvaus < arvottuluku:
        print("Liian pieni luku.")
    if arvaus > arvottuluku:
        print("Liian suuri luku.")
    arvaus=int(input("Mikä luku 1-10 väliltä?"))

print("Onneksi olkoon, arvasit oikean luvun!")
