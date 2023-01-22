quantity=int(input("enter quantity"))
price=int(input("enter price"))
total_amount=quantity*price
if total_amount>1000:
    print(total_amount-(total_amount/10))
elif total_amount<=1000:
    print(total_amount)
else:
    print("error")