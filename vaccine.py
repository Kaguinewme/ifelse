def vaccination():
    person=int(input("enter the age"))
    if person>=18:
        print("can vaccinate")
        dose=input("enter dose")
        if dose=="first dose":
            print("can take second dose")
        elif dose=="second dose":
            print("congratulation")
        elif dose =="none":
            print("go for first dose")
    else:
        print("cannot vaccinate")
vaccination()
