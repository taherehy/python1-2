# از کاربر دریافت شماره ماه
kuukausi = int(input("Anna kuuksuden numero (1-12): "))

# بررسی شرایط برای تعیین فصل
if kuukausi == 12 or kuukausi <= 2:
    print("on talvi.")
elif 3 <= kuukausi <= 5:
    print("on kevät.")
elif 6 <= kuukausi <= 8:
    print("on kesä.")
elif 9 <= kuukausi <= 11:
    print("on syksy.")
else:
    print("error kuukausi ei löytyy.")
