'''Muokkaa edellistä funktiota siten, että funktio saa
parametrinaan nopan tahkojen yhteismäärän. Muokatun funktion
avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa
kunnes saadaan nopan maksimisilmäluku, joka kysytään käyttäjältä ohjelman
suorituksen alussa.'''


import random

def noppa(tahkot):
    return (random.randint(1, tahkot))

def paakoodi():
    tahkot = int(input("Monta tahkoa nopalla on?"))
    while True:
        silmaluku = noppa(tahkot)
        print(f"silmäluku on: {silmaluku}")
        if silmaluku == tahkot:
            break

paakoodi()




