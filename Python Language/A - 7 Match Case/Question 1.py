#Write a python script to display the number of days in a given month number.
month = int(input("Enter a month number: "))
match month:
  case 1:
    print("31 Days in month of January.")
  case 2:
    print("28 or 29 Days in month of February.")
  case 3:
    print("31 Days in month of March.")
  case 4:
    print("30 Days in month of April.")
  case 5:
    print("31 Days in month of May.")
  case 6:
    print("30 Days in month of June.")
  case 7:
    print("31 Days in month of July.")
  case 8:
    print("31 Days in month of August.")
  case 9:
    print("30 Days in month of September.")
  case 10:
    print("31 Days in month of October.")
  case 11:
    print("30 Days in month of November.")
  case 12:
    print("31 Days in month of December.")
  case _:
    print("Invalid Number")
#-------------Another Approach Using Tuple---------------
'''
month = int(input("Enter a Month Number: "))
match month:
  case month if month in (1,3,5,7,8,10,12):
    print("31 Days in This Month")
  case month if month in (4,6,9,11):
    print("30 Days in This Month")
  case 2:
    print("28 or 29 Days in This Month")
  case _:
    print("Invalid Month Number")

'''