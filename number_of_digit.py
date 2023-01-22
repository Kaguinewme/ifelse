num=int(input('enter the number'))
if num>=0 and num<=9:
    print("one digit")
elif num>=10 and num<=99:
    print("two digit")
elif num>=100 and num<=999:
    print("three digit")
else:
    print("more than three digit")