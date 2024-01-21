
kuhan_pituus = float(input("Kuinka pitkä kuhasi on senttimetreinä? "))


alamittainen_raja = 37
if kuhan_pituus < alamittainen_raja:
    puuttuva_pituus = alamittainen_raja - kuhan_pituus
    print(f"Voi ei! Kuhasi on liian pieni. Laske se takaisin veteen. Tarvitset vielä {puuttuva_pituus} cm.")
else:
    print("Hienoa! Kuhasi on tarpeeksi iso. Voit pitää sen.")

