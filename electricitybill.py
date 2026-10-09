print("-----Electricity bill-----")
units=int(input("Enter electricity units: "))
if units<0:
    print("Invalid units")
else:
    if units<=100:
        bill=units*1.5
    elif units<=200:
        bill=100*1.5+(units-100)*2.5
    elif units<=300:
        bill=100*1.5+100*2.5+(units-200)*4
    else:
        bill=100*1.5+100*2.5+100*4
        bill+=(units-300)*6
    print("Units Consumed:",units)
    print("Electricity Bill: Rs.",round(bill,2))
