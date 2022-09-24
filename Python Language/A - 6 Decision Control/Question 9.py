#Write a python script to check whether a given year is a leap year or not.


year = int(input("Enter a Year: "))
if (year%400==0 or year%100!=0 and year%4==0):
    print("Leap Year")
else:
   print("Not Leap Year")


'''

def isLeap(year):
  import calendar
  return (calendar.isleap(year))

year = 1900

if(isLeap(year)):
  print("Leap Year")
else:
  print("Not Leap Year")

'''