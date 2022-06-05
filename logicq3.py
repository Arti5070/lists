date=int(input("enter the date"))
month=int(input("enter the month"))
year=int(input("enter the year"))
if date>=1 and date<30:
    print(date+1,month,year)
if month==1 and month==3 and month==5 and month==7 and month==8 and month==10 and month==12 and date==31:
    print("1",month+1,year)
if month==4 and month==6 and month==9 and month==11 and date==30:
    print("1",month+1,year)
if month==2 and date==28:
    print("1",month+1,year)
if month==12 and date==31:
    print("1","1",year+1)
