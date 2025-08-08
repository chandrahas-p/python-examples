def add(a,b):
  return a + b

def subtract(a,b):
  return a - b

def multiply(a,b):
  return a * b

def divide(a,b):
  return a / b

def power(a,b):
  return a ** b

def main_menu():
  # this will display the main menu
  print ("-" * 20)
  print ("Main menu")
  print ("-" * 20)
  print ("1. Add")
  print ("2. Subtract")
  print ("3. Multiply")
  print ("4. Divide")
  print ("5. Power")
  print ("6. Exit")
  print ("-" * 20)

while True:
  main_menu()
  choice = input("Enter your choice: ")
  if choice == "6":
    break
  a = int(input("Enter first number: "))
  b = int(input("Enter second number: "))
  if choice == "1":
    print ("Result: ", add(a,b))
  if choice == "2":
    print ("Result: ", subtract(a,b))
  if choice == "3":
    print ("Result: ", multiply(a,b))
  if choice == "4":
    print ("Result: ", divide(a,b))
  if choice == "5":
    print ("Result: ", power(a,b))