#Write a python script to check whether a given number is positive, negative or zero.

number  = int(input("Enter a Number: "))

if number > 0:
  print("Positive")
elif number == 0:
  print("Zero")
else:
  print("Negative")