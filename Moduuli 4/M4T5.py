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