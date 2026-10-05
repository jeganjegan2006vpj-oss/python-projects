contacts={}
while True:
    print("1. contact save")
    print("2. sontact search")
    print("3. contact details")
    print("4. exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
      name=input("Enter your name:")
      phone=int(input("Enter mobile number:"))
      contacts[name]=phone
      print("Contacts saved")
    elif choice==2:
        name=input("Enter search name :")
        if name in contacts:
            print("phone number :",contacts[name])
        else:
            print("Contacts not found...")
    elif choice==3:
        for name,phone in contacts.items():
            print(name,":",phone)
    elif choice==4:
        print("Exit the phone and tabs")
    else:
        print("Contacts not found")
