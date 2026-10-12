print("STUDENT GRADE MANAGEMENT SYSTEM")
print("====================================")
name=input("Enter Student Name: ")
m1=float(input("Enter Tamil Mark: "))
m2=float(input("Enter English Mark: "))
m3=float(input("Enter Maths Mark: "))
m4=float(input("Enter Science Mark: "))
m5=float(input("Enter Computer Mark: "))
total=m1+m2+m3+m4+m5
average=total/5
if average>=90:
    grade="A+"
elif average>=80:
    grade="A"
elif average>=70:
    grade="B"
elif average>=60:
    grade="C"
elif average>=50:
    grade="D"
else:
    grade="F"
print("\n==================================")
print("RESULT")
print("====================================")

print("Student Name :",name)
print("Tamil :",m1)
print("English :",m2)
print("Maths :",m3)
print("Science :",m4)
print("Computer science:",m5)
print("Total :",total)
print("Average :",average)
print("Grade :",grade)
