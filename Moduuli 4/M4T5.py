'''Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen
 ja salasanan. Jos jompikumpi tai molemmat ovat väärin, tunnus
  ja salasana kysytään uudelleen. Tätä jatketaan kunnes kirjautumistiedot
   ovat oikein tai väärät tiedot on syötetty viisi kertaa. Edellisessä
   tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
   (Oikea käyttäjätunnus on python ja salasana rules).'''

kirjautumiskerrat = 0

kt = input("Kirjoita käyttäjätunnus: ")
ss = input("Kirjoita salasana: ")

while kt != 'python' or ss != 'rules':
    kirjautumiskerrat +=1
    if kirjautumiskerrat >= 5:
        print("Liian monta yritystä.")
        break
    print("Väärät kirjautumistiedot.")

    kt = input("Kirjoita käyttäjätunnus: ")
    ss = input("Kirjoita salasana: ")

if kt == 'python' and ss == 'rules':
    print("Tervetuloa!")


#Lyhenne kirjautumiskerrat = kirjautumiskerrat + 1 = Kirjautumiskerrat +=1