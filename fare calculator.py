# fare calculator
age=int(input("Enter age: "))
ticket_price=120

if age<=5:
    print("no ticket")
elif age<=12:
    print("your ticket is : ",ticket_price*.5)
elif age<60:
    print("your ticket is : ",ticket_price)
elif age>=60:
    print("your ticket is : ",ticket_price*.7)


