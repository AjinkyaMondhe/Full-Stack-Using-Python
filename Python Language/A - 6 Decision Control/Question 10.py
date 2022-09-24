'''
Write a python script to print greater among three numbers. Print number only once
even if the numbers are the same.
'''

number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))
number3 = int(input("Enter number 3: "))


print(((number1)if (number1>number3) else (number3)) if (number1>number2) else  (number2) if(number2>number3) else (number3))