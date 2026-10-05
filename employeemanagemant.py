print("="*25,"Industry employee management","="*25)
def employee_details():
     employees=[

        {
             "id":104019,"name":"Jegan","Dept":"Full Stack","salary":45000,"experience":"3year"
        },
        {
             "id":104025,"name":"Manasseh","Dept":"Data Analyst","salary":35000,"experience":"2year"
        },
        {
             "id":104017,"name":"Immanuel","Dept":"Java Developer","salary":38000,"experience":"2year"
        },
        {
            "id":104022,"name":"Krishnakumar","Dept":"Full Stack","salary":55000,"experience":"5year"
        },
        {
              "id":104053,"name":"Ashok","Dept":"Python Develper","salary":48000,"experience":"1.5year"
        },
        {
              "id":104048,"name":"Siva subramanian","Dept":"AIML Engineer","salary":56000,"experience":"2.5year"  
        },
        {
             "id":104031,"name":"Mohammed Pakkir mydeen","Dept":"Devops engineer","salary":39000,"experience":"3year"
        }
    ]
     
     for emp in employees:
       print(
        emp["id"],
        emp["name"],
        emp["Dept"],
        emp["salary"],
        emp["experience"])
def employees_found():
         employees2=[
              {
             "id":104019,"name":"Jegan","Dept":"Full Stack","salary":45000,"experience":"3year"
        },
        {
             "id":104025,"name":"Manasseh","Dept":"Data Analyst","salary":35000,"experience":"2year"
        },
        {
             "id":104017,"name":"Immanuel","Dept":"Java Developer","salary":38000,"experience":"2year"
        },
        {
            "id":104022,"name":"Krishnakumar","Dept":"Full Stack","salary":55000,"experience":"5year"
        },
        {
              "id":104053,"name":"Ashok","Dept":"Python Develper","salary":48000,"experience":"1.5year"
        },
        {
              "id":104048,"name":"Siva subramanian","Dept":"AIML Engineer","salary":56000,"experience":"2.5year"  
        },
        {
             "id":104031,"name":"Mohammed Pakkir mydeen","Dept":"Devops engineer","salary":39000,"experience":"3year"
        }

         ]
         search_id=int(input("Enter your employee search id: "))
         for employ in employees2:
             if employ["id"]==search_id:
                print("Employee found")
                print("Employee name:",employ["name"])
                print("Employee department:",employ["Dept"])
def salary_calculate():
    total_salary=int(input("Enter employee total salary in month: "))
    transport=total_salary+0.20
    pf=total_salary-2000
    gst=total_salary*0.5
    print("Total Salary:",total_salary)
    print("Transport:",transport)
    print("PF amount:",pf)
    print("Gst :",gst)
employee_details()
employees_found()
salary_calculate()
