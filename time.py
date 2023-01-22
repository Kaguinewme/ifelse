year=int(input("enter the year"))
month=int(input("enter the month"))
day=int(input("enter the date"))
hour=int(input("enter the hour"))
min=int(input("enter the min"))
sec=int(input("enter the sec"))
if year>=0 and month>=1 and month<=12 and day>=1 and day<=31 and hour>=0 and hour<=12 and min>=0 and min<=60 and sec>=0 and sec<=60:
    print(" ",year,month,day, "\n",hour,":",min,":",sec,":")
else:
    print("time error")