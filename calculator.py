choice=int(input("Enter your choice (1/2): "))
if choice==1:
 print("="*50)
 print("-----------------Normal calculation------------------")
 print("="*50)
 num=int(input("Enter the number: "))
 x=(input("Enter the function (+-*/)"))
 num1=int(input("Enter the number: "))
 if x=="+":
    print("Addition: ",num+num1)
 elif x=="-":
    print("Subtraction: ",num-num1)
 elif x=="*":
    print("Multiplication: ",num*num1)
 elif x=="/":
    print("Division : ",num/num1)
 elif x=="%":
    print("Floor division:",num%num1)
 elif x=="//":
    print("Double divide: ",num//num1)
 else:
    print("Not function to be used please check the function....")
elif choice==2:
    print("="*50)
    print("---------Scientific calculation-----------")
    print("="*50)
    from math import *
    num2=int(input("Enter the number:"))
    y=input("Enter the function(sin/cos/tan/log/pi/e/floor/fabs/factorial/lcm/gcd/sqrt/pow): ")
    num3=int(input("Enter the number: "))
    if y=="sin":
        print(sin(num2))
    elif y=="cos":
        print(cos(num2))
    elif y=="tan":
        print(tan(num2))
    elif y=="log":
        print(log(num2))
    elif y=="pi":
        print(pi)
    elif y=="e":
        print(e)
    elif y=="floor":
        print(floor(num2))
    elif y=="fabs":
        print(fabs(num2))
    elif y=="factorial":
        print(factorial(num2))
    elif y=="lcd":
        print(lcd(num2,num3))
    elif y=="gcd":
        print(gcd(num2,num3))
    elif y=="sqrt":
        print(sqrt(num2))
    elif y=="pow":
        print(num2**2)
    else:
        print("choice not declared.....!!!!")
else:
    print("No choice to be difference added")

 
