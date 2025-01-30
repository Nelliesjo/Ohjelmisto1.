import random

arpakuutiot = int(input("Kuinka monta arpakuutiota on?"))

summa = 0
for i in range(arpakuutiot):
    heitto = (random.randint(1, 6))
    summa = summa + heitto

    print(heitto)


print (f"luvut lisättynä: {summa}")



