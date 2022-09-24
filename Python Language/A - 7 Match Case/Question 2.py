"""
Write a menu driven program to perform following operations - Addition, Subtraction,
Multiplication, Division
"""


menu = int(input("Enter the Option:\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n"))
match (menu):
  case 1:
    a = int(input("Enter a Number 1: "))
    b = int(input("Enter a Number 2: "))
    Addition = a + b
    print("Addition =",Addition)
  case 2:
    a = int(input("Enter a Number 1: "))
    b = int(input("Enter a Number 2: "))
    Subtraction = a - b
    print("Subtraction =",Subtraction)
  case 3:
    a = int(input("Enter a Number 1: "))
    b = int(input("Enter a Number 2: "))
    Multiplication = a * b
    print("Product =",Multiplication)
  case 4:
    a = int(input("Enter a Number 1: "))
    b = int(input("Enter a Number 2: "))
    Division = a//b
    print("Remainder =",Division)
  case _:
    print("Invalid Number")
