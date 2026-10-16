print("========Instagram clone=====")
posts=[]
while True:
    print("=====MINI INSTAGRAM=====")
    print("1.Create Post")
    print("2.View Posts")
    print("3.Like Post")
    print("4.Exit")
    choice=input("Enter choice: ")
    if choice=="1":
        username=input("Enter username: ")
        caption=input("Enter caption: ")
        posts.append({
            "username":username,
            "caption":caption,
            "likes":0
        })
        print("Post created!")
    elif choice=="2":
        print("=====POSTS=====")
        for i, post in enumerate(posts):
            print("\nPost:",i + 1)
            print("User:",post["username"])
            print("Caption:",post["caption"])
            print("Likes:",post["likes"])
    elif choice=="3":
        number=int(input("Enter post number: "))
        if 1<=number<=len(posts):
            posts[number-1]["likes"]+=1
            print("Post liked!")
        else:
            print("Invalid post!")
    elif choice=="4":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
