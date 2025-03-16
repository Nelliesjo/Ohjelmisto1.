import mysql.connector

yhteys = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='peli',
         user='root',
         password='tuut',
         autocommit=True
         )

def lentokenttä(maakoodi):
    sql = f"SELECT type,count(*) FROM airport WHERE iso_country ='{maakoodi}' group by type desc"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    result = kursori.fetchall()
    if kursori.rowcount >0 :
        print(f"Maan lentokentät: ")
        for rivi in result:
            print(rivi)

    else:
        print("Ei löydy.")
    return

lentokenttä_koodi = input("Please enter the country code of the country: ").upper()
lentokenttä(lentokenttä_koodi)