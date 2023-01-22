mark=int(input("enter the mark"))
if mark<25:
    print("fail")
elif mark>=25 and mark<45:
    print("grade e")
elif mark>=45 and mark<50:
    print("grade d")
elif mark>=50 and mark<60:
    print("grade c")
elif mark>=60 and mark<80:
    print("grade b")
else:
    print("grade a")