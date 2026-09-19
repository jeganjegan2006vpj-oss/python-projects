
def account_details():
   print("="*25,"Account Details","="*25)
   name=input("Enter your name: ")
   age=int(input("Enter your age: "))
   bank=input("Enter yiur bank: ")
   accouttype=input("Enter account type(saving/primary)")
   account_number=int(input("Enter your account number: "))
   print("="*25,"Bank account details","="*25)
   atmpin=int(input("Enter your pin: "))
   print("Account holder name: ",name)
   print("Selected your  bank: ",bank)
   print("Account number :",account_number)
   print("Atm pin :",atmpin)
    
def deposit():
    print("="*25,"Deposited process","="*25)
    amount=int(input("Enter your amount: "))
    money=int(input("Enter deosit money: "))
    amount+=money
    print(f"deposited amount {money}in your bank in successfully")
    print("Totally balance: ",amount)
def withdraw():
    print("="*25,"Withdrawal process","="*25)
    amount=int(input("Enter your amount: "))
    withdraw=int(input("Enter withdrawal amount:"))
    amount-=withdraw
    print(f"withdrawal amount {withdraw} has been debited in your bank")
    print("Remaining Balance: ",amount)
def loan_process():
    print("="*25,"Loan process","="*25)
    loanamount=int(input("Enter your amount: "))
    income=int(input("Enter your annual income: "))
    if loanamount<=50000 and income<=250000:
        print(f"Loan process successfully applied in amount ${loanamount}")
    else:
        print("Least amount will be provided")
choice=int(input("Enter your choice (1/2/3/4): "))
if choice==1:
    account_details()
elif choice==2:
    loan_process()
elif choice==3:
    deposit()
elif choice==4:
    withdraw()
else:
    print("selected your wrong choice!\nplease take the right choice")
