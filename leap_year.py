year=int(input("enter the year"))
if year%4==0:
    print("leap year")
    if year%400==0:
        print("leap year")
        if year%100==0:
            print("leap year")
        elif year%4!=0 or year%400!=0 or year%100!=0:
            print("not_leap year")
    elif year%4==0 or year%100==0:
        print("leap year")
else:
    print("not leap year")