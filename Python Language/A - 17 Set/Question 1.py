"""
1. Write a python program to store all the programming languages known to you using
Set.
"""
print("Enter All Programming Language Known To You Separated by Comma: ")
set1 =set ([e for e in input().split(',')])
print(set1)
print(type(set1))

set2 = set(["Python","C","Java","CPP"]) # We can pass tuple also i.e set(("Python","C","Java","CPP"))
print(set2)
print(type(set2))

set3 = {"Python","C","Java","CPP"}
print(set3)
print(type(set3))