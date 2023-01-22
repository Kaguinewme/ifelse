expd_date=int(input("enter the expd_date"))
expd_month=int(input("enter the expd_month"))
expd_year=int(input("enter the expd_year"))
return_date=int(input("enter the return_date"))
return_month=int(input("enter the return_month"))
return_year=int(input("enter the return_year"))
if expd_year==return_year:
    if return_month==expd_month:
        if return_date<=expd_date:
            print("no fine")
        else:
            print("fine is",(return_date-expd_date)*15)
    else:
        print("fine is",(return_month-expd_month)*500)
else:
    print("fine is",(return_year-expd_year)*1000)