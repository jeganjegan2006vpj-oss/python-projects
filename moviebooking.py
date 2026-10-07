print("------Movie ticket booking-------")
movies={
    1:("Meesayam murukku2",170),
    2:("Modha rathiri ",120),
    3:("Bison kaalamadan",160),
    4:("KGF 2",200),
    5:("Batha",150),
    6:("Sirai",190),
}
print("------Movie list------")
for number,movie in movies.items():
    print(number,movie[0],"--",movie[1])
choice=int(input("ENtre your choice: "))
quantity=int(input("Total of quantity of tickets: "))
if choice in movies:
    movie_name=movies[choice][0]
    price=movies [choice][1]
    total=quantity*price
print("-----Ticket booking------")
print("Movie name : ",movie_name)
print("Total seats : ",quantity)
print("Total amount : ",total)
