a=input("enter the string:-")
if len(a)>=3:
    if "ing" not in a:
        print(a+"ing")
    elif "ing" in a:
        print(a+"ly")
    else:
        print("error")
else:
    print(a)