nimi = "Matti"
print("moi " + nimi + ", mitä kuuluu?")
print(f"Moi {nimi}, kuinkas nyt menee?")

#käyttäjän syötteen lukeminen
#Huom:input lukee kaikki syötteet
#aina merkkijonoina
lukuA_str = input("Anna kokonaisluku: ")
#muunnetaan merkkijono kokonaisluvuksi
lukuA =int(lukuA_str)
#luen käyttäjän syötteen lukuna
#Huom :
lukuB = int(input("Anna toinen luku: "))
summa = lukuA + lukuB
print(f"Lukujesi summa = {summa}")

