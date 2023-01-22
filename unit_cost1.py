unit=int(input("enter the number"))
if unit<50:
    print(unit*0.50)
elif unit>50 and unit<=150:
    print(unit*0.75)
elif unit>150 and unit<=250:
    print(unit*1.20)
elif unit>250:
    print(unit*1.50)
else:
    print("invalid")