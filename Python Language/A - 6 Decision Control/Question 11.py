'''
Write a python script to take the month value in numeric format and display the
number of days in it.
'''

"""
month = int(input("Enter a month in number:"))
match month:
  case 1:
    print("There Are 31 Days In Month of January")
  case 2:
    print("There Are 28/29 Days Month of In February")
  case 3:
    print("There Are 31 Days In Month of March")
  case 4:
    print("There Are 30 Days In Month of April")
  case 5:
    print("There Are 31 Days In Month of May")
  case 6:
    print("There Are 30 Days In Month of June")
  case 7:
    print("There Are 31 Days In Month of July")
  case 8:
    print("There Are 31 Days In Month of August")
  case 9:
    print("There Are 30 Days In Month of September")
  case 10:
    print("There Are 31 Days In Month of October")
  case 11:
    print("There Are 30 Days In Month of November")
  case 12:
    print("There Are 31 Days In Month of December")
  case _:
    print("Invalid Number")
"""

#----------------- Another Approach Given By Sir Using Tuple -----------------

month = int(input("Enter a Month Number: "))

if month in (1,3,5,7,8,10,12):
  print("31 Days in This Month")
elif month in (4,6,9,11):
  print("30 Days in This Month")
elif month==2:
  print("28/29 Days in This Month")
else:
  print("Invalid Month Number")

