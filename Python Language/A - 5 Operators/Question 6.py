"""
Write a python script which takes a three digit number from the user and displays
only its middle digit.
"""

number  = int(input("Enter the number:"))
number = number//10
print(number)
number = number%10
print(number)
