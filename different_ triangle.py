side1=int(input("enter the number"))
side2=int(input("enter the number"))
side3=int(input("enter the number"))
if side1==side2 and side2==side3:
    print("equilateral")
elif side1==side2 and side2!=side3:
    print("isosceles")
else:
    print("scalene")