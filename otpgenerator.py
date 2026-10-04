print("="*20,"otp gernertor","="*20)
import random
otp=random.randint(100000,999999)
print("Your OTP on mobile phone :",otp)
user_otp=int(input("Enter your otp: "))
if user_otp==otp:
    print("verified successfully... ")
else:
    print("Not valid in otp\nPlease check your otp")
