balance=500
print("===MOBILE RECHARGE===")
mobile=input("Enter mobile number: ")
amount=float(input("Enter recharge amount: "))
if amount<=balance:
    balance=balance-amount
    print("Recharge Successful!")
    print("Mobile:",mobile)
    print("Recharge Amount:",amount)
    print("Remaining Balance:",balance)
else:
    print("Insufficient Balance")
