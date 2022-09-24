"""
Write a program which takes a number from user. Print Saurabh Shukla if the number
is even, print Prateek Jain if the number is negative odd number and print Aditya
Choudhary if number is positive odd number.
"""
number = int(input("Enter a number: "))

match number:
  case number if(number%2==0):
      print("Saurabh Shukla Sir")
  case number if(number%2!=0 and number<0):
    print("Prateek Jain Sir")
  case number if(number>0 and number%2!=0):
      print("Aditya Choudhary Sir")