num=int(input("enter the number"))
num1=int(input("enter the number"))
num2=int(input("enter the number"))
if num>num1 and num<num2 or num>num2 and num<num1:
    print(num, "is the second largest number")
elif num1>num and num1<num2 or num1>num2 and num1<num:
    print(num1,  "is the second largest number")
elif num2>num and num2<num1 or num2<num and num2>num1:
    print(num2, "is the second largest number")
else:                                                                                   
    print("error")