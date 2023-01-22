month=int(input("enter the number"))
if month==2:
    print("28/29")
elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    print("31")
else:
    print("30")