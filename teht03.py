
sukupuoli = input("Oletko nainen vai mies? ")
hemoglobiiniarvo = float(input("Kerro hemoglobiiniarvosi (g/l): "))


if sukupuoli == "nainen" and 117 <= hemoglobiiniarvo <= 175:
    print("Hemoglobiiniarvosi on normaali.")
elif sukupuoli == "mies" and 134 <= hemoglobiiniarvo <= 195:
    print("Hemoglobiiniarvosi on normaali.")
else:
    print("Hemoglobiiniarvosi ei ole normaalialueella.")

