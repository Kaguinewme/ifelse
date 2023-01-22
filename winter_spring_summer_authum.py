month=input("enter the month")
days=int(input("enter the days"))
if month=="jan" or month=="feb" or month=="march" and days<=31:
    print("winter")
elif month=="april" or month=="may" or month=="june" and days<=31:
    print("spring")
elif month=="july" or month=="aug" or month=="sept" and days<=31:
    print("summer")
elif month=="oct" or month=="nov" or month=="dec" and days<=30:
    print("autum")
else:
    print("error")