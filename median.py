a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=int(input("enter the third number"))
if a>b and a<c or a>c and a<b:
    print(a, "is the median")
elif b>a and b<c or b>c and b<a:
    print(b, "is the median")
else:
    print(c,"is the median")