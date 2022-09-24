"""
Write a python program to check whether a given string is a multiword string or single
word string using match case statement
"""
string = input("Enter a String: ")
string = string.strip()
match string:
  case string if ' ' in string:
      print("Mulit-Word String")
  case string if ' ' not in string:
      print("Single-Word String")