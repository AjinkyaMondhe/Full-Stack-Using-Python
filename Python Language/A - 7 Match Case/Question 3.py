"""
Write a menu driven program with the following options:
a. Check whether a given set of three numbers are lengths of an isosceles
triangle or not
b. Check whether a given set of three numbers are lengths of sides of a right
angled triangle or not
c. Check whether a given set of three numbers are equilateral triangle or not
d. Exit.
"""

a=int (input("Enter a Number: "))
b=int (input("Enter a Number: "))
c=int (input("Enter a Number: "))

menu = input("Choice Option:\na Isosceles Triangle\nb Right Angle Triangle\nc Equilateral Triangle\nd Exit\n")

match menu:
  case 'a':
    if(a==b or b==c or c==a):
      print("Isosceles Triangle")
    else:
      print("Not Isosceles Triangle")
  case 'b':
    if(a**2 + b**2 == c**2):
      print("Right Angle Triangle")
    else:
      print("Not Right Angle Triangle")
  case 'c':
    if (a==b and b==c):
      print("Equilateral Triangle")
    else:
      print("Not Equilateral Triangle")
  case 'd':
    exit()
  case _:
    print("Invalid Number")