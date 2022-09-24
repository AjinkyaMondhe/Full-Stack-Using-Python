"""
Write a python script to check whether a given year is
a. Non century leap year
b. Century leap year
c. Non century non leap year
d. Century non leap year
"""

year = eval(input("Enter Your Year: "))
match year:
  case year if (year%100!=0 and year%400==0):
      print("Non Century Year but Leap Year.")
  case year if (year%100==0 and year%400==0):
      print("Century Year and Leap Year.")
  case year if(year%100!=0 and year%400!=0):
      print("Non Century Year and Non Leap Year.")
  case year if (year%100==0 and year%400!=0):
      print("Century Year but Non Leap Year.")
  case _:
      print("Invalid Number")