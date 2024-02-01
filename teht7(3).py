lentoasemat = {}

while True:
    print( "\n Valitse numero!")
    print("1. Anna uus lentoasema. " )
    print("2. Hae lentoaseman tiedot. " )
    print("3. loppu!")

    valinta = input(" \n valintasi on?  (1، 2 tai 3)?  ")

    if valinta == "1":
        ICAO_KOODI = input("lento aseman ICAO_koodi?  ")
        nimi = input("\n Lentoaseman nimi?  ")
        lentoasemat[ICAO_KOODI] = nimi
    elif valinta == "2":
        ICAO_KOODI = input("\n lentoaseman ICAO_koodi? : ")
        print("\n alentoaseman nimi  :", lentoasemat.get(ICAO_KOODI, "  ei löytynyt lentoasema."))
    elif valinta == "3":
        break
    else:
        print(" \n \n --->Virhe!<--- Syötää seuravista numeroista  (1، 2 tai 3) .")
