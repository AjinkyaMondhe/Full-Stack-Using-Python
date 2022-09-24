'''
Write a python script which takes a three digit number from the user and displays
only its first digit.
'''
number  = int(input("Enter the number:"))
number = number//100
print(number)
