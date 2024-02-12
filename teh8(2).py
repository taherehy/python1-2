import mysql.connector

def hae_lentokentat_maassa(maakoodi):
    # Yhdistetään tietokantaan
    connection = mysql.connector.connect(
        host="localhost",
        user="kayttajanimi",
        password="salasana",
        database="lentokentat"
    )
    cursor = connection.cursor()

    # Haetaan lentokenttien tiedot maakoodin perusteella ja ryhmitellään tyypeittäin
    cursor.execute("""
        SELECT type, COUNT(*) 
        FROM airport 
        WHERE iso_country = %s 
        GROUP BY type
    """, (maakoodi,))
    lentokentat = cursor.fetchall()

    # Suljetaan tietokantayhteys
    connection.close()

    return lentokentat

def main():
    # Kysytään käyttäjältä maakoodi
    maakoodi = input("Anna maakoodi: ").strip().upper()

    # Haetaan maassa olevien lentokenttien lukumäärät tyypeittäin
    lentokentat = hae_lentokentat_maassa(maakoodi)

    # Tulostetaan lentokenttien lukumäärät tyypeittäin
    if lentokentat:
        print(f"Lentokenttien lukumäärät tyypeittäin maassa {maakoodi}:")
        for tyyppi, lukumaara in lentokentat:
            print(f"{tyyppi}: {lukumaara}")
    else:
        print("Lentokenttiä ei löytynyt annetulla maakoodilla.")

if __name__ == "__main__":
    main()
