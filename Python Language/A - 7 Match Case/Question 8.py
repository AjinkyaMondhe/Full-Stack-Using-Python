"""
Write a python script to check whether two given strings are identical, first string
comes before the second in dictionary order or first string comes after the second
string in dictionary order using match case statement
"""

string1 = input("Enter a First String: ")
string2 = input("Enter a Second String: ")
match (string1,string2):
    case (string1,string2) if (string1 == string2):
      print("{} are Identical".format(string1))
    case (string1,string2)  if(string1>string2):
          print("{} Comes First and {} Comes Second In Dictionary Format".format(string2,string1))
    case (string1,string2) if(string2>string1):
          print("{} Comes First and {} String Comes Second In Dictionary Format".format(string1,string2))
    case _:
        print("Invalid Input")
