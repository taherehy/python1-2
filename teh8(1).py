import mysql.connector

def hae_lentokentta_tiedot(icao_koodi):
    # Yhdistetään tietokantaan
    connection = mysql.connector.connect(
        host="localhost",
        user="kayttajanimi",
        password="salasana",
        database="lentokentat"
    )
    cursor = connection.cursor()

    # Haetaan lentokentän tiedot annetulla ICAO-koodilla
    cursor.execute("SELECT name, municipality FROM airport WHERE ident = %s", (icao_koodi,))
    lentokentta_tiedot = cursor.fetchone()

    # Suljetaan tietokantayhteys
    connection.close()

    return lentokentta_tiedot

def main():
    # Kysytään käyttäjältä lentokentän ICAO-koodi
    icao_koodi = input("Anna lentokentän ICAO-koodi: ").strip().upper()

    # Haetaan lentokentän tiedot tietokannasta
    lentokentta_tiedot = hae_lentokentta_tiedot(icao_koodi)

    # Tulostetaan lentokentän tiedot, jos ne löytyvät
    if lentokentta_tiedot:
        nimi, sijaintikunta = lentokentta_tiedot
        print(f"Lentokenttä: {nimi}")
        print(f"Sijaintikunta: {sijaintikunta}")
    else:
        print("Lentokenttää ei löytynyt annetulla ICAO-koodilla.")

if __name__ == "__main__":
    main()
