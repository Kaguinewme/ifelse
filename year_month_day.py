 (5 sloc)  193 Bytes

year=int(input("enter the year"))
month=int(input("enter the month"))
day=int(input("enter the day"))
if year>=0 and month>=1 and month<=12 and day>=1 and day<=31:
    print(year, month, day+1)