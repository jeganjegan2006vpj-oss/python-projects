print("="*24,"Food ordering details","="*24)
foods=[]
def add_item():
    name=input("Enter your name: ")
    price=float(input("Enter the amount: "))
    quantity=float(input("No of items: "))
    total=price*quantity
    foods.append(
        {
            "Name":name,
            "Price":price,
            "Quantity":quantity,
            "Total":total
        }
    )
    print("Added successfully........")
def bill_details():
    if len(foods)==0:
        print("No recors found!please order the food....")
    grand_total=0
    for food in foods:
        print("Name: ",food["Name"])
        print("Price: ",food["Price"])
        print("Quantity: ",food["Quantity"])
        print("Total: ",food["Total"])
        grand_total+=food["Total"]
        print("Total amount of: ",grand_total)
while True:
    choice=int(input("Ener your choice: "))
    if choice==1:
        add_item()
    elif choice==2:
        bill_details()
    else:
        print("Enter not selected your choice!!!")
