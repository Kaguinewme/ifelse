days=int(input("enter the days"))
charge=int(input("enter the charge"))
if days<=5 and charge==2:
    print(days*charge)
elif days>=6 and days<=10 and charge==3:
    print(days*charge)
elif days>10 and days<=15 and charge==4:
    print(days*charge)
elif days>15 and charge==5:
    print(days*charge)
else:
    print("error")