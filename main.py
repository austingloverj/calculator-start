#Python Calculator
from art import logo
print(logo)

keep_going = True

while keep_going:
  n1 = int(input("Enter your first number: "))
  n2 = int (input("Enter your second number: "))
  opperation = input("What opperation would you like to perform? Type '+', '-', '*', '/': ")

  print(f"{n1} {opperation} {n2} = ")

  if opperation == "+":
    def add(n1, n2):
      return n1 + n2
    print(add(n1, n2))
  elif opperation == "-":
    def subtract(n1, n2):
      return n1 - n2
    print(subtract(n1, n2))
  elif opperation == "*":
    def multiply(n1, n2):
      return n1 * n2
    print(multiply(n1, n2))
  elif opperation == "/":
    def divide(n1, n2):
      return n1 / n2
    print(divide(n1, n2))




  go_again = input("\nWould you like to go again? Type 'y' for yes and 'n' for no: ")
  
  if go_again == "n":
    keep_going = False

