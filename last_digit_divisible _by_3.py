num=int(input("enter the number"))
last_digit=num%10
if last_digit%3==0:
    print("divisible by 3")
else:
    print("not divisible")