vuosiluku = int(input("Mikä vuosi sinua kiinnostaa? "))

if (vuosiluku % 4 == 0 and vuosiluku % 100 != 0) or (vuosiluku % 400 == 0):
    print(f"Vuosi {vuosiluku} on karkausvuosi.")
else:
    print(f"Vuosi {vuosiluku} ei ole karkausvuosi.")
