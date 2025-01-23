import random

n = 0
toistot = 0
N = int(input("Monta pistettä neliön sisällä?"))

while N >= toistot:
    x=random.uniform(-1,1)
    y=random.uniform(-1,1)
    if x**2+y**2 < 1:
        n = n+1
    toistot = toistot +1

tulos= 4*n/N

print("Saatu piin arvo on:" + str(tulos))