#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. Lopuksi
# ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä
# suurimmasta alkaen. Vihje: listan alkioiden lajittelujärjestyksen voi kääntää
# antamalla sort-metodille argumentiksi reverse=True.

luvut =[]

luku = input("Anna luku, tyjhä lopettaa:")
while luku != "":
    luku = int(luku)
    luvut.append(luku)
    luku = input("Anna luku, tyhjä lopettaa:")

luvut.sort(reverse=True)
print(luvut [0:5])

#tulos = luvut[0:6]
#print (tulos)





#while
#for