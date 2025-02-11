#kk = input("Mikä kuukausi numerona? "[1-12]:)

kuukaudet = ("Tammikuu", "Helmikuu", "Maaliskuu", "Huhtikuu", "Toukokuu", "Kesäkuu", "Heinäkuu", "Elokuu", "Syyskuu", "Lokakuu", "Marraskuu", "Joulukuu")
vuodenajat = ("Talvi", "Kevät", "Kesä", "Syksy")

kuukausinr = int(input("Mikä kuukausi numerona?(1-12): "))
kk = kuukaudet[kuukausinr-1]

print (f"{kuukausinr}. kuukausi on {kk}.")

def vuodenaika(kk):
    if kk in kuukaudet[2:5]:
        print(f"Vuodenaika on: {vuodenajat[1]}")
    elif kk in kuukaudet[5:8]:
        print(f"Vuodenaika on: {vuodenajat[2]}")
    elif kk in kuukaudet[8:11]:
        print(f"Vuodenaika on: {vuodenajat[3]}")
    else:
        print(f"Vuodenaika on: {vuodenajat[0]}")

    return
vuodenaika(kk)
