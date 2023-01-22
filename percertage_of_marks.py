phy=int(input("enter the mark"))
chem=int(input("enter the mark"))
bio=int(input("enter the mark"))
math=int(input("enter the mark"))
comp=int(input("enter the mark"))
total=phy+chem+bio+math+comp
percentage=(total/500)*100
print(percentage)
if percentage>=90:
    print("grade a")
elif percentage>=80:
    print("grade b")
elif percentage>=70:
    print("grade c")
elif percentage>=60:
    print("grade d")
elif percentage>=40:
    print("grade e")
elif percentage<=40:
    print("grade")