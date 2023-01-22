### check if a year is leap year or not

year=int(input("enter the year"))
if year%400==0 or year%100==0 or year%4==0:
    print("leap year")
else:
    print("not leap year")