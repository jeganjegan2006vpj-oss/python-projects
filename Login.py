print("===== LOGIN SYSTEM =====")
correct_username="jegan"
correct_password="12345"
username=input("Enter username: ")
password=input("Enter password: ")
if username==correct_username and password==correct_password:
    print("Login Successful")
    print("Welcome",username)
else:
    print("Invalid Username or Password")
