unit=int(input("enter the number"))
cost=int(input("enter the number"))
if cost>1000:
    print(unit*cost-10/cost)
else:
    print(unit*cost)