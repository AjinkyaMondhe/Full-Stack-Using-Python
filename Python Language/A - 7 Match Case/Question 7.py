"""
Write a python program to check whether a given number is positive, negative or
zero using match case statement
"""

number = int(input("Enter a number: "))
match number:
  case number   if(number > 0):
      print("Positive")
  case number if(number == 0):
   
      print("Zero")
  case number if(number < 0):
      print("Negative")
  case _:
    print("Invalid Number")