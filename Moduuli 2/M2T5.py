luoti = 13.3
naula = luoti * 32
leiviska = naula * 20

luodit_str = float(input("Anna luodit: "))
naulat_str = float(input("Anna naulat: "))
leiviskat_str = float(input("Anna leiviskat: "))

massa_g = (luodit_str * luoti) + (naulat_str * naula) + (leiviskat_str * leiviska)


mKG = int(massa_g/1000)
mG = int(massa_g%1000)


print(f"Massa nykymittojen mukaan on: {mKG}kg ja {mG}g")
