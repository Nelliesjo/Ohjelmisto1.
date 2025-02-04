def bensiini(gal):
    return gal * 3.785

def paakoodi():
    gal = int(input("Paljon bensiiniä galloonissa?"))
    while gal >= 0:
        gallonat = bensiini(gal)
        print(f"Yhteensä {gallonat} litraa")
        gal = int(input("Paljon bensiiniä galloonissa?"))
paakoodi()
