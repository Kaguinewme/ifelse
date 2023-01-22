### check if a number is divisible by both 5 and 11

num=int(input("enter the number"))
if num%5==0 and num%11==0:
    print(num,"is divisible")
else:
    print(num,"is not divisible")