luvut =[]

luku = input("Anna luku, tyjhä lopettaa:")
while luku != "":
    luku = int(luku)
    luvut.append(luku)
    luku = input("Anna luku, tyhjä lopettaa:")

luvut.sort(reverse=True)
print(luvut [0:5])