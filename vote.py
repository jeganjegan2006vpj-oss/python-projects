print("="*20,"Voting Machine","="*20)
def vote_eligible():
    age=int(input("Enter your age: "))
    if age>=18:
        print("Eligible for vote")
        print("Voter id applied")
    else:
        print("Not Eligible for vote and age!!!")
def vote_details():
    print("----------------CM Vote Selection-----------------")
    vote=input("Enter your vote(TVK/DMK/ADMK/NTK/NOTA):")
    if vote.upper()=="ADMK":
        print(f"successfully your vote in {vote.upper()}")
    elif vote.upper()=="DMK":
        print(f"successfully your vote in {vote.upper()}")
    elif vote.upper()=="TVK":
        print(f"successfully your vote in {vote.upper()}")
    elif vote.upper()=="NTK":
        print(f"successfully your vote in {vote.upper()}")
    elif vote.upper()=="NOTA":
        print(f"successfully your vote in {vote.upper()}")
    else:
        print("Not vote selected!!!!")
def vote_list():
    win=int(input("Enter your win places: "))
    print("Total Win places in tamil Nadu: ",win)
    if win>=100:
        print("Election win by TVK ")
        print("Chief minister of Tamil Nadu")
    elif win>=80:
        print("Election win by DMK ")
        print("Chief minister of Tamil Nadu")
    elif win>=30:
        print("Election win by ADMK ")
        print("Chief minister of Tamil Nadu")
    elif win>=10:
        print("Election win by NTK ")
        print("Chief minister of Tamil Nadu")
    elif win<10:
        print("NOTA votes in electon")
    else:
        print("Removed in votes")
while True:
 choice=int(input("Enter your choice: "))
 if choice==1:
    vote_eligible()   
 elif choice==2:
    vote_details()
 elif choice==3:
    vote_list()
 else:
    print("Not selected your choice!!!")
