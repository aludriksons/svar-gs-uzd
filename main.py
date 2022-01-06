import rekins

termins=int(input("ievadi līguma termiņu: "))
rad1=float(input("ievadi iepriekšējo rādijumu: "))
rad2=float(input("ievadi esošo rādijumu: "))

print(f"jāmaksā ir {rekins.cena(termins,rad1,rad2)[0]}")
print(f"iztērētie kWh ir {rekins.cena(termins,rad1,rad2)[1]}")
