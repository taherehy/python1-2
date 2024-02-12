from geopy.distance import geodesic
import mysql.connector

def hae_koordinaatit(icao_koodi):
    # Yhdistetään tietokantaan ja haetaan koordinaatit
    connection = mysql.connector.connect(
        host="localhost",
        user="kayttajanimi",
        password="salasana",
        database="lentokentat"
    )
    cursor = connection.cursor()

    # Haetaan lentokentän koordinaatit
    cursor.execute("SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s", (icao_koodi,))
    koordinaatit = cursor.fetchone()

    # Suljetaan tietokantayhteys
    connection.close()

    return koordinaatit

def laske_etaisyys(koordinaatit1, koordinaatit2):
    # Muodostetaan koordinaateista tuples
    koordinaatti1 = (koordinaatit1[0], koordinaatit1[1])
    koordinaatti2 = (koordinaatit2[0], koordinaatit2[1])

    # Lasketaan etäisyys geodesic-luokan avulla
    etaisyys = geodesic(koordinaatti1, koordinaatti2).kilometers
    return etaisyys

def main():
    # Kysytään käyttäjältä kahden lentokentän ICAO-koodit
    icao_koodi1 = input("Anna ensimmäisen lentokentän ICAO-koodi: ").strip().upper()
    icao_koodi2 = input("Anna toisen lentokentän ICAO-koodi: ").strip().upper()

    # Haetaan koordinaatit kummallekin lentokentälle
    koordinaatit1 = hae_koordinaatit(icao_koodi1)
    koordinaatit2 = hae_koordinaatit(icao_koodi2)

    # Lasketaan etäisyys
    if koordinaatit1 and koordinaatit2:
        etaisyys = laske_etaisyys(koordinaatit1, koordinaatit2)
        print(f"Lentokenttien välinen etäisyys: {etaisyys:.2f} kilometriä")
    else:
        print("Jokin meni pieleen. Tarkista, että annetut ICAO-koodit ovat oikein.")

if __name__ == "__main__":
    main()
