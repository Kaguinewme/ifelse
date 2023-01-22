unit=int(input("enter the unit"))
if unit<=100:
    print("no charge")
elif unit>100 and unit<200:
    print(unit*5)
elif unit>200:
    print(unit*10)