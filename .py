a=int(input("enter the age"))
b=int(input("enter the age"))
c=int(input("enter the age"))
if a>b and b>c:
    print(a,"is young",b,"is younger",c,"is youngest")
elif b>c and c>a:
    print(b,"is young",c,"is younger",a,"is youngest")
elif c>a and a>b:
    print(c,"is young",a,"is younger",b,"is youngest")
elif b>c and a>c:
    print(b,"is young",a,"is younger",c,"is youngest")
elif c>a and b>a:
    print(c,"is young",b,"is younger",a,"is youngest")
elif a>b and c>b:
    print(a,"is young",c,"is younger",b,"is youngest")
else:
    print("invalid")