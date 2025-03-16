import mysql.connector

yhteys = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='peli',
         user='root',
         password='tuut',
         autocommit=True
         )

def lentokenttä(icao):
    sql = f"SELECT name FROM airport WHERE ident='{icao}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    result = kursori.fetchall()
    if kursori.rowcount >0 :
        for rivi in result:
            print(f"Valitsemasi lentokenttä: {rivi[0]} ")
    else:
        print("Ei löydy.")
    return

icao_koodi = input("Syötä ICAO-koodi: ")
lentokenttä(icao_koodi)