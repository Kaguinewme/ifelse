age=int(input("enter the age:"))
sex=input("enter the sex")
marital_status=input("enter the marital_status:")
if sex=="female":
    print("she can work in urban areas:")
elif sex=="male":
    if age>=20 and age<40:
        if marital_status=="yes" or "no":
            print("can work anywhere")
        else:
            print("error")
    elif sex=="male":
        if age>=40 and age<60:
            if marital_status=="yes" or "no":
                print("he can work in urban areas")
            else:
                print("error")
        else:
            print("error")
    else:
        print("error")
else:
    print("error")