
hyttiluokka = input("Minkälaista hyttiä haluaisit (LUX, A, B, C)? ")

if hyttiluokka == "LUX":
    print("LUX on yläkannella ja siinä on parveke.")
elif hyttiluokka == "A":
    print("A on yläkannella ja siinä on ikkuna.")
elif hyttiluokka == "B":
    print("B on yläkannella ja siinä ei ole ikkunaa.")
elif hyttiluokka == "C":
    print("C on alakannella ja siinä ei ole ikkunaa.")
else:
    print("Anteeksi, en ymmärtänyt. Yritä uudelleen.")

