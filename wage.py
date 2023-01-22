age=int(input("enter the age"))
sex=input("enter the sex")
days=int(input("enter the days"))
wage=int(input("enter the wage"))
if age>=18 and age<30 and sex=="male" and "female":
    print(wage*days)
elif age>=30 and age<=40 and sex=="female" and "male":
    print(wage*days)
else:
    print("enter the appropriate age")