import random
choices=["rock","paper","scisors","active"]
user=input("select your choices(rock/paper/scisors): ")
computer=random.choice(choices)
print("Computer selcted:",computer)
if user==computer:
    print("Draw the match!")
elif (
    (user=="rock" and computer=="scisors")or
    (user=="paper" and computer=="rock")or
    (user=="scisors" and computer=="active")or
    (user=="active" and computer=="paper")
):
    print("You win the match.....")
else:
    print("Opponent win the match!...")
