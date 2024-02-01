nimet = [] # ایجاد یک لیست خالی برای ذخیره نام‌ه

#حلقه بی‌نهایت
while True:         # دریافت نام از کاربر

    nimi = input("Syötä nimi (tyhjä rivi lopettaa): ")

## بررسی اینکه آیا ورودی خالی است یا نه
    if not nimi:
        # اگر ورودی خالی بود، حلقه را خاتمه بده
        break


    if nimi in nimet:
        print("Aiemmin syötetty nimi") ## Jos nimi on jo listassa, tulostetaan viesti
    else:
        print("Uusi nimi")
        nimet.append(nimi)  # Lisätään nimi listalle

# Tulostetaan syötetyt nimet
print("\nSyötetyt nimet:")
for nimi in nimet: # Käydään läpi kaikki listassa olevat nimet
    print(nimi)
