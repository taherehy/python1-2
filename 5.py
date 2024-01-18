leiviskat = float(input("Anna leiviskät? "))
naulat = float(input("Anna naulat? "))
luodit = float(input("Anna luodit? "))

paino_kg = (leiviskat*20*32*13.3/1000) + (naulat*32*13.3/1000) + (luodit*13.3/1000)
paino_g = paino_kg * 1000

print("Massa nykymittojen mukaan:")
print(int(paino_kg), "kilogrammaa ja", round(paino_g % 1000, 2), "grammaa.")
